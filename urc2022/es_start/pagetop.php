<!-- ページトップボタン -->
<div id="pagetop">
	<a href="#"><img src="images/top_btn.png" class="w-75"></a>
</div>
<!-- スクロールによる表示非表示処理 -->
<script>
	var topBtn = $('#pagetop');
	topBtn.hide();

	// ボタンの表示非表示処理
	$(window).scroll(function () {
		var winw = $(window).innerWidth(); //ウィンドウの幅
		if (winw > 575) { // ウィンドウ幅が575pxより大きい時のみ表示
			//スクロールが100に達したらボタン表示
			if ($(this).scrollTop() > 100) {
				topBtn.fadeIn("slow");
			}
			else {
				topBtn.fadeOut('slow');
			}
		}
		else {
			topBtn.fadeOut('slow');
		}
	});

	// クリックでスクロール処理
    topBtn.click(function () {
        $('body,html').animate({
            scrollTop: 0
        }, 0);
        return false;
    });
</script>