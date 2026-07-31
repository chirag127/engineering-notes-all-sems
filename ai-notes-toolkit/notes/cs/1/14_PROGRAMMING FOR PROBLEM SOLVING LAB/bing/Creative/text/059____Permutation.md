## Permutation

- A permutation is an arrangement of objects in a specific order.
- The order of the objects matters in a permutation.
- For example, the permutations of the letters A, B, and C are ABC, ACB, BAC, BCA, CAB, and CBA. Changing the order of the letters produces different permutations.
- The number of permutations of n distinct objects is n factorial, denoted by n!.
- n! = n * (n-1) * (n-2) * ... * 3 * 2 * 1
- For example, the number of permutations of 3 distinct objects is 3! = 3 * 2 * 1 = 6.
- If some of the objects are identical, the number of permutations is reduced by dividing by the factorial of the number of identical objects.
- For example, the number of permutations of the letters A, A, and B is 3! / 2! = 3, since there are 2 identical A's.
- A permutation of r objects chosen from n distinct objects is called a permutation of n objects taken r at a time, denoted by nPr.
- nPr = n! / (n-r)!
- For example, the number of permutations of 2 letters chosen from 3 distinct letters is 3P2 = 3! / (3-2)! = 6.
- A permutation of r objects chosen from n identical objects is called a permutation with repetition, denoted by n^r.
- n^r = n * n * ... * n (r times)
- For example, the number of permutations of 2 letters chosen from 3 identical letters is 3^2 = 9.