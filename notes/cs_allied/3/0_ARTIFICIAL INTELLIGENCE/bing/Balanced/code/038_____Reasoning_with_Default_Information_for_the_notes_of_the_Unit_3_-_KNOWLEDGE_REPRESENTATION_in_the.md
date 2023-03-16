# Reasoning with Default Information

- Reasoning with default information is a form of non-monotonic reasoning that allows for drawing plausible conclusions from incomplete or uncertain information, based on general rules that may have exceptions .
- Non-monotonic reasoning is a type of reasoning that does not follow the principle of monotonicity, which states that adding new information to a set of premises cannot reduce the set of conclusions that can be derived from them. In other words, non-monotonic reasoning allows for revising or retracting conclusions when new information contradicts or invalidates them .
- Reasoning with default information is useful in artificial intelligence because it can model common sense reasoning and deal with situations where the knowledge base is not complete or consistent .
- One of the main approaches to reasoning with default information is default logic, which was proposed by Raymond Reiter in 1980 . Default logic is based on the idea of assuming the truth of something unless there is evidence to the contrary. For example, if we know that birds can fly, we can assume that Tweety can fly, unless we have evidence that Tweety is a penguin or has a broken wing.
- A default logic consists of two components: a set of facts (or a first-order theory) and a set of default rules. A default rule has the form:

```
p : q / r
```

where p is the prerequisite, q is the justification, and r is the consequent. This rule means that if p is true and q is consistent with the facts, then we can conclude r. For example, the rule:

```
Bird(x) : Fly(x) / Fly(x)
```

means that if x is a bird and flying is consistent with the facts, then we can conclude that x can fly.

- A default theory can have multiple extensions, which are sets of conclusions that can be derived from the facts and the default rules. An extension is a maximal consistent set of formulas that contains the facts and is closed under the application of the default rules. For example, if we have the facts:

```
Bird(Tweety)
Bird(Polly)
Penguin(Polly)
```

and the default rules:

```
Bird(x) : Fly(x) / Fly(x)
Penguin(x) : ¬Fly(x) / ¬Fly(x)
```

then we have two extensions: one that contains `Fly(Tweety)` and `¬Fly(Polly)`, and another that contains `¬Fly(Tweety)` and `¬Fly(Polly)`. The first extension is more intuitive and preferred, but the second extension is also possible and consistent.

- Default logic is not the only way to reason with default information. There are other methods, such as circumscription, autoepistemic logic, and preferential logic, that have different advantages and disadvantages. However, default logic is one of the most influential and widely studied forms of non-monotonic reasoning in artificial intelligence  .