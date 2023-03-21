### Inference Theory of Predicate Logic

Inference theory in predicate logic deals with the process of deriving new statements from given statements using logical rules. In this unit, we will discuss the various rules of inference that can be used to deduce new statements from existing ones in predicate logic.

#### Universal Instantiation (UI)

The universal instantiation rule allows us to infer a specific instance of a universally quantified statement. The rule states that if ∀x P(x) is true, then P(c) is true for any individual constant c. The symbol used to represent universal instantiation is:

```
∀x P(x)
--------
 P(c)
```

#### Existential Instantiation (EI)

The existential instantiation rule allows us to infer the existence of an object that satisfies an existential quantifier. The rule states that if ∃x P(x) is true, then there exists a constant c such that P(c) is true. The symbol used to represent existential instantiation is:

```
∃x P(x)
--------
 P(c)
```

#### Universal Generalization (UG)

The universal generalization rule allows us to generalize a statement from a specific instance to a universal statement. The rule states that if P(c) is true for any individual constant c, then ∀x P(x) is true. The symbol used to represent universal generalization is:

```
 P(c)
-------
∀x P(x)
```

#### Existential Generalization (EG)

The existential generalization rule allows us to infer the existence of an object that satisfies an existential quantifier. The rule states that if P(c) is true for some individual constant c, then ∃x P(x) is true. The symbol used to represent existential generalization is:

```
 P(c)
-------
∃x P(x)
```

#### Modus Ponens (MP)

The modus ponens rule allows us to infer a conclusion from a conditional statement and the affirmation of its antecedent. The rule states that if P → Q and P are true, then Q is true. The symbol used to represent modus ponens is:

```
P → Q
  P
---
  Q
```

#### Modus Tollens (MT)

The modus tollens rule allows us to infer a conclusion from a conditional statement and the negation of its consequent. The rule states that if P → Q and ¬Q are true, then ¬P is true. The symbol used to represent modus tollens is:

```
P → Q
 ¬Q
---
 ¬P
```

#### Disjunctive Syllogism (DS)

The disjunctive syllogism rule allows us to infer a conclusion from a disjunction and the negation of one of its disjuncts. The rule states that if P ∨ Q and ¬P are true, then Q is true. The symbol used to represent disjunctive syllogism is:

```
 P ∨ Q
 ¬P
-----
  Q
```

#### Constructive Dilemma (CD)

The constructive dilemma rule allows us to infer a conclusion from a conditional statement, the disjunction of its antecedent and consequent, and the affirmation of one of the disjuncts. The rule states that if P → Q and R → S and P ∨ R are true, then Q ∨ S is true. The symbol used to represent constructive dilemma is:

```
 P → Q
 R → S
 P ∨ R
-------
 Q ∨ S
```

#### Simplification (SIMP)

The simplification rule allows us to infer a conclusion from a conjunction by affirming one of its conjuncts. The rule states that if P ∧ Q is true, then P is true. The symbol used to represent simplification is:

```
P ∧ Q
------
  P
```

#### Conjunction (CONJ)

The conjunction rule allows us to infer a conjunction from two statements. The rule states that if P and Q are true, then P ∧ Q is true. The symbol used to represent conjunction is:

```
 P
 Q
---
 P ∧ Q
```

In conclusion, inference theory plays a crucial role in predicate logic as it enables us to derive new statements from existing ones using logical rules. Understanding these rules is important for constructing valid arguments and proofs in predicate logic.