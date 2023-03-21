

### Baye’s Theorem

Baye’s theorem is an important concept in probability theory. This theorem is used to find out the probability of an event happening, given that another event has already happened. Baye’s theorem is named after Thomas Bayes, who first described it in the 18th century.

#### Formula

The formula for Baye’s theorem is:

P(A|B) = P(B|A)*P(A) / P(B)

where:

- P(A|B) is the probability of event A happening, given that event B has happened.
- P(B|A) is the probability of event B happening, given that event A has happened.
- P(A) is the probability of event A happening.
- P(B) is the probability of event B happening.

#### Steps to use Baye’s Theorem

To use Baye’s theorem, follow these steps:

1. Identify the events A and B.
2. Find the probability of event A happening, P(A).
3. Find the probability of event B happening, P(B).
4. Find the probability of event B happening, given that event A has happened, P(B|A).
5. Use Baye’s theorem formula to find the probability of event A happening, given that event B has happened, P(A|B).

#### Example

Suppose a doctor has a patient who has a cough. The doctor suspects that the patient has either a cold or lung cancer. The doctor knows that the probability of a person having a cold is 60%, and the probability of a person having lung cancer is 40%. The doctor also knows that the probability of a person with a cold having a cough is 30%, and the probability of a person with lung cancer having a cough is 90%.

Using Baye’s theorem, the doctor can find the probability of the patient having lung cancer, given that the patient has a cough.

1. Identify the events A and B. 
   - Event A: The patient has lung cancer.
   - Event B: The patient has a cough.

2. Find the probability of event A happening, P(A). 
   - P(A) = 0.4 (given in the problem).

3. Find the probability of event B happening, P(B). 
   - P(B) = P(cough|cold)*P(cold) + P(cough|cancer)*P(cancer)
   - P(B) = 0.3*0.6 + 0.9*0.4
   - P(B) = 0.54 + 0.36
   - P(B) = 0.9

4. Find the probability of event B happening, given that event A has happened, P(B|A).
   - P(B|A) = P(cough|cancer)
   - P(B|A) = 0.9 (given in the problem)

5. Use Baye’s theorem formula to find the probability of event A happening, given that event B has happened, P(A|B).
   - P(A|B) = P(B|A)*P(A) / P(B)
   - P(A|B) = 0.9*0.4 / 0.9
   - P(A|B) = 0.4

Therefore, the probability of the patient having lung cancer, given that the patient has a cough, is 0.4 or 40%.