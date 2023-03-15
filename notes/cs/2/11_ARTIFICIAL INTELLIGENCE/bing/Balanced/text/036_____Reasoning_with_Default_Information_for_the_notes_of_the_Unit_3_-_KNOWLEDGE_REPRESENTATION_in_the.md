### Reasoning with Default Information

- Default information is the information that is usually true, but not always true, in a given domain.
- For example, birds can fly, but penguins and ostriches cannot. This is a default rule that has exceptions.
- Reasoning with default information is the process of drawing conclusions based on default rules, while being able to retract or revise them when new information contradicts them.
- Reasoning with default information is useful for dealing with incomplete or uncertain knowledge, which is common in many real-world domains.
- There are different formalisms for representing and reasoning with default information, such as default logic, nonmonotonic logic, circumscription, and logic programming.
- Default logic is a formalism that uses default rules of the form: p : q / r, which means that if p is true and q is consistent, then infer r, unless there is evidence to the contrary.
- Nonmonotonic logic is a general term for any logic that allows the inference of new information to invalidate previous conclusions, unlike classical logic which is monotonic (i.e., adding new information can only increase the set of conclusions).
- Circumscription is a formalism that minimizes the extension of certain predicates, based on the assumption that what is not known to be true is false. For example, by circumscribing the predicate Abnormal, we can infer that birds can fly, unless they are abnormal.
- Logic programming is a formalism that uses rules of the form: p :- q1, q2, ..., qn, which means that p is true if q1, q2, ..., qn are true. Logic programming can be extended to handle default information by using negation as failure, which means that not p is true if p cannot be proven to be true.