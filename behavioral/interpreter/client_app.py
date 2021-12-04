from behavioral.interpreter.expression_parser import ExpressionParser
from behavioral.interpreter.variable import Variable


def main() -> None:
    """
    Client app
    """
    Variable.names['x'] = 5
    Variable.names['y'] = 2

    expression = "x+9 - 13 + z + 7-y"
    print("x=5\ny=2")
    print(f'Expression: {expression}')
    try:
        expr_parser = ExpressionParser(expression)

        abstract_syntax_tree = expr_parser.build_ast()
        ast_root = abstract_syntax_tree.pop()
        print(f'Result: {ast_root.interpret()}')

    except ValueError as err:
        print(f'Error: {err}')


if __name__ == '__main__':
    main()
