<?php
	$fr = fopen("csv/read.csv", "r"); // peatixから取得した元のcsvファイル
	$fw = fopen("csv/write.csv", "w"); // 投票サイトで使用する編集後のcsvファイル
	if ($fr==true) { // 正常に元のファイルが開けた場合
		// ファイルを1行ずつ読み込み、各列を配列形式で$dataに格納する
		$row = 0; // 行数カウント用
		while ($data = fgetcsv($fr, 0, "\t")) { // fgetcsv(csvファイルポインタ,最大行数,区切り文字)
			$csv_array_split[$row] = $data; // 管理できるように各行ごとに番号をふって配列を作成
			$row++;
		}
		fclose($fr);
		echo '<script>console.log(' . json_encode($csv_array_split) . ');</script>';
		
		// 動画タイトル格納用の配列を作成
		$list = [];
        for ($i=1; $i<$row-1; $i++) { // 取得したデータの行数分ループ(1行目(0)は各列の項目名なのでスルー)
            $num = $i-1; // 配列に0から格納するための調整
			$ticket_num_array[$num] = $csv_array_split[$i][8];  // 各行の9列目（チケット番号）を取得
			$mov_url_array[$num]    = $csv_array_split[$i][17]; // 各行の18列目（動画URL）を取得
            $mov_title_array[$num]  = $csv_array_split[$i][18]; // 各行の19列目（タイトル）を取得
			// 必要な要素を新しい配列の先頭に追加(8:チケット番号, 17:動画URL, 18:動画タイトル)
			$csv_array_name  = 'csv_array'. $i; // 配列の名前を設定
			$$csv_array_name = []; // 可変変数で配列を宣言
			// 取得した各要素を配列に格納
			array_unshift($$csv_array_name, $ticket_num_array[$num], $mov_url_array[$num], $mov_title_array[$num]);
			// 作成した配列を新しい配列に追加してまとめる
			array_push($list, $$csv_array_name);
        }

		if (true == $fw) { // 正常に編集後のファイルが開けた場合
			foreach ($list as $fields) { // 複数の配列をまとめた配列を順番に読み込む
				fputcsv($fw, $fields, "\t"); // 新しいcsvファイルに書き込む
			}
		}
		fclose($fw);
	}
?>

