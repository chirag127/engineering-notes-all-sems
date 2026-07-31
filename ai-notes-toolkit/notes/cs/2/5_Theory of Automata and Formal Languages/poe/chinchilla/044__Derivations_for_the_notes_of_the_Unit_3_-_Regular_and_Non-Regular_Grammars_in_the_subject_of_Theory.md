### Derivations for the notes of the Unit 3 - Regular and Non-Regular Grammars in the subject of Theory of Automata and Formal Languages

In the study of formal languages, a grammar is a set of rules for generating strings in the language. A derivation is a sequence of steps that start with the start symbol of the grammar and end with a string in the language. In this unit, we will cover the derivations for regular and non-regular grammars.

#### Derivations for Regular Grammars

Regular grammars are a type of grammar that can be expressed using regular expressions. They are useful for describing simple patterns in strings, such as email addresses or phone numbers. Here are the steps for a derivation in a regular grammar:

1. Start with the start symbol of the grammar.
2. Apply a production rule that replaces a non-terminal symbol with a string of terminal symbols or other non-terminal symbols.
3. Repeat step 2 until no non-terminal symbols remain, and the resulting string is in the language of the grammar.

For example, consider the regular grammar with start symbol S and production rules:

```
S -> aS
S -> b
```

To derive the string "abab", we can follow these steps:

1. Start with the start symbol S.
2. Apply the rule S -> aS. This gives us "aS".
3. Apply the rule S -> b. This gives us "ab".
4. Apply the rule S -> aS. This gives us "abaS".
5. Apply the rule S -> b. This gives us "abab".

#### Derivations for Non-Regular Grammars

Non-regular grammars are more complex than regular grammars and cannot be expressed using regular expressions. They are useful for describing more complicated patterns in strings, such as programming languages or natural languages. Here are the steps for a derivation in a non-regular grammar:

1. Start with the start symbol of the grammar.
2. Apply a production rule that replaces a non-terminal symbol with a string of terminal symbols or other non-terminal symbols.
3. Repeat step 2 until no non-terminal symbols remain, or a loop is detected.

In a non-regular grammar, it is possible to get stuck in a loop where the same non-terminal symbol is generated repeatedly. This is called left recursion and can cause the derivation to never terminate. To avoid this, non-regular grammars often use right recursion instead.

For example, consider the non-regular grammar with start symbol S and production rules:

```
S -> aSb
S -> SS
S -> ε
```

To derive the string "aabbb", we can follow these steps:

1. Start with the start symbol S.
2. Apply the rule S -> aSb. This gives us "aSb".
3. Apply the rule S -> aSb again. This gives us "aaSbb".
4. Apply the rule S -> ε. This gives us "aabbb".

Note that if we had used left recursion instead of right recursion, we would have gotten stuck in a loop and the derivation would never terminate.