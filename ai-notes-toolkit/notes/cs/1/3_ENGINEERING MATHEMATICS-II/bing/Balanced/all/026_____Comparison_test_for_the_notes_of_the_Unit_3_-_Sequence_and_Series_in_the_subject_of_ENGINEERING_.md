# Comparison test for the notes of the Unit 3 - Sequence and Series in the subject of ENGINEERING MATHEMATICS-II

- The comparison test is a method to test the convergence or divergence of a series by comparing it to another series whose convergence or divergence is known.
- The comparison test is based on the following principle: if a series of positive terms is smaller than a convergent series, then it also converges; if a series of positive terms is larger than a divergent series, then it also diverges.
- The comparison test can be applied to a series ∑∞n=1an if the terms an are positive and a suitable series ∑∞n=1bn can be found such that an≤bn or an≥bn for all n.
- The comparison test can be stated as follows:

  - If 0≤an≤bn for all n and ∑∞n=1bn converges, then ∑∞n=1an also converges.
  - If 0≤bn≤an for all n and ∑∞n=1bn diverges, then ∑∞n=1an also diverges.

- The comparison test is useful when the series ∑∞n=1an has a similar form to a known series, such as a geometric series or a p-series, which can be used as ∑∞n=1bn.
- The comparison test can be illustrated by the following examples:

  - Example 1: Test the convergence of the series ∑∞n=1(1+1/n)^(n^2)/n!.
    - Solution: We can compare this series to the series ∑∞n=1e^n/n!, where e is the base of the natural logarithm. We know that the latter series converges by the ratio test. To use the comparison test, we need to show that 0≤(1+1/n)^(n^2)/n!≤e^n/n! for all n. This is equivalent to showing that 0≤(1+1/n)^n≤e for all n, which is true by the definition of e as the limit of (1+1/n)^n as n approaches infinity. Therefore, by the comparison test, the series ∑∞n=1(1+1/n)^(n^2)/n! converges.
  - Example 2: Test the convergence of the series ∑∞n=1(1/n)^(1+1/n).
    - Solution: We can compare this series to the series ∑∞n=11/n, which is a harmonic series and diverges. To use the comparison test, we need to show that 0≤1/n≤(1/n)^(1+1/n) for all n. This is equivalent to showing that 0≤n≤n^(1+1/n) for all n, which is true by the property of exponential functions. Therefore, by the comparison test, the series ∑∞n=1(1/n)^(1+1/n) diverges.