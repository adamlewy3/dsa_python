def factorial(n):
    if n < 0:
        raise ValueError
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def draw_line(tick_length, tick_label = ''):
    line = '-' * tick_length
    if tick_label:
        line += ' ' + tick_label
    print(line)

def draw_interval(centre_length):
    if centre_length > 0:
        draw_interval(centre_length - 1)
        draw_line(centre_length)
        draw_interval(centre_length - 1)

def draw_ruler(num_inches, major_length):
    draw_line(major_length, '0')
    for j in range(1, 1+num_inches):
        draw_interval(major_length - 1)
        draw_line(major_length, str(j))


def binary_search(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True, mid
        elif target < data[mid]:
            return binary_search(data, target, low, mid-1)
        else:
            return binary_search(data, target, mid+1, high)

data = [1,3,6,7,8,11,14,25,26]

# A recursive function for summing a sequence

def linear_sum(S,n):
    """Returns the sum of the first n elements in a sequence
    
    S: array of floats
    n: number of elements
    """
    if n == 0:
        return 0
    else:
        return linear_sum(S,n-1) + S[n-1]

print(linear_sum(data,3))

# A recursive function for reversing a sequence

def reverse_seq(S,start, stop):
    """ Returns the function S with order reversed """
    if start < stop-1: #At least 2 elements
        S[start], S[stop-1] = S[stop-1], S[start]
        reverse_seq(S, start+1, stop-1)

print(reverse_seq(data, 0, len(data)))
