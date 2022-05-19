"""
・キー操作
・キャラ操作2
・BGM,SE再生
・画面端に接触した時の処理
"""
# -*- coding: utf-8 -*-
import pygame               # pygameの基本的なモジュールの読み込み
from pygame.locals import * # pygameで使える定数の読み込み（pygame.key参照）
import sys                  # pythonの実行に必要なライブラリの読み込み

(SCR_WIDTH, SCR_HEIGHT) = (288, 240)   # 画面サイズ
(x, y) = (SCR_WIDTH/2, SCR_HEIGHT/2)
pygame.init()       # pygame初期化
screen = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT))  # 画面設定
pygame.display.set_caption("test5")        # ウィンドウタイトル設定

# 画像をロード
player = pygame.image.load("d:/work/pygame/test5/megaman.png")
bg     = pygame.image.load("d:/work/pygame/test5/stage.png")
player_rect = player.get_rect()    # 画像の情報(rect)を取得
player_rect.center = (x, y)        # 画像の中心値を指定（初期値）

# 効果音をロード
step_sound = pygame.mixer.Sound("d:/work/pygame/test5/step.wav")

clock = pygame.time.Clock()        # ゲームのFPSを設定する関数

# BGMを再生
pygame.mixer.music.load("d:/work/pygame/test5/cutman.wav")
pygame.mixer.music.play(-1)        # 引数は再生回数（-1でループ再生）

while (1):
    clock.tick(60)  # 60fps(1secに60回描画する)

    # キーの入力をチェック
    pressed_key = pygame.key.get_pressed()
    if pressed_key[K_LEFT]:
        player_rect.move_ip(-2, 0)
    if pressed_key[K_RIGHT]:
        player_rect.move_ip(2, 0)
    if pressed_key[K_UP]:
        player_rect.move_ip(0, -2)
    if pressed_key[K_DOWN]:
        player_rect.move_ip(0, 2)

    # 画面端に接触した時の処理
    if player_rect.left < 0: 
        step_sound.play()
        player_rect.move_ip(2, 0)
    if player_rect.right > SCR_WIDTH:
        step_sound.play()
        player_rect.move_ip(-2, 0)
    if player_rect.bottom > SCR_HEIGHT:
        step_sound.play()
        player_rect.move_ip(0, -2)
    if player_rect.top < 0:
        step_sound.play()
        player_rect.move_ip(0, 2)

    screen.fill((0, 20, 0, 0))  # 画面の背景色を設定
    screen.blit(bg, (0, 0))     # 背景画像の描画
    screen.blit(player, player_rect)   # プレイヤー画像の描画
    pygame.display.update()     # 画面更新

    # 終了用のイベント処理
    for event in pygame.event.get():
        if event.type == QUIT:          # 閉じるボタンが押されたとき
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:       # キーが押されたとき
            if event.key == K_ESCAPE:   # Escキーが押されたとき
                pygame.quit()
                sys.exit()