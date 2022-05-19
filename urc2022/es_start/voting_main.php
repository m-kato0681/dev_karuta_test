<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="keywords" content="ArtecRobo, UNIVERSAL ROBOTICS CHALLENGE, ユニバーサルロボティクスチャレンジ, 小学生,　中学生, ロボットコンテスト">
    <meta name="description" content="ユニバーサルロボティクスチャレンジとは、小中学生を対象とした国際ロボット競技会です。ロボティクス初級者から上級者まで幅広く参加できるようになっています。子どもたちがロボティクス技術への興味・関心を深め、仲間と学び合い、チームワークにより課題解決を目指す大会です。">
    <title>小・中学生のための国際ロボット競技会 UNIVERSAL ROBOTICS CHALLENGE アイデアコンテスト 小学校部門 投票サイト</title>
    <!-- CSS -->
    <link rel="stylesheet" href="css/bootstrap.css">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.6.1/css/all.css">
    <link rel="stylesheet" href="css/mycss.css">
    <link rel="stylesheet" href="css/jpn.css">
    <!-- JS -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <script src="js/my_count_down_timer.js"></script>
    <script src="js/my_compare_voting_cookie.js"></script> <!-- 投票完了時の処理 -->
    <script src="js/bootstrap.min.js"></script>
    <script>$(function() {$('html,body').animate({ scrollTop: 0 }, '1');});</script> <!-- ページリロード時トップへ移動 -->
