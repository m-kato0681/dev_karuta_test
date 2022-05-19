"""
・スプライトの使い方1(個別)
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys
 
SCR_RECT = Rect(0, 0, 640, 480)
 
class MySprite(pygame.sprite.Sprite): # pygame.sprite.Spriteを継承してオリジナルのスプライトクラスを作成
    def __init__(self, filename, x, y, vx, vy): # コンストラクタ（インスタンス生成時に実行される初期化用メソッド）
        pygame.sprite.Sprite.__init__(self) # クラスを継承するために必要な処理
        """
        Spriteでは以下の3つを定義する必要がある。
        ・self.image（画像の指定）・self.rect（位置とサイズの指定）
        ・update()（1フレームでの更新処理内容の指定）
        """
        self.image = pygame.image.load(filename).convert_alpha()
        width = self.image.get_width()   # 画像の横幅を取得
        height = self.image.get_height() # 画像の立幅を取得
        self.rect = Rect(x, y, width, height)
        self.vx = vx # x移動速度を代入
        self.vy = vy # y移動速度を代入
        
    def update(self):
        self.rect.move_ip(self.vx, self.vy) # 移動速度でrectを動かす
        # 壁にぶつかったら跳ね返る
        if self.rect.left < 0 or self.rect.right > SCR_RECT.width:
            self.vx = -self.vx
        if self.rect.top < 0 or self.rect.bottom > SCR_RECT.height:
            self.vy = -self.vy
        # 画面からはみ出ないようにする
        self.rect = self.rect.clamp(SCR_RECT) # rect.clamp()を実行すると引数で指定した別のRectオブジェクトの中に収まるようにRectを移動させることができる。
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)

def main():
    pygame.init()
    screen = pygame.display.set_mode(SCR_RECT.size)
    pygame.display.set_caption(u"スプライトの使い方")
    
    # スプライトを作成 (MySpriteクラスからインスタンスを作成)
    python1 = MySprite("d:/work/pygame/test5/megaman.png", 0, 0, 2, 2)
    python2 = MySprite("d:/work/pygame/test5/megaman.png", 10, 10, 5, 5)
    python3 = MySprite("d:/work/pygame/test5/megaman.png", 320, 240, -2, 3)
    
    clock = pygame.time.Clock() # ゲームのFPSを設定する関数をインスタンス化（使いやすいように定義する）
    
    while True:
        clock.tick(60)  # 60fps
        
        screen.fill((0,0,255)) # 背景色を指定
        
        # スプライトを更新
        python1.update()
        python2.update()
        python3.update()
        
        # スプライトを描画
        python1.draw(screen)
        python2.draw(screen)
        python3.draw(screen)
        
        pygame.display.update() # 画面更新
        
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

if __name__ == "__main__":  # スクリプトを実行すると__name__に__main__が入る
                            # python特有の書き方
    main()                  # スクリプトが実行されたらmain関数を実行する