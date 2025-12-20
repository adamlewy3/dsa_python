class Vector:
    """Represent a vector in multidimensional space."""

    def __init__(self, d):
        """Create d-dimensional vector of zeros."""
        self._coords = [0] * d
    
    def __len__(self):
        """Return the dimension of the vector."""
        return len(self._coords)

    def __getitem__(self, j):
        """Return j'th coordiante of vector."""
        return self._coords[j] #This is clearly not robust

    def __setitem__(self, j, val):
        """Set the jth coordinate of vector to given value.

            Notice that this is a mutator method - we are not returning a new object, but updating 
            this instance of the object. """
        self._coords[j] = val
        
    def __add__(self, other):
        """Return sum of two vectors."""
        if len(self) != len(other): #relies on __len__ method defined above
            raise ValueError("Dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result #We are returning a new instance of our Vector class 

    def __sub__(self, other):
        return self + -other

    def __neg__(self):
        neg = Vector(len(self))
        for i in range(len(self)):
            neg[i] = -self[i]
        return neg

    def __eq__(self, other):
        return self._coords == other._coords
        
    def __ne__(self, other):
        return not self == other

    def __str__(self):
        """Produce string representation of vector."""
        return '<' + str(self._coords)[1:-1] + '>'


if __name__ == '__main__':
    v = Vector(3)
    w = Vector(3)
    
    for i in range(len(v)):
        v[i] = i

    w[0] = 2
    w[1] = 3
    w[2] = 4

    print(v)
    print(w)
    print(-v)
    print(v-w)
    print(v+w)

    """Again, this class is not robust yet. Need more type-checking, for instance"""
