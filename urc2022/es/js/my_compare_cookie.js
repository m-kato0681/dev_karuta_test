// 【投票待機サイトにアクセスした際】の不正投票防止処理
// クッキーの読み書きを行い最終アクセス時間をもとにアクセスページを変える

var cookie; // cookieデータを格納
var cStart, cEnd; // cookieからタイムスタンプ部分を切り取る為の位置を格納
var timestamp_log; // クッキーに記録されているタイムスタンプを格納
// 投票待機サイトにアクセスした時のタイムスタンプを取得（JST:日本標準時）
var access_timestamp = new Date(new Date().toLocaleString({ timeZone: 'Asia/Tokyo' })).getTime();

if (navigator.cookieEnabled) // cookieが取得できる場合
{
    console.log("クッキー取得成功");
    cookie = document.cookie + ";";  // 変数cookieにcookieデータを格納(整理しやすいように;を付けて格納)
    // cookieが既にあるか検索（変数cStartにデータの最初の位置を入れる）
    cStart = cookie.indexOf("time=");
    if (cStart == -1) { // cookieがない場合（初回アクセス）
        location = "voting_main.php"; // 投票サイトにアクセス
    }
    else { // cookieがある場合（2回目以降のアクセス）
        cEnd = cookie.indexOf(";", cStart); // cokieデータ内での「;」の位置を取得
        timestamp_log = cookie.substring(cStart + 5, cEnd); // タイムスタンプの部分だけを切り取る
        timestamp_log = parseInt(timestamp_log); // タイムスタンプの文字列を数字に変換
        var difference_timestamp = access_timestamp - timestamp_log; // タイムスタンプの差分を計算
        console.log(access_timestamp,"-",timestamp_log,"=",difference_timestamp);
        if (difference_timestamp > 86400000) { // 投票完了から24時間(86,400,000msec)経過している場合
        // if (difference_timestamp > 300000) { // （テスト用）投票完了から5分(300,000msec)経過している場合
            location = "voting_main.php"; // 投票サイトにアクセス
        }
    }
}
else { // cookieが取得できない場合
    console.log("クッキー取得失敗");
    // 投票待機サイトの文章を変更してcookieを有効にするように促す
    document.querySelector("#after_voting_comment").innerHTML = '<br><div id="cookie_alert" class="text-center alert-text fas fa-exclamation-triangle"><br><br>当ページでは投票を管理するためにCookie（クッキー）を使用しています。<br><br>当ページに対するCookie（クッキー）の使用を有効にしてください。</div>';
}
