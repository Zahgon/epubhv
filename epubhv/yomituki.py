"""
This file is copy from https://github.com/Mumumu4/furigana4epub great thanks
The pinyin is from https://github.com/shotazc/pinyin2epub/blob/master/pinyin2epub.py 
I made some change

"""

# coding: utf-8
import re
from itertools import groupby

import jieba
from bs4 import BeautifulSoup
from bs4.element import NavigableString, Script, Stylesheet, Tag, TemplateString
from fugashi import Tagger
from pypinyin import pinyin
from ToJyutping import get_jyutping_list

tagger = Tagger()  # pyright: ignore

katakana_chart = "ァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロヮワヰヱヲンヴヵヶヽヾ"
hiragana_chart = "ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをんゔゕゖゝゞ"
h2k = str.maketrans(hiragana_chart, katakana_chart)
k2h = str.maketrans(katakana_chart, hiragana_chart)

white_space_re = re.compile(r"(\s+)")


class RBString(NavigableString):
    """class for <ruby> tag"""

    pass


class RTString(NavigableString):
    """class for <rt> tag"""

    pass


class RPString(NavigableString):
    """class for <rp> tag"""

    pass


# strings in tag which in string_containers will not appear in bs4's get_text()
# this could be controlled by a parameter of get_text() ,see its docstring
string_containers = {
    "rp": RPString,
    "rt": RTString,
    "style": Stylesheet,
    "script": Script,
    "template": TemplateString,
}
basesoup = BeautifulSoup("<b></b>", "lxml", string_containers=string_containers)


def point_ruby_to_blod(soup):
    pass


def kata2hira(str):
    pass


def hantei_japanese(word):
    pass


def hantei_chinese(word):
    # follow the old api for Chinese pinyin
    pass


def hantei_cantonese(word):
    # follow the old api for Chinese pinyin for cantonese
    pass


def cut_end(text, hira):
    pass


def yomituki(sentence, lang="zh"):
    pass


def ruby_wrap(text, yomi):
    pass


def tag_wrap(name, str):
    pass


def ruby_text(text, lang="zh"):
    pass


class RubySoup:
    def __init__(self, ruby_language, is_ruby_rp=True) -> None:
        self.is_ruby_rp = is_ruby_rp
        self.ruby_language = ruby_language

    def ruby_soup(self, soup):
        pass

    def ruby_navigablestring(self, navigablestring):
        pass

    def ruby_wrap_bs4(self, text, yomi):
        pass

    def ruby_wraps_bs4(self, yomis):
        pass
