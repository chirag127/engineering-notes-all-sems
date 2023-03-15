# Probability mass function and Probability density function

- A **probability mass function (PMF)** is a function that gives the probability that a **discrete random variable** is exactly equal to some value.
- A **probability density function (PDF)** is a function that gives the probability that a **continuous random variable** falls within some interval.
- The PMF and PDF are different ways of describing the distribution of a random variable.
- The PMF assigns a probability to each point in the sample space, while the PDF assigns a probability to each interval in the sample space.
- The PMF and PDF must satisfy the following properties:
  - They must be non-negative, i.e., f(x) ≥ 0 for all x.
  - They must sum or integrate to one, i.e., Σf(x) = 1 for PMF and ∫f(x)dx = 1 for PDF.
  - They must reflect the relative likelihood of different outcomes, i.e., f(x) > f(y) implies that x is more likely than y.
- The value of the random variable having the largest probability mass or density is called the **mode**.
- The PMF and PDF can be used to calculate various measures of central tendency and dispersion, such as mean, variance, standard deviation, etc.
- Some examples of PMF and PDF are:
  - The PMF of a fair coin toss is f(x) = 0.5 for x = H or T, and f(x) = 0 for any other x.
  - The PDF of a standard normal distribution is f(x) = (1/√(2π))e^(-x^2/2) for any x.
  - The PMF of a binomial distribution with parameters n and p is f(x) = (nCx)p^x(1-p)^(n-x) for x = 0, 1, ..., n, and f(x) = 0 for any other x.
  - The PDF of a uniform distribution on the interval [a, b] is f(x) = 1/(b-a) for a ≤ x ≤ b, and f(x) = 0 for any other x.