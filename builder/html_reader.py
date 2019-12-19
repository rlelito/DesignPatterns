import re
from configuration import Configuration
from text_converter import TextConverter


class HTLMReader(object):
    def __init__(self, builder, text: str) -> None:
        self._builder = Configuration().handle_request(builder)
        self._text: str = text

    def parse_file(self) -> str:
        result = ""
        pos = 0

        while pos < len(self._text):
            curr = self._text[pos]
            if curr != "<":
                result += self._builder.convert_character(curr)
                pos += 1
            else:
                tag = re.search(r'<(\w+?)>(.+?)</\1>', self._text[pos:])
                result += self._builder.convert_tag(tag.groups())
                pos += len(tag.group())

        return result

    @property
    def builder(self) -> TextConverter:
        return self._builder

    @builder.setter
    def builder(self, value) -> None:
        self._builder = Configuration().handle_request(value)
