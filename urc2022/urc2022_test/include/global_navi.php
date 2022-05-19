<?php
// ファイル名(拡張子無)と表示する文言を定義
$array = [
  "index" => "HOME",
  "02_overview" => "開催概要",
  "03_history" => "過去の大会",
  "04_committee" => "実行委員会",
  "05_contact" => "お問い合わせ"
];
?>

<body>
  <div class="container-fluid naviback">
    <div class="container">

      <ul class="nav_current nav nav-pills nav-justified">
        <?php
        foreach ($array as $key => $value) {
        ?>
          <li class="nav-item pill">
            <a class="nav-link<?php if (strcmp($currentSelection, $key . '.php') == 0) echo ' active'; ?>" href="<?php echo $key; ?>.php"><?php echo $value; ?></a>
          </li>
        <?php
        }
        ?>
      </ul>
    </div>
  </div>