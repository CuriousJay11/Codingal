import math

print("Value of pi:",math.pi)
print("Value of e:", math.e)

print("Square root of 16",math.sqrt(16))

print("GCD of 48 and 18",math.gcd(48,18))

print("2 raised to the power of 3:", math.pow(2,3))

print("Ceiling of 4.2:",math.ceil(4.2))
print("Floor of 4.8:", math.floor(4.8))

print("Factorial of 5:",math.factorial(5))

print("Is NaN", math.isnan(float("nan")))
print("Is Infinity", math.isinf(float("inf")))

values = [-4,-9,-16]
positive_values =  [math.copysign(abs(num),1)for num in values]