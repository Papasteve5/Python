
shift = 4

with open('caesar.txt') as c:
    for line in c:
        code = line.strip()
        print('Inhalt: ', code)


for char in code:
    num = ord(char)
    print(chr((num + shift) % 256), end = "")