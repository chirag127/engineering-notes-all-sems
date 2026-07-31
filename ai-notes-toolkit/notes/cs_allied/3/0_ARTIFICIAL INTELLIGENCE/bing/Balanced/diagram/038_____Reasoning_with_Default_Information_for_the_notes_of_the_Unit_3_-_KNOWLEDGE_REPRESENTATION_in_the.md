### Reasoning with Default Information

- Reasoning with default information is a form of non-monotonic reasoning that allows for drawing plausible conclusions from incomplete or uncertain information, based on general rules that may have exceptions .
- Non-monotonic reasoning is a type of reasoning that does not follow the principle of monotonicity, which states that adding new information to a set of premises cannot reduce the set of conclusions that can be derived from them. In other words, non-monotonic reasoning allows for revising or retracting conclusions when new information contradicts or invalidates them .
- Reasoning with default information is useful in artificial intelligence, as it can model common sense reasoning and handle situations where the knowledge base is not complete or consistent .
- One of the most influential formalisms for reasoning with default information is default logic, proposed by Raymond Reiter in 1980 . Default logic consists of a set of facts and a set of default rules, each of which has the form:

```
p : q / r
```

- This means that if p is true, and q is consistent with the facts, then we can conclude r. However, this conclusion can be withdrawn if new information shows that r is false or inconsistent .
- For example, consider the following default rule:

```
Bird(x) : Flies(x) / Flies(x)
```

- This means that if x is a bird, and it is consistent with the facts that x flies, then we can conclude that x flies. However, this conclusion can be retracted if we learn that x is a penguin or an ostrich, which are exceptions to the general rule that birds fly .
- Default logic can handle multiple default rules and multiple possible conclusions, by generating different extensions, which are sets of consistent conclusions that can be derived from the facts and the default rules. An extension is preferred if it contains more default conclusions than another extension .
- For example, consider the following facts and default rules:

```
Facts: Bird(Tweety), Bird(Polly), Penguin(Polly)
Default rules: Bird(x) : Flies(x) / Flies(x)
               Bird(x) : ¬Flies(x) / ¬Flies(x)
```

- There are two possible extensions for this example:

```
Extension 1: {Bird(Tweety), Bird(Polly), Penguin(Polly), Flies(Tweety), ¬Flies(Polly)}
Extension 2: {Bird(Tweety), Bird(Polly), Penguin(Polly), ¬Flies(Tweety), ¬Flies(Polly)}
```

- Extension 1 is preferred, as it contains more default conclusions than extension 2. Extension 2 is not preferred, as it violates the default rule that birds fly, without any evidence to the contrary .
- Reasoning with default information is not without challenges, as it may lead to ambiguity, inconsistency, or incompleteness. For example, there may be no preferred extension, or more than one preferred extension, or no extension at all, depending on the facts and the default rules. Moreover, default logic is not decidable, meaning that there is no algorithm that can determine whether a given conclusion belongs to a preferred extension or not, in general .
- Therefore, various extensions and modifications of default logic have been proposed to address these issues, such as circumscription, autoepistemic logic, defeasible logic, and answer set programming. These are alternative formalisms for reasoning with default information that have different properties and applications in artificial intelligence.