# Using Ambiguous Grammars

- A grammar is **ambiguous** if it can generate more than one **leftmost derivation** or **rightmost derivation** for the same sentence .
- Ambiguous grammars are **undesirable** for compiler design because they can lead to **conflicts** in parsing and **multiple meanings** for the same program.
- Ambiguous grammars can be **detected** by using **parsing algorithms** such as **top-down** or **bottom-up** parsing and checking if they produce more than one **parse tree** for the same sentence .
- Ambiguous grammars can be **resolved** by using **precedence** and **associativity** rules for operators, **eliminating** left recursion and common prefixes, **introducing** new non-terminals, or **rewriting** the grammar in an **unambiguous** way  .
- An example of an ambiguous grammar is:

```
S -> i E t S | i E t S e S | a
E -> b
```

This grammar can generate two different parse trees for the sentence `i b t a e a`:

```
     S                        S
    /|\                      /|\
   / | \                    / | \
  i  E  t                  i  E  t
     |   |                    |   \
     b   S                    b    S
        /|\                       /|\
       / | \                     / | \
      i  E  t                   i  E  t
         |   |                    |   \
         b   S                    b    S
            /|\                       / \
           / | \                     /   \
          e  S  S                   e     S
             |  |                         |
             a  a                         a
```

The sentence can have two different meanings depending on which parse tree is chosen. The first parse tree corresponds to the interpretation `(if b then (if b then a else a))`, while the second parse tree corresponds to the interpretation `(if b then (if b then a) else a)`.