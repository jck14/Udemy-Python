def lesser_of_two_evens(a, b):

    if not(a % 2) and not(b % 2):
        return min(a, b)
    else:
        return max(a, b)


def animal_crackers(s):
    tmp = s.lower().split(' ')
    if tmp[0][0] == tmp[1][0]:
        return True
    else:
        return False


def makes_twenty(a, b):
    return a + b == 20 or a == 20 or b == 20


if __name__ == '__main__':

    print(lesser_of_two_evens(3, 4))

    print(animal_crackers('Lazy hlama'))

    print(makes_twenty(10, 10))
