from converter_remove_teg import RemoveTagConverter
from convert_tag_to_uppercase import TagToUppercaseConverter
from converter_capitalize_tag import CapitalizeTagConverter
from converter_format_tag import FormatTagConverter


class Configuration(object):
    remove_tag = "RemoveTag"
    tag_to_uppercase = "TagToUppercase"
    capitalize_tag = "CapitalizeTag"
    format_tag = "FormatTag"

    @staticmethod
    def handle_request(request):
        switcher = {
            "RemoveTag": RemoveTagConverter(),
            "TagToUppercase": TagToUppercaseConverter(),
            "CapitalizeTag": CapitalizeTagConverter(),
            "FormatTag": FormatTagConverter()
        }
        return switcher.get(request, "[ERROR] Undefined converter")
