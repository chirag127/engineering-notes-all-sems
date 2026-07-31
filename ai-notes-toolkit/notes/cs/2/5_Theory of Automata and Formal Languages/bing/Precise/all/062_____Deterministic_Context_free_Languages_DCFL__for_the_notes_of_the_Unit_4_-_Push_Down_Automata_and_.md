# Deterministic Context free Languages(DCFL)

- Deterministic Context-Free Languages (DCFL) are a subset of Context-Free Languages (CFL).
- DCFLs are recognized by a Deterministic Pushdown Automaton (DPDA).
- A DPDA is a Pushdown Automaton (PDA) that has at most one transition for each combination of input symbol and stack symbol.
- A DPDA can be in at most one configuration for each input symbol.
- DCFLs have some properties that are different from general CFLs.
- For example, the intersection of two DCFLs is not necessarily a DCFL, while the intersection of two CFLs is always a CFL.
- DCFLs are closed under complementation, while CFLs are not.
- DCFLs are also closed under concatenation and Kleene closure.
- The emptiness problem for DCFLs is decidable, while it is undecidable for general CFLs.
- The membership problem for DCFLs can be solved in linear time, while it is NP-complete for general CFLs.
