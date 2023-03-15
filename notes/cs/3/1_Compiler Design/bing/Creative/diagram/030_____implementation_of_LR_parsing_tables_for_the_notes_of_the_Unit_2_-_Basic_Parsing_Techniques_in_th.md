### Implementation of LR Parsing Tables

LR parsing tables are a two-dimensional array in which each entry represents an action or a goto entry. LR parsing tables are used to guide the LR parser in parsing the input string and recognizing the underlying grammar. LR parsing tables consist of two parts: the action part and the goto part. The action part has columns for lookahead terminal symbols, and the goto part has columns for non-terminal symbols. The rows of the table correspond to the states of the LR parser, which are derived from the items of the grammar. An item is a production with a dot indicating how much of the right-hand side has been seen so far.

There are different types of LR parsers, such as SLR, CLR, and LALR, which differ in the way they construct the LR parsing tables and resolve conflicts. A conflict occurs when there is more than one possible action for a given state and lookahead symbol. SLR stands for Simple LR, and it is the easiest and most cost-effective to implement, but it fails to handle some classes of grammars. CLR stands for Canonical LR, and it is the most powerful and general, but it produces large and complex tables. LALR stands for Lookahead LR, and it is a compromise between SLR and CLR, which can handle more grammars than SLR, but with smaller tables than CLR.

The general algorithm for constructing LR parsing tables is as follows:

- Step 1: Augment the grammar by adding a new start symbol S' and a new production S' -> S, where S is the original start symbol.
- Step 2: Compute the canonical collection of LR(0) items for the augmented grammar, which is a set of item sets, each representing a possible state of the parser. An item set is computed by applying the closure and goto operations on the items.
- Step 3: Number each item set in the collection as a state, and construct the action and goto tables as follows:
  - For each state I and each terminal symbol a, do the following:
    - If [A -> α.aβ] is in I, set action[I, a] to shift and the state resulting from the goto operation on I and a.
    - If [A -> α.] is in I and A is not S', set action[I, a] to reduce by the production A -> α, for all a in the follow set of A.
    - If [S' -> S.] is in I, set action[I, $] to accept.
  - For each state I and each non-terminal symbol A, do the following:
    - If the goto operation on I and A results in a state J, set goto[I, A] to J.
- Step 4: If any entry in the action or goto tables is multiply defined, report a conflict and choose a resolution strategy, such as preferring shift over reduce, or using lookahead symbols to disambiguate.

Here is an example of constructing an LR parsing table for the following grammar:

S -> if E then S | if E then S else S | a

E -> b

The augmented grammar is:

S' -> S

S -> if E then S | if E then S else S | a

E -> b

The canonical collection of LR(0) items is:

I0: [S' -> .S], [S -> .if E then S], [S -> .if E then S else S], [S -> .a]

I1: [S' -> S.]

I2: [S -> if .E then S], [E -> .b]

I3: [S -> a.]

I4: [E -> b.]

I5: [S -> if E then .S], [S -> .if E then S], [S -> .if E then S else S], [S -> .a]

I6: [S -> if E then S.], [S -> if E then S .else S]

I7: [S -> if E then S else .S], [S -> .if E then S], [S -> .if E then S else S], [S -> .a]

I8: [S -> if E then S else S.]

The action and goto tables are:

| State | if | then | else | a | b | $ | S | E |
| ----- | -- | ---- | ---- | - | - | - | - | - |
| 0     | s2 |      |