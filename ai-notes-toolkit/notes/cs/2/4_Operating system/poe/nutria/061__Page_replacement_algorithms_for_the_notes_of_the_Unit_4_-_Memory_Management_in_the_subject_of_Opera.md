
### Page Replacement Algorithms

Page replacement algorithms are used to manage memory in operating systems. These algorithms determine which memory pages should be replaced when new pages need to be allocated.

1. First In First Out (FIFO): In this algorithm, the page that was allocated first is replaced first when a new page needs to be allocated.
2. Least Recently Used (LRU): In this algorithm, the page that has been used least recently is replaced first when a new page needs to be allocated.
3. Optimal: In this algorithm, the page that will not be used for the longest time in the future is replaced first when a new page needs to be allocated.
4. Clock: In this algorithm, pages are kept in a circular list. A pointer (the “clock hand”) moves around the list and when a page needs to be replaced, the page at which the pointer is pointing is replaced.
5. Working Set: In this algorithm, the pages that are actively used are kept in memory and the pages that are not actively used are replaced when new pages need to be allocated.