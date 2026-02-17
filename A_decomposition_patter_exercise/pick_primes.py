from is_prime import is_prime
def pick_primes(lst):
    primes = []
    for num in lst:
        if is_prime(num):
            primes.append(num)
    return primes 
    
print(pick_primes([12,3,7,18,11]))
# [3, 7, 11]

print(pick_primes([17,23,9,42]))
# [17, 23]

print(pick_primes([4,2048,100,55]))
# []