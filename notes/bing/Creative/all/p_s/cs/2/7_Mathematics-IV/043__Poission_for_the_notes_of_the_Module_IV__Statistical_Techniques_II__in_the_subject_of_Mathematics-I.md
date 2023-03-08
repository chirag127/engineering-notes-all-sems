### Poisson Distribution

- A Poisson distribution is a discrete probability distribution that expresses the probability of a given number of events occurring in a fixed interval of time or space if these events occur with a known constant mean rate and independently of the time since the last event.
- The Poisson distribution is often used to model the number of occurrences of rare events, such as the number of phone calls received by a call center, the number of defects in a manufactured product, the number of goals scored in a soccer match, etc .
- The Poisson distribution has only one parameter, λ (lambda), which is the mean number of events per interval. The parameter λ can be any positive real number.
- The probability mass function (PMF) of the Poisson distribution is given by:

  ```
  P(X = k) = e^(-λ) * (λ^k) / k!
  ```

  where k is the number of events, e is the base of the natural logarithm, and k! is the factorial of k.
- The mean and variance of the Poisson distribution are both equal to λ . The standard deviation is the square root of λ.
- The Poisson distribution is a special case of the binomial distribution when the number of trials (n) is very large and the probability of success (p) is very small, such that np = λ .
- The Poisson distribution is also a special case of the discrete compound Poisson distribution with only a parameter.
- The Poisson distribution can be approximated by the normal distribution when λ is sufficiently large (usually λ > 30), using the continuity correction. The normal approximation is given by:

  ```
  P(X = k) ≈ P(k - 0.5 < Z < k + 0.5)
  ```

  where Z is a standard normal random variable with mean 0 and standard deviation 1.
- The Poisson distribution can be used to test the hypothesis that the observed number of events follows a Poisson distribution with a given mean rate. The test statistic is the likelihood ratio, which is given by:

  ```
  L = (λ^x) * e^(-λ) / x!
  ```

  where x is the observed number of events and λ is the expected mean rate. The p-value is the probability of observing a value of L less than or equal to the observed value, which can be calculated using the chi-square distribution with one degree of freedom.
- Some examples of applications of the Poisson distribution are:

  - The number of customers arriving at a bank in an hour follows a Poisson distribution with λ = 10. What is the probability that exactly 12 customers will arrive in an hour?

    ```
    P(X = 12) = e^(-10) * (10^12) / 12!
    P(X = 12) = 0.0948
    ```

  - The number of typos in a book follows a Poisson distribution with λ = 3. What is the probability that there are no typos in a page?

    ```
    P(X = 0) = e^(-3) * (3^0) / 0!
    P(X = 0) = 0.0498
    ```

  - The number of goals scored by a soccer team in a season follows a Poisson distribution with λ = 80. What is the probability that the team will score more than 90 goals in a season?

    ```
    P(X > 90) = 1 - P(X ≤ 90)
    P(X > 90) = 1 - [P(X = 0) + P(X = 1) + ... + P(X = 90)]
    P(X > 90) = 1 - 0.9644
    P(X > 90) = 0.0356
    ```

I'm not sure what topic you are referring to, but I can try to help you find some good mnemonics and learning tricks if you tell me more. Mnemonics and learning tricks can be very helpful for memorizing and understanding complex or unfamiliar information, as long as they are easy to remember and relevant to the topic. Do you have a specific subject or area of interest that you want to learn more about?