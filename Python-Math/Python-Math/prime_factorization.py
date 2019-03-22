import sys


primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]
# Prime Factorization

def prime_factorization(x):
    exponents = []
    for prime in primes:
        if prime > x / 2:
            return zip(primes,exponents[:primes.index(prime)])

        count = 0
        _x = x
        while(True):
            rem = _x % prime
            
            if (rem > 0):
                exponents.append(count)
                break
            
            _x /= prime

            count += 1

    return zip(primes,exponents)        

def main():
    try:
        x = int(sys.argv[1])
    except Exception as e:
        print(f'Error:\n\n{e}\n\nUsage: python script.py <x>')
        exit(1)

    result = prime_factorization(x)
    print(list(result))

if __name__ == '__main__':
    main()