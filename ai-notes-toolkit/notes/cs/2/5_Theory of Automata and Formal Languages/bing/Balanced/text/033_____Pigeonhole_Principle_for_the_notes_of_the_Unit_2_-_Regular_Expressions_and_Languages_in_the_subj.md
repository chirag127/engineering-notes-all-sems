### Pigeonhole Principle

- The pigeonhole principle is a simple but useful mathematical concept that states that if there are more items than containers, then at least one container must hold more than one item.
- For example, if there are 10 pigeons and 9 pigeonholes, then at least one pigeonhole must have more than one pigeon.
- The pigeonhole principle can be used to prove the existence of certain patterns or properties in discrete mathematics, such as combinatorics, number theory, graph theory, etc.
- The pigeonhole principle can also be applied to regular expressions and languages, which are the topics of this unit.
- A regular expression is a string that describes a set of strings, called a regular language, using symbols and operators such as concatenation, union, and Kleene star.
- A regular language is a set of strings that can be recognized by a finite automaton, which is a model of computation that has a finite number of states and transitions.
- The pigeonhole principle can be used to show that some regular languages are infinite, that some regular expressions are equivalent, and that some regular languages are not regular.

#### Examples of using the pigeonhole principle for regular expressions and languages

- To show that the regular language L = {a^n b^n | n >= 0} is infinite, we can use the pigeonhole principle as follows:
  - Suppose L is finite and has k strings, where k is a positive integer.
  - Let n be the largest number such that a^n b^n is in L.
  - Then, L contains all the strings of the form a^i b^i for i = 0, 1, ..., n.
  - Consider the string s = a^(n+1) b^(n+1), which has length 2n + 2.
  - Since s is not in L, it must be different from every string in L.
  - However, s has only n + 1 distinct symbols, namely a and b.
  - Therefore, by the pigeonhole principle, there must be two positions in s that have the same symbol, say s[i] = s[j].
  - Without loss of generality, assume that s[i] = s[j] = a.
  - Then, the string t = s[1..i-1] s[i+1..j-1] s[j+1..2n+2] is in L, because it has the form a^m b^m for some m <= n.
  - But t has length 2n, which is less than the length of s, and t is different from s, which contradicts the assumption that n is the largest number such that a^n b^n is in L.
  - Therefore, L must be infinite.

- To show that the regular expressions (a + b)* and (a* + b*)* are equivalent, we can use the pigeonhole principle as follows:
  - Let L1 and L2 be the regular languages described by (a + b)* and (a* + b*)*, respectively.
  - We need to show that L1 = L2, that is, every string in L1 is also in L2, and vice versa.
  - To show that L1 is a subset of L2, we can use induction on the length of the strings in L1.
    - Base case: The empty string is in L1, and also in L2, because it is the result of applying the Kleene star zero times to a* + b*.
    - Induction step: Suppose s is a non-empty string in L1, and s has length n. Then s has the form xy, where x and y are strings in L1, and x has length k and y has length n - k, for some k between 0 and n. By the induction hypothesis, x and y are also in L2. Then, x has the form a^i b^j for some i, j >= 0, and y has the form a^k b^l for some k, l >= 0. We need to show that xy is also in L2. There are two cases to consider:
      - Case 1: j = 0. Then, xy has the form a^(i+k) b^l, which is in L2, because it is the result of applying the Kleene star once to a* + b*, and then applying the Kleene star l times to b*.
      - Case 2: j > 0. Then, xy has the form a^i b^(j+k) a^l, which is in L2, because it is the result of applying