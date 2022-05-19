"""
・キーボードによる横移動
"""
#!/usr/bin/env python
#coding: utf-8
import pygame   # pygameの基本的なモジュールを読み込む
from pygame.locals import * # pygameで使う定数を読み込む
import os   # OSに依存した機能を利用するためのモジュールを読み込む
import sys  # pythonを実行するために必要なライブラリを読み込む

SCR_RECT = Rect(0, 0, 640, 480) # ScreenのサイズをRect（四角形）で定義

class PyAction: # 新しいクラスを定義
    def __init__(self): # コンストラクタを定義
        pygame.init()   # pygameを初期化
        screen = pygame.display.set_mode(SCR_RECT.size) # SCR_RECTのサイズに従ってscreenを定義
        pygame.display.set_caption("左右移動")  # ウィンドウのタイトルを設定
        
        # 画像のロード
        # 左向きの画像を設定
        Python.right_image = load_image("d:/work/pygame/test12/megaman.png", -1)
        # 右向きの画像を設定
        # 左右反転：第二引数を1, 上下反転：第三引数を1
        Python.left_image = pygame.transform.flip(Python.right_image, 1, 0)
        
        # オブジェクとグループと蛇の作成
        # 描画先範囲の情報を取得する
        self.all = pygame.sprite.RenderUpdates()
        # Pythonクラスのプロパティcontainersに描写先範囲の情報を代入する
        Python.containers = self.all
        Python()
        
        # メインループ
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            self.update()
            self.draw(screen)
            pygame.display.update()
            self.key_handler()

    def update(self):
        """スプライトの更新"""
        self.all.update()
    
    def draw(self, screen):
        """スプライトの描画"""
        screen.fill((0,0,0))
        self.all.draw(screen)
    
    def key_handler(self):
        """キー入力処理"""
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

class Python(pygame.sprite.Sprite): # Spriteクラスを継承してPythonクラス作成
    """パイソン"""
    MOVE_SPEED = 5.0  # 移動速度
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.right_image
        self.rect = self.image.get_rect()
        self.rect.bottom = SCR_RECT.bottom
        
        # 浮動小数点の位置と速度
        self.fpx = float(self.rect.x)
        self.fpy = float(self.rect.y)
        self.fpvx = 0.0
        self.fpvy = 0.0
    
    def update(self):
        """スプライトの更新"""
        # キー入力取得
        pressed_keys = pygame.key.get_pressed()

        # 左右移動
        if pressed_keys[K_RIGHT]:
            self.image = self.right_image
            self.fpvx = self.MOVE_SPEED
        elif pressed_keys[K_LEFT]:
            self.image = self.left_image
            self.fpvx = -self.MOVE_SPEED
        else:
            self.fpvx = 0.0
        
        # 浮動小数点の位置を更新
        self.fpx += self.fpvx
        
        # 浮動小数点の位置を整数座標に戻す
        # スプライトを動かすにはself.rectの更新が必要！
        self.rect.x = int(self.fpx)
        self.rect.y = int(self.fpy)

def load_image(filename, colorkey=None):
    """画像をロードして画像と矩形を返す"""
    filename = os.path.join("data", filename)
    try:
        image = pygame.image.load(filename)
    except pygame.error as message:
        print("Cannot load image:", filename)
        raise SystemExit(message)
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image

if __name__ == "__main__":
    PyAction()