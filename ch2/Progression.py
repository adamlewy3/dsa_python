class Progression:
    """Iterator producing a generic progression.

    Default iterator produces the whole numbers 0, 1, 2,.. """

    def __init__(self, start=0):
        """Initialise current to the first value of the progression."""
        self._current = start

    def _advance(self):
        """By convention, if current is set to None, this designates
        the end of a finite progression."""
        self._current += 1

    def __next__(self):
        """Return the next element, or raise a StopIteration error."""
        if self._current == None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance() # advance to prepare for next time
            return answer

    def __iter__(self):
        return self

    def sum_progression(self, n):
        """Retuns the sum of the next n values of the progression"""
        total = 0
        for j in range(n):
            total += next(self) 
        
        print(total)

    def print_progression(self, n):
        """Print the next n values of the progression."""
        print(' '.join(str(next(self)) for j in range(n)))
        

class ArithmeticProgression(Progression):
    """An arithmetic progression iterator which extends Progression."""
    def __init__(self, step=1, start = 0):
        super().__init__(start)
        self._step = step
            
    def _advance(self):
        self._current += self._step


class GeometricProgression(Progression):
    """ A geometric progression iterator extending Progression."""
    def __init__(self, ratio= 2, start = 2):
        """Create a new geometric progression.
            
        start: the first term of the progression (default 1)
        ratio: the fixed constant multiplied to each term (default 2)
        """

        super().__init__(start)
        self._ratio = ratio

    def _advance(self):
        self._current *= self._ratio


class FibonacciProgression(Progression):
    """ A fibonacci progression iterator extending Progression."""
    def __init__(self, first = 0, second = 1):
        """ Initialise a new iterator

        first: the first term of the progression (default 0)
        second: the second term of the progression (default 1). """

        super().__init__(first)
        self._prev = second - first # fictitious value preceding the first

    def _advance(self):
        """Update current value by taking sum of previous two."""
        self._prev, self._current = self._current, self._prev + self._current
        

if __name__ == '__main__':
    print('Default progression:')
    Progression().print_progression(10)
 
    print('Arithmetic progression with increment 5:')
    ArithmeticProgression(5).print_progression(10)

    print('Geometric progression with ratio 2:')
    GeometricProgression(2).print_progression(10)

    print('Geometric progression with ratio 3:')
    GeometricProgression(3).print_progression(10)

    print('Fibonacci progression with default start values:')
    FibonacciProgression().print_progression(10)

    print('Fibonacci progression with start values 4 and 6:')
    FibonacciProgression(4,6).print_progression(10)
