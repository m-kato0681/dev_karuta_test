""" pygame """
""" テキストボックスサンプル """

import pygame as pg # pygameをimportしてpgとして定義

def main():
    screen = pg.display.set_mode((640, 480)) # 指定サイズでゲームウィンドウを定義
    font = pg.font.Font(None, 32) # フォントをデフォルトに設定して文字の大きさを指定
    clock = pg.time.Clock() # pygameの時間管理に役立つオブジェクトをインスタンス化
    input_box = pg.Rect(100, 100, 140, 32) # テキストボックスの矩形を定義
    color_inactive = pg.Color('lightskyblue3') # pygame.Colorで色を指定
    color_active = pg.Color('dodgerblue2')
    color = color_inactive
    active = True
    text = ''
    done = False

    while not done:
        for event in pg.event.get(): # イベントを取得して実行
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN: # マウスがクリックされた場合
                if input_box.collidepoint(event.pos): # イベントが起こった点座標が指定した矩形の中に入っている場合
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pg.KEYDOWN: # 何かのキーが押された場合
                if active: # マウスがテキストボックスをクリックしていた場合
                    if event.key == pg.K_RETURN: # エンターキーが押された場合
                        print(text) # 現在入力されている文字列を出力
                        text = '' # 文字列を空にする
                    elif event.key == pg.K_BACKSPACE: # バックスペースを押した場合
                        text = text[:-1] # -1より前の要素を取得して代入(1文字消える)
                    else:
                        text += event.unicode # 入力された文字を文字列に追加する

        screen.fill((30, 30, 30)) # スクリーンの背景色を指定
        txt_surface = font.render(text, True, color) # 指定した文字列を描画
        width = max(200, txt_surface.get_width()+10) # 200と入力した文字列の横幅の大きい方を代入
        input_box.w = width # テキストボックスの横幅を更新
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5)) # 指定位置にサーフェス(入力したテキスト)を描画
        pg.draw.rect(screen, color, input_box, 2) # 矩形（テキストボックス）を描画

        pg.display.flip() # 画面を更新
        clock.tick(30) # 動作フレームを設定（この場合は30fpsを超える速度では実行されないことになる）


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()