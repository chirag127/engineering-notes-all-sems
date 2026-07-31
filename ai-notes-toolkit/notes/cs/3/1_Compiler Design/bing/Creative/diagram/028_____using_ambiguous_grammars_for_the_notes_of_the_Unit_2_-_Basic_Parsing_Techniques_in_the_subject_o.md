### Using ambiguous grammars for the notes of the Unit 2 - Basic Parsing Techniques in the subject of Compiler Design

- A grammar is a set of rules that define the syntax of a language, i.e., how the symbols of the language can be combined to form valid sentences.
- A grammar is said to be **ambiguous** if there exists more than one way to derive the same sentence from the start symbol, i.e., there are multiple leftmost or rightmost derivations or parse trees for the same sentence  .
- Ambiguity is a property of grammar, not of language. A language can have both ambiguous and unambiguous grammars.
- Ambiguous grammars are undesirable for compiler design because they can lead to confusion and inconsistency in the meaning and interpretation of the source code .
- Some examples of ambiguous grammars are:

  - The grammar for arithmetic expressions with + and * operators, where the precedence and associativity of the operators are not specified. For example, the sentence `a+b*c` can have two parse trees, one where `a+b` is evaluated first and one where `b*c` is evaluated first  .
  - The grammar for `if-then-else` statements, where the else clause can be associated with either the nearest or the farthest if statement. For example, the sentence `if a then if b then s1 else s2` can have two parse trees, one where `else s2` is associated with `if b` and one where `else s2` is associated with `if a`  .
  - The grammar for dangling else problem, where the else clause can be associated with either the nearest or the farthest if statement. For example, the sentence `if a then if b then s1 else s2` can have two parse trees, one where `else s2` is associated with `if b` and one where `else s2` is associated with `if a`  .

- To resolve the ambiguity of a grammar, we can use various techniques, such as:

  - Adding precedence and associativity rules to the grammar, which specify the order and direction of evaluation of the operators. For example, we can add the rule that * has higher precedence than + and both operators are left-associative, which means that `a+b*c` is equivalent to `(a+b)*c` and `a*b+c` is equivalent to `((a*b)+c)`  .
  - Adding parentheses to the grammar, which explicitly indicate the grouping and scope of the expressions. For example, we can add the rule that parentheses can be used to enclose any expression, which means that `a+b*c` can be written as `(a+b)*c` or `a+(b*c)` depending on the intended meaning  .
  - Adding extra symbols or keywords to the grammar, which disambiguate the association of the clauses. For example, we can add the keyword `fi` to the grammar, which marks the end of an if statement, which means that `if a then if b then s1 else s2` can be written as `if a then if b then s1 else s2 fi` or `if a then if b then s1 fi else s2` depending on the intended meaning  .

- Some parsing techniques, such as LR parsers, can handle ambiguous grammars by using conflict resolution rules, such as operator precedence and associativity, to choose one of the possible derivations or parse trees for a given sentence. However, this may not always reflect the intended meaning of the source code, and may introduce errors or bugs in the compiled program .
- Therefore, it is advisable to use unambiguous grammars for compiler design, as they ensure that there is a unique and consistent way to parse and interpret the source code .