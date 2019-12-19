from typing import Tuple
from text_converter import TextConverter


class CapitalizeTagConverter(TextConverter):
    @staticmethod
    def convert_character(character: str) -> str:
        return character

    @staticmethod
    def convert_tag(tag: Tuple[str, str]) -> str:
        tag_name, content = tag
        return f"<{tag_name}>{content.upper()}</{tag_name}>"
