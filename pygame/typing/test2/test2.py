""" タイピングゲーム """
""" enterキーで文字列の切りかえ """

import random # ランダムモジュールを読み込み
import sys # pythonを実行するためのライブラリを読み込み
import os  # 各OSのもつ標準機能を扱うための機能を読み込み
import pygame # pygameの基本的なモジュールを読み込み
from pygame.locals import *  # pygameで扱える定数を読み込み(*で全て)


def select_word():
    """ 単語帳からランダムに単語を選ぶ """
    word_list = [
        'imput',
        'def',
        'sys',
        'pygame',
        'return'
    ]

    num_of_elements = len(word_list) # リストの要素数を取得
    i = random.randint(0, num_of_elements - 1) # 0<=n<num_of_elements-1 の範囲で乱数生成
    return word_list[i]


def cut_head_char(word):
    """ 文字列の先頭を削除する """
    return word[1:] # 0を除き1つめの要素以降を全て取得


def is_empty_word(word):
    """ 単語が空かチェック
    空の時はTrueを返す。"""
    return not word


def run_game():
    """ ゲーム実行 """
    pygame.init() # pygameを初期化
    screen = pygame.display.set_mode((720, 480)) # 指定サイズでゲームウィンドウとなるスクリーンを設定
    font_big = pygame.font.SysFont(None, 128) # pygame上で表示する文字のフォントと大きさを指定
    word = select_word() # ランダムで取得した文字列を代入

    while True:
        screen.fill((200, 200, 200)) # ウィンドウの背景色を指定

        sf_word = font_big.render(word, True, (0, 0, 0)) # 取得した文字列を描画
        center_x = screen.get_rect().width / 2 - sf_word.get_rect().width / 2
        # スクリーンの幅と現在描画されている文字列の幅を取得して中央値を計算
        screen.blit(sf_word, (center_x, 200)) # 指定位置に画像を描画する

        pygame.display.update() # スクリーンを更新

        for event in pygame.event.get(): # pygame.event.get()から要素を1つずつ取り出してeventに代入して実行する(pygame.event.get()はpygame実行中に起きたイベントを監視して記録する関数)
            if event.type == pygame.QUIT: # ウィンドウの×ボタンを押されたとき
                sys.exit() # システム終了
            if event.type == pygame.KEYDOWN: # 何かキーが押されたとき
                if event.key == K_KP_ENTER:
                    word = select_word() # ランダムで文字列を取得する
                else:
                    if chr(event.key) == word[0]: # 押されたキーが取得した文字列の先頭と同じ場合
                        word = cut_head_char(word) # 文字列の先頭をカットする
                        if is_empty_word(word): # 文字列の要素数が0の場合
                            word = select_word() # ランダムで文字列を取得する


run_game()