"""
・アニメーションの作成
・全画面表示
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame               # pygameの基本的なモジュールを読み込む
from pygame.locals import *  # pygameで扱える定数を読み込む
import sys                  # pythonの実行に必要なライブラリを読み込む

SCR_RECT = Rect(0, 0, 1024, 768) # 全画面表示は使用しているるPCの全画面の解像度に合わせる。

def load_image(filename, colorkey=None):    # 画像読み込み用の関数
    try:  # 例外が発生する可能性のあるコード
        image = pygame.image.load(filename)
    except pygame.error as message:  # 例外が発生した場合(pygameの標準エラーとして発生したオブジェクトを変数messageに格納)
        print("Cannot load image:", filename)
        raise SystemExit(message) # 自作の例外処理を実行
    image = image.convert() # 画像をピクセル化する
    if colorkey is not None: # colorkeyの中身が空ではない場合
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image


def split_image(image):
    """96x24のキャラクターイメージを24x24の4枚のイメージに分割
    分割したイメージを格納したリストを返す"""
    imageList = []  # 空のリストを用意
    for i in range(0, 96, 24):
        surface = pygame.Surface((24, 24))  # x*yのSurface（画像を描画できる場所）を用意
        surface.blit(image, (0, 0), (i, 0, 24, 24))  # 3つめの引数で描画範囲を指定
        surface.set_colorkey(surface.get_at((0, 0)), RLEACCEL)  # 透明色を取得
        surface.convert()  # ピクセル形式を変更⇒透過処理
        imageList.append(surface)  # リストに要素を追加
    return imageList


class Character(pygame.sprite.Sprite):
    animcycle = 10  # アニメーション速度
    frame = 0

    def __init__(self, filename, x, y):
        pygame.sprite.Sprite.__init__(self, self.containers) # グループ登録
        self.images = split_image(load_image(filename)) # 読み込んだ画像を分割
        self.image = self.images[0] # 分割した画像の0番目を代入
        self.rect = self.image.get_rect(topleft=(x, y)) # 0番目の画像で矩形(rect)を作成

    def update(self): # 1fごとに実行される処理
        # キャラクターアニメーション
        self.frame += 1 # 変数frameを1ずつ増加
        self.image = self.images[self.frame//self.animcycle % 4]
        # python3では[//]とすることで整数値の結果を算出できる
        # 整数の算出結果に応じて順番に画像を描画


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCR_RECT.size)
    pygame.display.set_caption(u"キャラクターアニメーション")

    all = pygame.sprite.RenderUpdates()
    Character.containers = all

    player = Character("d:/work/pygame/test9/megaman_run.png", 0, 0)

    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        screen.fill((0, 0, 255))
        all.update()
        all.draw(screen)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()


if __name__ == "__main__":
    main()
