# typing-practice - Typing Practice
#
# Copyright (c) 2020 Esrille Inc.
#
# Licensed under the Apache License, Version 2.0 (the License);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at:
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an AS IS BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# This file is a template file processed by the configure script.
# The file name is listed in AC_CONFIG_FILES of configure.ac.

import os
import gi
from gi.repository import GLib


HIRAGANA_IME_KEY = 'org.freedesktop.ibus.engine.hiragana'


def get_name():
    return 'esrille-typing-practice'


def get_version():
    return '0.2.0'


def get_prefix():
    return '/usr'


def get_datadir():
    return '/usr/share/esrille-typing-practice'


def get_user_datadir():
    return os.path.join(GLib.get_user_data_dir(), 'esrille-typing-practice')


def get_localedir():
    return '/usr/share/locale'


def get_domain():
    source = Gio.SettingsSchemaSource.get_default()
    if source.lookup(HIRAGANA_IME_KEY, True):
        config = Gio.Settings.new(HIRAGANA_IME_KEY)
        path = config.get_string('dictionary')
        path = os.path.basename(path)
        if path in ('restrained.1.dic', 'restrained.2.dic', 'restrained.3.dic', 'restrained.4.dic', 'restrained.5.dic', 'restrained.6.dic'):
            return get_name() + '.kids'
    return get_name()
