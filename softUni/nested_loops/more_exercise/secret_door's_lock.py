hundreds = int(input())
tens = int(input())
ones = int(input())

one = 0
ten = 0
hun = 0


def is_prime(tens):
    if ten < 2:
        return False
    for i in range(2, tens):
        if ten % i == 0:
            return False
    return True


for hun in range(1, hundreds + 1):
    for ten in range(2, tens + 1):
        for one in range(1, ones + 1):
            if hun % 2 == 0 and one % 2 == 0 and is_prime(ten):

                print(hun, ten, one)
