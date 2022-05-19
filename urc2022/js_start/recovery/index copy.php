<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="keywords" content="ArtecRobo, UNIVERSAL ROBOTICS CHALLENGE, ユニバーサルロボティクスチャレンジ, 小学生,　中学生, ロボットコンテスト">
    <meta name="description" content="ユニバーサルロボティクスチャレンジとは、小中学生を対象とした国際ロボット競技会です。ロボティクス初級者から上級者まで幅広く参加できるようになっています。子どもたちがロボティクス技術への興味・関心を深め、仲間と学び合い、チームワークにより課題解決を目指す大会です。">
    <title>小・中学生のための国際ロボット競技会 UNIVERSAL ROBOTICS CHALLENGE アイデアコンテスト 投票サイト 待機画面</title>
    <!-- CSS -->
    <link rel="stylesheet" href="css/mycss.css">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.6.1/css/all.css">
    <link rel="stylesheet" href="css/bootstrap.css">
    <!-- JS -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
    <script src="js/my_prohibit_back.js"></script> <!-- ブラウザバックを禁止 -->
</head>
<body>
    <!-- ヘッダー -->
    <div class="fixed-top">
        <?php include "search_form.php" ?> <!-- 検索窓 -->
    </div>
    <header>
        <?php include "header.php" ?>
    </header>
    <!-- アクセスログを作成 -->
    <?php include "accesslog.php" ?>
    <script src="js/my_compare_cookie.js"></script> <!-- 投票完了からの経過時間を測定 -->
    <main class="text-center">
        <div id="after_voting_comment">
            <br>投票ありがとうございました！
        </div>
        <div id="after_voting_comment_sub">
            24時間後に再投票が可能です。<br>投票再開まで今しばらくお待ちください。
        </div>
        
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
            </div>
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
        var search_hit_flag = 0; // 複数項目を検索して1つでもヒットした場合：1, 1つもヒットしない場合：0
        let respace    = /[^\s]+/g; // 空白を含まない一文字以上の文字列をすべて検索して配列として格納する正規表現
        let matchText  = searchText.value.match(respace); // 検索文字列を変換
        console.log(matchText);
        
        let mov_title_array = <?php echo $mov_title_array_json; ?>; // 動画タイトルを保存した配列
        var search_result = []; // 検索でヒットした動画タイトルのみを格納する配列
        if (searchText.value!="") { // 検索欄が空ではない場合
            // 作品を全て非表示にする
            num_array.forEach(element => {
                var delete_target  = document.getElementById("col" + element); // 該当するタイトルのIDを取得
                delete_target.style.display  = "none"; // 指定したIDのサムネイル、タイトル、ボタンを非表示にする
            });
            var title_search_array = mov_title_array; // 動画タイトル配列をコピー
            var element_num;
            var element_title_num_array = [];
            for (const elem of matchText) {
                search_result = title_search_array.filter(value => value.match(elem)); // 部分一致で検索
                if (search_result != "") {  // 検索にヒットした場合
                    search_hit_flag = 1;
                    searchBox.style.backgroundColor = "orange"; // 検索欄の色を変更
                    search_result.forEach(element => {
                        // 部分一致した動画タイトルがmov_title_array内で何番目に当たるのかを検索して格納
                        element_num = mov_title_array.indexOf(element);
                        // 取得したインデックスが存在していない場合
                        if (element_title_num_array.indexOf(element_num)==-1) {
                            // mov_title_array内でのインデックスを追加
                            element_title_num_array.push(element_num);
                        }
                        console.log(element_title_num_array);
                    });
                    // mov_title_arrayでの各インデックスがnum_array内で何番目に当たるのかを検索して格納
                    var element_num_num_array = [];
                    element_title_num_array.forEach(element => {
                        element_num = num_array.indexOf(element);
                        element_num_num_array.push(element_num); // num_array内でのインデックスを格納
                    });
                    // 検索で一致した作品のみ表示する
                    element_num_num_array.forEach(element => {
                        var delete_target  = document.getElementById("col" + element); // 該当するタイトルのIDを取得
                        delete_target.style.display  = ""; // 指定したIDのサムネイル、タイトル、ボタンを表示する
                    });
                }
            }
            // ボタンの表示を切り替え
            searchResetButton.style.display = "block";
            // 説明文と調整用スペースを表示
            notfound_text.textContent = element_title_num_array.length + "件の作品が見つかりました。"
            notfound_text.style.display = "block";
            result_space.style.display  = "block";
            console.log(search_result);                
            
            if (search_hit_flag==0) { // 検索に1つもヒットしなかった場合
                searchBox.style.backgroundColor = "lightgray"; // 検索欄の色を戻す
                // ボタンの表示を切り替え
                searchResetButton.style.display = "block";
                // 説明文と調整用スペースを表示
                notfound_text.textContent = "作品は見つかりませんでした。"
                notfound_text.style.display = "block";
                result_space.style.display  = "block";
                // 作品を全て非表示にする
                num_array.forEach(element => {
                    var delete_target  = document.getElementById("col" + element); // 該当するタイトルのIDを取得
                    delete_target.style.display  = "none"; // 指定したIDのサムネイル、タイトル、ボタンを非表示にする
                });
            }
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
    <!-- フッター -->
    <?php include "footer.php" ?>
</body>
</html>