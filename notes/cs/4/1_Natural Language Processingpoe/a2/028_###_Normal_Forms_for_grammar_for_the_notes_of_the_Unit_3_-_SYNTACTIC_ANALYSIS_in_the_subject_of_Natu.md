 Here is the content in markdown format for the topic ### Normal Forms for grammar for the notes of the Unit 3 - SYNTACTIC ANALYSIS in the subject of Natural Language Processing:

## Normal Forms for grammar

There are mainly 3 normal forms for grammars:

1. Chomsky Normal Form (CNF):
- Every rule is of the type:
A -> BC or
A -> a
- Where A, B and C are non-terminals and a is a terminal
- Advantage: Easy to convert a grammar to CNF and further simplify proofs/constructions
- Disadvantage: May lead to an exponential increase in the number of rules

2. Greibach Normal Form (GNF):
- Every rule is of the type:
A -> aB or
A -> a
- Where A and B are non-terminals and a is a terminal
- Similar advantages/disadvantages as CNF

3. Kuroda Normal Form:
- A subset of GNF where no non-terminal appears on the right-hand side of more than one rule
- Further limits the number of rules but can be more restrictive than GNF/CNF

**Mnemonics:**
Think CNG (Chomsky Normal Form) for **C**onverting/**C**leaning up grammars
Think GNF (Greibach Normal Form) for **G**eneral use
Think KNF (Kuroda Normal Form) for most constrained/**K**ept simple grammars

**Examples:**
CNF:
S -> NP VP
NP -> Det N
VP -> V NP
N -> dog
Det -> the
V -> chased

GNF:
S -> NP VP
NP -> Det N
VP -> V NP
N -> dog
Det -> the
V -> chased

KNF (not possible for the above grammar - `NP` appears on both sides):
S -> dog

**Applications:**
- Proofs of properties like ambiguity, equivalence, etc. become easier with normalized grammars
- Conversion to normal forms enables applying various algorithms/constructs efficiently