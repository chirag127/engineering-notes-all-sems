#### Real-world Map Reduce

MapReduce is a programming model used to perform distributed processing in parallel in a Hadoop cluster, which makes Hadoop working so fast. When you are dealing with Big Data, serial processing is no more of any use. MapReduce has mainly two tasks which are divided phase-wise:

- Map Task
- Reduce Task

Let us understand it with a real-time example, and the example helps you understand MapReduce Programming Model in a story manner:

Suppose the Indian government has assigned you the task to count the population of India. You can demand all the resources you want, but you have to do this task in 4 months. Calculating the population of such a large country is not an easy task for a single person (you). So what will be your approach?.

One of the ways to solve this problem is to divide the country by states and assign individual in-charge to each state to count the population of that state.

Task Of Each Individual:

Each Individual has to visit every home present in the state and need to keep a record of each house members as:

| State_Name | Member_House1 | Member_House2 | Member_House3 | ... | Member_House n |
|------------|---------------|---------------|---------------|-----|----------------|
| State_A    | 5             | 4             | 6             | ... | 3              |
| State_B    | 7             | 8             | 9             | ... | 4              |
| State_C    | 6             | 5             | 4             | ... | 7              |

For Simplicity, we have taken only three states. This is a simple Divide and Conquer approach and will be followed by each individual to count people in his/her state. Once they have counted each house member in their respective state. Now they need to sum up their results and need to send it to the Head-quarter at New Delhi.

We have a trained officer at the Head-quarter to receive all the results from each state and aggregate them by each state to get the population of that entire state. and Now, with this approach, you are easily able to count the population of India by summing up the results obtained at Head-quarter.

The Indian Govt. is happy with your work and the next year they asked you to do the same job in 2 months instead of 4 months. Again you will be provided with all the resources you want.

Since the Govt. has provided you with all the resources, you will simply double the number of assigned individual in-charge for each state from one to two. For that divide each state in 2 division and assigned different in-charge for these two divisions as:

| State_Name | Incharge_division1 | Incharge_division2 |
|------------|--------------------|--------------------|
| State_A    | A1                 | A2                 |
| State_B    | B1                 | B2                 |
| State_C    | C1                 | C2                 |

Similarly, each individual in charge of its division will gather the information about members from each house and keep its record.

We can also do the same thing at the Head-quarters, so let’s also divide the Head-quarter in two division as:

| Head-qurter | Division1 | Division2 |
|-------------|-----------|-----------|
| New Delhi   | D1        | D2        |

Now with this approach, you can find the population of India in two months. But there is a small problem with this, we never want the divisions of the same state to send their result at different Head-quarters then, in that case, we have the partial population of that state in Head-quarter_Division1 and Head-quarter_Division2 which is inconsistent because we want consolidated population by the state, not the partial counting.

To solve this problem, we need to make sure that the divisions of the same state send their results to the same Head-quarter division. For example, A1 and A2 should send their results to D1, B1 and B2 should send their results to D2, and C1 and C2 should send their results to D1. This way, we can get the complete population of each state in one Head-quarter division.

This is the basic idea of MapReduce. The individuals who are counting the population of each division are the mappers, who are mapping the state name to the number of people in each house. The Head-quarter divisions who are aggregating the results from the mappers are the reducers, who are reducing the state name to the total population of that state. The process