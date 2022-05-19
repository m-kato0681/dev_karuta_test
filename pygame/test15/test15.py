"""
・マップスクロール
・BGM,SE再生
・アニメーション
・コスチューム切りかえ
・相対パス
"""
#!/usr/bin/env Megaman
#coding: utf-8
import pygame  # pygameの基本的なモジュールを読み込み
from pygame.locals import *  # pygameで扱える定数を読み込み(*で全て)
import os  # 各OSのもつ標準機能を扱うための機能を読み込み
import sys  # pythonを実行するためのライブラリを読み込み

import data


SCR_RECT = Rect(0, 0, 1024, 600)  # ウィンドウのサイズと位置を定義(left,top,width,height)
IMG_MULTI = int(SCR_RECT.width / 1024 * 4)   # 各画像を大きくするための倍率(整数で算出)


class PyAction:
    """ キー操作や画面の更新などを行うクラス """

    def __init__(self):  # コンストラクタ
        data_path = data.__path__[0] # dataフォルダのパスを取得
        pygame.init()  # pygameを初期化
        screen = pygame.display.set_mode(
            SCR_RECT.size)  # 指定したサイズでゲームウィンドウとなるスクリーンを設定
        pygame.display.set_caption("マップスクロール")  # ウィンドウのタイトルを設定

        """画像のロード"""
        # ロックマン右向き
        Megaman.right_image = load_image(data_path + "/" + "megaman.png", -1)
        # Megaman.right_image = load_image("../data/megaman.png", -1)
        Megaman.rect = Megaman.right_image.get_rect()  # 矩形情報を取得
        Megaman.right_image = pygame.transform.scale(
            Megaman.right_image, (Megaman.rect.width * IMG_MULTI, Megaman.rect.height * IMG_MULTI))  # サイズ変更
        # ロックマン左向き(第二引数：左右反転、第三引数：上下反転)
        Megaman.left_image = pygame.transform.flip(Megaman.right_image, 1, 0)
        # ロックマンジャンプ右向き
        Megaman.jump_right_image = load_image("../data/megaman_jump.png", -1)
        Megaman.rect = Megaman.jump_right_image.get_rect()  # 矩形情報を取得
        Megaman.jump_right_image = pygame.transform.scale(Megaman.jump_right_image, (
            Megaman.rect.width * IMG_MULTI, Megaman.rect.height * IMG_MULTI))  # サイズ変更
        # ロックマンジャンプ左向き
        Megaman.jump_left_image = pygame.transform.flip(
            Megaman.jump_right_image, 1, 0)
        # ロックマン走る右向き
        Megaman.run_right_image_all = load_image(
            "../data/megaman_run.png", -1)  # 分割前
        Megaman.rect = Megaman.run_right_image_all.get_rect()  # 矩形情報を取得
        Megaman.run_right_image_all = pygame.transform.scale(Megaman.run_right_image_all, (
            Megaman.rect.width * IMG_MULTI, Megaman.rect.height * IMG_MULTI))  # サイズ変更
        Megaman.run_right_image = split_image(Megaman.run_right_image_all)
        # ロックマン走る左向き
        Megaman.run_left_image_all = pygame.transform.flip(
            Megaman.run_right_image_all, 1, 0)  # 分割前
        Megaman.run_left_image = split_image(Megaman.run_left_image_all)
        # ロックマンショット右向き
        Megaman.shot_right_image = load_image("../data/megaman_shot.png", -1)
        Megaman.rect = Megaman.shot_right_image.get_rect()  # 矩形情報を取得
        Megaman.shot_right_image = pygame.transform.scale(
            Megaman.shot_right_image, (Megaman.rect.width * IMG_MULTI, Megaman.rect.height * IMG_MULTI))  # サイズ変更
        # ロックマン左向き(第二引数：左右反転、第三引数：上下反転)
        Megaman.shot_left_image = pygame.transform.flip(Megaman.shot_right_image, 1, 0)

        # ブロック
        Block.image = load_image("../data/block2.png", -1)
        Block.rect  = Block.image.get_rect()  # 矩形情報を取得
        Block.image = pygame.transform.scale(Block.image, (Block.rect.width * IMG_MULTI, Block.rect.height * IMG_MULTI))  # サイズ変更

        """音声のロード"""
        # ロックマンのSE
        Megaman.step_sound = load_sound(
            "../data/megaman_step2.wav")
        # マップのBGM
        Map.cutman_bgm = load_sound(
            "../data/cutman_stage2.wav")

        # マップデータのロード
        # self.map = Map("d:/work/pygame/test15/data/cutman.map")
        # self.map = Map("../data/cutman.map")
        self.map = Map("cutman.map")

        # メインループ
        clock = pygame.time.Clock()  # fps設定用クラスをインスタンス化
        self.fullscreen_flag = 0  # フルスクリーン表示切りかえ用の変数（0:通常、1：フル）
        while True:
            clock.tick(60) # 60
            self.update()
            self.draw(screen)
            pygame.display.update()
            self.key_handler()

    def update(self):
        self.map.update()

    def draw(self, screen):
        self.map.draw()

        offsetx, offsety = self.map.calc_offset()  # オフセットの値を格納

        # 端ではスクロールしない
        if offsetx < 0:
            offsetx = 0
        elif offsetx > self.map.width - SCR_RECT.width:
            offsetx = self.map.width - SCR_RECT.width

        if offsety < 0:
            offsety = 0
        elif offsety > self.map.height - SCR_RECT.height:
            offsety = self.map.height - SCR_RECT.height

        # マップの一部を画面に描画
        screen.blit(self.map.surface, (0, 0),
                    (offsetx, offsety, SCR_RECT.width, SCR_RECT.height))

    def key_handler(self):
        for event in pygame.event.get():
            if event.type == QUIT:  # ウィンドウのＸで終了
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_ESCAPE:  # escキーで終了
                pygame.quit()
                for i in range(2):
                    sys.exit()
            elif event.type == KEYDOWN and event.key == K_F2:  # F2キーでフルスクリーン
                self.fullscreen_flag = not self.fullscreen_flag
                if self.fullscreen_flag:
                    self.screen = pygame.display.set_mode(
                        SCR_RECT.size, FULLSCREEN)
                else:
                    self.screen = pygame.display.set_mode(SCR_RECT.size)


