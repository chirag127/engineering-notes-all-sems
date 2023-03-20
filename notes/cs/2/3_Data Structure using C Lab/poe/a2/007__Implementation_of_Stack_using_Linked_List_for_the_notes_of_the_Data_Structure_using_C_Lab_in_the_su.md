 Here is the formal content on the given topic in markdown format without any emojis or external links:

### Implementation of Stack using Linked List

1. Stack: Stack is a linear data structure which follows a particular order in which the operations are performed. The order may be LIFO(Last In First Out) or FILO(First In Last Out).

2. Linked List: A Linked List is a linear collection of nodes where each node has a data field and a reference (link) to the next node in the list.

3. Implementation: To implement a stack using a linked list, we create a new node in the linked list for every element to be pushed into the stack. We keep a reference to the top of the stack or the head of the list.

4. Push Operation: To push an element to the stack, we simply create a new node with the data to be pushed and make the next of this new node point to the current top. We then update the top to point to the new node.

5. Pop Operation: To pop an element out of the stack, we check if the stack is empty. If not empty, we store a reference to the current top node. We then update the top to point to the next of current top. Finally, we return the data from the node we stored. This results in the removal of the top node.

6. Check if Empty: We can simply check if the top is pointing to null to confirm if the stack is empty.

7. Time Complexity: The time complexity of push and pop operations on a linked list based stack implementation is O(1) as we are simply updating references.

The content aims to be formal, informative and helpful as study material to learn the Implementation of Stack using Linked List. It is written in points along with proper headings and uses markdown format as instructed.