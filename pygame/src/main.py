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
from gi.repository import GLib # gi.repositoryの中のpythonパッケージのGlibをインポート

GLib.set_prgname(package.get_name()) # get_nameで取得した文字列をGlibの対象となるプログラム名として設定

from application import Application # applicationファイルのApplicationクラスをインポート

import gettext # テキスト翻訳用のフレームワーク(Python標準ライブラリ)
import locale # プログラムを実行する国や地域を設定する標準ライブラリ
import logging # ログを出力（ロギング）するためのモジュール（標準ライブラリ）
import os # OS依存の機能を利用するためのモジュール（標準ライブラリ）
import sys # pythonの実行環境


logger = logging.getLogger(__name__) # ( )でログの出力名を設定してloggingをインスタンス化。nameにはmainか外部のファイル名が入る
_ = lambda a : gettext.dgettext(package.get_name(), a)
# aを引数として後ろの処理の返り値を代入
# dgettextで指定した文字列から「a」を探す

if __name__ == '__main__': # main.pyが直接実行された場合
    os.umask(0o077) # main.pyへのパーミッション（アクセス権限）を設定。
    # マスク値077⇒000 111 111なので、パーミッションは111 000 000 となりユーザー（管理者）以外はアクセス権が無くなっている
    try:
        locale.bindtextdomain(package.get_name(), package.get_localedir()) # (ドメイン, パス)として、ドメインのパスを設定。指定したファイルを国際対応可能な仕様にする。
    except Exception: # 例外を取得してもスルー
        pass
    gettext.bindtextdomain(package.get_name(), package.get_localedir()) # ドメインのパスを設定。指定したファイルを翻訳対応可能な仕様にする。
    logging.basicConfig(level=logging.DEBUG) # loggingのログレベルをDEBUG(10)に設定
    app = Application() # Applicationクラスをインスタンス化
    exit_status = app.run(sys.argv) # Applicationクラスのrunを実行
    # sys.argvで渡されるコマンドライン引数のリストには何が入っているのか？
    # 恐らくアプリの実行に必要なデータなどが実行用のクラスに渡されている
    sys.exit(exit_status) # 実行が出来なかった場合はプログラムを終了させる
