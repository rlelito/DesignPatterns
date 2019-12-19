from configuration import Configuration
from html_reader import HTLMReader

if __name__ == "__main__":
    text = "A<b>l</b>a ma <i>k</i>o<u>t</u>a"
    print(f"Oryginalny tekst:\n\t{text}\n")
    # 1)RemoveTag    2)TagToUppercase    3)CapitalizeTag    4)FormatTag

    builder_list = [Configuration().remove_tag, Configuration().tag_to_uppercase,
                    Configuration().capitalize_tag, Configuration().format_tag]

    reader = HTLMReader(None, text)
    for i, builder in enumerate(builder_list):
        reader.builder = builder
        print(f"{i+1}){str(reader.builder)}:\n\t{reader.parse_file()}")
