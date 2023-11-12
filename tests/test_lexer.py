import pytest
from interpreter.lexer import Lexer, TokenType


class TestLexer:
    @pytest.fixture
    def lexer(self):
        return Lexer()

    def test_read_keyword(self, lexer):
        lexer.init("BEGIN")
        token = lexer.next()
        assert token.type_ == TokenType.BEGIN
        assert token.value == "BEGIN"

    def test_read_number(self, lexer):
        lexer.init("123.45")
        token = lexer.next()
        assert token.type_ == TokenType.NUMBER
        assert token.value == "123.45"

    def test_read_operator(self, lexer):
        lexer.init("+-*/")
        operators = ["+", "-", "*", "/"]

        for op in operators:
            token = lexer.next()
            assert token.type_ == TokenType.OPERATOR
            assert token.value == op

    def test_read_parentheses(self, lexer):
        lexer.init("()")

        token = lexer.next()
        assert token.type_ == TokenType.LPAREN
        assert token.value == "("

        token = lexer.next()
        assert token.type_ == TokenType.RPAREN
        assert token.value == ")"

    def test_read_dot(self, lexer):
        lexer.init(".")
        token = lexer.next()
        assert token.type_ == TokenType.DOT
        assert token.value == "."

    def test_read_colon(self, lexer):
        lexer.init(":=")
        token = lexer.next()
        assert token.type_ == TokenType.ASSIGN
        assert token.value == ":="

    def test_read_colon_no_assign(self, lexer):
        lexer.init(":")
        lexer.read_colon()

    def test_read_semicolon(self, lexer):
        lexer.init(";")
        token = lexer.next()
        assert token.type_ == TokenType.SEMICOLON
        assert token.value == ";"

    def test_read_comma(self, lexer):
        lexer.init(",")
        token = lexer.next()
        assert token.type_ == TokenType.COMMA
        assert token.value == ","

    def test_bad_token(self, lexer):
        with pytest.raises(SyntaxError):
            lexer.init("$")
            lexer.next()

    def test_read_assign_operator(self, lexer):
        lexer.init("=")
        token = lexer.next()
        assert token.type_ == TokenType.ASSIGN
        assert token.value == "="
