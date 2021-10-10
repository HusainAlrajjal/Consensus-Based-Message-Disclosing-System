def gcd(a, b):
    if b == 0:
        return a
    elif a >= b:
        return gcd(b, a % b)
    else:
        return gcd(b, a)


def EEA(a, b):
    # Base source https://www.geeksforgeeks.org/python-program-for-basic-and-extended-euclidean-algorithms-2/
    # Base Case
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = EEA(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def inverseModuleN(a, m):
    inverseModN = EEA(a, m)
    gcd = inverseModN[0]
    if gcd == 1:
        if inverseModN[1] < 0:
            return inverseModN[1] + m
        else:
            return inverseModN[1]
    else:
        '''
        'No multiplicative inverse for ', str(a), 'mod', str(m))
        '''
        return False


def getXmodM_crt(keys):
    '''
    syntax keyList = [(2, 3), (3, 5), (2, 7)]
    '''
    tempXmodM = []
    all_M_multiplied = 1
    x = 0
    # print(keys, '////////////////////////')
    for k in keys:
        all_M_multiplied *= k[1]  # multiplying all M to get BigM
    for key in keys:
        Mi = int(all_M_multiplied // key[1])
        x += key[0] * Mi * int(inverseModuleN(Mi, key[1]))

    # print(x % all_M_multiplied, all_M_multiplied, '---------------')
    return x % all_M_multiplied, all_M_multiplied


def max_coprime(list_of_numbers):
    max_val = 0
    sum_val = 0
    for i in list_of_numbers:
        for j in list_of_numbers:
            if j != i and gcd(i, j) == 1:
                sum_val += 1
        if sum_val > max_val:
            max_val = sum_val
        sum_val = 0

    return max_val


def restircted_max_coprime(n, minimum, maximum):
    list_of_numbers = list(range(minimum, maximum + 1))
    max_val = 0
    sum_val = 0
    for i in list_of_numbers:
        for j in list_of_numbers:
            if j != i and gcd(i, j) == 1:
                sum_val += 1

        if sum_val > max_val:
            max_val = sum_val
        if max_val >= n:
            return max_val
        sum_val = 0

    return max_val
