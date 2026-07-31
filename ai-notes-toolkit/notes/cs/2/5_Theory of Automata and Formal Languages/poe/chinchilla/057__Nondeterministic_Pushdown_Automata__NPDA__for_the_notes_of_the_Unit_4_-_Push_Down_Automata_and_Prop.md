### Nondeterministic Pushdown Automata (NPDA)

In the previous section, we studied Pushdown Automata (PDA) which accepts Context-Free Languages. In this section, we will learn about Nondeterministic Pushdown Automata (NPDA), which are a variant of PDA that can accept the same class of languages as PDA.

#### Definition

A Nondeterministic Pushdown Automaton (NPDA) is a 7-tuple `(Q, Σ, Γ, δ, q₀, Z, F)` where:

- `Q` is a finite set of states.
- `Σ` is the input alphabet.
- `Γ` is the stack alphabet.
- `δ : Q × (Σ ∪ {ε}) × Γ → 2^(Q × Γ*)` is the transition function.
- `q₀ ∈ Q` is the start state.
- `Z ∈ Γ` is the initial stack symbol.
- `F ⊆ Q` is the set of accepting states.

#### Working

The working of NPDA is similar to PDA, but there are some differences. In NPDA, for each input symbol, there can be multiple transitions from a state to another state with different stack symbols. The NPDA accepts an input string if there exists at least one path from the start state to an accepting state that consumes the entire input string and empties the stack.

#### Acceptance

The NPDA accepts an input string `w` if there exists at least one path from the start state to an accepting state that consumes the entire input string and empties the stack. Formally, we say that `w` is accepted by the NPDA `(Q, Σ, Γ, δ, q₀, Z, F)` if there exists a sequence of configurations `c₀, c₁, ..., c_n` such that:

1. `c₀ = (q₀, w, Z)`.
2. For each `i` from `0` to `n-1`, `cᵢⱼ → cᵢ₊₁` according to `δ`.
3. `cₙ = (q, ε, γ)` for some `q ∈ F` and `γ ∈ Γ*`.

#### Example

Let's take an example to understand the working of NPDA. Consider the language `L = {a^n b^n | n ≥ 0}`. The NPDA for this language is:

- `Q = {q₀, q₁, q₂, q₃}`
- `Σ = {a, b}`
- `Γ = {Z, X}`
- `δ(q₀, a, Z) = {(q₁, ZX)}`
- `δ(q₁, a, X) = {(q₁, XX)}`
- `δ(q₁, b, X) = {(q₂, ε)}`
- `δ(q₂, b, X) = {(q₂, ε)}`
- `δ(q₂, ε, Z) = {(q₃, Z)}`
- `q₀` is the start state.
- `Z` is the initial stack symbol.
- `F = {q₃}`

The NPDA works as follows:

- Initially, the NPDA is in state `q₀` and has `Z` on the stack.
- For each `a` in the input string, the NPDA makes a transition from `q₀` to `q₁` and pushes `X` on the stack.
- For each `a` in the input string, the NPDA makes a transition from `q₁` to `q₁` and pushes `X` on the stack.
- For each `b` in the input string, the NPDA makes a transition from `q₁` to `q₂` and pops `X` from the stack.
- For each `b` in the input string, the NPDA makes a transition from `q₂` to `q₂` and pops `X` from the stack.
- After consuming the entire input string, the NPDA makes a transition from `q₂` to `q₃` and replaces `Z` on the stack with `Z`.

The NPDA accepts the input string `aabb` since there exists a path from `q₀` to `q₃` that consumes the input string `aabb` and empties the stack.