### Extended Euclidean Algorithm

- The extended Euclidean algorithm is an algorithm to compute integers x and y such that ax + by = gcd(a,b) given a and b, where gcd(a,b) is the greatest common divisor of a and b.
- The existence of such integers is guaranteed by Bézout's lemma, which states that for any two integers a and b, there exist integers x and y such that ax + by = gcd(a,b).
- The extended Euclidean algorithm can be viewed as the reciprocal of modular exponentiation, which is the operation of computing a^b mod n, where a, b and n are integers and n > 0.
- The extended Euclidean algorithm is particularly useful when a and b are coprime, meaning that gcd(a,b) = 1. In this case, the algorithm can be used to find the multiplicative inverse of a modulo b, which is the unique integer x such that ax ≡ 1 (mod b).
- The extended Euclidean algorithm can also be used to solve linear congruences of the form ax ≡ c (mod b), where a, b and c are given integers and x is the unknown integer. To solve such a congruence, we first find the gcd(a,b) using the Euclidean algorithm, and then check if c is divisible by gcd(a,b). If not, then the congruence has no solution. If yes, then we divide both sides of the congruence by gcd(a,b) and apply the extended Euclidean algorithm to find x.
- The extended Euclidean algorithm can also be generalized to compute the polynomial greatest common divisor and the coefficients of Bézout's identity of two univariate polynomials. The algorithm works similarly to the integer case, except that the division and remainder operations are replaced by polynomial division and remainder operations.
- The extended Euclidean algorithm can be implemented using the following pseudocode:

```
function extended_euclidean(a, b)
  if b == 0 then
    return (a, 1, 0) // gcd(a,b) = a, x = 1, y = 0
  else
    (d, x, y) = extended_euclidean(b, a mod b) // recursive call
    return (d, y, x - (a div b) * y) // gcd(a,b) = d, x = y, y = x - (a div b) * y
  end if
end function
```

- The algorithm returns a tuple (d, x, y) such that d = gcd(a,b) and ax + by = d.
- The algorithm has a time complexity of O(log(min(a,b))) and a space complexity of O(1).