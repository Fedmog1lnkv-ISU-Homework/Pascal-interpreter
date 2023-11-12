import pytest
from interpreter import Interpreter
from interpreter.ast import Number, BinOp, UnaryOp
from interpreter.interpreter import NodeVisitor
from interpreter.token import Token, TokenType


@pytest.fixture(scope="function")
def interpreter():
    return Interpreter()


class TestInterpreter:
    interpreter = Interpreter()

    def substitution(self, expression):
        return f"BEGIN\nx:={expression};\nEND."

    def test_add(self, interpreter):
        assert interpreter.eval(self.substitution("2+2")) == {"x": 4}

    def test_sub(self, interpreter):
        assert interpreter.eval(self.substitution("2-2")) == {"x": 0}

    def test_mul(self, interpreter):
        assert interpreter.eval(self.substitution("2*2")) == {"x": 4}

    def test_div(self, interpreter):
        assert interpreter.eval(self.substitution("2/2")) == {"x": 1}

    def test_add_with_letter(self, interpreter):
        with pytest.raises(ValueError):
            interpreter.eval(self.substitution("2+a"))
        with pytest.raises(ValueError):
            interpreter.eval(self.substitution("t+2"))

    def test_wrong_operator_binop(self, interpreter):
        with pytest.raises(SyntaxError):
            interpreter.eval(self.substitution("2&3"))

    @pytest.mark.parametrize(
        "interpreter, code", [(interpreter, "2 + 2"),
                              (interpreter, "2 +2 "),
                              (interpreter, " 2+2")]
    )
    def test_add_spaces(self, interpreter, code):
        assert interpreter.eval(self.substitution(code)) == {"x": 4}

    def test_unary_minus(self, interpreter):
        assert interpreter.eval(self.substitution("-2")) == {"x": -2}

    def test_unary_plus(self, interpreter):
        assert interpreter.eval(self.substitution("+2")) == {"x": 2}

    def test_unary_expression(self, interpreter):
        assert interpreter.eval(self.substitution("-(2-3)")) == {"x": 1}

    def test_visit_invalid_node(self, interpreter):
        node = "invalid"
        with pytest.raises(ValueError):
            interpreter.visit(node)

    def test_interpreter_visit_binop_error(self, interpreter):
        with pytest.raises(ValueError):
            interpreter.visit(BinOp(Number(1), Token(TokenType.OPERATOR, "S"), Number(2)))

    def test_interpreter_visit_unaryop_error(self, interpreter):
        with pytest.raises(ValueError):
            interpreter.visit(UnaryOp(Token(TokenType.OPERATOR, "S"), Number(1)))

    def test_big_expression(self, interpreter):
        assert interpreter.eval(
            "BEGIN\ny: = 2;\nBEGIN\na := 3;\na := a;\nb := 10 + a + 10 * y / 4;\nc := a - b\nEND;\nx := 11;\nEND.") == {
                   'y': 2.0, 'a': 3.0, 'b': 18.0, 'c': -15.0, 'x': 11.0}
