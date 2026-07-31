### Sorting and Merging: Selection Sort, Merge List, Merge Sort, Higher Order Sort

- Sorting is the process of arranging data in a specific order, such as ascending or descending, based on some criteria.
- Merging is the process of combining two or more sorted lists into one sorted list.
- There are different algorithms for sorting and merging data, each with different advantages and disadvantages.

#### Selection Sort

- Selection sort is a simple sorting algorithm that works by repeatedly finding the minimum or maximum element in the unsorted part of the list and moving it to the sorted part.
- The algorithm maintains two sublists: one that is already sorted and one that is unsorted.
- The algorithm iterates over the unsorted sublist, finds the smallest or largest element, and swaps it with the first element of the unsorted sublist.
- The algorithm repeats this process until the unsorted sublist is empty and the sorted sublist contains all the elements.
- The time complexity of selection sort is O(n^2), where n is the number of elements in the list, because it has to compare each element with all the other elements in the unsorted sublist.
- The space complexity of selection sort is O(1), because it only requires a constant amount of extra space to store the index of the minimum or maximum element.
- Selection sort is not stable, meaning that it does not preserve the relative order of equal elements in the list.
- Selection sort is not adaptive, meaning that it does not take advantage of the existing order in the list.

#### Merge List

- Merge list is a function that takes two sorted lists as input and returns a new sorted list that contains all the elements from both lists.
- The function works by comparing the first elements of the two lists and appending the smaller one to the output list, then advancing the pointer of the list that contained the smaller element.
- The function repeats this process until one of the lists is exhausted, then appends the remaining elements of the other list to the output list.
- The time complexity of merge list is O(m + n), where m and n are the lengths of the two lists, because it has to iterate over both lists once.
- The space complexity of merge list is O(m + n), because it has to create a new list that contains all the elements from both lists.
- Merge list is stable, meaning that it preserves the relative order of equal elements in the lists.
- Merge list is adaptive, meaning that it takes advantage of the existing order in the lists.

#### Merge Sort

- Merge sort is a recursive sorting algorithm that works by dividing the list into two halves, sorting each half recursively, and then merging the two sorted halves using the merge list function.
- The algorithm follows the divide and conquer approach, where a complex problem is broken down into smaller and simpler subproblems, and then the solutions of the subproblems are combined to form the solution of the original problem.
- The algorithm uses a helper function called merge sort helper that takes the list, a start index, and an end index as parameters, and sorts the sublist between the start and end indices.
- The algorithm calls the merge sort helper function on the whole list, passing 0 and the length of the list minus one as the start and end indices.
- The merge sort helper function checks if the start index is less than the end index, meaning that the sublist has more than one element, and if so, it calculates the middle index by adding the start and end indices and dividing by two.
- The merge sort helper function then calls itself recursively on the left half of the sublist, passing the start and middle indices as the new start and end indices, and on the right half of the sublist, passing the middle plus one and end indices as the new start and end indices.
- The merge sort helper function then calls the merge list function on the two sorted halves of the sublist, and returns the merged list as the output.
- The time complexity of merge sort is O(n log n), where n is the number of elements in the list, because it divides the list into two halves at each level of recursion, and merges the two halves in linear time at each level of recursion.
- The space complexity of merge sort is O(n), because it requires extra space to store the temporary lists created by the merge list function at each level of recursion.
- Merge sort is stable, meaning that it preserves the relative order of equal elements in the list.
- Merge sort is not adaptive, meaning that it does not take advantage of the existing order in the list.

#### Higher Order Sort

- Higher order sort is a term that refers to sorting algorithms that can take