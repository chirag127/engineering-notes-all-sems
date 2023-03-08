### Binomial Distribution

- A binomial distribution is a type of probability distribution that models the number of successes or failures in a repeated trial or experiment with two possible outcomes    .
- The two possible outcomes are usually called success and failure, and are denoted by 1 and 0 respectively .
- The binomial distribution is a discrete distribution, meaning that it can only take integer values from 0 to n, where n is the number of trials  .
- The binomial distribution is characterized by two parameters: n and p, where n is the number of trials and p is the probability of success in each trial    .
- The probability mass function (PMF) of a binomial distribution is given by:

    `P(X = x) = nCx * p^x * (1 - p)^(n - x)`

    where x is the number of successes, nCx is the binomial coefficient, and p is the probability of success    .

- The mean and variance of a binomial distribution are given by:

    `E(X) = np`

    `Var(X) = np(1 - p)`

    where n is the number of trials and p is the probability of success    .

- Some properties of a binomial distribution are:

    - The PMF is symmetric when p = 0.5, and skewed to the right when p < 0.5, and skewed to the left when p > 0.5  .
    - The mode (most likely value) of a binomial distribution is given by:

        `Mode = floor((n + 1)p)`

        where n is the number of trials and p is the probability of success .

    - The binomial distribution can be approximated by a normal distribution when n is large and p is not too close to 0 or 1, using the following formula:

        `Z = (X - np) / sqrt(np(1 - p))`

        where X is a binomial random variable, n is the number of trials, p is the probability of success, and Z is a standard normal random variable  .

- Some examples of binomial distribution are:

    - The number of heads in 10 tosses of a fair coin  .
    - The number of defective items in a batch of 100 products  .
    - The number of correct answers in a multiple-choice test with 20 questions and 4 options each  .
    - The number of voters who prefer candidate A in a sample of 500 voters  .

Some possible mnemonics and learning tricks for the binomial distribution are:

- To remember the formula for the PMF, use the acronym BInoMial: B for binomial coefficient, I for index of success, M for power of success probability, and AL for power of failure probability.
- To remember the formula for the mean and variance, use the acronym MEan VAriance: ME for mean, VA for variance, and RI for product of trials and success probability.
- To remember the conditions for using the normal approximation, use the acronym NPQ: N for number of trials, P for success probability, and Q for failure probability. The conditions are: N > 30, NP > 5, and NQ > 5.