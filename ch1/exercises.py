#R-1.1
def is_multiple(n,m):
    x1,y1 = divmod(n,m)
    x2,y2 = divmod(m,n)
    if y1 == 0 or y2 == 0:
        return True
    else:
        return False

#R-1.2
def is_even(k):
    k = k if k >= 0 else -k
    factors = {k-2*i for i in range(0,k+1)}
    if 0 in factors:
        return True
    else:
        return False
#The above function to me seems quite inefficent, given that we are working in base 2 it is
#probably possible to do this bitwise.

#R-1.3
def minmax(data):
    data = sorted(data)
    return  data[0], data[-1]

#print(minmax((2,4,61,2,3,8,1,23,4)))

#R-1.4, 1.5
def sumofsquares(k):
    return sum(k*k for k in range(1,k))

def sumofsquares2(k):
    return (k-1)*(k)*(2*(k-1)+1)/6

#print(sumofsquares(56))
#print(sumofsquares2(56))

#R-1.6, 1.7
def sumofsquares3(k):
    return sum(k*k for k in range(1,k,2))

#R-1.9

gen1 = (i for i in range(50,90,10))

#for num in gen1:
#    print(num)

#R-1.10
gen2 = (i for i in range(8,-10,-2))

#for num in gen2:
#    print(num)

#R-1.11

list1 = [2**i for i in range(9)]
#print(list1)

#C-1.18
list2 = [i**2 + i for i in range(10)]
#print(list2)

#C-1.19
my_str = "thequickbrownfoxjumpsoverthelazydog"
my_list = sorted(set(my_str))
#print(my_list)
print(ord('a'))


print([chr(i+65) for i in range(26)])
print([chr(i+97) for i in range(26)])
