 Here is the content in Markdown format without any emojis or external links:

### Mathematical Preliminaries for Lossless compression

1. Entropy - It is a measure of uncertainty associated with a random variable. It indicates the minimum number of bits needed to encode a symbol. For a discrete random variable X with possible values {x1, x2, ..., xn} and corresponding probabilities {p(x1), p(x2), ..., p(xn)}, the entropy is given by
H(X) = -Σp(xi)log2p(xi)

2. Conditional Entropy - Entropy of a random variable X given that another random variable Y has a particular value y. It is given by
H(X|Y=y) = -Σp(x|y)log2p(x|y)

3. Mutual Information - It measures the amount of information that X and Y share. It is given by
I(X;Y) = ΣxΣyp(x,y)log[(p(x,y)/(p(x)p(y))]

It is always non-negative and is 0 if and only if X and Y are independent. It forms the basis for lossless data compression as it represents the maximum compression achievable.

4. Kraft Inequality - It gives a necessary and sufficient condition for the existence of a unique prefix code for a given set of symbols. For a set of symbols with probabilities {p1, p2, ..., pn}, the Kraft inequality is
Σ2-lnpi ≤ 1
where ln is the binary logarithm.

The content is written in a formal tone with points and without any emojis or external links as instructed. Please let me know if you would like me to modify or expand the content in any way.