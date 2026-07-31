 Here is the content in markdown format without any emojis or external links, written in points and in a formal tone:

### Apriori algorithm for the notes of the Unit 5 - Frequent Itemsets and Clustering in the subject of Data Analytics

1. Apriori is an algorithm for frequent item set mining and association rule learning over transactional databases.
2. It proceeds by identifying the frequent individual items in the database and extending them to larger and larger item sets as long as those item sets appear sufficiently often in the database.
3. The frequent item sets determined by Apriori can be used to determine association rules which highlight general trends in the database: this has applications in market basket analysis.
4. The Apriori algorithm was proposed in 1994 by Rakesh Agrawal and Ramakrishnan Srikant.
5. Apriori uses a "bottom up" approach, where frequent subsets are extended one item at a time (a step known as candidate generation), and groups of candidates are tested against the data.
6. The algorithm assumes that any subset of a frequent item set must also be frequent. This is called the Apriori property.
7. Apriori uses a tree structure to count candidate item sets efficiently and prunes the search space of candidate item sets based on their frequency.
8. The steps in the basic Apriori algorithm are:
    1. Find the frequent items (initial candidates)
    2. Form candidate item sets of size k from item sets of size k-1
    3. Prune the candidates which have an infrequent sub pattern
    4. Use the remaining candidates to scan the database and obtain their support
    5. Repeat steps 2 to 4 until no more frequent item sets are found
9. Tuning parameters for Apriori include minimum support threshold and the method for generating candidate item sets.