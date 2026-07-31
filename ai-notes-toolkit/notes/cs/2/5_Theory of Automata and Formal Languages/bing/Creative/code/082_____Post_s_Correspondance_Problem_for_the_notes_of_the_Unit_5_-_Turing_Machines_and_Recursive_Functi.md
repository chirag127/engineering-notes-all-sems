### Post's Correspondence Problem

- The Post's Correspondence Problem (PCP) is an undecidable decision problem that was introduced by Emil Post in 1946  .
- The PCP problem over an alphabet Σ is stated as follows:
  - Given two lists, M and N, of non-empty strings over Σ, such as:
    - M = (x<sub>1</sub>, x<sub>2</sub>, x<sub>3</sub>, ..., x<sub>n</sub>)
    - N = (y<sub>1</sub>, y<sub>2</sub>, y<sub>3</sub>, ..., y<sub>n</sub>)
  - Find a sequence of indices (i<sub>1</sub>, i<sub>2</sub>, i<sub>3</sub>, ..., i<sub>k</sub>) such that:
    - x<sub>i1</sub>x<sub>i2</sub>x<sub>i3</sub>...x<sub>ik</sub> = y<sub>i1</sub>y<sub>i2</sub>y<sub>i3</sub>...y<sub>ik</sub>
  - If such a sequence exists, the PCP problem has a positive solution. Otherwise, it has a negative solution.
- The PCP problem is undecidable, meaning that there is no algorithm that can always determine whether a given instance of PCP has a positive or a negative solution   .
- The PCP problem is often used in proofs of undecidability, because it is simpler than the halting problem and the Entscheidungsproblem .
- The PCP problem can be generalized to the modified PCP (MPCP), where the first index in the sequence must be 1, and the bounded PCP (BPCP), where the length of the sequence is bounded by a constant. Both MPCP and BPCP are also undecidable.