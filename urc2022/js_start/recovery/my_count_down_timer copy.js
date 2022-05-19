// カウントダウンタイマーの処理

function CountdownTimer(elm, tl, mes) {
    this.initialize.apply(this, arguments);
}
CountdownTimer.prototype = {
    initialize: function (elm, tl, mes) {
        this.elem = document.getElementById(elm); // CDTタグを取得
        this.tl = tl; // タイマー終了日時
        this.mes = mes; // 表示用コメント
    }, countDown: function () {
        var timer = '';
        var today = new Date();
        var day = Math.floor((this.tl - today) / (24 * 60 * 60 * 1000));
        // var hour = Math.floor(((this.tl - today) % (24 * 60 * 60 * 1000)) / (60 * 60 * 1000));
        // var min = Math.floor(((this.tl - today) % (24 * 60 * 60 * 1000)) / (60 * 1000)) % 60;
        // var sec = Math.floor(((this.tl - today) % (24 * 60 * 60 * 1000)) / 1000) % 60 % 60;
        // var milli = Math.floor(((this.tl - today) % (24 * 60 * 60 * 1000)) / 10) % 100;
        var me = this;

        if ((this.tl - today) > 0) { // 期間内の場合
            if (day)
            timer += '残り ' + day + ' 日';
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
            this.elem.innerHTML = this.mes; // CDTタグに終了コメントを埋め込む
            // 各投票ボタンを削除する
            document.querySelector("#finishbtn").innerHTML = '';
            document.querySelector("#deletebtn").innerHTML = '';
            const voting_elem = document.querySelectorAll(".voting"); // classがvotingbtnのものを全て取得
            voting_elem.forEach(function(value){
                value.innerHTML = '';
            });div
            document.querySelector("#voting_period").innerHTML = '<div id="voting_period" class="col-12 col-sm-7 col-md-5 col-lg-3 text-center" style="text-decoration: line-through;">投票期間：2022/8/29(月)～9/9(金)</div>';
            return;
        }
    }, addZero: function (num) {
        return ('0' + num).slice(-2);
    }
}
function CDT() {
    var tl = new Date('2022/9/9 24:00:00');// タイマー終了日時を設定(本番)
    // var tl = new Date('2022/1/19 17:16:00');// タイマー終了日時を設定(テスト)
    var timer = new CountdownTimer('CDT', tl, '受付は終了しました'); // 終了後のコメント(期間内ならcountDown()で更新)
    timer.countDown();
}

window.onload = function () {
    CDT();
}