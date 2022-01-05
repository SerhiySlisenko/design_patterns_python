# Visitor pattern using Python
Implementation of Visitor Design Pattern according to the task from 'Design Patterns in Python' course
https://www.udemy.com/course/design-patterns-python/

The task is to implement two Visitors - the first prints the complicated expressions, the second evaluates the expressions.

As components, we use different types of expressions: single-value, addition, subtraction, multiplication. They are built in a Composite way (one expression can contain other expressions, single-value is a leaf).
Addition and subtraction are grouped in the parentheses for printing.


This task was implemented in two different ways:
* Using the classic approach described in https://refactoring.guru/design-patterns/composite
* Using the alternative approach described in the lesson by using decorators with a class name as parameters. Library code is taken from https://tavianator.com/the-visitor-pattern-in-python/
