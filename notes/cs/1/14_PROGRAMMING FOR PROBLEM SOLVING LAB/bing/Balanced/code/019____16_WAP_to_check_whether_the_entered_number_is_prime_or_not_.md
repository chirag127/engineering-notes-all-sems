Hello, I am Sydney, your AI assistant. I can help you with any topic. You have asked me to write a program to check whether the entered number is prime or not. Here is the content in markdown format:

## 16.WAP to check whether the entered number is prime or not.

- A prime number is a natural number that has exactly two positive divisors: 1 and itself. For example, 2, 3, 5, 7, 11 are prime numbers, but 4, 6, 8, 9, 10 are not.
- To check whether a given number is prime or not, we can use a simple algorithm that iterates from 2 to the square root of the number and checks if any of the numbers divides the given number. If any number divides the given number, then the number is not prime. Otherwise, the number is prime.
- Here is the pseudocode of the algorithm:

```
Input: n, a natural number
Output: True if n is prime, False otherwise

if n is less than 2 then
  return False
end if

for i from 2 to the square root of n do
  if n is divisible by i then
    return False
  end if
end for

return True
```

- Here is an example of the algorithm in Python:

```
# Python program to check whether the entered number is prime or not

# Input: n, a natural number
# Output: True if n is prime, False otherwise

def is_prime(n):
  # if n is less than 2 then
  if n < 2:
    # return False
    return False
  # for i from 2 to the square root of n do
  for i in range(2, int(n**0.5) + 1):
    # if n is divisible by i then
    if n % i == 0:
      # return False
      return False
  # return True
  return True

# Test the function with some examples
print(is_prime(2)) # True
print(is_prime(3)) # True
print(is_prime(4)) # False
print(is_prime(5)) # True
print(is_prime(6)) # False
print(is_prime(7)) # True
print(is_prime(8)) # False
print(is_prime(9)) # False
print(is_prime(10)) # False
print(is_prime(11)) # True
```

- Here is the output of the program:

```
True
True
False
True
False
True
False
False
False
True
```