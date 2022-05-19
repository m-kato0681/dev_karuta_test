// 投票ボタン
var img_src = new Array("images/votingbtn_vote.png","images/votingbtn_cancel.png");
function changeBtnImg(btn_id_num) {
    var current_img_src   = document.getElementById(btn_id_num).src;
    var voting_btn_id     = document.getElementById(btn_id_num).id; // votingBtn〇 （投票ボタンのIDを取得）
    var voting_btn_id_rep = voting_btn_id.replace("votingBtn",""); // votingBtn〇 ⇒ 〇 （IDの数字部分を取得）
    var voting_btn_mov_id = mov_id_array[num_array[voting_btn_id_rep]]; // 投票ボタンに紐づく動画IDを取得
    // console.log(current_img_src); // 投票ボタンの現在の画像src[http://...〇〇.png]
    // console.log(voting_btn_id_rep); // サイト上での表示順に応じた番号[0スタート]
    console.log(voting_btn_mov_id); // 投票ボタンに紐づいた動画ID
     // 投票
    if (current_img_src == "http://www.localhost/urc2022_votingsite/images/votingbtn_vote.png") {
        document.getElementById(btn_id_num).src = img_src[1]; // ボタンの画像を取り消しに変更
        mov_id_key_array[voting_btn_mov_id] = 1; // 動画IDと同じキーの要素の値を投票済みを表す「1」に変更
        console.log(mov_id_key_array[voting_btn_mov_id]); // 投票状態
    }
    // 取り消し
    else {
        document.getElementById(btn_id_num).src = img_src[0]; // ボタンの画像を投票に変更
        mov_id_key_array[voting_btn_mov_id] = 0; // 動画IDと同じキーの要素の値を未投票を表す「0」に変更
        console.log(mov_id_key_array[voting_btn_mov_id]); // 投票状態
    }
}

// 投票完了ボタン
function finishVoting() {
    // 投票数をカウント
    var voting_num = 0;
    var myModal= document.getElementById("alertModal");
    var alertModal= bootstrap.Modal.getOrCreateInstance(myModal)
    
    Object.keys(mov_id_key_array).forEach(key => {
        if (mov_id_key_array[key]) { // 投票されていた場合
            voting_num++;
        }
    });
    console.log("voting_num: "+ voting_num);
    if (voting_num > 1) { // 投票が2票以上の場合
        location = "standby_screen.php"
    }
    else { // 投票が2票未満の場合
        alertModal.show()
    }
}

// 投票取り消しボタン
function deleteVoting() {
    // 投票状態と投票ボタンの画像をリセットする
    var cnt = 0;
    Object.keys(mov_id_key_array).forEach(key => {
        if (mov_id_key_array[key]) { // 投票されていた場合
            mov_id_key_array[key] = 0; // 未投票に戻す
        }
        var votingBtn_id  = "votingBtn" + cnt;
        var votingBtn_src = document.getElementById(votingBtn_id).src; // 投票ボタンの画像ソースを取得
        if (votingBtn_src == "http://www.localhost/urc2022_votingsite/images/votingbtn_cancel.png") { // 投票済みの場合
            document.getElementById(votingBtn_id).src = img_src[0]; // ボタンの画像を投票に変更
        }
        console.log("key: " + key);
        console.log("value: " + mov_id_key_array[key]);
        cnt++;
    });
}