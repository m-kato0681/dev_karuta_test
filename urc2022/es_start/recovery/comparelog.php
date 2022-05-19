<!-- アクセスログを比較する -->
<?php
    $current_ip = getenv("REMOTE_ADDR"); // IPアドレス
    date_default_timezone_set('Asia/Tokyo'); // タイムゾーンを指定
    $current_timestamp = time(); // アクセス時のタイムスタンプ

    $read_log   = @file("log/accesslog.cgi"); // ログファイルを1行ずつ配列に格納
    $number_log = count($read_log); // 要素数=ログファイルの行数を算出

    $row = 0; // 行数記録用
    $compare_match = ""; // 一致した行の文字列を保存する用
    for($cnt=0; $cnt<$number_log; $cnt++){
        $compare[$cnt] = stripos($read_log[$cnt] , $current_ip); // 第二引数と同じ文字列が見つかった場所を返す
        if ($compare[$cnt] !== false) { // 同じIPアドレスがあった場合
            $row = $cnt; // 行数を記録
            $compare_match = $read_log[$row]; // 指定行の文字列を取得（後の行に同じIPがあれば更新）
        }
    }
    if ($compare_match) { // 比較用文字列が取得された場合（同じIPアドレスがあった場合）
        $compare_match_split = explode(",", $compare_match,3); // 指定行の文字列を,で分割し3要素格納
        $compare_timestamp   = $compare_match_split[2]; // 指定のIPアドレスで投票を完了した際のタイムスタンプ
        $difference_timestamp = $current_timestamp - $compare_timestamp; // タイムスタンプの差分を計算
        if ($difference_timestamp<86400) { // 投票完了から24時間経過していない場合
            require("standby_screen.php"); // 投票待機サイトにアクセス
        }
    }
    else {
        require("index.php"); // 投票サイトにアクセス
    }
?>