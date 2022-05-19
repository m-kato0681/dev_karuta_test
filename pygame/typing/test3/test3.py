""" タイピングゲーム """
""" 打ち込んだ文字を表示する """

import random # ランダムモジュールを読み込み
import sys # pythonを実行するためのライブラリを読み込み
import os  # 各OSのもつ標準機能を扱うための機能を読み込み
import pygame # pygameの基本的なモジュールを読み込み
from pygame.locals import *  # pygameで扱える定数を読み込み(*で全て)

myword = []

def stock_word(word):
    """ 入力した文字列をリストに保存していく """
    myword.append(word)
    num_of_elements = len(myword) # リストの要素数を取得


def run_game():
    """ ゲーム実行 """
    pygame.init() # pygameを初期化
    screen = pygame.display.set_mode((720, 480)) # 指定サイズでゲームウィンドウとなるスクリーンを設定
    font_big = pygame.font.SysFont(None, 128) # pygame上で表示する文字のフォントと大きさを指定

    while True:
        screen.fill((200, 200, 200)) # ウィンドウの背景色を指定

        sf_word = font_big.render(''.join(myword), True, (0, 0, 0)) # 取得した文字列を描画
        center_x = screen.get_rect().width / 2 - sf_word.get_rect().width / 2
        # スクリーンの幅と現在描画されている文字列の幅を取得して中央値を計算
        screen.blit(sf_word, (center_x, 200)) # 指定位置に画像を描画する

        pygame.display.update() # スクリーンを更新

        for event in pygame.event.get(): # pygame.event.get()から要素を1つずつ取り出してeventに代入して実行する(pygame.event.get()はpygame実行中に起きたイベントを監視して記録する関数)
            if event.type == pygame.QUIT: # ウィンドウの×ボタンを押されたとき
                sys.exit() # システム終了
            if event.type == pygame.KEYDOWN: # 何かキーが押されたとき
                print(event.key)
                if event.key != 1073742049:
                    stock_word(chr(event.key)) # 押されたキーを文字列に変換してリストに追加する

run_game()