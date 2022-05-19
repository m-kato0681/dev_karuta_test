"""
・画面編集
・文字列表示
・全画面表示（全画面はWinキーで解除）
"""

import pygame
from pygame.locals import *
import sys


def main():
    pygame.init()                                   # Pygameの初期化
    screen = pygame.display.set_mode((500, 500), FULLSCREEN)    # 画面の大きさを設定(px)
    pygame.display.set_caption("Test GAME")         # タイトルバーに表示する文字
    font = pygame.font.Font(None, 55)               # フォントの設定（55px）
    while (1):
        screen.fill((255, 255, 255))      # 画面を(#)色に塗りつぶし
        text = font.render("TEST", True, (0, 0, 0))   # 描画する文字列の設定, Trueにすると文字の角が滑らかに描画される
        screen.blit(text, [0, 0])
        pygame.display.update()     # 画面を更新
        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:  # 閉じるボタンが押されたら終了
                pygame.quit()       # Pygameの終了(画面閉じられる)
                sys.exit()


if __name__ == "__main__":
    main()
