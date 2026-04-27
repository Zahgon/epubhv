import re
from typing import Dict, Literal


class Punctuation:
    def convert(
        self, text: str, horizontal: bool, source_locale: str, target_locale: str
    ) -> str:
        pass

    def map_locale(self, x: str) -> Literal["hans", "hant"]:
        pass

    def batch_replace(self, text: str, replacement_dict: Dict[str, str]) -> str:
        pass
