 Here are the notes for the topic **Sorting and Order Statistics - Heap Sort** for the unit **Introduction: Algorithms, Analyzing Algorithms, Complexity of Algorithms, Growth of Functions, Performance Measurements, Sorting and Order Statistics - Shell Sort, Quick Sort, Merge Sort, Heap Sort, Comparison of Sorting Algorithms, Sorting in Linear Time** in the subject of **Design and Analysis of Algorithms**:

### Heap Sort

- Heap sort is a comparison based sorting technique based on Binary Heap data structure.
- In heap sort, we first build a max heap (or min heap) from the input data. A max heap is a complete binary tree where the root element is the maximum among all elements in the tree.
- Then, we replace the root element with the last element of the heap followed by sinking down the new root to restore the heap property.
- This is repeated until the heap size reduces to 1.
- The key steps are:

1. Build a max heap from the input data.
2. Replace the root element with the last element of the heap.
3. Sink down the new root to restore the heap property.
4. Repeat steps #2 and #3 until the heap size reduces to 1.

- The time complexity of heap sort is **O(n log n)** as the build heap operation takes O(n) time and we need to do it only once. The rest of the steps take O(log n) time.
- Heap sort is an in-place sorting algorithm as it requires a constant amount of additional storage.
- Heap sort is not a stable sort as the relative order of elements with equal keys is not preserved.
- The advantage of heap sort is that it has an excellent locality of reference which makes it useful for external sorting.

**Diagram:**

[A diagram showing the steps of heap sort with max heap]

**Code:**

[A code snippet showing the implementation of heap sort]