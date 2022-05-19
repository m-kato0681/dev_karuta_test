<!-- アクセスログを作成する -->
<?php
    $memory_ip = getenv("REMOTE_ADDR"); // IPアドレス
    $filename  = "log/accesslog.cgi"; // ログファイル名
    date_default_timezone_set('Asia/Tokyo'); // タイムゾーンを指定
    $time = date("Y/m/d H:i:s"); // 投票完了時刻
    $memory_timestamp = time();  // 投票完了時のタイムスタンプ
    
    //ログ本文
    $log = "\n---------------------------------".
            "\n". $memory_ip .
            ",".$time .
            ",".$memory_timestamp ;            
    
    //ログ書き込み
    $fp = fopen($filename, "a");
    fputs($fp, $log);
    fclose($fp);
?>