fp = open('test.txt')

prepared_file = []

print(fp.read())
print(type(fp.read()))
print(len(fp.read()))

print(fp.readline())
for line in fp:
    if fp.readline() != '\n':
        prepared_file.append(line)


