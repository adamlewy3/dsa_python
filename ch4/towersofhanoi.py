class Hanoi:
    def __init__(self, n):
        """ 
        n: the number of disks.
        3 rods
        
        store the position of each disk as a n x 3 matrix
        """
        self.n = n
        m, n = self.n, 3
        self.pos = []
        self.move_number = 0
        self.move_storage = {}

        for i in range(3):
            self.pos.append([0] * m)

        for  i in range(m):
            self.pos[0][i] = i+1

    #Next step - define legal moves.
    def print_pos(self):
        print(self.pos)

    def move_disk(self,n,m, printed_move = False):
        """
        Move the top disk from rod n to rod m
        """    
        assert isinstance(n, int)    
        assert isinstance(m, int)

        if n <= 0 or m <= 0:
            raise ValueError("Inputs must be between 1 and 3")

        if n >3 or m >3:
            raise ValueError("Inputs must be between 1 and 3")

        if printed_move == True:
            print(f"Attempted to move from rod {n} to rod {m}")

        # [[1,2,3], [0,0,0], [0,0,0]]

        first_zero = Hanoi.find_first_zero(self.pos[m-1])
        last_zero = Hanoi.find_last_zero(self.pos[m-1])
        first_nonzero = Hanoi.find_first_nonzero(self.pos[n-1])
        moved_disk = self.pos[n-1][first_nonzero]
        top_disk = self.pos[m-1][Hanoi.find_first_nonzero(self.pos[m-1])]


        if type(first_nonzero) == str:
            return "There are no disks on this rod!"
        if type(first_zero) == str:
            return "Cannot move here - the rod is full!" 

        if top_disk == 0:
            self.pos[m-1][last_zero] = moved_disk
            self.pos[n-1][first_nonzero] = 0
            self.move_number += 1
            self.move_storage.update({self.move_number: [n,m]})

        elif moved_disk > top_disk:
            raise ValueError("Cannot move a larger disk onto a smaller disk!")
        else:
            self.pos[m-1][last_zero] = moved_disk
            self.pos[n-1][first_nonzero] = 0
            self.move_number += 1
            self.move_storage.update({self.move_number : [n,m]})

        
    @staticmethod
    def find_first_zero(data):
        """
        Takes in a 1D array and returns the index of the first zero 
        """
        for i in range(len(data)):
            if data[i] == 0:
                return i
        return "No zeros"
    
    @staticmethod
    def find_last_zero(data):
        for i in range(len(data)-1, -1, -1):
            if data[i] == 0:
                return i
        return "No zeros"

    @staticmethod
    def find_first_nonzero(data):
        """
        Takes in a 1D array and returns the index of the first non-zero element
        """
        for i in range(0,len(data)):
            if data[i] != 0:
                return i
        return 0 

    def is_solved(self):
        if self.pos[-1] == [i+1 for i in range(self.n)]:
            return True
        else:
            return False

    def hanoi_solve(self):
        "A function that will solve the towers of hanoi puzzle"
        pass


    def move_top(self, i, n, m):
        self.print_pos()
        """
        Moves the top i <= self.n blocks from rod n to rod m

        Here, we also assume that the we are starting with a fresh block orientation.

        """
        for x in range(2):
            if x+1 not in {n,m}:
                aux_rod = x

        print(aux_rod)
        if i == 1:
            self.move_disk(n,m,printed_move = True)

        if i == 2:
            self.move_disk(n,aux_rod)
            self.move_disk(n,m)
            self.move_disk(aux_rod,m)

        else:
            self.move_top(i-1,n, aux_rod)
            self.move_disk(n,m)
            self.move_top(i-1, aux_rod,m)

if __name__ == '__main__':
    """
    h1 = Hanoi(3)
    h1.print_pos()
    h1.move_disk(1,2)
    h1.print_pos()
    h1.move_disk(1,3)
    h1.print_pos()
    h1.move_disk(3,1)
    h1.print_pos()
    """

    h3 = Hanoi(3)
    h3.move_top(3,1,3)
    h3.print_pos()
