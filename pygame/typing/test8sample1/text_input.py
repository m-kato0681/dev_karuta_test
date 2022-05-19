import sys
import pygame
from pygame.locals import *

from text import Text


def draw_text(text: str) -> None:
    """
    入力文字を描画するための関数
    """
    text_surface = font.render(text, True, (0, 0, 0))
    screen.fill((112, 225, 112))
    # テキストに応じて上下左右中央揃えにする
    center_w = (800 / 2) - (text_surface.get_width() / 2)
    center_h = (600 / 2) - (text_surface.get_height() / 2)
    screen.blit(text_surface, (center_w, center_h))
    pygame.display.update()


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    font = pygame.font.SysFont("yumincho", 30)
    text = Text()  # テキスト処理のロジックTextクラスをインスタンス化
    # テキスト入力時のキーとそれに対応するイベント
    call_trigger = {
        K_BACKSPACE: text.delete,
        K_LEFT: text.move_cursor_left,
        K_RIGHT: text.move_cursor_right,
        K_RETURN: text.enter,
    }
    pygame.key.start_text_input()  # input, editingイベントをキャッチするようにする
    input_text = format(text)
    draw_text(input_text)  # 起動時にカーソルを表示するようにする
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
            # キーダウンかつ、全角のテキスト編集中でない
            elif event.type == KEYDOWN and not text.is_editing:
                if event.key in call_trigger.keys():
                    input_text = call_trigger[event.key]()
                # 入力の確定
                if event.unicode in ("\r", "") and event.key == K_RETURN:
                    print(input_text)  # 確定した文字列を表示
                    draw_text(format(text))  # テキストボックスに"|"を表示
                    input_text = format(text)  # "|"に戻す
                    break
            elif event.type == TEXTEDITING:  # 全角入力
                input_text = text.edit(event.text, event.start)
            elif event.type == TEXTINPUT:  # 半角入力、もしくは全角入力時にenterを押したとき
                input_text = text.input(event.text)
            # 描画しなおす必要があるとき
            if event.type in [KEYDOWN, TEXTEDITING, TEXTINPUT]:
                draw_text(input_text)