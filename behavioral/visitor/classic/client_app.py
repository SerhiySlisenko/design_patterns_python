from behavioral.visitor.classic.visitor_impl.expr_printer import ExpressionPrinter
from behavioral.visitor.classic.visitor_impl.expr_evaluator import ExpressionEvaluator
from behavioral.visitor.classic.expressions import ValueExpression, AdditionExpression, SubtractionExpression, \
    MultiplicationExpression


def main() -> None:
    """
    Client app
    """
    evaluator = ExpressionEvaluator()
    printer = ExpressionPrinter()

    expr = AdditionExpression(ValueExpression(2), ValueExpression(3))
    expr.accept(printer)  # instead of `printer.visit(expr)`
    print(f"PrinterVisitor: (2+3) = {printer} -> {'(2+3)' == str(printer)}")
    expr.accept(evaluator)  # instead of `evaluator.visit(expr)`
    print(f"EvaluatorVisitor: {printer} = {evaluator} -> {eval('(2+3)') == evaluator.value}\n")
    printer.reset()

    expr = MultiplicationExpression(
        AdditionExpression(ValueExpression(2), ValueExpression(3)),
        ValueExpression(4)
    )
    expr.accept(printer)
    print(f"PrinterVisitor: (2+3)*4 = {printer} -> {'(2+3)*4' == str(printer)}")
    expr.accept(evaluator)
    print(f"EvaluatorVisitor: {printer} = {evaluator} -> {eval('(2+3)*4') == evaluator.value}\n")
    printer.reset()

    expr = MultiplicationExpression(
        AdditionExpression(
            SubtractionExpression(ValueExpression(7), ValueExpression(3)),
            ValueExpression(6)
        ),
        SubtractionExpression(ValueExpression(-2), ValueExpression(3))
    )
    expr.accept(printer)
    print(f"PrinterVisitor: ((7-3)+6)*(-2-3) = {printer} -> {'((7-3)+6)*(-2-3)' == str(printer)}")
    expr.accept(evaluator)
    print(f"EvaluatorVisitor: {printer} = {evaluator} -> {eval('((7-3)+6)*(-2-3)') == evaluator.value}\n")


if __name__ == '__main__':
    main()
