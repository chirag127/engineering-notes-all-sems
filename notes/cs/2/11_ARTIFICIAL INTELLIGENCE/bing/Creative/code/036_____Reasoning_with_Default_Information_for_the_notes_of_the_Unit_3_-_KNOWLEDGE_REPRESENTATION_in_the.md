# Reasoning with Default Information

- Default reasoning is a form of nonmonotonic reasoning where plausible conclusions are inferred based on general rules which may have exceptions (defaults) .
- It is nonmonotonic in the sense that additional information may force us to withdraw earlier conclusions, namely whenever the additional information shows that the case at hand is exceptional .
- For example, if we know that birds can fly (general rule), we can infer that Tweety can fly (plausible conclusion), unless we learn that Tweety is a penguin (exceptional case).
- Default reasoning is useful for representing and reasoning with incomplete or uncertain knowledge, which is common in artificial intelligence .
- Default reasoning requires two facilities, one that forces conclusions to be retracted in light of new refuting evidence and another that protects conclusions from retraction in light of new but irrelevant evidence .
- Commonsense reasoning evidently involves two types of default rules: expectation-evoking and explanation-evoking .
- Expectation-evoking rules are those that generate plausible conclusions that can be overridden by new information, such as "birds can fly".
- Explanation-evoking rules are those that provide possible explanations for observed facts that can be replaced by better explanations, such as "if the grass is wet, then it rained".
- There are various logical models of default reasoning, such as default logic, circumscription, autoepistemic logic, and nonmonotonic modal logic .
- These models differ in how they formalize the notion of default, how they handle conflicting defaults, and how they define the consequences of a set of defaults .
- Default reasoning can also be implemented in artificial intelligence programming languages, such as Prolog, by using various techniques, such as default assignments to variables, the closed world assumption, the frame default for causal worlds, exceptions as defaults, and negation .
- These techniques allow the programmer to express and manipulate default knowledge in a declarative and efficient way .