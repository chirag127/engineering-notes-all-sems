### Recursively defined functions

- A recursively defined function is a function that is defined by a set of rules that specify how to compute the value of the function for any input by using the values of the function for smaller inputs.
- A recursively defined function consists of two parts: a base case and a recursive step.
- The base case defines the value of the function for the smallest or simplest input, such as 0 or 1.
- The recursive step defines the value of the function for any input in terms of the value of the function for a smaller or simpler input, usually by using a formula that involves the input and the function itself.
- For example, the factorial function n! is defined recursively by the rules:

  - 0! = 1 (base case)
  - (n + 1)! = (n + 1)· n ! (recursive step)

- To compute the value of n! for any positive integer n, we can use the recursive step repeatedly until we reach the base case of 0! = 1, and then multiply the results.
- For example, to compute 3!, we can use the recursive step to get:

  - 3! = (3 + 1)! / 4 = 4! / 4
  - 4! = (4 + 1)! / 5 = 5! / 5
  - 5! = (5 + 1)! / 6 = 6! / 6
  - 6! = (6 + 1)! / 7 = 7! / 7
  - 7! = (7 + 1)! / 8 = 8! / 8
  - 8! = (8 + 1)! / 9 = 9! / 9
  - 9! = (9 + 1)! / 10 = 10! / 10
  - 10! = (10 + 1)! / 11 = 11! / 11
  - 11! = (11 + 1)! / 12 = 12! / 12
  - 12! = (12 + 1)! / 13 = 13! / 13
  - 13! = (13 + 1)! / 14 = 14! / 14
  - 14! = (14 + 1)! / 15 = 15! / 15
  - 15! = (15 + 1)! / 16 = 16! / 16
  - 16! = (16 + 1)! / 17 = 17! / 17
  - 17! = (17 + 1)! / 18 = 18! / 18
  - 18! = (18 + 1)! / 19 = 19! / 19
  - 19! = (19 + 1)! / 20 = 20! / 20
  - 20! = (20 + 1)! / 21 = 21! / 21
  - 21! = (21 + 1)! / 22 = 22! / 22
  - 22! = (22 + 1)! / 23 = 23! / 23
  - 23! = (23 + 1)! / 24 = 24! / 24
  - 24! = (24 + 1)! / 25 = 25! / 25
  - 25! = (25 + 1)! / 26 = 26! / 26
  - 26! = (26 + 1)! / 27 = 27! / 27
  - 27! = (27 + 1)! / 28 = 28! / 28
  - 28! = (28 + 1)! / 29 = 29! / 29
  - 29! = (29 + 1)! / 30 = 30! / 30
  - 30! = (30 + 1)! / 31 = 31! / 31
  - 31! = (31 + 1)! / 32 = 32! / 32
  - 32! = (32 + 1)! / 33 = 33! / 33
  - 33! = (33 + 1)! / 34 =