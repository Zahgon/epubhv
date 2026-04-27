from argparse import ArgumentParser, RawTextHelpFormatter
from pathlib import Path
from typing import cast

from epubhv.epubhv import EPUBHV, list_all_epub_in_dir


class Options:
    epub: str
    method: str
    convert: str
    punctuation: str
    ruby: bool
    cantonese: bool
    dest: Path


def main() -> None:
    pass


if __name__ == "__main__":
    main()
