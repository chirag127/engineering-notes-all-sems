# Binomial Distribution

- Binomial distribution is a type of **discrete probability distribution** that describes the possible outcomes of a series of **independent and identical trials** where each trial has only **two possible outcomes**: success or failure .
- Binomial distribution is used to model the number of successes in a fixed number of trials, where the probability of success is constant for each trial .
- Binomial distribution can be expressed by the following formula :

    ![P(X=x) = \binom{n}{x}p^x(1-p)^{n-x}](https://latex.codecogs.com/png.latex?P%28X%3Dx%29%20%3D%20%5Cbinom%7Bn%7D%7Bx%7Dp%5Ex%281-p%29%5E%7Bn-x%7D)

    where:

    - P(X=x) is the probability of getting x successes in n trials
    - n is the number of trials
    - x is the number of successes
    - p is the probability of success in each trial
    - 1-p is the probability of failure in each trial
    - \binom{n}{x} is the binomial coefficient, which is the number of ways to choose x successes from n trials

- Binomial distribution has the following properties :

    - The mean of the binomial distribution is np
    - The variance of the binomial distribution is np(1-p)
    - The standard deviation of the binomial distribution is \sqrt{np(1-p)}
    - The mode of the binomial distribution is \lfloor (n+1)p \rfloor or \lceil (n+1)p \rceil - 1, where \lfloor \cdot \rfloor and \lceil \cdot \rceil are the floor and ceiling functions, respectively
    - The skewness of the binomial distribution is \frac{1-2p}{\sqrt{np(1-p)}}
    - The kurtosis of the binomial distribution is \frac{1-6p(1-p)}{np(1-p)}

- Binomial distribution can be used to answer questions such as:

    - What is the probability of getting exactly 5 heads in 10 coin tosses?
    - What is the probability of getting at least 3 defective items in a batch of 20 items?
    - What is the probability of getting no more than 2 correct answers in a multiple-choice test with 10 questions and 4 options each?
    - What is the expected number of customers who will buy a product in a day if the probability of buying is 0.1 and there are 100 potential customers?