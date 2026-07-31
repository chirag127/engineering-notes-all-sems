### Probability mass function and Probability density function

- A **probability mass function (PMF)** is a function that gives the probability that a **discrete random variable** is exactly equal to some value.
- A **probability density function (PDF)** is a function that gives the probability that a **continuous random variable** falls within some interval.
- A PMF differs from a PDF in that the latter must be **integrated** over an interval to yield a probability, while the former can be evaluated at a single point.
- The value of the random variable having the largest probability mass or density is called the **mode**.
- The **shape** of the graph of a PMF is usually a **histogram**, while the shape of the graph of a PDF is usually a **bell curve**.
- The **properties** of a PMF are:
  - It is **non-negative**, i.e., f(x) ≥ 0 for all x in the sample space.
  - It **sums up to one**, i.e., ∑f(x) = 1 for all x in the sample space.
  - It gives the **probability** of each possible outcome, i.e., P(X = x) = f(x) for all x in the sample space.
- The **properties** of a PDF are:
  - It is **non-negative**, i.e., f(x) ≥ 0 for all x in the sample space.
  - It **integrates to one**, i.e., ∫f(x)dx = 1 for all x in the sample space.
  - It gives the **probability density** of each possible outcome, i.e., P(a ≤ X ≤ b) = ∫f(x)dx for any interval [a, b] in the sample space.
- An **example** of a PMF is the **binomial distribution**, which gives the probability of getting k successes in n independent trials, each with probability p of success.
- An **example** of a PDF is the **normal distribution**, which gives the probability density of a random variable that is symmetrically distributed around a mean μ and has a standard deviation σ.
- A **graph** of a PMF and a PDF is shown below:

```markdown
![PMF and PDF](pmf_pdf.png)
```