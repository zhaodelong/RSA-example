# sage RSA
# Learn from Network Security class 
# Demo for https://factorable.net/weakkeys12.extended.pdf 
# Philip Knous presentation
p = Primes().next(ZZ.random_element(2^1024))
p
q = Primes().next(ZZ.random_element(2^1024))
q
n = p * q
n
e = 65537
d = mod(e, (p - 1) * (q - 1)) ^(-1)
M = 123456789 # plain text
C = mod(M^e, n) # cipher text
C
mod(C^d, n) # decryption
z = Primes().next(ZZ.random_element(2^1024))
x = q * z
x
gcd(x, n)
gcd(x, n) == q
n / q 
n / q == p
