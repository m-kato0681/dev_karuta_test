<!-- サイト内検索 -->
<div id="search_box" class="container-fluid">
	<div class="row justify-content-center">
		<input type="text" id="search_text" placeholder="探したい作品名を入力"  class="col-7 col-sm-5 col-md-4 col-lg-4 col-xl-3 mx-1">
		<input type="button" id="search_button" value="検索" class="col-3 col-md-1 col-lg-1 col-xl-1 mx-1 btn btn-light">
		<div id="search_notfound_txt" class="col-12 text-center"></div> <!-- 検索がヒットしなかった場合の説明文 -->
		<input type="button" id="search_reset_button" onclick="location.href='#'" value="一覧に戻る" class="col-5 col-md-2 col-lg-2 col-xl-1 mx-1 btn btn-light">
	</div>
</div>
<!-- スクロールによる表示非表示処理 -->
<script>
	var search_Box = $('#search_box');
	search_Box.show();
	let scrollPoint
	let lastPoint
	// 検索エリアの表示非表示処理
	$(window).scroll(function () {
		var winw = $(window).innerWidth(); //ウィンドウの幅
		if (winw < 575) { // ウィンドウ幅が575pxより小さい時のみ実行
			scrollPoint = window.scrollY; // Y座標を記録
			// 下スクロールの場合
			if (scrollPoint > lastPoint && scrollPoint > 100) {
				search_Box.hide();
			}
			else { // 上スクロールの場合
				search_Box.show();
			}
			lastPoint = scrollPoint;
		}
	});
</script>