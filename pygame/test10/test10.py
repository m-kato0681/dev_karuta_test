"""
・グループ化についての整理
・フルスクリーン
"""

import pygame
from pygame.locals import *
import sys

SCR_RECT = Rect(0, 0, 640, 480)

class MySprite(pygame.sprite.Sprite): # クラスを継承してMySpriteクラスを作成
    def __init__(self, filename, x, y, vx, vy):  # コンストラクタを定義
        pygame.sprite.Sprite.__init__(self, self.containers)
        # 親クラスを初期化(Spriteクラスを継承した際は必ず実行する)
        # 引数にGroupクラスのインスタンスを設定することで所属Groupを設定できる
        self.image = pygame.image.load(filename).convert_alpha()  # 画像を読み込んで透過処理
        width = self.image.get_width()  # 画像の横幅を読み込み
        height = self.image.get_height()  # 画像の縦幅を読み込み
        self.rect = Rect(x, y, width, height)  # 画像のrect（画像のエリアを示す四角形）を設定
        self.vx = vx # 引数(インスタンス変数)を初期化
        self.vy = vy

    def update(self):  # 1フレームごとの更新処理
        self.rect.move_ip(self.vx, self.vy)  # rectを1フレームごとに動かす
        # 壁にぶつかったら跳ね返る
        if self.rect.left < 0 or self.rect.right > SCR_RECT.width:
            self.vx = -self.vx
        if self.rect.top < 0 or self.rect.bottom > SCR_RECT.height:
            self.vy = -self.vy
        # 画面からはみ出ないようにする
        # clampの引数で指定したrect内にrectが収まるようにする
        self.rect = self.rect.clamp(SCR_RECT)


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCR_RECT.size)  # スクリーンサイズ指定
    pygame.display.set_caption(u"フルスクリーンモード")  # ディスプレイタイトル設定

    # 描画先範囲の情報を取得する
    group = pygame.sprite.RenderUpdates()    
    # Myspriteクラスのプロパティcontainersに描写先範囲の情報を代入する
    MySprite.containers = group
    
    # スプライトを作成
    python1 = MySprite("d:/work/pygame/test10/megaman.png", 0, 0, 2, 2)
    python2 = MySprite("d:/work/pygame/test10/megaman.png", 10, 10, 5, 5)
    python3 = MySprite("d:/work/pygame/test10/megaman.png", 320, 240, -2, 3)

    clock = pygame.time.Clock()

    fullscreen_flag = False

    while True:
        clock.tick(60)  # 60fps
        screen.fill((0, 0, 255)) # 背景を指定色で塗りつぶす
        group.update()  # グループの全てのSpriteの画像を更新
        group.draw(screen)  # グループの全てのSpriteの画像を引数で指定したSurface上に描画
        pygame.display.update()  # 画面を更新

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_F2:
                # F2キーでフルスクリーンモードへの切り替え
                fullscreen_flag = not fullscreen_flag  # 変数の値を逆にする
                if fullscreen_flag: # set_modeの引数にFULLSCREENを指定するとフルスクリーンになる
                    screen = pygame.display.set_mode(SCR_RECT.size, FULLSCREEN)
                else:
                    screen = pygame.display.set_mode(SCR_RECT.size, 0)


if __name__ == "__main__":
    main()
