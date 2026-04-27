"""
Follow these steps to change epub books to vertical or horizontal.
"""

import logging
import os
import shutil
import zipfile
from collections import Counter, defaultdict
from pathlib import Path
from typing import Dict, List, Optional

import cssutils
import opencc
from bs4 import BeautifulSoup as bs
from bs4 import NavigableString, PageElement, ResultSet, Tag
from cssutils import CSSParser
from cssutils.css import CSSStyleSheet
from langdetect import LangDetectException, detect

from epubhv.punctuation import Punctuation
from epubhv.yomituki import RubySoup, string_containers  # pyright: ignore

cssutils.log.setLevel(logging.CRITICAL)  # type: ignore

WRITING_KEY_LIST: List[str] = [
    "writing-mode",
    "-webkit-writing-mode",
    "-epub-writing-mode",
]
V_STYLE_LINE: str = (
    '<link rel="stylesheet" href="../Style/style.css" type="text/css" />'
)
# same as v
H_STYLE_LINE: str = (
    '<link rel="stylesheet" href="../Style/style.css" type="text/css" />'
)
V_STYLE_LINE_IN_OPF: str = '<meta content="vertical-rl" name="primary-writing-mode"/>'
H_STYLE_LINE_IN_OPF: str = '<meta content="horizontal-lr" name="primary-writing-mode"/>'
V_ITEM_TO_ADD_IN_MANIFEST: str = (
    '<item id="stylesheet" href="Style/style.css" media-type="text/css" />'
)
# same as v
H_ITEM_TO_ADD_IN_MANIFEST: str = (
    '<item id="stylesheet" href="Style/style.css" media-type="text/css" />'
)


def list_all_epub_in_dir(path: Path) -> set[Path]:
    pass


def make_epub_files_dict(dir_path: Path) -> Dict[str, List[Path]]:
    pass


def load_opf_meta_data(opf_file: Path) -> bs:
    pass


class EPUBHV:
    book_path: Path
    book_name: str
    opf_file: Path

    def __init__(
        self,
        file_path: Path,
        convert_to: Optional[str] = None,
        convert_punctuation: str = "auto",
        need_ruby: bool = False,
        need_cantonese: bool = False,
    ) -> None:
        # declare instance fields
        self.epub_file = file_path
        self.has_css_file: bool = False
        # for language ruby
        self.need_ruby: bool = need_ruby
        self.ruby_language = None
        self.cantonese = need_cantonese
        self.files_dict: Dict[str, List[Path]] = {}
        self.content_files_list: List[Path] = []
        self.convert_punctuation = convert_punctuation
        self.convert_to = convert_to

        self.converter = opencc.OpenCC(convert_to) if convert_to is not None else None

    def extract_one_epub_to_dir(self) -> None:
        pass

    @staticmethod
    def _add_stylesheet_to_html(html_file_path: Path, stylesheet_line: str):
        pass

    def make_epub_values(self) -> None:
        pass

    def __detect_language(self):
        pass

    def _make_ruby_language(self, soup):
        pass

    def change_epub_to_vertical(self) -> None:
        pass

    def change_epub_to_horizontal(self) -> None:
        pass

    def convert(self, method: str = "to_vertical") -> None:
        pass

    def pack(self, method: str = "to_vertical", dest: Path = Path.cwd()) -> Path:
        pass

    def run(self, method: str = "to_vertical", dest: Path = Path.cwd()) -> Path:
        pass
