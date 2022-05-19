<!-- 動画再生用モーダルの設定 -->
<div class="modal fade" id="playerModal" tabindex="-1">
    <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content bg-transparent border-0">
            <!-- モーダル閉じる用のボタン -->
            <div class="modal-header border-0 p-1">
                <button type="button" class="btn-close btn-close-white fs-4" data-bs-dismiss="modal" aria-label="閉じる"></button>
            </div>
            <div class="modal-body p-0">
                <div class="ratio ratio-16x9">
                    <div id="player"></div>
                </div>
            </div>
        </div>
    </div>
</div>
<!-- 投票完了確認用モーダルの設定 -->
<div class="modal fade" id="finishModal" tabindex="-1" role="dialog" aria-labelledby="basicModal" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
            <div class="modal-header justify-content-center">
                <h3 class="modal-title">
                    <label>投票を完了しますか？</label>
                </h3>
            </div>
            <div class="modal-body text-center">
                <label>※投票を完了すると再投票までに24時間が必要です。</label>
            </div>
            <div class="modal-footer justify-content-center">
                <button type="button" class="btn btn-default" data-bs-dismiss="modal">いいえ</button>
                <button type="button" class="btn btn-danger" onclick="finishVoting()" data-bs-dismiss="modal">はい</button>
            </div>
        </div>
    </div>
</div>
<!-- 投票条件アナウンス用モーダルの設定 -->
<div class="modal fade" id="alertModal" tabindex="-1" role="dialog" aria-labelledby="basicModal" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
            <div class="modal-body text-center">
                <label style="color: rgba(255, 0, 0, 0.8);">
                    <strong><i class="fas fa-exclamation-triangle"></i> 2票以上投票してください。</strong>
                </label>
            </div>
        </div>
    </div>
</div>
<!-- 投票取り消し確認用モーダルの設定 -->
<div class="modal fade" id="deleteModal" tabindex="-1" role="dialog" aria-labelledby="basicModal" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
            <div class="modal-header justify-content-center">
                <h3 class="modal-title">
                    <label>投票を取り消しますか？</label>
                </h3>
            </div>
            <div class="modal-body text-center">
                <label>※投票中のものを全て投票前の状態に戻します。</label>
                <label>過去に投票を完了したものは取り消されません。</label>
            </div>
            <div class="modal-footer justify-content-center">
                <button type="button" class="btn btn-default" data-bs-dismiss="modal">いいえ</button>
                <button type="button" class="btn btn-danger" onclick="deleteVoting()" data-bs-dismiss="modal">はい</button>
            </div>
        </div>
    </div>
</div>