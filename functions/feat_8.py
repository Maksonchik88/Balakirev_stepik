x = input()

t = {'A', 'E', 'I', 'O', 'U', 'Y', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V',
     'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_', 'a', 'e', 'i', 'o', 'u', 'y', 'b', 'c',
     'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', '@', '.'}


def email(x):
    b = 0
    if x.find('@') != -1 and x.find('@') != -1:
        x = x.replace('@', '')
        x = x.replace('.', '')
        for i in x:
            if i in t:
                b += 1
    else:
        print('НЕТ')
    if b == len(x):
        print('ДА')
    else:
        print('НЕТ')


email(x)
