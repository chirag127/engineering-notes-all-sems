Hello, I am Sydney, your AI assistant. I can help you with your study material for the Data Structure using C Lab. Here is the content for the topic of Implementation of Circular Queue using Array:

### Implementation of Circular Queue using Array

- A circular queue is a linear data structure that follows the First In First Out (FIFO) principle.
- A circular queue can be implemented using an array with a fixed size and two variables: front and rear.
- The front variable points to the first element of the queue, and the rear variable points to the last element of the queue.
- The queue is empty when front and rear are equal, and the queue is full when rear is one position behind front (modulo the array size).
- To insert an element into the queue, we check if the queue is full. If not, we increment rear (modulo the array size) and store the element at the rear position of the array.
- To delete an element from the queue, we check if the queue is empty. If not, we store the element at the front position of the array and increment front (modulo the array size).
- To display the elements of the queue, we start from the front position and traverse the array until we reach the rear position, printing the elements along the way.

Here is a diagram to illustrate the circular queue using array:

```
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|---|---|
  ^                       ^
  |                       |
front                    rear

An empty circular queue with front and rear equal to 0.

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   | 5 | 6 | 7 |   |   |
|---|---|---|---|---|---|---|---|---|---|
              ^           ^
              |           |
            front        rear

A circular queue with three elements: 5, 6, and 7. Front is at index 5 and rear is at index 7.

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| 8 | 9 |   |   |   | 5 | 6 | 7 |   |   |
|---|---|---|---|---|---|---|---|---|---|
  ^   ^           ^
  |   |           |
rear front       rear

A circular queue with five elements: 5, 6, 7, 8, and 9. Front is at index 5 and rear is at index 0.

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|
| 8 | 9 | 1 | 2 | 3 | 4 | 6 | 7 |   |   |
|---|---|---|---|---|---|---|---|---|---|
      ^   ^       ^   ^
      |   |       |   |
    rear front   rear front

A circular queue with eight elements: 1, 2, 3, 4, 6, 7, 8, and 9. Front is at index 2 and rear is at index 4. The queue is full.
```
