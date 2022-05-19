// カウントダウンタイマーの処理

function CountdownTimer(elm, tl, t2, mes) {
    this.initialize.apply(this, arguments);
}
CountdownTimer.prototype = {
    initialize: function (elm, tl, t2, mes) {
        this.elem = document.getElementById(elm); // CDTタグを取得
        this.tl = tl; // タイマー終了日時
        this.t2 = t2; // タイマー開始日時
        this.mes = mes; // 表示用コメント
    }, 
    countDown: function () {
        var timer = '';
        // var today = new Date(); // 本番用
        var today = new Date('2022/8/30 00:00:00'); // テスト用
        var day1 = Math.floor((this.tl - today) / (24 * 60 * 60 * 1000)); // 投票終了までの残り日数を計算
        var day2 = Math.floor((this.t2 - today) / (24 * 60 * 60 * 1000)); // 投票開始までの残り日数を計算
        // var hour = Math.floor(((this.tl - today) % (24 * 60 * 60 * 1000)) / (60 * 60 * 1000));
        // var min = Math.floor(((this.tl - today) % (24 * 60 * 60 * 1000)) / (60 * 1000)) % 60;
        // var sec = Math.floor(((this.tl - today) % (24 * 60 * 60 * 1000)) / 1000) % 60 % 60;
        // var milli = Math.floor(((this.tl - today) % (24 * 60 * 60 * 1000)) / 10) % 100;
        var me = this;

        if (0 <= day1 && day1 <= 12) { // 期間内（12日間）の場合
            timer += '投票終了まで残り ' + day1 + ' 日';
            // if (hour)
            // timer += '' + hour + '時間';
            // timer += '' + this.addZero(min) + '分' +
            //     this.addZero(sec) + '秒';
            this.elem.innerHTML = timer; // CDTタグに時刻を埋め込む
            tid = setTimeout(function () {
                me.countDown();
            }, 10);
        }
        else { // 期間外の場合
            if (day1 < 0) { // 期間後
                this.elem.innerHTML = this.mes; // CDTタグに終了コメントを埋め込む
                document.querySelector("#header_comment").innerHTML = ''; // 投票の説明文を削除
                document.querySelector("#header_comment_sub").innerHTML = ''; // 投票の説明文を削除
                // 各投票ボタンを削除する
                document.querySelector("#footer_fixed_container").innerHTML = ''; // 固定フッター削除
                const voting_elem = document.querySelectorAll(".voting"); // classがvotingbtnのものを全て取得して削除
                voting_elem.forEach(function(value){
                    value.innerHTML = '';
                });
                // 投票期間の文字列に取り消し線を引く
                document.querySelector("#voting_period").innerHTML = '<div id="voting_period" class="col-12 text-center" style="text-decoration: line-through;">投票期間：2022/8/29(月)～9/9(金)</div>';
            }
            else { // 期間前
                timer += '投票開始まで残り ' + day2 + ' 日';
                this.elem.innerHTML = timer; // CDTタグに時刻を埋め込む
                document.querySelector("#header_comment").innerHTML = ''; // 投票の説明文を削除
                document.querySelector("#header_comment_sub").innerHTML =
                    '※作品の画像を押すと動画が再生されます。<br>※現在掲載されている作品は昨年の【小学校部門】の応募作品です。<br>※今年の応募作品ではありませんのでご注意ください。'; // 投票の説明文を削除
                // 各投票ボタンを削除する
                document.querySelector("#footer_fixed_container").innerHTML = ''; // 固定フッター削除
                const voting_elem = document.querySelectorAll(".voting","#header_comment"); // classがvotingbtnのものを全て取得して削除
                voting_elem.forEach(function(value){
                    value.innerHTML = '';
                });
            }
            return;
        }
    },
    addZero: function (num) {
        return ('0' + num).slice(-2);
    }
}
function CDT() {
    var tl = new Date('2022/9/10 00:00:00'); // タイマー終了日時を設定
    var t2 = new Date('2022/8/29 00:00:00'); // タイマー開始日時を設定
    var timer = new CountdownTimer('CDT', tl, t2, '受付は終了しました'); // 終了後のコメント(期間内ならcountDown()で更新)
    timer.countDown();
}

window.onload = function () {
    CDT();
}