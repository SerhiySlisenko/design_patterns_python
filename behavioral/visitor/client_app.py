# taken from https://tavianator.com/the-visitor-pattern-in-python/
def _qualname(obj):
    """Get the fully-qualified name of an object (including module)."""
    return obj.__module__ + '.' + obj.__qualname__


def _declaring_class(obj):
    """Get the name of the class that declared an object."""
    name = _qualname(obj)
    return name[:name.rfind('.')]


# Stores the actual visitor methods
_methods = {}


# Delegating visitor implementation
def _visitor_impl(self, arg):
    """Actual visitor method implementation."""
    key = (_qualname(type(self)), type(arg))
    if not key in _methods:
        raise Exception('Key % not found' % key)
    method = _methods[key]
    return method(self, arg)


# The actual @visitor decorator
def visitor(arg_type):
    """Decorator that creates a visitor method."""

    def decorator(fn):
        declaring_class = _declaring_class(fn)
        _methods[(declaring_class, arg_type)] = fn

        # Replace all decorated methods with _visitor_impl
        return _visitor_impl

    return decorator

# ↑↑↑ LIBRARY CODE ↑↑↑


class Value:
    def __init__(self, value):
        self.value = value


class AdditionExpression:
    def __init__(self, left, right):
        self.right = right
        self.left = left


class MultiplicationExpression:
    def __init__(self, left, right):
        self.right = right
        self.left = left


class ExpressionPrinter:
    def __init__(self):
        self.buffer = []

    @visitor(Value)
    def visit(self, elem):
        self.buffer.append(str(elem.value))

    @visitor(AdditionExpression)
    def visit(self, elem):
        self.buffer.append("(")
        self.visit(elem.left)
        self.buffer.append("+")
        self.visit(elem.right)
        self.buffer.append(")")

    @visitor(MultiplicationExpression)
    def visit(self, elem):
        self.visit(elem.left)
        self.buffer.append("*")
        self.visit(elem.right)

    def __str__(self):
        return "".join(self.buffer)

    def reset(self):
        self.buffer = []


def main() -> None:
    """
    Client app
    """

    expr = AdditionExpression(Value(2), Value(3))
    ep = ExpressionPrinter()
    ep.visit(expr)
    print(f"(2+3) = {ep}")

    ep.reset()
    expr = MultiplicationExpression(
        AdditionExpression(Value(2), Value(3)),
        Value(4)
    )
    ep.visit(expr)
    print(f"(2+3)*4 = {ep}")


if __name__ == '__main__':
    main()
