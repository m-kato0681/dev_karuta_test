
<?php
$path = './'; 
include(dirname(__FILE__).'/include/header.php');
$currentSelection = basename(__FILE__);
include(dirname(__FILE__).'/include/global_navi.php'); ?>
<div class="container text-center">
	<h1 class="contenttitle text-center">開催概要</h1>
	<div class="text18px">
		以下の2部門から選んで参加申し込みください。<br class="for_pc">詳細は各部門名をクリックしてご確認ください。</div>
	<div class="text16px">※複数部門への応募は可能ですが、1部門につき1エントリーまでとします。</div>
	<div class="col-xs-12 col-md-10 col-md-offset-1 panel_margin">
		<div class="panel_blue">
			<div class="panel panel-default">
				<div class="panel-heading">
					<p class="panel-title text-center"> <a data-toggle="collapse" data-parent="#accordion" href="#collapseOne">アイデアコンテスト部門<br class=for_mobile>（クリックで開閉）</a> </p>
				</div>
				<div id="collapseOne" class="panel-collapse collapse">
					<div class="panel-body">
						<div class="text18px">オリジナルの作品づくりに挑戦し、YouTubeに動画をアップロードして参加します。</div>
						<div class="text16px">※応募時にYouTube投稿されたロボットの動画およびアイデアシート・プログラムファイルが必要です。</div>
						<h2>2021年のテーマ</h2>
						<div class="text28px">『感染症対策』</div>
						<h2>＜ 参加資格 ＞</h2>
						<div class="text18px">小学生または中学生</div>
						<h2>＜ 参加費用 ＞</h2>
						<div class="text18px">1,000円（税込み）</div>
						<h2>＜ 競技ルール ＞</h2>
						<div class="text16px">※競技ルールについてはこちらからダウンロードしてください</div>
						<a href="#" class="btn btn-success">アドバンス部門<br class=for_mobile>ルールブック（PDF）</a>
						<h2>＜ 参加概要 ＞</h2>
						<div class="text16px">※参加概要についてはこちらからダウンロードしてください。</div>
						<a href="#" class="btn btn-success">&nbsp;参加概要（PDF）&nbsp;</a>
						<h2>＜ 競技参加用動画サンプル ＞</h2>
						<!-- 16:9 aspect ratio -->
						<div class="lb-embed">
							<div class="embed-responsive embed-responsive-16by9">
								<iframe src="https://www.youtube.com/embed/3lcAIl41VK0" frameborder="0" allowfullscreen></iframe>
							</div>
						</div>
						<h2>＜入賞者には豪華賞品をプレゼント＞</h2>
						<img src="images/overview/prize.png" class="img-responsive center-block img_margin" alt="">
						<div class="text20px">投稿された動画を元に実行委員会によりルールに基づき厳正に採点します。</div>
						<div class="text20px">結果は9月27日にこのサイト上で公開します。</div>
						<br>
						<div class="col-xs-12 col-md-8 col-md-offset-2">
							<a href="#" class="btn btn-primary btn-block">応募フォームはこちら<br>応募期間<br class=for_mobile>2022年<br class=for_mobile>00月00日～00月00日まで</a>
							<br>
							<a data-toggle="collapse" data-parent="#accordion" href="#collapseOne" class="btn btn-danger">&nbsp;×閉じる&nbsp;</a>
						</div>
					</div>
				</div>
			</div>
			<div class="panel_red">
				<div class="panel panel-default">
					<div class="panel-heading">
						<p class="panel-title text-center"> <a data-toggle="collapse" data-parent="#accordion" href="#collapseTwo">シミュレーションロボット競技部門<br class=for_mobile>（クリックで開閉）</a> </p>
					</div>
					<div id="collapseTwo" class="panel-collapse collapse">
						<div class="panel-body">
							<div class="text18px">インターネットブラウザー上で動作する「ロボットシミュレーター」を用いて<br class="for_pc">オンラインでプログラミングスキルを競います。</div>
							<h2>＜ 開催日程 ＞</h2>
							<div class="text22px_red">日本予選：2021年9月4日（土）15:00～</div>
							<div class="text22px_red">決勝戦：2021年9月18日（土）15:00～</div>
							<h2>2021年のテーマ</h2>
							<div class="text28px">『ウイルス対策ロボット』</div>
							<h2>＜ 参加資格 ＞</h2>
							<div class="text18px">小学生または中学生</div>
							<h2>＜ 参加費用 ＞</h2>
							<div class="text18px">2,200円（税込み）</div>
							<h2>＜ 参加概要 ＞</h2>
							<div class="text16px">※参加概要についてはこちらからダウンロードしてください。</div>
							<a href="#" class="btn btn-success">参加概要（PDF）</a>
							<h2>＜入賞者には豪華賞品をプレゼント＞</h2>
							<img src="images/overview/prize.png" class="img-responsive center-block img_margin" alt="">
							<div class="text20px">日本予選結果は、9月10日にこのサイト上で公開します。</div>
							<div class="text20px">上位入賞者は、9月18日の決勝戦に参加できます。</div>
							<div class="text20px">決勝戦の結果は、9月27日にこのサイト上で公開します。</div>
							<br>
							<div class="col-xs-12 col-md-8 col-md-offset-2">
								<a href="#" class="btn btn-primary btn-block">応募フォームはこちら<br>応募期間<br class=for_mobile>2022年<br class=for_mobile>00月00日～00月00日まで</a>
								<br>
								<a data-toggle="collapse" data-parent="#accordion" href="#collapseTwo" class="btn btn-danger">&nbsp;×閉じる&nbsp;</a>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</div>
</section>
<?php include(dirname(__FILE__).'/include/footer.php'); ?>
