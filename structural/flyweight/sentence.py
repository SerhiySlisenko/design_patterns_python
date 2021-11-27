from .word_formatting import WordFormatting


class Sentence:
    """
    This class provides an interface such that the indexer returns a flyweight
    that can be used to capitalize or make in bold/italic a particular word in the sentence
    """
    def __init__(self, plain_text: str) -> None:
        self.words = plain_text.split(' ')
        self.tokens = {}

    def __getitem__(self, item: int) -> WordFormatting:
        wt = WordFormatting()
        self.tokens[item] = wt
        return self.tokens[item]

    def __str__(self) -> str:
        result = []
        for index in range(len(self.words)):
            word = self.words[index]
            if index in self.tokens and self.tokens[index].capitalized:
                word = word.upper()
            if index in self.tokens and self.tokens[index].bold:
                word = f"\033[1m{word}\033[0m"
            if index in self.tokens and self.tokens[index].capitalized:
                word = f"\x1B[3m{word}\x1B[3m"
            result.append(word)
        return ' '.join(result)

