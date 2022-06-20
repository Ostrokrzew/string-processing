"""
Zajęcia Python Luzino
Sławomir Jankowski
"""


class StringProcessing:
    """
    Klasa przetwarzająca ciąg znaków otrzymany przy inicjacji.
    """

    _string = ''
    """
    Prywatne pole, w którym przetrzymywana jest aktualna wartość przetwarzanego ciągu znaków.
    """

    # zadanie nr 1
    def __init__(self, string: str = ''):
        """
        Inicjuje obiekt przetwarzający ciągi znaków.

        :param string: ciąg znaków do przetwarzania
        """
        self._string = string
        pass

    # zadanie nr 2
    def get_current_processing_result(self) -> str:
        """
        Zwraca aktualną wartość przetwarzanego ciągu znaków.

        :return: _string
        """
        return self._string

    # zadanie nr 3
    def trim_string(self):
        """
        Usuwa tzw. białe znaki z początku i z końca przetwarzanego ciągu znaków.
        """
        self._string = self._string.strip()
        pass

    # zadanie nr 4
    def replace_substring(self, what: str, to: str):
        """
        Zastępuje dowolny ciąg znaków wewnątrz przetwarzanego ciągu znaków dowolnym ciągkiem znaków.

        :param what: ciąg znaków, który zostanie zastąpiony
        :param to: ciąg znaków, który zastąpi poprzednią sekwencję
        """
        self._string = self._string.replace(what, to)
        pass

    # zadanie nr 5
    def add_prefix(self, prefix: str):
        """
        Dodaje przedrostek na początku przetwarzanego ciągu znaków, o ile ten przedrostek nie rozpoczyna słowa.

        :param prefix: przedrostek do dodania
        """
        prefix_length = len(prefix)
        self._string = prefix + self._string if self._string[:prefix_length] != prefix else self._string
        pass

    #zadanie nr 6
    def add_suffix(self, suffix: str):
        """
        Dodaje przyrostek na końcu przetwarzanego ciągu znaków, o ile ten przyrostek nie kończy słowa.

        :param suffix: przyrostek do dodania
        """
        suffix_length = len(suffix)
        self._string = self._string + suffix if self._string[-suffix_length:] != suffix else self._string
        pass


if __name__ == '__main__':
    pass
