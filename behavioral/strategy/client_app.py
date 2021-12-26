import cmath

from behavioral.strategy.quadratic_equation_solver import QuadraticEquationSolver
from behavioral.strategy.impl import RealDiscriminantStrategy, OrdinaryDiscriminantStrategy


def main() -> None:
    """
    Client app
    """
    strategy = OrdinaryDiscriminantStrategy()
    solver = QuadraticEquationSolver(strategy)
    results = solver.solve(1, 10, 16)
    print(f"Results of 'x^2 + 10x + 16 = 0' equation using Ordinary Discriminant Strategy"
          f"should be equal to '{complex(-2, 0)}' and '{complex(-8, 0)}' complex numbers.")
    print(f"Actual results are: x1 = {results[0]}, x2 = {results[1]}\n")

    solver.strategy = RealDiscriminantStrategy()
    results = solver.solve(1, 10, 16)
    print(f"Results of 'x^2 + 10x + 16 = 0' equation using Real Discriminant Strategy"
          f"should be equal to '{complex(-2, 0)}' and '{complex(-8, 0)}' complex numbers.")
    print(f"Actual results are: x1 = {results[0]}, x2 = {results[1]}\n")

    solver.strategy = RealDiscriminantStrategy()
    results = solver.solve(1, 4, 5)
    print(f"Results of 'x^2 + 4x + 5 = 0' equation using Real Discriminant Strategy"
          f"should be equal to '{complex(-2, 1)}' and '{complex(-2, -1)}' complex numbers.")
    print(f"Actual results are: x1 = {results[0]}, x2 = {results[1]}\n")

    solver.strategy = OrdinaryDiscriminantStrategy()
    results = solver.solve(1, 4, 5)
    # Discriminant = 4*4 - 4*1*5 = -4
    # In case of using Ordinary Discriminant Strategy we return NAN
    # So the result imaginary and real part of complex number should be equal to NAN
    print(f"Results of 'x^2 + 4x + 5 = 0' equation using Ordinary Discriminant Strategy should be equal to "
          f"'{complex(cmath.nan, cmath.nan)}' and '{complex(cmath.nan, cmath.nan)}' complex numbers.")
    print(f"Actual results are: x1 = {results[0]}, x2 = {results[1]}\n")

    print(f"Real part of first result is NAN: {cmath.isnan(results[0].real)}")
    print(f"Real part of second result is NAN: {cmath.isnan(results[0].real)}")
    print(f"Imaginary part of first result is NAN: {cmath.isnan(results[0].real)}")
    print(f"Imaginary part of second result is NAN: {cmath.isnan(results[0].real)}")


if __name__ == '__main__':
    main()
