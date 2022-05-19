"""
・キー操作
・キャラ操作1
"""
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys

def main():
    (w,h) = (288,240)   # 画面サイズ
    (x,y) = (w/2, h/2)  # x軸y軸の中心を設定画面の中心にする
    pygame.init()       # pygame初期化
    pygame.display.set_mode((w, h))  # 画面設定
    screen = pygame.display.get_surface()   # 画面の情報をscreenに代入

    # 背景画像の取得
    bg = pygame.image.load("d:/work/pygame/test4/stage.png")
    # プレイヤー画像の取得
    player = pygame.image.load("d:/work/pygame/test4/megaman.png")

    while (1):
        # キーイベント処理(キャラクタ画像の移動)
        pressed_key = pygame.key.get_pressed()
        if pressed_key[K_LEFT]:
            x-=2
        if pressed_key[K_RIGHT]:
            x+=2
        if pressed_key[K_UP]:
            y-=2
        if pressed_key[K_DOWN]:
            y+=2

        pygame.display.update()     # 画面更新
        pygame.time.wait(30)        # 更新時間間隔
        screen.fill((255, 255, 255, 0)) # 画面の背景色
        screen.blit(bg, (0, 0))

        # 円を描画
        # pygame.draw.circle(screen, (0, 200, 0), (int(x), int(y)), 5)
        
        # キャラクターを描画
        screen.blit(player, (int(x), int(y)))

        # イベント処理
        for event in pygame.event.get():
            # 画面の閉じるボタンを押したとき
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # キーを押したとき
            if event.type == KEYDOWN:
                # ESCキーなら終了
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()


if __name__ == "__main__":
    main()