from .token import Token, TokenType

KEYWORDS = {
    "BEGIN": Token(TokenType.BEGIN, "BEGIN"),
    "END": Token(TokenType.END, "END"),
}


class Lexer:
    def __init__(self):
        self._pos = 0
        self._text = ""
        self._current_char = None

    def init(self, text):
        self._text = text
        self._pos = 0
        self._current_char = self._text[self._pos]

    def advance(self):
        self._pos += 1
        self._current_char = self._text[self._pos] if self._pos < len(self._text) else None

    def skip_whitespace(self):
        while self._current_char is not None and self._current_char.isspace():
            self.advance()

    def read_number(self):
        result = []
        dot_count = 0
        while self._current_char is not None and (self._current_char.isdigit() or self._current_char == "."):
            result.append(self._current_char)
            self.advance()
        return "".join(result)

    def read_colon(self):
        self.advance()
        while self._current_char is not None and self._current_char.isspace():
            self.advance()  # pragma: no cover
        if self._current_char == "=":
            self.advance()
            return Token(TokenType.ASSIGN, ":=")
        return Token(TokenType.COLON, ":")

    def read_keyword(self):
        result = ''
        while self._current_char is not None and self._current_char.isalnum():
            result += self._current_char
            self.advance()
        return KEYWORDS.get(result, Token(TokenType.ID, result))

    def read_operator_token(self, operator_type):
        op = self._current_char
        self.advance()
        return Token(operator_type, op)

    def next(self):
        while self._current_char:
            if self._current_char.isspace():
                self.skip_whitespace()
                continue
            if self._current_char.isalpha():
                return self.read_keyword()
            if self._current_char.isdigit():
                return Token(TokenType.NUMBER, self.read_number())

            if self._current_char in ["+", "-", "/", "*"]:
                return self.read_operator_token(TokenType.OPERATOR)

            if self._current_char == "(":
                return self.read_operator_token(TokenType.LPAREN)
            if self._current_char == ")":
                return self.read_operator_token(TokenType.RPAREN)
            if self._current_char == ".":
                return self.read_operator_token(TokenType.DOT)
            if self._current_char == ":":
                return self.read_colon()
            if self._current_char == ";":
                return self.read_operator_token(TokenType.SEMICOLON)
            if self._current_char == "=":
                return self.read_operator_token(TokenType.ASSIGN)
            if self._current_char == ",":
                return self.read_operator_token(TokenType.COMMA)

            raise SyntaxError("Bad token")
