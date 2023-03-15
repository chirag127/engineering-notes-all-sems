### Probability mass function and Probability density function

- A **probability mass function (PMF)** is a function that gives the probability that a **discrete random variable** is exactly equal to some value.
- A **probability density function (PDF)** is a function that gives the probability that a **continuous random variable** falls within some interval.
- A PMF differs from a PDF in that the latter must be **integrated** over an interval to yield a probability, while the former can be evaluated at a single point.
- The **mode** of a random variable is the value that has the largest probability mass or density.
- The PMF and PDF must satisfy the following properties:
  - They are **non-negative**, i.e., f(x) ≥ 0 for all x.
  - They **sum or integrate** to 1, i.e., ∑f(x) = 1 for PMF and ∫f(x)dx = 1 for PDF, where the summation or integration is over the **support** of the random variable, which is the set of possible values it can take.
  - They give the probability of an **event** by summing or integrating over the values in the event, i.e., P(A) = ∑f(x) for PMF and P(A) = ∫f(x)dx for PDF, where A is a subset of the support.
- Examples of PMFs are the **binomial**, **Poisson**, and **geometric** distributions, which are used to model discrete phenomena such as coin tosses, counts of rare events, and waiting times, respectively.
- Examples of PDFs are the **normal**, **exponential**, and **uniform** distributions, which are used to model continuous phenomena such as heights, lifetimes, and random numbers, respectively.