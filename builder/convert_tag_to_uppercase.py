from typing import Tuple
from text_converter import TextConverter


class TagToUppercaseConverter(TextConverter):
    @staticmethod
    def convert_character(character: str) -> str:
        return character.lower()

    @staticmethod
    def convert_tag(tag: Tuple[str, str]) -> str:
        tag_name, content = tag
        return content.upper()
