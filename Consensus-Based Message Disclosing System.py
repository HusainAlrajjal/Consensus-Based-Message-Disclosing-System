import sys

from Code.MLS import *
import math
import string

from Code.main import generatePairWiseCoPrimes, save_keys

sys.setrecursionlimit(4500)

supported_chars = string.printable
chars = list()
chars.append('RESERVED')
for i in supported_chars[:-1]:
    chars.append(i)


def map_to_numbers(secret_text):
    mapped_chars = list()
    for i in secret_text:
        mapped_chars.append(format((chars.index(i)), '02d'))
    number = ''
    for i in mapped_chars:
        number += i

    return number


def input_request():
    secret_text = input('Enter the text you wanna hide:>> ')
    print(len(secret_text), secret_text)

    n = int(input('Enter the number of secret-keepers (n): '))  # number of keys
    print('n= ', n)

    k = int(input('How many of them is sufficient (k)? '))  # threshold
    print('k= ', k)

    return secret_text, n, k


def check_for_sufficient_coprimes(N, n, k):
    minimum, maximum = math.ceil(pow(N, 1 / k)), math.floor(pow(N, 1 / (k - 1)))
    range_possible = maximum - minimum + 1
    n_cop = restircted_max_coprime(n, minimum, maximum)
    return range_possible, n_cop, minimum, maximum


def n_keys_generation_and_save(N, n, minimum, maximum):
    mList = list()
    M = 1
    keys = []
    while N >= M or (0 in keys):
        keys = []
        M = 1
        mList = list(generatePairWiseCoPrimes(n, minimum, maximum))
        for m in mList:
            M *= m
        keys = [N % m for m in mList]

    testingKeys = []
    for i in range(len(mList)):
        testingKeys.append((keys[i], mList[i]))
    save_keys(testingKeys)
    return testingKeys


def map_to_text(number):
    number = str(number)
    if len(number) % 2 != 0:
        number = '0' + number

    original_chars = list()
    for i in range(0, len(number), 2):
        original_chars.append(int(number[i:i + 2]))

    text = ''
    for i in original_chars:
        text += chars[i]

    return text


def main():
    secret_text, n, k = input_request()

    secret_N = map_to_numbers(secret_text)

    N = int(secret_N)

    # Check For sufficient Co-primes
    range_possible, n_cop, minimum, maximum = check_for_sufficient_coprimes(N, n, k)

    if range_possible < n or n_cop < n:
        print('It is not feasible!!')
        return

    # n KEYS GENERATION
    n_keys_generation_and_save(N, n, minimum, maximum)

    print("please enter the key pair separated by space [e.g. 62 102]: ")
    print('To exit, please enter e\n')
    print('k = ', k, 'n = ', n, "\n")

    testingKeys = []
    count = 0
    while True:
        count += 1
        userInput = input("key " + str(count) + ":\t").split()
        if userInput[0] == 'e' or userInput[1] == 'e':
            print('')
            break
        testingKeys.append((int(userInput[0]), int(userInput[1])))

    XmodM = getXmodM_crt(set(testingKeys))

    x = XmodM[0]
    M = XmodM[1]

    print(x)
    real_text = map_to_text(x)
    print(len(real_text), real_text)


if __name__ == '__main__':
    main()
