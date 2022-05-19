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
</head>
<body>
    <!-- ヘッダー -->
    <header>
        <?php include "header.php" ?>
    </header>
    <!-- アクセスログを作成 -->
    <?php include "accesslog.php" ?>
    <div  class="text-center">
        投票ありがとうございました！<br>投票再開まで今しばらくお待ちください。
    </div>
    <script>
        // ブラウザバックを禁止する
        history.pushState(null, null, location.href); // 直前の履歴スタックに空のオブジェクト(アクセス先がない状態)を追加して
        window.addEventListener('popstate', (e) => { // popstate:履歴変更時に自動で起動
            history.go(1); // 1つ前の履歴にあるサイト(追加した空のサイト)にアクセス
        });
    </script>
</body>
</html>