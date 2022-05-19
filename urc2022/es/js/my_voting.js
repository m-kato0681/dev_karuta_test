// 投票ボタン
var img_src = new Array("images/votingbtn_vote.png","images/votingbtn_cancel.png");
var voting_array = []; // 投票された動画IDのみを格納する配列

function changeBtnImg(btn_id_num) {
    var current_img_src   = document.getElementById(btn_id_num).src; // 投票ボタンの現在の画像src[http://...〇〇.png]
    var split_current_img_src = current_img_src.split("images/");    // 画像srcからURL部分を分割
    var voting_btn_id     = document.getElementById(btn_id_num).id;  // votingBtn〇 （投票ボタンのIDを取得）
    var voting_btn_id_rep = voting_btn_id.replace("votingBtn","");   // votingBtn〇 ⇒ 〇 （IDの数字部分を取得）
    var voting_btn_mov_id = mov_id_array[num_array[voting_btn_id_rep]]; // 投票ボタンに紐づく動画IDを取得
     // 投票
    if (split_current_img_src[1] == "votingbtn_vote.png") {
        document.getElementById(btn_id_num).src = img_src[1]; // ボタンの画像を取り消しに変更
        mov_id_key_array[voting_btn_mov_id] = 1; // 動画IDと同じキーの要素の値を投票済みを表す「1」に変更
    }
    // 取り消し
    else {
        document.getElementById(btn_id_num).src = img_src[0]; // ボタンの画像を投票に変更
        mov_id_key_array[voting_btn_mov_id] = 0; // 動画IDと同じキーの要素の値を未投票を表す「0」に変更
    }
}

// 投票完了ボタン
function finishVoting() {
    // 投票数をカウント
    var voting_num = 0;
    let finishM = document.getElementById("finishModal");
    let alertM = document.getElementById("alertModal");
    let finishModal = bootstrap.Modal.getOrCreateInstance(finishM);
    let alertModal  = bootstrap.Modal.getOrCreateInstance(alertM);
    
    Object.keys(mov_id_key_array).forEach(key => {
        if (mov_id_key_array[key]) { // 投票されていた場合
            voting_array[voting_num] = key; // 投票された動画IDだけを別の配列に格納
            voting_num++;
        }
    });
    if (voting_num > 1) { // 投票が2票以上の場合
        finishModal.show();
    }
    else { // 投票が2票未満の場合
        alertModal.show();
    }
}

// 投票確定処理
function confirmVoting() {
    // 投票完了時のタイムスタンプ取得（JST:日本標準時）
    var voting_timestamp = new Date(new Date().toLocaleString({ timeZone: 'Asia/Tokyo' })).getTime();
    document.cookie = "time=" + voting_timestamp + ";"; // cookieにタイムスタンプを書き込む
    
    // 投票数分だけformのinputタグを追記する
    var form_parent = document.getElementById('form_parent'); // phpのフォームタグを取得
    var index = 0;
    for (const cont of voting_array) {
        var elem   = document.createElement('input');
        elem.type  = 'hidden';
        elem.name  = 'child_form[' + index + ']'; // POSTで受信した際に配列で参照できるようにnameに[]を付ける
        elem.value = cont; // 動画ID
        form_parent.appendChild(elem); // 親要素に子要素(elem)を追加
        index++;
    }

    // フォームを送信
    $('#form_parent').attr('action', 'database.php');
    document.form_parent.submit(); // データベースの処理を行うphpファイルに送信(送信するformはタグのname属性で指定)
}

// 投票取り消しボタン
function deleteVoting() {
    // 投票状態と投票ボタンの画像をリセットする
    var cnt = 0;
    Object.keys(mov_id_key_array).forEach(key => {
        if (mov_id_key_array[key]) { // 投票されていた場合
            mov_id_key_array[key] = 0; // 未投票に戻す
        }
        voting_array = [];
        var votingBtn_id  = "votingBtn" + cnt;
        var votingBtn_src = document.getElementById(votingBtn_id).src; // 投票ボタンの画像ソースを取得
        var split_votingBtn_src = votingBtn_src.split("images/");    // 画像srcのURLを分割
        if (split_votingBtn_src[1] == "votingbtn_cancel.png") { // 投票済みの場合
            document.getElementById(votingBtn_id).src = img_src[0]; // ボタンの画像を投票に変更
        }
        console.log("key: " + key);
        console.log("value: " + mov_id_key_array[key]);
        cnt++;
    });
}