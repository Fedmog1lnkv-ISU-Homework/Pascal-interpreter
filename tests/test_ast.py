from interpreter.ast import Number, BinOp, UnaryOp
from interpreter.token import Token, TokenType


class TestAst():
    def test_number_str(self):
        assert str(Number(Token(TokenType.NUMBER, "1"))) == "Number (Token(TokenType.NUMBER, 1))"

    def test_binop_str(self):
        assert str(BinOp(Number(1), Token(TokenType.OPERATOR, "+"), Number(2))) == "BinOp+ (Number (1), Number (2))"

    def test_unaryop_str(self):
        assert str(UnaryOp(Token(TokenType.OPERATOR, "-"), Number(1))) == "UnaryOp- (Number (1))"
