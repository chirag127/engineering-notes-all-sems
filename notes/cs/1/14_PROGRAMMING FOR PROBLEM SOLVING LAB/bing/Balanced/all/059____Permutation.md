## Permutation

- A permutation is an arrangement of objects in a specific order.
- The order of the objects matters in a permutation.
- For example, the permutations of the letters A, B, and C are ABC, ACB, BAC, BCA, CAB, and CBA. Changing the order of the letters produces different permutations.
- The number of permutations of n distinct objects is n factorial, denoted by n!.
- n! = n * (n-1) * (n-2) * ... * 3 * 2 * 1
- For example, the number of permutations of 3 distinct objects is 3! = 3 * 2 * 1 = 6.
- If some of the objects are repeated, the number of permutations is reduced by dividing by the factorial of the number of repetitions.
- For example, the number of permutations of the letters A, A, and B is 3! / 2! = 3, because there are 2 repetitions of A. The permutations are AAB, ABA, and BAA.
- A permutation of r objects chosen from n distinct objects is called a permutation of n objects taken r at a time, denoted by P(n, r).
- P(n, r) = n! / (n-r)!
- For example, the number of permutations of 2 letters chosen from 3 distinct letters is P(3, 2) = 3! / (3-2)! = 6. The permutations are AB, AC, BA, BC, CA, and CB.