<?php
	// $_POSTでフォームのデータを受信
	$form_array = $_POST['child_form'];

	// DBの登録
	$host_name = $_SERVER['SERVER_NAME']; // サーバーのホスト名取得
	$pattern = '(www\.urc21\.org)'; // 本番用のサーバーのホスト名
	if (!preg_match($pattern, $host_name)) {
		// ローカルサーバーのデータベース設定
		$dsn = 'mysql:dbname=urc2022;host=127.0.0.1;port=3306;charset=utf8';
		$usr = 'root';
		$passwrd = '';
	}
	else {
		// 本番用のDB設定
		$dsn = 'mysql:dbname=VxvhcCBrYg996;host=mysql540.in.shared-server.net;port=55198;charset=utf8';
		$usr = 'VxvhcCBrYg996';
		$passwrd = 's7XHzB6L';
	}
	
	try {
		// DBに接続
		$db = new PDO(
			$dsn,
			$usr,
			$passwrd,
			[
				PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION, // エラー発生時にPDOExceptionオブジェクトを返す
				PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC, // 2つのカラムをキーと値のペアとした配列で取得
			]
		);
	}
	catch (PDOException $error) {
		exit($error->getMessage()); // エラーメッセージを表示してスクリプト終了
	}

	// DBの更新
	try {
		foreach ($form_array as $form_elem) {
			$stt = $db->prepare('SELECT num_of_votes FROM voting_result_es WHERE movie_id = :id');
			$stt->bindValue(':id', $form_elem); // :idにform_elemを入れて同じIDがある場合はSELECTで投票数のカラムを取得するSQL
			$stt->execute(); // SQL実行
			
			if($row = $stt->fetch(PDO::FETCH_ASSOC)) { // 該当するDBのデータを1行取得
				// 既に同じIDがあった場合
				$stt = $db->prepare('UPDATE voting_result_es SET num_of_votes = :num WHERE movie_id = :id');
				$stt->bindValue(':num', $row['num_of_votes'] + 1); // 現在の投票数に+1
				$stt->bindValue(':id', $form_elem);
			}
			else { // 同じIDがない場合
				$stt = $db->prepare('INSERT INTO voting_result_es (movie_id, num_of_votes) VALUES (:id, :num)');
				$stt->bindValue(':id',$form_elem); // 動画ID
				$stt->bindValue(':num',1); // 票数は1
			}
			$stt->execute(); // SQL実行
		}
		// SQL実行後に投票完了サイトに遷移
		header('Location: index.php');
		exit;
	}
	catch (PDOException $error) {
		exit($error->getMessage()); // エラーメッセージを表示してスクリプト終了
	}
?>