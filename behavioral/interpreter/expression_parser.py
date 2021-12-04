from __future__ import annotations
import re
from typing import List, Union

from behavioral.interpreter.variable import Variable
from behavioral.interpreter.abstract_expression import AbstractExpression
from behavioral.interpreter.expressions import NumberExpression, AddExpression, SubExpression


class ExpressionParser:
    """
    Class is used to parse an expression and add the ability to automatically create
    an Abstract Syntax Tree for future processing by the Interpreter.
    """

    def __init__(self, expression: str) -> None:
        self.expression = expression

    def _parse(self) -> List[Union[NumberExpression, str]]:
        result = []
        i = 0
        non_whitespace_expr = self.expression.replace(" ", "")

        while i < len(non_whitespace_expr):
            char = non_whitespace_expr[i]
            if not re.search(r"[0-9a-zA-Z+-]", char):
                raise ValueError("Invalid symbols in the expression. "
                                 "Supported only integer numbers, single-letter variables, '+' and '-'!")
            elif char == '+':
                result.append('+')
            elif char == '-':
                result.append('-')
            elif char.isalpha():
                # if var is not defined - use 0, otherwise use defined value
                var_value = Variable.names.get(char) if Variable.names.get(char) else 0
                result.append(NumberExpression(var_value))
                if i < len(non_whitespace_expr) - 1:
                    next_char = non_whitespace_expr[i + 1]
                    if next_char.isalpha():
                        raise ValueError("Supported only single-letter variables")
            else:  # Must be a number
                digits = [char]
                for j in range(i + 1, len(non_whitespace_expr)):
                    if non_whitespace_expr[j].isdigit():
                        digits.append(non_whitespace_expr[j])
                        i += 1
                    else:
                        number = int(''.join(digits))
                        result.append(NumberExpression(number))
                        break
                else:
                    result.append(NumberExpression(int(''.join(digits))))

            i += 1

        return result

    def build_ast(self) -> List[AbstractExpression]:
        tokens = self._parse()
        ast: List[AbstractExpression] = []

        if tokens is not None:
            ast_head = 0
            sign_index = 1

            for i in tokens[1:-1:2]:
                if i == '+':
                    ast.append(
                        AddExpression(ast[ast_head-1] if len(ast) else tokens[sign_index - 1], tokens[sign_index + 1])
                    )
                else:
                    ast.append(
                        SubExpression(ast[ast_head-1], tokens[sign_index + 1])
                    )

                ast_head += 1
                sign_index += 2

            else:
                if not len(ast):
                    ast.append(tokens[sign_index - 1])

        return ast
