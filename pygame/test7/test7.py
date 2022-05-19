"""
・スプライトの使い方2(スプライトグループ)
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame                # pygameの基本的なモジュールの読み込み
from pygame.locals import *  # pygameで使える定数の読み込み（pygame.key参照）
import sys                   # pythonの実行に必要なライブラリの読み込み

SCR_RECT = Rect(0, 0, 640, 480)

class MySprite(pygame.sprite.Sprite): # クラスを継承して新しいクラスを作成
    def __init__(self, filename, x, y, vx, vy): # コンストラクタ
        pygame.sprite.Sprite.__init__(self) # 継承する親クラスを作成したクラスで初期化
        self.image = pygame.image.load(filename).convert_alpha()
        width = self.image.get_width()
        height = self.image.get_height()
        self.rect = Rect(x, y, width, height)
        self.vx = vx
        self.vy = vy
        
    def update(self): # 1フレームごとの更新処理
        self.rect.move_ip(self.vx, self.vy)
        # 壁にぶつかったら跳ね返る
        if self.rect.left < 0 or self.rect.right > SCR_RECT.width:
            self.vx = -self.vx
        if self.rect.top < 0 or self.rect.bottom > SCR_RECT.height:
            self.vy = -self.vy
        # 画面からはみ出ないようにする
        self.rect = self.rect.clamp(SCR_RECT)

def main():
    pygame.init()
    screen = pygame.display.set_mode(SCR_RECT.size)
    pygame.display.set_caption(u"スプライトグループの使い方")
    
    # スプライトを作成
    python1 = MySprite("d:/work/pygame/test7/megaman.png", 0, 0, 2, 2)
    python2 = MySprite("d:/work/pygame/test7/megaman.png", 10, 10, 5, 5)
    python3 = MySprite("d:/work/pygame/test7/megaman.png", 320, 240, -2, 3)
    
    # スプライトグループを作成してスプライトを追加
    group = pygame.sprite.RenderUpdates() # スプライトグループの更新と描画を行うクラス
    group.add(python1) # addメソッドを実行し、スプライトをグループに追加
    group.add(python2)
    group.add(python3)

    clock = pygame.time.Clock()

    while True:
        clock.tick(60)  # 60fps
        screen.fill((0,0,255))
        group.update() # スプライトグループを更新
        group.draw(screen) # スプライトグループを描画
        pygame.display.update() # 画面を更新

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
 
if __name__ == "__main__":
    main()