### Implementation of Queue using Array

- A queue is a linear data structure that follows the First In First Out (FIFO) principle, meaning that the element that is inserted first is removed first.
- A queue can be implemented using an array by maintaining two variables: front and rear, that point to the first and last element of the queue respectively.
- To insert an element into the queue, we check if the queue is full by comparing the rear index with the size of the array. If the queue is full, we display an overflow message and return. Otherwise, we increment the rear index by one and store the element at the rear position of the array.
- To delete an element from the queue, we check if the queue is empty by comparing the front and rear indices. If the queue is empty, we display an underflow message and return. Otherwise, we store the element at the front position of the array in a variable, increment the front index by one, and return the variable.
- To display the elements of the queue, we use a loop to traverse the array from the front index to the rear index and print the elements.