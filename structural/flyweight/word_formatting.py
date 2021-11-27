class WordFormatting:
    """
    Flyweight class that provides formatting for any word
    """
    def __init__(self, capitalized: bool = False, bold: bool = False, italic: bool = False) -> None:
        self.capitalized = capitalized
        self.bold = bold
        self.italic = italic
