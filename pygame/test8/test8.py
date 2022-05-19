"""
・スプライトの使い方3(デフォルトスプライトグループ)
（スプライトの作成と同時にグループに追加する方法
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame               # pygameの基本的なモジュールを読み込む
from pygame.locals import * # pygameで扱える定数を読み込む
import sys                  # pythonの実行に必要なライブラリを読み込む
 
SCR_RECT = Rect(0, 0, 640, 480)
 
class MySprite(pygame.sprite.Sprite): # Spriteクラスを継承して新しいクラスを作成
    def __init__(self, filename, x, y, vx, vy): # コンストラクタ
        # デフォルトグループをセット
        pygame.sprite.Sprite.__init__(self, self.containers)
        # 新しく作成したクラスで親クラスを初期化し、スプライトクラス内でグループを指定する
        # .containersはクラスの定義とは別の部分で指定する
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
    pygame.display.set_caption(u"スプライトグループの使い方2")
    
    # スプライトグループを作成してスプライトクラスに割り当て
    group = pygame.sprite.RenderUpdates() # スプライトグループの更新と描画を行うクラス
    MySprite.containers = group # Myspriteクラスのプロパティcontainersにグループを代入
    
    # スプライトを作成
    # 上で既にMySpriteクラスは「group」というグループが指定されているので
    # addをせずにスプライトを作成するだけで、グループの指定が行える
    python1 = MySprite("d:/work/pygame/test8/megaman.png", 0, 0, 2, 2)
    python2 = MySprite("d:/work/pygame/test8/megaman.png", 10, 10, 5, 5)
    python3 = MySprite("d:/work/pygame/test8/megaman.png", 320, 240, -2, 3)
    
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