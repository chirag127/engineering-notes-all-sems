### Multivariate Probability Calculations

- Multivariate probability is the study of random variables that are jointly distributed over a sample space. It involves the calculation of probabilities of events that depend on more than one random variable. 
- Multivariate probability distributions are functions that assign probabilities to vectors of random variables. There are many types of multivariate distributions, such as multivariate normal, multivariate binomial, multivariate Poisson, etc. 
- One example of a multivariate distribution is the multinomial distribution, which is a generalization of the binomial distribution. It is used to model the outcomes of a multinomial experiment, which is an experiment that has a fixed number of trials, each with a finite number of possible outcomes, and the probability of each outcome is constant across trials. 
- The probability mass function of a multinomial distribution is given by:

$$
P(X_1 = x_1, X_2 = x_2, \dots, X_k = x_k) = \frac{n!}{x_1! x_2! \dots x_k!} p_1^{x_1} p_2^{x_2} \dots p_k^{x_k}
$$

where $n$ is the number of trials, $k$ is the number of possible outcomes, $x_i$ is the number of times outcome $i$ occurs, and $p_i$ is the probability of outcome $i$. The conditions for a multinomial distribution are:

- $n$ is fixed and known
- Each trial has $k$ possible outcomes
- The trials are independent
- The probabilities of the outcomes are constant and sum to 1

- To calculate the probability of a multivariate event using a multinomial distribution, we need to identify the values of $n$, $k$, $x_i$, and $p_i$, and plug them into the formula. For example, suppose we toss a fair die 10 times and want to find the probability of getting exactly 2 ones, 3 twos, and 5 threes. In this case, we have:

- $n = 10$
- $k = 6$
- $x_1 = 2, x_2 = 3, x_3 = 5, x_4 = x_5 = x_6 = 0$
- $p_1 = p_2 = p_3 = p_4 = p_5 = p_6 = 1/6$

- Plugging these values into the formula, we get:

$$
P(X_1 = 2, X_2 = 3, X_3 = 5) = \frac{10!}{2! 3! 5! 0! 0! 0!} \left(\frac{1}{6}\right)^{2} \left(\frac{1}{6}\right)^{3} \left(\frac{1}{6}\right)^{5} \left(\frac{1}{6}\right)^{0} \left(\frac{1}{6}\right)^{0} \left(\frac{1}{6}\right)^{0}
$$

$$
= \frac{10 \times 9 \times 8 \times 7 \times 6}{2 \times 3 \times 5 \times 6^6} = \frac{504}{6^7} \approx 0.0037
$$

- This is the probability of getting exactly 2 ones, 3 twos, and 5 threes in 10 tosses of a fair die.