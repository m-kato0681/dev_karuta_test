// ブラウザバックを禁止する
history.pushState(null, null, null); // 直前の履歴スタックに空のオブジェクト(アクセス先がない状態)を追加
window.addEventListener('popstate', (e) => { // 履歴が変更された際のリスナー
	location = "https://www.urc21.org/test/urc2022_test/"; // URCのトップページにアクセス
});
