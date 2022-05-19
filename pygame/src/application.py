# typing-practice - Typing Practice
#
# Copyright (c) 2020 Esrille Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at:
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import package # ドメインやパスの情報が記されたpackageファイルをインポート

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gio, Gtk, Gdk # Gio,Gtk,GdkなどGUIを作成するためのライブラリをインポート

from window import TypingWindow # Gtk.ApplicationWindowを継承したクラスをインポート
# アプリのメニューとメニューバーを処理することが可能

import gettext # テキスト翻訳用のフレームワーク
import logging # ログを出力するためのモジュール
import os # OS依存の機能を利用するためのモジュール


logger = logging.getLogger(__name__) # このファイルを直接実行したらapplication.pyが入り、外部から呼ばれた場合は外部のファイルの実行ログが記録されるようになる
_ = lambda a : gettext.dgettext(package.get_name(), a)
# package.get_nameで取得した文字列の中から引数aを探す

class Application(Gtk.Application): # Gtk.Applicationはアプリのメニューバーなどの処理を可能にする
    def __init__(self, *args, **kwargs): # 3つの引数でコンストラクタを実行
        super().__init__( # 親クラス「Gtk.Application」のコンストラクタを実行
            *args,
            application_id="com.esrille.typing",
            flags=Gio.ApplicationFlags.HANDLES_OPEN,
            **kwargs
        )
        self.window = None # Gtk.ApplicationのwindowをNoneに設定

    def do_activate(self):
        if not self.window: # windowがFalseの場合
            filename = os.path.join(package.get_datadir(), 'lessons/menu.txt')
            # /usr/share/esrille-typing-practice と s/menu.txt を1つの文字列にまとめる
            self.window = TypingWindow(application=self, filename=filename) # アプリのメニューとメニューバー
            self.cursor = Gdk.Cursor.new_from_name(self.window.get_display(), "default")
            # カーソルのテーマ（アイコン）をデフォルトのものに変更
        self.window.present()

    def do_open(self, files, *hint):
        if not self.window:
            self.window = TypingWindow(application=self, filename=files[0].get_path())
            self.cursor = Gdk.Cursor.new_from_name(self.window.get_display(), "default")
        self.window.present()

    def do_startup(self):
        Gtk.Application.do_startup(self)

        action = Gio.SimpleAction.new("help", None)
        action.connect("activate", self.on_help)
        self.add_action(action)
        action = Gio.SimpleAction.new("about", None)
        action.connect("activate", self.on_about)
        self.add_action(action)
        action = Gio.SimpleAction.new("quit", None)
        action.connect("activate", self.on_quit)
        self.add_action(action)
        self.set_accels_for_action("app.help", ["F1"])
        self.set_accels_for_action("win.menu", ["F10"])
        self.set_accels_for_action("app.quit", ["<Primary>q"])

    def do_window_removed(self, window):
        logger.info('do_window_removed')
        window.quit()
        self.quit()

    def on_about(self, action, param):
        dialog = Gtk.AboutDialog(transient_for=self.window, modal=True)
        dialog.set_program_name(_("Typing Practice"))
        dialog.set_copyright("Copyright 2020 Esrille Inc.")
        dialog.set_authors(["Esrille Inc."])
        dialog.set_documenters(["Esrille Inc."])
        dialog.set_website("file://" + os.path.join(package.get_datadir(), "help/index.html"))
        dialog.set_website_label(_("Introduction to Typing Practice"))
        dialog.set_logo_icon_name(package.get_name())
        dialog.set_version(package.get_version())
        dialog.present()
        # To close the dialog when "close" is clicked, e.g. on Raspberry Pi OS,
        # the "response" signal needs to be connected on_about_response
        dialog.connect("response", self.on_about_response)
        dialog.show()

    def on_about_response(self, dialog, response):
        dialog.destroy()

    def on_help(self, *args):
        url = "file://" + os.path.join(package.get_datadir(), "help/index.html")
        Gtk.show_uri_on_window(self.window, url, Gdk.CURRENT_TIME)
        if self.window:
            # see https://gitlab.gnome.org/GNOME/gtk/-/issues/1211
            self.window.get_window().set_cursor(self.cursor)

    def on_quit(self, *args):
        if self.window:
            self.window.quit()
        self.quit()
