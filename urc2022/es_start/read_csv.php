<!-- CSVの読み込みと配列の作成 -->
<div>
    <?php
        // 読み込み("r")でファイルを指定
        $fopen = fopen("csv/write.csv", "r");
        if (true == $fopen) { // 正常にファイルが開けた場合
            // ファイルを1行ずつ読み込み、各列を配列形式で$dataに格納する
            $row = 0; // ファイルの行数管理用
            while ($csv_array = fgetcsv($fopen, 0, "\t")) {
                $csv_array_split[$row] = $csv_array; // 管理できるように各行ごとに番号をふって配列を作成
                $row++;
            }
        }
        // 読み込んでいたファイルを閉じる
        fclose($fopen);

        // 動画タイトル格納用の配列を作成
        for ($i=0; $i<$row; $i++) { // 取得したデータの行数分ループ
            $mov_title_array[$i] = $csv_array_split[$i][2]; // 各行の3列目（タイトル）を取得
        }

        // YouTube動画URL格納用の配列を作成
        for ($i=0; $i<$row; $i++) { // 取得したデータの行数分ループ
            $mov_url_array[$i] = $csv_array_split[$i][1]; // 各行の2列目（URL）を取得
            // URLを分割
            $mov_url_array_split = explode("/", $mov_url_array[$i]);
            $mov_id_array[$i] = $mov_url_array_split[3]; // パターン1
            // ショート動画のURLの場合
            if ($mov_id_array[$i] == "shorts") {
                $mov_id_array[$i] = $mov_url_array_split[4]; // パターン2
            }
            // URLを直接コピペしている場合(v=が含まれる)
            if (strpos($mov_id_array[$i],"v=") !== false) {
                // URLを分割
                $mov_url_array_split = explode("v=", $mov_id_array[$i]);
                $mov_id_array[$i] = $mov_url_array_split[1]; // パターン3
            }
            // URLにオプションが埋め込まれている場合(?や&が含まれる)
            if (strpos($mov_id_array[$i],"?") !== false) {
                // URLを分割
                $mov_url_array_split = explode("?", $mov_id_array[$i]);
                $mov_id_array[$i] = $mov_url_array_split[0]; // パターン4
            }
            if (strpos($mov_id_array[$i],"&") !== false) {
                // URLを分割
                $mov_url_array_split = explode("&", $mov_id_array[$i]);
                $mov_id_array[$i] = $mov_url_array_split[0]; // パターン5
            }
        }
    ?>
</div>