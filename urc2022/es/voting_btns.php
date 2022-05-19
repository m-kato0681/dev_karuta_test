<!-- 投票完了・取り消しボタン -->
<div id="footer_fixed_container" class="container-fluid">
    <div id="voting_btns_container" class="row align-items-center justify-content-center">
        <!-- PC表示用の余白,sm以上で表示 -->
        <div id="fixed_bottom_margin_pc" class="col-12 d-none d-sm-inline"></div>
        <div id="fixed_bottom_margin" class="col-12"></div> <!-- 余白 -->
        <!-- 投票完了ボタン -->
        <div id="finishbtn" class="col-8 col-sm-5 col-md-4 col-lg-3 col-xl-3 align-item-center my-1">
            <!-- <img id="voting_finish_btn" src="images/votingbtn_finish.png" class="voting img-fluid" data-bs-toggle="modal" data-bs-target="#finishModal"> -->
            <img id="voting_finish_btn" src="images/votingbtn_finish.png" class="voting img-fluid" onclick="compare_voting_time()">
        </div>
        <!-- 投票取り消しボタン -->
        <div id="deletebtn" class="col-8 col-sm-5 col-md-4 col-lg-3 col-xl-3 align-item-center my-1">
            <img id="voting_delete_btn" src="images/votingbtn_delete.png" class="voting img-fluid" data-bs-toggle="modal" data-bs-target="#deleteModal">
        </div>
        <div id="fixed_bottom_margin" class="col-12"></div> <!-- 余白 -->
        <!-- PC表示用の余白,sm以上で表示 -->
        <div id="fixed_bottom_margin_pc" class="col-12 d-none d-sm-inline"></div>
    </div>
</div>
