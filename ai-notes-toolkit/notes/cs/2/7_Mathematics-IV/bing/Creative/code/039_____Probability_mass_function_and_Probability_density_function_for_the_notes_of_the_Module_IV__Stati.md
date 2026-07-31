### Probability mass function and Probability density function

- A **probability mass function (PMF)** is a function that gives the probability that a **discrete random variable** is exactly equal to some value.
- A **probability density function (PDF)** is a function that gives the probability that a **continuous random variable** falls within some interval.
- The difference between PMF and PDF is that the latter must be **integrated** over an interval to yield a probability, while the former can be directly evaluated at a point.
- The PMF and PDF can be used to describe the **distribution** of a random variable, and to calculate its **expected value**, **variance**, and other **moments**.
- The value of the random variable having the largest probability mass or density is called the **mode**.
- The PMF and PDF must satisfy the following properties:
  - They must be **non-negative**, i.e., f(x) ≥ 0 for all x.
  - They must **sum or integrate** to 1, i.e., ∑f(x) = 1 for PMF and ∫f(x)dx = 1 for PDF.
  - They must reflect the **symmetry** and **skewness** of the distribution.
- Some examples of PMF and PDF are:
  - The **binomial distribution** has a PMF given by f(x) = (nCx)p^x(1-p)^(n-x), where n is the number of trials, x is the number of successes, and p is the probability of success.
  - The **normal distribution** has a PDF given by f(x) = (1/√(2πσ^2))e^(-(x-μ)^2/(2σ^2)), where μ is the mean and σ is the standard deviation.
  - The **Poisson distribution** has a PMF given by f(x) = (λ^x e^-λ)/x!, where λ is the average rate of occurrence.
  - The **exponential distribution** has a PDF given by f(x) = λe^-λx, where λ is the rate parameter.