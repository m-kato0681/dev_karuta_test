""" pygame """
""" テキストボックスサンプルの改造 """
""" ボックスの削除、お手本の表示と正誤判定 """
""" ミスタイプ数とミスタイプの割合、クリアタイムの計測　"""

import random # ランダムモジュールを読み込み
import sys # pythonを実行するためのライブラリを読み込み
import os # 各OSのもつ標準機能を扱うための機能を読み込み
import pygame as pg # pygameをimportしてpgとして定義
from pygame.locals import * # pygameで扱える定数を全て読み込み
import time # 時間を扱うモジュールを読み込み
from decimal import Decimal, ROUND_HALF_UP # 四捨五入モジュールの読み込み

def select_word():
    word_list = [
        'import random',
        'def',
        'sys',
    ]
    i = random.randint(0, len(word_list) - 1) # 指定範囲で数値をランダムに取得
    return word_list[i]

def time_set():
    start = time.time() # 計測開始時間を更新
    return start

def calc_quantize(score): # 四捨五入計算
    result = Decimal(str(score))
    result = result.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP) # 0.01の桁で四捨五入
    return result

def main():
    screen = pg.display.set_mode((640, 480)) # 指定サイズでゲームウィンドウを定義
    font = pg.font.Font(None, 32) # フォントをデフォルトに設定して文字の大きさを指定
    clock = pg.time.Clock() # pygameの時間管理に役立つオブジェクトをインスタンス化

    color_inactive = pg.Color('lightskyblue3') # pygame.Colorで色を指定
    color_active = pg.Color('dodgerblue2')
    color = color_inactive
    active = True
    text = ''
    done = False

    true_word = select_word() # ランダムで文字列を取得して代入
    start_time = time_set() # 計測開始時間を代入
    typing_stop = 0 # 文字列入力を制限するフラグ
    miss_typing = 0 # ミスタイプの回数

    while not done:
        for event in pg.event.get(): # イベントを取得して実行
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.KEYDOWN: # 何かのキーが押された場合
                if active:
                    if event.key == pg.K_RETURN: # エンターキーが押された場合
                        print(text) # 現在入力されている文字列を出力
                        text = '' # 文字列を空にする
                        true_word = select_word() # ランダムで文字列を取得して代入
                        start_time = time_set() # 計測開始時間を代入
                    elif event.key == pg.K_BACKSPACE: # バックスペースを押した場合
                        text = text[:-1] # 一番後ろの要素より前を取得して代入(1文字消える)
                        typing_stop = 0
                    elif event.key == K_ESCAPE:  # escキーで終了
                        pygame.quit()
                        sys.exit()
                    else:
                        if not typing_stop:
                            text += event.unicode # 入力された文字を文字列に追加する
                        else:
                            miss_typing += 1
                            print('ミス：', miss_typing)

        screen.fill((30, 30, 30)) # スクリーンの背景色を指定
        true_txt_surface = font.render(true_word, True, color) # お手本文字列をrenderにセット
        screen.blit(true_txt_surface, (100, 100)) # 指定位置にお手本文字列を描画

        if len(text) > 0: # 入力文字列textの文字数が0より大きい場合
            if len(text) > len(true_word): # 同時押しなどで入力文字数が上回ってしまった場合
                for i in range(len(text)-len(true_word)):
                    text = text[:-1]
            if text[-1] == true_word[len(text)-1]: # 入力文字とお手本が等しい場合
                typing_stop = 0
                input_txt_surface = font.render(text, True, color_inactive)
                screen.blit(input_txt_surface, (100, 120)) # 指定位置に入力文字列を描画
                if len(text) == len(true_word):
                    elapsed_time = calc_quantize(time.time() - start_time) # 経過時間を計算（四捨五入用に文字列に変換してDecimalオブジェクトに代入）
                    print('経過時間：', elapsed_time, '秒')
                    miss_ratio = calc_quantize((miss_typing / len(true_word) * 100)) # ミスタイプ率を計算
                    print('ミスタイプ率',miss_ratio, '%')
                    print(text) # 現在入力されている文字列を出力
                    text = '' # 文字列を空にする
                    miss_typing = 0
                    true_word = select_word() # ランダムで文字列を取得して代入
                    start_time = time_set() # 計測開始時間を代入
            else: # 入力文字とお手本が異なる場合
                if typing_stop == 0:
                    typing_stop = 1
                    miss_typing += 1
                    print('ミス：', miss_typing)
                input_txt_surface = font.render(text, True, color_active)
                screen.blit(input_txt_surface, (100, 120)) # 指定位置に入力文字列を描画

        # 最終文字のみ色付けする方法（保留）
        # if len(text) > 0: # 入力文字列textの文字数が0より大きい場合
        #     for num in range(len(text)): # 文字数分ループ
        #         if text[num] != true_word[num]: # 入力文字とお手本文字の該当箇所が異なる場合
        #             input_txt_surface = font.render(text[num], True, color_active) # 入力文字をrenderにセット
        #         else:
        #             input_txt_surface = font.render(text[num], True, color_inactive) # 入力文字をrenderにセット
        #         screen.blit(input_txt_surface, (100, 120)) # 指定位置に入力文字列を描画

        pg.display.flip() # 画面を更新
        clock.tick(30) # 動作フレームを設定（この場合は30fpsを超える速度では実行されないことになる）


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()