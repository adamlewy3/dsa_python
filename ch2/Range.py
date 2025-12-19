class Range:
    """A class mimicing the built-in range class."""
    def __init__(self, start, stop=None, step=1):
        """Initialise a Range instance"""

        if step == 0:
            raise ValueError('step cannot be 0')

        if stop is None:
            start, stop = 0, start #says that Range(n) should be Range(0,n)

        #calculate the effective length once
        self._length = max(0, (stop-start+step-1) // step)

        #need knowledge of start and step (but not stop) to support __getitem__
        self._start = start
        self._step = step

    def __len__(self):
        return self._length

    def __getitem__(self, k):
        if k < 0:
            k+=len(self)

        if not 0 <= k < self._length:
            raise IndexError('Index out of range')

        return self._start + k*self._step


if __name__ == '__main__':
    r = Range(10)
    print(r[5])
    for i in Range(1, 150, 20):
        print(i)