class Megaman(pygame.sprite.Sprite):
    """ロックマン"""
    MOVE_SPEED = 7.0    # 移動速度
    JUMP_SPEED = 25.0    # ジャンプの初速度
    GRAVITY = 1.4       # 重力加速度
    MAX_JUMP_COUNT = 1  # ジャンプ段数の回数

    def __init__(self, pos, blocks):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.right_image  # PyActionクラスでロードした右向き画像データをインスタンス変数imageに代入
        self.direction = 0  # キャラクターの向き（0:右, 1:左）
        self.run_frame = 0  # 走りアニメーション用のアニメーションコマ数
        self.rect = self.image.get_rect()  # ロードした画像の矩形情報を取得
        self.rect.x, self.rect.y = pos[0], pos[1]  # 矩形の座標を設定
        self.blocks = blocks  # pygame.sprite.Group()のインスタンスをインスタンス変数に代入

        # ジャンプ回数を数える変数を初期化
        self.jump_count = 0

        # 浮動小数点で座標と速度用の変数を定義
        self.fpx = float(self.rect.x)  # 微細な座標の更新が求められるので小数点で設定できるように変更しておく
        self.fpy = float(self.rect.y)
        self.fpvx = 0.0
        self.fpvy = 0.0

        # ブロック上にいるかを判別する用の変数
        self.on_floor = False

    def update(self):
        """スプライトの更新"""
        # キー入力取得
        pressed_keys = pygame.key.get_pressed()

        # 左右移動
        if pressed_keys[K_RIGHT]:
            self.direction = 0
            # self.image = self.right_image
            self.run_frame += 1
            self.fpvx = self.MOVE_SPEED
        elif pressed_keys[K_LEFT]:
            self.direction = 1
            # self.image = self.left_image
            self.run_frame += 1
            self.fpvx = -self.MOVE_SPEED
        else:
            self.fpvx = 0.0  # 何も押していない時はx軸スピードを0に設定
            self.run_frame = 0  # 走りアニメーションのコマ数をリセット
            # if self.on_floor and not pressed_keys[K_UP]:
            #     if not self.direction: # 右向きの時
            #         self.image = self.right_image
            #     else: # 左向きの時
            #         self.image = self.left_image

        # ジャンプ
        if pressed_keys[K_UP]:
            if self.on_floor:  # ブロック上にいる場合
                self.fpvy = - self.JUMP_SPEED  # 上向きに初速度を与える
                self.on_floor = False
                self.jump_count = 0
            # elif not self.prev_button and self.jump_count < self.MAX_JUMP_COUNT: #
            #     self.fpvy = -self.JUMP_SPEED
            #     self.jump_count += 1

        # y軸の速度を更新
        if not self.on_floor:
            # if self.jump_count > 2:
            #     if not self.direction: # 右向きの時
            #         self.image = self.jump_right_image
            #     else: # 左向きの時
            #         self.image = self.jump_left_image

            self.fpvy += self.GRAVITY  # 下向きに重力をかける
            self.jump_count += 1  # 床の上にいなければカウントアップ

        self.collision_x()  # X方向の衝突判定処理
        self.collision_y()  # Y方向の衝突判定処理

        self.costume()  # コスチュームを変更

        # 浮動小数点の位置を整数座標に戻す
        # スプライトを動かすにはself.rectの更新が必要！
        self.rect.x = int(self.fpx)
        self.rect.y = int(self.fpy)

        # ボタンのジャンプキーの状態を記録
        self.prev_button = pressed_keys[K_UP]

    def collision_x(self):
        """X方向の衝突判定処理"""
        # ロックマンのサイズを変数に代入
        width = self.rect.width
        height = self.rect.height

        # X方向の移動先の座標と矩形を求める
        newx = self.fpx + self.fpvx  # 矩形の現在の座標に速度を足す
        newrect = Rect(newx, self.fpy, width, height)

        # ブロックとの衝突判定
        for block in self.blocks:  # blocksグループに登録されたスプライト情報を変数blockに代入して順番に参照していく
            # A.colliderect(B):AとBの矩形範囲が衝突していたらTrue
            collide = newrect.colliderect(block.rect)
            if collide:  # 衝突するブロックあり
                if self.fpvx > 0:    # 右に移動中に衝突
                    # めり込まないように調整して速度を0に
                    self.fpx = block.rect.left - width
                    self.fpvx = 0
                elif self.fpvx < 0:  # 左に移動中に衝突
                    self.fpx = block.rect.right
                    self.fpvx = 0
                break  # 衝突ブロックは1個調べれば十分
            else:
                # 衝突ブロックがない場合、位置を更新
                self.fpx = newx

    def collision_y(self):
        """Y方向の衝突判定処理"""
        # ロックマンのサイズ
        width = self.rect.width
        height = self.rect.height

        # Y方向の移動先の座標と矩形を求める
        newy = self.fpy + self.fpvy  # 矩形の現在の座標に速度を足す
        newrect = Rect(self.fpx, newy, width, height)  # 新しい矩形を作成

        # ブロックとの衝突判定
        for block in self.blocks:  # blocksグループに登録されたスプライトの情報を変数blockに代入して順番に参照する
            collide = newrect.colliderect(block.rect)
            if collide:  # 衝突するブロックあり
                if self.fpvy > 0:    # 下に移動中に衝突
                    # めり込まないように調整して速度を0に
                    self.fpy = block.rect.top - height
                    if self.jump_count > 2:
                        self.step_sound.play()  # 着地の音を再生
                    self.fpvy = 0
                    # 下に移動中に衝突したなら床の上にいる
                    self.on_floor = True
                    self.jump_count = 0  # ジャンプカウントをリセット
                elif self.fpvy < 0:  # 上に移動中に衝突
                    self.fpy = block.rect.bottom
                    self.fpvy = 0
                break  # 衝突ブロックは1個調べれば十分
            else:
                # 衝突ブロックがない場合、位置を更新
                self.fpy = newy
                # 衝突ブロックがないなら床の上にいない
                self.on_floor = False

    def costume(self):
        """コスチュームの変更処理"""
        pressed_keys = pygame.key.get_pressed()
        animycle = 10  # アニメーション速度
        if self.jump_count > 2:  # 空中
            if not self.direction:  # 右向きの時
                self.image = self.jump_right_image
            else:  # 左向きの時
                self.image = self.jump_left_image
        else:
            if not pressed_keys[K_UP]:
                if self.run_frame > 0:  # 走るアニメーションのコマ数>0なら
                    if not self.direction:  # 右向きの時
                        self.image = self.run_right_image[self.run_frame//animycle % 4]
                    else:  # 左向きの時
                        self.image = self.run_left_image[self.run_frame//animycle % 4]
                else:  # 立つ
                    if not self.direction:  # 右向きの時
                        self.image = self.right_image
                    else:  # 左向きの時
                        self.image = self.left_image


class Block(pygame.sprite.Sprite):
    """ブロック"""

    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self, self.containers)  # スプライトのをグループに登録
        self.rect = self.image.get_rect()
        self.rect.topleft = pos  # ブロックの生成位置は左上を基準とする


class Map:
    """マップ（プレイヤーや内部のスプライトを含む）"""
    GS = 80 * IMG_MULTI / 5 # グリッドサイズ(クラス変数)

    def __init__(self, filename):  # コンストラクタ
        # スプライトグループの登録
        # スプライトの描画と更新を行うクラスのインスタンスをall(インスタンス変数)に代入
        self.all = pygame.sprite.RenderUpdates()
        # 複数のスプライトの情報を扱うことのできるクラスのインスタンスをblocks(インスタンス変数)に代入
        self.blocks = pygame.sprite.Group()
        # 複数のスプライトの情報を扱うことで衝突判定などを行うことができる
        Megaman.containers = self.all  # Megamanクラスをallグループに登録
        Block.containers = self.all, self.blocks  # Blockクラスをallとblocksグループに登録

        # プレイヤーの作成
        self.Megaman = Megaman((100, 200), self.blocks)
        # インスタンス変数MegamanにMegamanクラスの実行結果を代入（インスタンス化）
        # 引数には座標と、接触判定用としてインスタンス変数blocksを指定

        # マップデータをロードしてマップ内スプライトの作成
        self.load(filename)

        # マップサーフェイスを作成
        self.surface = pygame.Surface(
            (self.col*self.GS, self.row*self.GS)).convert()

        # マップBGMを作成
        self.cutman_bgm.play(-1)  # BGM再生引数は再生回数（-1でループ再生）

    def draw(self):
        """マップサーフェイスにマップ内スプライトを描画"""
        self.surface.fill((0, 50, 0))
        self.all.draw(self.surface)

    def update(self):
        """マップ内スプライトを更新"""
        self.all.update()

    def calc_offset(self):
        """オフセットを計算"""
        offsetx = self.Megaman.rect.topleft[0] - SCR_RECT.width/2
        # topleft[0](x座標) - ウィンドウ全体の半分の横幅
        offsety = self.Megaman.rect.topleft[1] - SCR_RECT.height/2
        # topleft[1](y座標) - ウィンドウ全体の半分の縦幅
        return offsetx, offsety

    def load(self, filename):
        """マップをロードしてスプライトを作成"""
        map = []  # マップ情報格納用のリスト
        fp = open(filename, "r")  # 指定したファイルをテキストとして読み込み
        for line in fp:  # 読み込んだテキストデータを変数lineに代入して処理
            # 改行で自動的に区切られ、行ごとに順番に変数lineに読み込まれる
            line = line.rstrip("\n")  # テキストデータlineから改行コードを削除
            map.append(list(line))  # mapリストの末尾にlist型のlineの要素を追加（要素は行単位になっている）
            self.row = len(map)  # mapリストの要素数を変数rowに代入
            self.col = len(map[0])  # mapリストの0番目の要素を変数colに代入
        self.width = self.col * self.GS  # map[0]なので天井の行の要素数（列数）*グリッドサイズ=横幅
        self.height = self.row * self.GS  # mapリストの要素数(行数)*グリッドサイズ=縦幅
        fp.close()  # openをしたら必ずcloseする

        # マップからスプライトを作成
        for i in range(self.row):  # 行数の回数分ループ
            for j in range(self.col):  # 天井の行の要素数（列数）分ループ
                if map[i][j] == 'B':  # i行のj列の要素を確認
                    Block((j*self.GS, i*self.GS))  # ブロックを生成


def load_image(filename, colorkey=None):
    """画像をロードして画像と矩形を返す"""
    filename = os.path.join("data", filename)
    try:  # 例外が発生する可能性のあるコード
        image = pygame.image.load(filename)
    # 例外が発生した場合(pygameの標準エラーとして発生したオブジェクトを変数messageに格納)
    except pygame.error as message:
        print("Cannot load image:", filename)
        raise SystemExit(message)  # 自作の例外処理を実行
    image = image.convert()  # 画像のピクセル形式を変更（引数がないのでPCウィンドウと同じピクセル形式（色空間）になる）
    if colorkey is not None:  # colorkeyの中身が空ではない場合
        if colorkey is -1:
            colorkey = image.get_at((0, 0))  # 透明色を取得
        # 透明色を設定(RLEACCELを設定すると描画が滑らかになる)
        image.set_colorkey(colorkey, RLEACCEL)
    return image


def split_image(image):
    """画像を分割して格納したリストを返す"""
    imageList = []  # 空のリストを用意
    for i in range(0, 96*IMG_MULTI, 24*IMG_MULTI):
        # x*yの空のSurface（画像を描画できる場所）を用意
        surface = pygame.Surface((24*IMG_MULTI, 24*IMG_MULTI))
        surface.blit(image, (0, 0), (i, 0, 24*IMG_MULTI,
                                     24*IMG_MULTI))  # 画像をSurfaceに描画
        # 引数で(画像,座標,描画範囲)を指定
        surface.set_colorkey(surface.get_at((0, 0)), RLEACCEL)  # 透明色を取得して設定
        surface.convert()  # 画像のピクセル形式を変更（引数がないのでPCウィンドウと同じピクセル形式（色空間）になる）
        imageList.append(surface)  # imageListリストの末尾に画像が描画されたSurfaceを追加
        # 描画範囲で指定した順に格納されていく
    return imageList


def load_sound(filename):
    """音声をロードする"""
    filename = os.path.join("data", filename)
    return pygame.mixer.Sound(filename)


if __name__ == "__main__":
    PyAction()
