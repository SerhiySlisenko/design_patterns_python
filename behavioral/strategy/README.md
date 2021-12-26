# Strategy pattern using Python
Implementation of Strategy Design Pattern according to the task from 'Design Patterns in Python' course
https://www.udemy.com/course/design-patterns-python/

In this task, a quadratic equation solver was implemented. It always returns complex numbers as defined by the API.

Users can follow two different strategies, Real or Ordinary Discriminant. 

In the case of using OrdinaryDiscriminantStrategy, the discriminant cannot be less than 0, so the discriminant result will be NaN (not a number). 
Hence, the results of solving of quadratic equation will have NaN in both real and imaginary parts.
