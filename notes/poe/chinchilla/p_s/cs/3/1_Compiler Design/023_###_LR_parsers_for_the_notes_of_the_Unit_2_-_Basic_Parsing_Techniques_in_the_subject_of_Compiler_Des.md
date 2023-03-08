### LR parsers

LR parsing is a bottom-up parsing technique that is commonly used in compiler design. LR stands for 'Left to Right' scanning of the input and producing a 'Rightmost Derivation' of the parse tree. In this method, the parser reads the input string from left to right and builds a parse tree from the bottom up.

#### Types of LR parsers

There are different types of LR parsers based on the number of tokens they look ahead in the input stream. The most commonly used ones are:

1. LR(0) parser: It looks at no lookahead token and uses only the current input symbol to make a parsing decision.

2. SLR(1) parser: It uses a single lookahead token to decide the parsing action. It is a simple and efficient parser but has some limitations.

3. LALR(1) parser: It is based on the SLR(1) parser but handles more lookahead tokens efficiently. It is the most widely used LR parser.

4. LR(1) parser: It uses one token lookahead and is the most powerful but also the most complex LR parser.

#### Advantages of LR parsers

- LR parsers are efficient and fast, and can handle a large class of grammars.
- They can handle left-recursive grammars, which cannot be handled by LL parsers.
- They can handle ambiguous grammars and provide a unique parse tree.
- They can be easily generated from a grammar using parser generators like Yacc, Bison, etc.

#### Disadvantages of LR parsers

- LR parsers require more memory and processing power than LL parsers.
- They are more complex to understand and implement than LL parsers.
- They can produce large parse tables, which can be difficult to handle.

#### Example of LR parsing

Consider the following grammar:

```
S → Aa | b
A → Ac | d
```

The LR(1) parsing table for this grammar is:

```
+----+-------------+-------------+-------------+-------------+-------------+-------------+
|    |     a       |     b       |     c       |     d       |     $       |     A       |
+----+-------------+-------------+-------------+-------------+-------------+-------------+
|  0 |   s1        |             |             |   s2        |             |   3         |
|  1 |             |   r2        |             |   r2        |   r2        |             |
|  2 |             |   r1        |   s4        |   r1        |   r1        |             |
|  3 |             |             |             |             |   accept    |             |
|  4 |   s1        |             |             |   s2        |             |   5         |
|  5 |             |   r4        |             |   r4        |   r4        |             |
+----+-------------+-------------+-------------+-------------+-------------+-------------+
```

Let's parse the input string 'adb' using the LR(1) parser:

```
Stack         Input        Action
---------------------------------------
0             adb$         Shift s1
0A1           db$          Reduce A → d
0A3           db$          Shift s2
0A3c4         b$           Reduce A → Ac
0A3S5         b$           Shift s2
0A3Sc4        $            Reduce A → Ac
0A3S1         $            Reduce S → Aa
0S6           $            Accept
```

The parse tree for the input string 'adb' is:

```
        S
       / \
      A   a
     / \
    A   c
   / \
  d   b
``` 

#### Applications of LR parsers

- LR parsers are used in compilers to parse and interpret programming languages.
- They are used in natural language processing for parsing sentences and generating parse trees.
- They are used in data processing for parsing and validating data formats like JSON, XML, etc.