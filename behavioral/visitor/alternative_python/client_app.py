from behavioral.visitor.alternative_python.visitor_impl.expr_printer import ExpressionPrinter
from behavioral.visitor.alternative_python.visitor_impl.expr_evaluator import ExpressionEvaluator
from behavioral.visitor.alternative_python.value import Value
from behavioral.visitor.alternative_python.expressions import AdditionExpression, SubtractionExpression, \
    MultiplicationExpression


def main() -> None:
    """
    Client app
    """
    evaluator = ExpressionEvaluator()
    printer = ExpressionPrinter()

    expr = AdditionExpression(Value(2), Value(3))
    printer.visit(expr)
    print(f"PrinterVisitor: (2+3) = {printer} -> {'(2+3)' == str(printer)}")
    evaluator.visit(expr)
    print(f"EvaluatorVisitor: {printer} = {evaluator} -> {eval('(2+3)') == evaluator.value}\n")
    printer.reset()
    expr = MultiplicationExpression(
        AdditionExpression(Value(2), Value(3)),
        Value(4)
    )
    printer.visit(expr)
    print(f"PrinterVisitor: (2+3)*4 = {printer} -> {'(2+3)*4' == str(printer)}")
    evaluator.visit(expr)
    print(f"EvaluatorVisitor: {printer} = {evaluator} -> {eval('(2+3)*4') == evaluator.value}\n")

    printer.reset()
    expr = MultiplicationExpression(
        AdditionExpression(
            SubtractionExpression(Value(7), Value(3)),
            Value(6)
        ),
        SubtractionExpression(Value(-2), Value(3))
    )
    printer.visit(expr)
    print(f"PrinterVisitor: ((7-3)+6)*(-2-3) = {printer} -> {'((7-3)+6)*(-2-3)' == str(printer)}")
    evaluator.visit(expr)
    print(f"EvaluatorVisitor: {printer} = {evaluator} -> {eval('((7-3)+6)*(-2-3)') == evaluator.value}\n")


if __name__ == '__main__':
    main()
