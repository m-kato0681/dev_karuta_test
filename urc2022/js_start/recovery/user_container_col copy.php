<!-- 1ユーザーの表示単位 -->
<div id=<?php echo "col".$id_num; ?> class="col-6 col-md-4 col-lg-3 mt-2 mb-4">
    <!-- モーダルボタン(サムネイル) -->
    <img id=<?php echo $id_num; ?> src=<?php echo $src[$id_num]; ?> onclick="loadMov(this.id)" class="img-fluid" data-bs-toggle="modal" data-bs-target="#playerModal" onerror="this.remove(); -> console.log('ERROR');">
    <!-- 投票or投票取り消しボタン -->
    <div class="voting">
        <img id=<?php echo "votingBtn".$id_num; ?> onclick="changeBtnImg(this.id)" src="images/votingbtn_vote.png" class="d-block mx-auto img-fluid w-50 mt-1">
    </div>
    <!-- 表示タイトル -->
    <div id=<?php echo "title".$id_num; ?> class="text-center fs-6 text-truncate-line-clamp"><?php echo $mov_title_array[$num_array[$id_num]]; ?></div>
    
    <!-- モーダルボタン(サムネイル)のサイズチェック -->
    <script>
        // 画像情報取得
        var image = document.getElementById("<?php echo $id_num ?>");
    </script>
</div>


