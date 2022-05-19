"""
・画像の描画（キャラと背景）
"""

import pygame
from pygame.locals import *
import sys

def main():
    pygame.init()       # pygame初期化
    pygame.display.set_mode((288, 240))  # 画面設定
    screen = pygame.display.get_surface()
    
    # 背景画像の取得
    bg = pygame.image.load("d:/work/pygame/test3/stage.png")
    # プレイヤー画像の取得
    player = pygame.image.load("d:/work/pygame/test3/megaman.png")

    while (1):
        pygame.time.wait(30)                 # 更新時間間隔
        pygame.display.update()              # 画面更新
        screen.fill((0, 100, 0))             # 画面の背景色
        
        screen.blit(bg, (0, 0))              # 背景画像の描画

        screen.blit(player, (0,0))           # プレイヤー画像の描画

        # 終了用のイベント処理
        for event in pygame.event.get():
            if event.type == QUIT:           # 閉じるボタンが押されたとき
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:        # キーを押したとき
                if event.key == K_ESCAPE:    # Escキーが押されたとき
                    pygame.quit()
                    sys.exit()

if __name__ == "__main__":
        main()