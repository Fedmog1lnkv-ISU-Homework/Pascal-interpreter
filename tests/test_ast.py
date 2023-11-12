import pytest
from interpreter.ast import Number, BinOp, UnaryOp, Assign, Var, ComplexStatement, Block, EmptyNode
from interpreter.token import Token, TokenType


class TestAstStr():
    def test_number_str(self):
        token = Token(TokenType.NUMBER, '1')
        number = Number(token)
        assert str(number) == f"Number ({token})"

    def test_binop_str(self):
        left = Number(Token(TokenType.NUMBER, '1'))
        right = Number(Token(TokenType.NUMBER, '2'))
        op = Token(TokenType.OPERATOR, '+')
        binop = BinOp(left, op, right)
        assert str(binop) == f"BinOp{op.value} ({left}, {right})"

    def test_unaryop_str(self):
        number = Number(Token(TokenType.NUMBER, '1'))
        op = Token(TokenType.OPERATOR, '-')
        unaryop = UnaryOp(op, number)
        assert str(unaryop) == f"UnaryOp{op.value} ({number})"

    def test_assign_str(self):
        left = Number(Token(TokenType.NUMBER, '1'))
        right = Number(Token(TokenType.NUMBER, '2'))
        op = Token(TokenType.OPERATOR, ':=')
        assign = Assign(left, op, right)
        assert str(assign) == f"Assign({left}, {op}, {right})"

    def test_complex_statement_str(self):
        complex_statement = ComplexStatement()
        assert str(complex_statement) == "ComplexStatement[]"

    def test_var_str(self):
        token = Token(TokenType.ID, 'x')
        var = Var(token)
        assert str(var) == "VarToken(TokenType.ID, x)"

    def test_block_str(self):
        complex_statement = ComplexStatement()
        block = Block(complex_statement)
        assert str(block) == f"Block{complex_statement}"

    def test_empty_node_str(self):
        empty_node = EmptyNode()
        assert str(empty_node) == "EmptyNode"
