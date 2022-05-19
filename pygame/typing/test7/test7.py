""" pygame """
""" test6 + 複数お手本ファイルの読み込み """

import random # ランダムモジュールを読み込み
import sys # pythonを実行するためのライブラリを読み込み
import os # 各OSのもつ標準機能を扱うための機能を読み込み
import pygame as pg # pygameをimportしてpgとして定義
from pygame.locals import * # pygameで扱える定数を全て読み込み
import time # 時間を扱うモジュールを読み込み
from decimal import Decimal, ROUND_HALF_UP # 四捨五入モジュールの読み込み

# 読み書き用ファイルのパスを定義
memo = ['memo1.txt', 'memo2.txt']

def file_read(name): # ファイル読み込み
    with open(name, 'r', encoding='utf-8') as f1: # 指定したファイルを読み込み用で開いてf1と名づける
        word_list = f1.read().split("\n") # 改行を区切りとしてf1の中身を読み込んでリスト化
        return word_list
        
# def select_word_random():
#     word_list = file_read(memo)
#     i = random.randint(0, len(word_list) - 1) # 指定範囲で数値をランダムに取得
#     return word_list[i]

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

    elapsed_time = 0 # タイピング経過時間計測用変数
    miss_ratio   = 0 # ミスタイプ率格納用変数

    color_active   = pg.Color(255,150,0,0) # お手本の該当文字列
    color_inactive = pg.Color(255,255,255,0)   # お手本の非該当文字列
    color_true     = pg.Color(0,150,255,0)   # 正しい入力文字列 & 表示用文字列
    color_false    = pg.Color(255,0,0,0)   # 誤った入力文字列
    key_active = True # キーの入力を制御するフラグ
    text = '' # 入力用の文字列
    display_text = [] # 表示用文字列の配列
    done = False

    # true_word = select_word() # ランダムで文字列を取得して代入
    start_time = time_set() # 計測開始時間を代入
    typing_stop = 0 # 文字列入力を制限するフラグ
    miss_typing = 0 # ミスタイプの回数
    comp_typing = 0 # 文字列を正しく打ち終わったことを判別するためのフラグ
    target_line = 0 # お手本文字のリストと入力文字のリストの該当箇所を指定する変数

    target_file = 0 # お手本となるファイルを指定するための変数
    true_word = file_read(memo[target_file]) # file_readで取得した文字列のリストを代入

    while not done:
        for event in pg.event.get(): # イベントを取得して実行
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.KEYDOWN: # 何かのキーが押された場合
                if key_active:
                    if event.key == pg.K_RETURN: # エンターキーが押された場合
                        if comp_typing == 1:
                            elapsed_time += calc_quantize(time.time() - start_time) # 経過時間を計算（四捨五入用に文字列に変換してDecimalオブジェクトに代入）
                            # miss_ratio += calc_quantize((miss_typing / len(true_word[target_line]) * 100)) # ミスタイプ率を計算
                            display_text.append(text) # 入力文字を表示用の配列に追加
                            # print(display_text) # 現在入力されている文字列を出力
                            # miss_typing = 0 # ミスタイプ回数をリセット
                            text = '' # 入力文字列を空に戻す
                            if target_line < len(true_word)-1: # お手本文字列がテキストファイルの最終行ではない場合
                                target_line += 1 # お手本リストと表示リストの該当箇所を変更
                            else: # 最終行の入力が完了した状態の場合
                                target_line = 0 # 該当箇所をリセット                                
                                display_text = [] # 表示文字列をリセット
                                true_word_txtnum = 0 # 文字数格納変数をリセット
                                for i in range(len(true_word)): # お手本ファイルの全文字数を計測
                                    true_word_txtnum += len(true_word[i])
                                miss_ratio = calc_quantize((miss_typing / true_word_txtnum * 100)) # ミスタイプ率を計算
                                print('経過時間：', elapsed_time, '秒')
                                print('ミスタイプ率',miss_ratio, '%')
                                elapsed_time = 0 # 経過時間をリセット
                                miss_typing = 0 # ミスタイプ回数をリセット
                                miss_ratio   = 0 # ミスタイプ率をリセット
                                start_time = time_set() # 計測開始時間を代入
                                if target_file < len(memo)-1: # お手本ファイル数に残りがある場合
                                    target_file += 1 # お手本ファイルを次のファイルへ
                                    true_word = file_read(memo[target_file]) # お手本ファイルを更新
                                else:
                                    pg.quit()
                                    sys.exit()
                    if event.key == pg.K_BACKSPACE: # バックスペースを押した場合
                        text = text[:-1] # 一番後ろの要素より前を取得して代入(1文字消える)
                        typing_stop = 0
                    elif event.key == K_ESCAPE:  # escキーで終了
                        pg.quit()
                        sys.exit()
                    else:
                        if not typing_stop:
                            if len(text) != len(true_word[target_line]):
                                text += event.unicode # 入力された文字を文字列に追加する
                        else:
                            miss_typing += 1
                            print('ミス：', miss_typing)

        screen.fill((30, 30, 30)) # スクリーンの背景色を指定

        for i in range(len(true_word)): # お手本文字配列の要素数分ループ
            if i == target_line: # 該当箇所と同じ場合
                true_txt_surface = font.render(true_word[i], True, color_active) # 該当文字列は色を変えてrenderにセット
            else:
                true_txt_surface = font.render(true_word[i], True, color_inactive) # お手本文字列をrenderにセット
            screen.blit(true_txt_surface, (100, 100+i*100)) # 指定位置にお手本文字列を描画

        for i in range(len(display_text)): # 表示用文字配列の要素数分ループ
            display_text_surface = font.render(display_text[i], True, color_true)
            screen.blit(display_text_surface, (100, 120+i*100)) # 指定位置に表示文字列を描画

        if len(text) > 0: # 入力文字列textの文字数が0より大きい場合
            if len(text) > len(true_word[target_line]): # 同時押しなどで入力文字数が上回ってしまった場合
                for i in range(len(text)-len(true_word[target_line])):
                    text[target_line] = text[:-1]
            if text[-1] == true_word[target_line][len(text)-1]: # 入力文字とお手本が等しい場合
                typing_stop = 0
                input_txt_surface = font.render(text, True, color_true)
                screen.blit(input_txt_surface, (100, 120+target_line*100)) # 指定位置に入力文字列を描画
                if len(text) == len(true_word[target_line]): # 全ての文字が正しく入力された場合
                    comp_typing = 1 # 全ての文字が正しく入力されたフラグを立てる
                else:
                    comp_typing = 0
            else: # 入力文字とお手本が異なる場合
                if typing_stop == 0:
                    typing_stop = 1
                    miss_typing += 1
                    print('ミス：', miss_typing)
                input_txt_surface = font.render(text, True, color_false)
                screen.blit(input_txt_surface, (100, 120+target_line*100)) # 指定位置に入力文字列を描画

        pg.display.flip() # 画面を更新
        clock.tick(30) # 動作フレームを設定（この場合は30fpsを超える速度では実行されないことになる）


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()