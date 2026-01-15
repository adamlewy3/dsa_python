class Polynomial:
    def __init__(self, d=0):
        assert isinstance(d, int)
        self._coeffs = [0] * (d+1)
        self._degree = d

    def __len__(self):
        return len(self._coeffs)

    def deg(self):
        return self._degree

    def __getitem__(self,j):
        """ Return the coefficient of x^j """
        return self._coeffs[j]

    def __setitem__(self, j, val):
        """ Set the coefficient of x^j """
        self._coeffs[j] = val

    def __eq__(self, other):
        return self._coeffs == other._coeffs

    def deriv(self): 
        output = Polynomial(self.deg()-1)
        for i in range(len(output)):
            output[i] = (i+1)*self[i+1]
        return output
    

if __name__ == '__main__':
    p1 = Polynomial(3)
    p1[0] = 1
    p1[1] = 3
    p1[2] = 2
    p1[3] = 5
    print(list(p1))
    print(list(p1.deriv()))
    #Works as expected
