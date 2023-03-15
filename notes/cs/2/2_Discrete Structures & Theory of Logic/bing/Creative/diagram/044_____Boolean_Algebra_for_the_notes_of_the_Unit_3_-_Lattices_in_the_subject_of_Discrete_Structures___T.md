# Boolean Algebra

- Boolean algebra is a branch of mathematics that deals with operations on logical values with binary variables  .
- The Boolean variables are represented as binary numbers to represent truths: 1 = true and 0 = false .
- The basic operations in Boolean algebra are the logical operations AND, OR and NOT .
- Boolean algebra traces its origins to an 1854 book by mathematician George Boole .
- Boolean algebra is used to simplify and analyze the logic of digital circuits, such as logic gates, flip-flops, multiplexers, etc .
- Boolean algebra can also be defined abstractly as any set with binary operations ∧ and ∨ and a unary operation ¬ thereon satisfying the Boolean laws .
- The Boolean laws are the axioms and rules of inference that govern the manipulation of Boolean expressions.
- Some of the common Boolean laws are:

| Law | Name | Expression |
| --- | --- | --- |
| Commutative | Order does not matter | x ∧ y = y ∧ x; x ∨ y = y ∨ x |
| Associative | Grouping does not matter | (x ∧ y) ∧ z = x ∧ (y ∧ z); (x ∨ y) ∨ z = x ∨ (y ∨ z) |
| Distributive | AND and OR can be distributed over each other | x ∧ (y ∨ z) = (x ∧ y) ∨ (x ∧ z); x ∨ (y ∧ z) = (x ∨ y) ∧ (x ∨ z) |
| Identity | 0 and 1 are identity elements | x ∧ 1 = x; x ∨ 0 = x |
| Complement | NOT reverses the value | x ∧ ¬x = 0; x ∨ ¬x = 1 |
| Idempotent | Repeating the same variable does not change the value | x ∧ x = x; x ∨ x = x |
| De Morgan's | NOT distributes over AND and OR with a change of operator | ¬(x ∧ y) = ¬x ∨ ¬y; ¬(x ∨ y) = ¬x ∧ ¬y |
| Absorption | A variable absorbs itself with another variable | x ∧ (x ∨ y) = x; x ∨ (x ∧ y) = x |
| Involution | Double negation cancels out | ¬(¬x) = x |