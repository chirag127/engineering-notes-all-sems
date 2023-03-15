# Poisson Distribution

- A Poisson distribution is a discrete probability distribution that expresses the probability of a given number of events occurring in a fixed interval of time or space if these events occur with a known constant mean rate and independently of the time since the last event.
- A Poisson distribution has only one parameter, λ (lambda), which is the mean number of events per interval.
- The probability mass function (PMF) of a Poisson distribution is given by:

$$P(X=k) = \frac{e^{-\lambda}\lambda^k}{k!}$$

where k is the number of events, e is the base of the natural logarithm, and k! is the factorial of k.

- The PMF of a Poisson distribution satisfies the following properties:

  - $P(X=k) \geq 0$ for all k
  - $\sum_{k=0}^{\infty} P(X=k) = 1$
  - $E(X) = \lambda$
  - $Var(X) = \lambda$

- A Poisson distribution can be used to model various phenomena, such as:

  - The number of customers arriving at a bank in an hour
  - The number of radioactive decays in a sample in a second
  - The number of typos in a page of a book
  - The number of goals scored in a soccer match

- A Poisson distribution can be approximated by a binomial distribution when the number of trials (n) is large and the probability of success (p) is small, such that np = λ. In this case, the PMF of a binomial distribution can be written as:

$$P(X=k) = \binom{n}{k}p^k(1-p)^{n-k} \approx \frac{e^{-\lambda}\lambda^k}{k!}$$

- A Poisson distribution can also be related to an exponential distribution, which is a continuous probability distribution that models the time between events in a Poisson process. The PMF of a Poisson distribution can be obtained by integrating the PDF of an exponential distribution over an interval of length t, such that λ = t/μ, where μ is the mean time between events. In this case, the PDF of an exponential distribution can be written as:

$$f(x) = \frac{1}{\mu}e^{-\frac{x}{\mu}}$$

and the PMF of a Poisson distribution can be written as:

$$P(X=k) = \int_{0}^{t} \frac{1}{\mu}e^{-\frac{x}{\mu}} dx = \frac{e^{-\lambda}\lambda^k}{k!}$$