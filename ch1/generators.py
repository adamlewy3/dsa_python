def factors(n):
    for k in range(1,n+1):
        if n % k == 0:
            yield k

user_input = int(input("Enter a number"))

for value in factors(user_input):
    print(value)
