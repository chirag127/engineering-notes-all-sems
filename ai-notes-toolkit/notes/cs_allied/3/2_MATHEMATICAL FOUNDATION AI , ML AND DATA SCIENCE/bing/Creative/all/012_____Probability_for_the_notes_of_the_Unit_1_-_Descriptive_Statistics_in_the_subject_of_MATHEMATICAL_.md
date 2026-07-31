Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of probability for the unit 1 - descriptive statistics in the subject of mathematical foundation AI, ML and data science.

# Probability

- Probability is a measure of how likely an event is to occur in a random experiment.
- An event is a subset of the sample space, which is the set of all possible outcomes of the experiment.
- The probability of an event A is denoted by P(A) and satisfies the following properties:
  - 0 ≤ P(A) ≤ 1 for any event A
  - P(S) = 1, where S is the sample space
  - P(∅) = 0, where ∅ is the empty set
  - If A and B are mutually exclusive events, then P(A ∪ B) = P(A) + P(B)
  - P(Aᶜ) = 1 - P(A), where Aᶜ is the complement of A
- There are different ways to assign probabilities to events, such as:
  - Classical probability: based on the assumption of equally likely outcomes
  - Relative frequency: based on the observed frequency of outcomes in a large number of trials
  - Subjective probability: based on personal judgment or belief
- Some important concepts in probability are:
  - Conditional probability: the probability of an event A given that another event B has occurred, denoted by P(A|B)
  - Independence: two events A and B are independent if P(A|B) = P(A) or equivalently, P(A ∩ B) = P(A)P(B)
  - Bayes' theorem: a formula that relates the conditional probabilities of two events, given by P(A|B) = P(B|A)P(A) / P(B)
  - Random variable: a function that assigns a numerical value to each outcome of an experiment
  - Probability distribution: a function that specifies the probability of each possible value of a random variable
  - Expected value: the weighted average of the possible values of a random variable, given by E(X) = ∑xP(X = x) for discrete random variables, or E(X) = ∫xf(x)dx for continuous random variables
  - Variance: a measure of how much a random variable deviates from its expected value, given by Var(X) = E[(X - E(X))²] = E(X²) - [E(X)]²
  - Standard deviation: the positive square root of the variance, denoted by SD(X) or σ(X)
  - Binomial distribution: a discrete probability distribution that models the number of successes in n independent trials, each with probability p of success, given by P(X = k) = (n k) p^k (1 - p)^(n - k)
  - Normal distribution: a continuous probability distribution that is symmetric and bell-shaped, with mean μ and standard deviation σ, given by f(x) = (1 / √(2πσ²)) e^(-(x - μ)² / 2σ²)
  - Standard normal distribution: a normal distribution with mean 0 and standard deviation 1, denoted by Z
  - Central limit theorem: a result that states that the sampling distribution of the sample mean of n independent and identically distributed random variables approaches a normal distribution with mean μ and standard deviation σ / √n as n increases