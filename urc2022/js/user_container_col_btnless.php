<!-- 1ユーザーの表示単位 -->
<div id=<?php echo "col".$id_num; ?> class="col-12 col-md-6 col-lg-4 col-xl-3 mt-2 mb-4">
    <!-- モーダルボタン(サムネイル) -->
    <img id=<?php echo $id_num; ?> src=<?php echo $src[$id_num]; ?> onclick="loadMov(this.id)" class="img-fluid mx-auto d-block" data-bs-toggle="modal" data-bs-target="#playerModal" onerror="this.remove(); -> console.log('ERROR');">
    <!-- 表示タイトル -->
    <div id=<?php echo "title".$id_num; ?> class="movie-title text-center text-truncate-line-clamp"><?php echo $mov_title_array[$num_array[$id_num]]; ?></div>
    
    <!-- モーダルボタン(サムネイル)のサイズチェック -->
    <script>
        // 画像情報取得
        var image = document.getElementById("<?php echo $id_num ?>");
    </script>
</div>