</head>
<body>
    <div>
        <!-- ヘッダー -->
        <div class="fixed-top">
            <?php include "search_form.php" ?> <!-- 検索窓 -->
        </div>
        <header>
            <?php include "header.php" ?>
            <?php include "count_down_timer.php" ?> <!-- 投票期間 -->
        </header>
        <!-- メイン -->
        <main>
            <!-- 一覧表示用の動画ID格納配列を作成 -->
            <?php
                // csvから表示用の動画タイトルとURLを取得
                include "read_csv.php";
                $mov_title_array_json = json_encode($mov_title_array); // 動画タイトル配列をJSONにエンコード
                $mov_id_array_json = json_encode($mov_id_array); // 動画ID配列をJSONにエンコード
                // 投票状態を管理するための連想配列を作成
                $mov_id_key_array = [];
                foreach ($mov_id_array as $id) {
                    $mov_id_key_array += array($id=>0); // 動画IDをキーとした連想配列（初期値は未投票を表す0）
                }
                $mov_id_key_array_json = json_encode($mov_id_key_array); // 投票状態を表す配列をJSONにエンコード

                $num = 0;
                // ランダム取得用の配列を作成
                foreach ($mov_id_array as $i) {
                    $num_array[$num] = $num; // 0から順に数字を要素として代入
                    $num ++;
                }
                shuffle($num_array); // 配列の中身をシャッフル
                $num_array_json = json_encode($num_array); // JSONにエンコード
                $num = 0;
                // シャッフルされた値をもとに指定した要素でsrcを指定
                foreach ($num_array as $mov_id) {
                    $thumb_size = "mqdefault.jpg";
                    $src[$num]  = sprintf("http://img.youtube.com/vi/%s/%s", $mov_id_array[$mov_id], $thumb_size );

                    if (@getimagesize($src[$num])==false) { // 指定した画像の情報が取得出来ない場合
                        $src[$num] = "./images/urc_logo_thumb.png"; // 画像の差し替え
                    }
                    $num ++;
                }
            ?>
            <div class="container">
                <!-- ヘッダーに被らないように余白を追加 -->
                <div class="mt-3"></div>
                <div class="row">
                    <!-- 1ユーザーの表示単位 -->
                    <?php
                        $id_num = 0;
                        // id数量分コードを読み込み
                        foreach ($mov_id_array as $i) {
                            include "user_container_col.php";
                            $id_num ++;
                        }
                    ?>
                </div>
            </div>
            <!-- モーダル -->
            <?php include "modal.php" ?>
            <div class="fixed-bottom">
                <!-- ページトップボタン -->
                <?php include "pagetop.php" ?>
                <!-- 投票完了・取り消しボタン -->
                <?php include "voting_btns.php" ?>
            </div>
            <!-- フォーム(中身は後からmy_voting.jsで追加する) -->
            <form id="form_parent" name="form_parent" method="POST"></form>
        </main>
        <!-- スペース調整用のフッター -->
        <?php include "footer_spacer.php" ?>
    </div>

    <script src="js/my_voting.js"></script> <!-- 投票ボタンの処理 -->
    <script>
        let mov_id_key_array = <?php echo $mov_id_key_array_json; ?>; // 動画IDと投票状況を保存した連想配列
        let num_array        = <?php echo $num_array_json; ?>; // 動画の表示順をシャッフルするために用意した配列

        // サイト内検索の処理
        let searchBox  = document.getElementById("search_box"); // 検索欄
        let searchText = document.getElementById("search_text"); // テキストボックス
        let searchButton = document.getElementById("search_button"); // 検索ボタン
        let searchResetButton = document.getElementById("search_reset_button"); // 検索リセットボタン
        let notfound_text = document.getElementById("search_notfound_txt"); // 検索結果テキスト
        let result_space  = document.getElementById("search_result_space"); // 調整用スペース
        searchButton.addEventListener("click", searchButton_click); // 検索ボタンのクリックリスナーを設定
        searchResetButton.addEventListener("click", searchResetButton_click); // 検索リセットボタンのクリックリスナーを設定
        window.document.onkeydown = function(event){
            // テキストボックスが空ではない状態でEnterキー押下時に検索処理を実行
            if (searchText.value!="" && event.key === 'Enter') {
                searchButton_click();
            }
        }
        
        // 検索ボタンの処理
        function searchButton_click() {
            let respace    = /[^\s]+/g; // 空白を含まない一文字以上の文字列をすべて検索して配列として格納する正規表現
            let searchText_array  = searchText.value.match(respace); // 検索文字列を変換（スペース区切りで検索ワード毎に分割して配列に格納）
            var common_result = []; // 最終的な共通の検索結果
            var matchText = {}; // 変換処理後の各検索文字列を格納する連想配列
            let mov_title_array = <?php echo $mov_title_array_json; ?>; // csvから取得した動画タイトルを保存した配列
            var search_result = []; // 検索でヒットした動画タイトルのみを格納する配列
            var search_result_compare = []; // 共通の検索結果のみを残すための比較用配列
            var element_num;
            
            // 分割した検索文字列の数だけ文字列の変換処理を実行           
            if (searchText.value!="") { // 検索欄が空ではない場合
                // 作品を全て非表示にする
                num_array.forEach(element => {
                    var delete_target  = document.getElementById("col" + element); // 該当するタイトルのIDを取得
                    delete_target.style.display  = "none"; // 指定したIDのサムネイル、タイトル、ボタンを非表示にする
                });
                for (var i=0; i<searchText_array.length; i++) {
                    // ---------------------------------------------------- //
                    let searchText_hira  = searchText_array[i].replace( /[あ-ん]/g, m => String.fromCharCode(m.charCodeAt(0) + 0x60)); // ひらがなをカタカナに変換
                    let searchText_kata  = searchText_array[i].replace( /[ア-ン]/g, m => String.fromCharCode(m.charCodeAt(0) - 0x60)); // カタカナをひらがなに変換
                    // カタカナの全角を半角に変換
                    let kata_halfw = { "ガ": "ｶﾞ", "ギ": "ｷﾞ", "グ": "ｸﾞ", "ゲ": "ｹﾞ", "ゴ": "ｺﾞ", "ザ": "ｻﾞ", "ジ": "ｼﾞ", "ズ": "ｽﾞ", "ゼ": "ｾﾞ", "ゾ": "ｿﾞ", "ダ": "ﾀﾞ", "ヂ": "ﾁﾞ", "ヅ": "ﾂﾞ", "デ": "ﾃﾞ", "ド": "ﾄﾞ", "バ": "ﾊﾞ", "ビ": "ﾋﾞ", "ブ": "ﾌﾞ", "ベ": "ﾍﾞ", "ボ": "ﾎﾞ", "パ": "ﾊﾟ", "ピ": "ﾋﾟ", "プ": "ﾌﾟ", "ペ": "ﾍﾟ", "ポ": "ﾎﾟ", "ヴ": "ｳﾞ", "ヷ": "ﾜﾞ", "ヺ": "ｦﾞ", "ア": "ｱ", "イ": "ｲ", "ウ": "ｳ", "エ": "ｴ", "オ": "ｵ", "カ": "ｶ", "キ": "ｷ", "ク": "ｸ", "ケ": "ｹ", "コ": "ｺ", "サ": "ｻ", "シ": "ｼ", "ス": "ｽ", "セ": "ｾ", "ソ": "ｿ", "タ": "ﾀ", "チ": "ﾁ", "ツ": "ﾂ", "テ": "ﾃ", "ト": "ﾄ", "ナ": "ﾅ", "ニ": "ﾆ", "ヌ": "ﾇ", "ネ": "ﾈ", "ノ": "ﾉ", "ハ": "ﾊ", "ヒ": "ﾋ", "フ": "ﾌ", "ヘ": "ﾍ", "ホ": "ﾎ", "マ": "ﾏ", "ミ": "ﾐ", "ム": "ﾑ", "メ": "ﾒ", "モ": "ﾓ", "ヤ": "ﾔ", "ユ": "ﾕ", "ヨ": "ﾖ", "ラ": "ﾗ", "リ": "ﾘ", "ル": "ﾙ", "レ": "ﾚ", "ロ": "ﾛ", "ワ": "ﾜ", "ヲ": "ｦ", "ン": "ﾝ", "ァ": "ｧ", "ィ": "ｨ", "ゥ": "ｩ", "ェ": "ｪ", "ォ": "ｫ", "ッ": "ｯ", "ャ": "ｬ", "ュ": "ｭ", "ョ": "ｮ", "。": "｡", "、": "､", "ー": "ｰ", "「": "｢", "」": "｣", "・": "･" };
                    let reg_falfw = new RegExp('(' + Object.keys(kata_halfw).join('|') + ')', 'g');
                    let searchText_kata_halfw = searchText_array[i].replace(reg_falfw, function (match) { return kata_halfw[match]; }).replace(/゛/g, 'ﾞ').replace(/゜/g, 'ﾟ');
                    // カタカナの半角を全角に変換
                    let kata_fullw = { 'ｶﾞ': 'ガ', 'ｷﾞ': 'ギ', 'ｸﾞ': 'グ', 'ｹﾞ': 'ゲ', 'ｺﾞ': 'ゴ', 'ｻﾞ': 'ザ', 'ｼﾞ': 'ジ', 'ｽﾞ': 'ズ', 'ｾﾞ': 'ゼ', 'ｿﾞ': 'ゾ', 'ﾀﾞ': 'ダ', 'ﾁﾞ': 'ヂ', 'ﾂﾞ': 'ヅ', 'ﾃﾞ': 'デ', 'ﾄﾞ': 'ド', 'ﾊﾞ': 'バ', 'ﾋﾞ': 'ビ', 'ﾌﾞ': 'ブ', 'ﾍﾞ': 'ベ', 'ﾎﾞ': 'ボ', 'ﾊﾟ': 'パ', 'ﾋﾟ': 'ピ', 'ﾌﾟ': 'プ', 'ﾍﾟ': 'ペ', 'ﾎﾟ': 'ポ', 'ｳﾞ': 'ヴ', 'ﾜﾞ': 'ヷ', 'ｦﾞ': 'ヺ', 'ｱ': 'ア', 'ｲ': 'イ', 'ｳ': 'ウ', 'ｴ': 'エ', 'ｵ': 'オ', 'ｶ': 'カ', 'ｷ': 'キ', 'ｸ': 'ク', 'ｹ': 'ケ', 'ｺ': 'コ', 'ｻ': 'サ', 'ｼ': 'シ', 'ｽ': 'ス', 'ｾ': 'セ', 'ｿ': 'ソ', 'ﾀ': 'タ', 'ﾁ': 'チ', 'ﾂ': 'ツ', 'ﾃ': 'テ', 'ﾄ': 'ト', 'ﾅ': 'ナ', 'ﾆ': 'ニ', 'ﾇ': 'ヌ', 'ﾈ': 'ネ', 'ﾉ': 'ノ', 'ﾊ': 'ハ', 'ﾋ': 'ヒ', 'ﾌ': 'フ', 'ﾍ': 'ヘ', 'ﾎ': 'ホ', 'ﾏ': 'マ', 'ﾐ': 'ミ', 'ﾑ': 'ム', 'ﾒ': 'メ', 'ﾓ': 'モ', 'ﾔ': 'ヤ', 'ﾕ': 'ユ', 'ﾖ': 'ヨ', 'ﾗ': 'ラ', 'ﾘ': 'リ', 'ﾙ': 'ル', 'ﾚ': 'レ', 'ﾛ': 'ロ', 'ﾜ': 'ワ', 'ｦ': 'ヲ', 'ﾝ': 'ン', 'ｧ': 'ァ', 'ｨ': 'ィ', 'ｩ': 'ゥ', 'ｪ': 'ェ', 'ｫ': 'ォ', 'ｯ': 'ッ', 'ｬ': 'ャ', 'ｭ': 'ュ', 'ｮ': 'ョ', '｡': '。', '､': '、', 'ｰ': 'ー', '｢': '「', '｣': '」', '･': '・' };
                    var reg_fullw = new RegExp('(' + Object.keys(kata_fullw).join('|') + ')', 'g');
                    let searchText_kata_fullw = searchText_array[i].replace(reg_fullw, function (match) { return kata_fullw[match]; }).replace(/ﾞ/g, '゛').replace(/ﾟ/g, '゜');

                    var searchText_fullw = searchText_array[i].replace( /[!-~]/g, m => String.fromCharCode(m.charCodeAt(0) + 0xFEE0)); // 英数字の半角を全角に変換
                    var searchText_halfw = searchText_array[i].replace( /[！-～]/g, m => String.fromCharCode(m.charCodeAt(0) - 0xFEE0)); // 英数字の全角を半角に変換
                    // コードシフトで変換できないその他の半角を全角に変換
                    searchText_fullw = searchText_halfw.replace(/&/g, "＆").replace(/\"/g, "”").replace(/'/g, "’").replace(/`/g, "‘").replace(/\\/g, "￥").replace(/ /g, "　").replace(/~/g, "〜");
                    // コードシフトで変換できないその他の全角を半角に変換
                    searchText_halfw = searchText_halfw.replace(/＆/g, "&").replace(/”/g, "\"").replace(/’/g, "'").replace(/‘/g, "`").replace(/￥/g, "\\").replace(/　/g, " ").replace(/〜/g, "~");
                    
                    let searchText_lower = searchText_array[i].toLowerCase(); // 英語を全て小文字に変換
                    let searchText_upper = searchText_array[i].toUpperCase(); // 英語を全て大文字に変換
                    
                    // 変換前の文字列と変換後の全ての文字列を1つに連結（変換した文字列の最後に空白を追加してから連結）
                    let searchText_connect = searchText_array[i] + " "
                                            + searchText_hira + " "
                                            + searchText_kata + " "
                                            + searchText_kata_halfw + " "
                                            + searchText_kata_fullw + " "
                                            + searchText_fullw + " "
                                            + searchText_halfw + " "
                                            + searchText_lower + " "
                                            + searchText_upper + " ";
                    // ---------------------------------------------------- //
                    matchText[i] = searchText_connect.match(respace); // 検索文字列を変換（スペース区切りで変換後の検索ワード毎に分割して配列に格納）

                    // 配列内の重複を取り除く
                    matchText[i] = matchText[i].filter(function(x, i, self){
                        return self.indexOf(x) === i;
                    });

                    // 各検索ワードでヒットする動画タイトルを配列に格納
                    var element_title_num_array = [];
                    var search_result_sum  = [];
                    var search_array_num = 0;
                    for (const element of matchText[i]) {
                        search_result[search_array_num] = mov_title_array.filter(value => value.match(element)); // 部分一致で検索、ヒットしたものを配列に格納
                        // 各検索ワードでヒットした動画タイトルの各配列の要素をまとめる（以降の検索結果も順次追加）
                        if (search_array_num > 0) {
                            search_result_sum[i] = search_result_sum[i].concat(search_result[search_array_num]);
                        }
                        else {
                            search_result_sum[i] = search_result[0];
                        }
                        search_array_num++;
                    }
                    // まとめた配列内の重複を取り除く
                    search_result_sum[i] = search_result_sum[i].filter(function(x, y, self){
                        return self.indexOf(x) === y;
                    });
                    // 「<各検索ワード>でヒットした動画タイトルを格納した配列」を1つの配列にまとめる
                    search_result_compare.push(search_result_sum[i]);
                    // 「<各検索ワード>でヒットした動画タイトルを格納した配列」の要素を1つにまとめる（以降の配列も順次追加）
                    common_result = common_result.concat(search_result_sum[i]);
                }
                // まとめた配列内の重複を取り除く
                common_result = common_result.filter(function(x, y, self){
                    return self.indexOf(x) === y;
                });

                // 全てのキーワードの検索結果に含まれる動画タイトルのみを抽出
                common_result = common_result.filter(function(val) {
                    var result = true;
                    search_result_compare.forEach(function(compare_array, i) {
                        result = (compare_array.indexOf(val) !== -1) && result;
                    });
                    return result;
                });
                console.log("common_result:", common_result);

                common_result.forEach(element => {
                    // 部分一致した動画タイトルがmov_title_array内で何番目に当たるのかを検索して格納
                    element_num = mov_title_array.indexOf(element);
                    // mov_title_array内でのインデックスを追加
                    element_title_num_array.push(element_num);
                });
                var element_num_num_array = [];
                // mov_title_arrayでの各インデックスがnum_array内で何番目に当たるのかを検索して格納
                element_title_num_array.forEach(element => {
                    element_num = num_array.indexOf(element);
                    element_num_num_array.push(element_num); // num_array内でのインデックスを格納
                });
                // 検索で一致した作品のみ表示する
                element_num_num_array.forEach(element => {
                    var delete_target  = document.getElementById("col" + element); // 該当するタイトルのIDを取得
                    delete_target.style.display  = ""; // 指定したIDのサムネイル、タイトル、ボタンを表示する
                });

                // 検索に1つもヒットしなかった場合
                if (common_result=="") {
                    searchBox.style.backgroundColor = "lightgray"; // 検索欄の色を戻す
                    notfound_text.textContent = "作品は見つかりませんでした。"
                }
                else {
                    searchBox.style.backgroundColor = "orange"; // 検索欄の色を変更
                    notfound_text.textContent = element_title_num_array.length + "件の作品が見つかりました。"
                }
                // ボタンの表示を切り替え
                searchResetButton.style.display = "block";
                // 説明文と調整用スペースを表示
                notfound_text.style.display = "block";
                result_space.style.display  = "block";
            }
        }

        // 検索リセットボタンの処理
        function searchResetButton_click() {
            searchBox.style.backgroundColor = "lightgray"; // 検索欄の色を戻す
            // ボタンの表示を切り替え
            searchResetButton.style.display = "none";
            // 説明文と調整用スペースを非表示
            notfound_text.style.display = "none";
            result_space.style.display  = "none";
            searchText.value = ""; // 検索欄は空に戻す
            // 作品を全て表示する
            num_array.forEach(element => {
                var delete_target  = document.getElementById("col" + element); // 該当するタイトルのIDを取得
                delete_target.style.display  = ""; // 指定したIDのサムネイル、タイトル、ボタンを表示する
            });
        }

        // モーダルでの動画再生処理
        var player;
        var player_id;
        let mov_id_array = <?php echo $mov_id_array_json; ?>; // 動画IDを保存した配列
        function loadMov(id) { //サムネイル画像をクリックした際に実行
            player_id = Number(id); // サムネイル画像に割り当てられているIDを取得
            player.cueVideoById({videoId: mov_id_array[num_array[player_id]]}); // 画像をタップした際にvideoIdを更新
        }
        // IFrame Player APIの読み込み 
        var tag = document.createElement("script"); // scriptタグを生成
        tag.src = "https://www.youtube.com/iframe_api"; // APIのURLを付与
        var firstScriptTag = document.getElementsByTagName("script")[0]; // 生成したタグをセット
        firstScriptTag.parentNode.insertBefore(tag, firstScriptTag); // HTML上に挿入
        // API 読み込み時に自動で実行
        function onYouTubePlayerAPIReady() {
            player = new YT.Player("player", { // YT.Playerオブジェクトを作成（'player'は動画の挿入先のid名）
                playerVars: {
                    playsinline: 1 // インライン再生（全画面ではなく表示領域内で再生）
                }
            });
        }
        // モーダルが閉じられたら動画を停止する
        $("#playerModal").on("hidden.bs.modal", function () {
            player.stopVideo();
        })
    </script>
</body>
</html>