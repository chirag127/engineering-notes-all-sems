### Poisson Distribution

- A Poisson distribution is a discrete probability distribution that models the number of events occurring in a fixed interval of time or space, given that the events are independent and rare  .
- The Poisson distribution is defined by a single parameter, lambda (λ), which is the mean number of occurrences during an observation unit . A rate of occurrence is simply the mean count per standard observation period. For example, a call center might receive an average of 32 calls per hour.
- The probability mass function of the Poisson distribution is given by  :

$$P(X=k) = \frac{e^{-\lambda}\lambda^k}{k!}$$

where $X$ is the random variable, $k$ is the number of events, $e$ is the base of the natural logarithm, and $!$ is the factorial function.
- The Poisson distribution has the following properties  :
  - The mean and the variance of the Poisson distribution are both equal to $\lambda$.
  - The Poisson distribution is skewed to the right when $\lambda$ is small, and becomes more symmetric as $\lambda$ increases.
  - The Poisson distribution approaches the normal distribution as $\lambda$ becomes large, with the approximation given by:

  $$X \sim N(\lambda, \lambda)$$

- The Poisson distribution is useful for characterizing events with very low probabilities of occurrence within some definite time or space. Some examples of applications of the Poisson distribution are   :
  - The number of radioactive decays per second from a source.
  - The number of customers arriving at a bank in an hour.
  - The number of typos in a book.
  - The number of goals scored by a soccer team in a match.
  - The number of cars passing through a toll booth in a day.