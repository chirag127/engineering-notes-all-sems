### Index Sequential Search

- Index sequential search is a searching technique that uses an index file to speed up the search process in a sorted array or database .
- An index file is a data structure that contains references to a group of records or blocks in the array or database, based on some key values .
- Each element in the index file points to a block of elements in the array or database, or another expanded index.
- The index file is searched first using a binary search or another efficient search algorithm, and then the corresponding block in the array or database is searched using a sequential search .
- The advantage of index sequential search is that it reduces the number of comparisons and accesses to the array or database, by narrowing down the search range using the index file .
- The disadvantage of index sequential search is that it requires extra space and time to create and maintain the index file, and it may become inefficient if the array or database is frequently updated .

#### Example of Index Sequential Search

- Suppose we have an array of 1000 records, sorted by name, and we want to search for a record with name "Alice".
- We can create an index file that contains 10 elements, each pointing to a block of 100 records in the array, based on the first letter of the name.
- The index file may look like this:

| Index | First Letter | Pointer |
| ----- | ------------ | ------- |
| 0     | A            | 0       |
| 1     | C            | 100     |
| 2     | E            | 200     |
| 3     | G            | 300     |
| 4     | J            | 400     |
| 5     | L            | 500     |
| 6     | N            | 600     |
| 7     | R            | 700     |
| 8     | T            | 800     |
| 9     | Z            | 900     |

- To search for "Alice", we first perform a binary search on the index file, and find that the first letter "A" matches the index 0, which points to the block 0-99 in the array.
- Then, we perform a sequential search on the block 0-99 in the array, and find the record with name "Alice" at the position 12.
- The total number of comparisons and accesses is 4 (binary search on the index file) + 13 (sequential search on the block) = 17, which is much less than 1000 (sequential search on the whole array).

#### C Program to Implement Index Sequential Search

- The following is a possible C program to implement index sequential search on an array of records, sorted by name. The program assumes that the index file is already created and stored in an array of structures.

```c
#include <stdio.h>
#include <string.h>

// Define the structure of a record
struct record {
  char name[20];
  int age;
  char gender;
};

// Define the structure of an index element
struct index {
  char first_letter;
  int pointer;
};

// Define the size of the array and the index file
#define ARRAY_SIZE 1000
#define INDEX_SIZE 10

// Declare the array of records and the index file as global variables
struct record array[ARRAY_SIZE];
struct index index_file[INDEX_SIZE];

// Function to perform index sequential search on the array of records
// Input: the name to be searched
// Output: the position of the record in the array, or -1 if not found
int index_sequential_search(char *name) {
  // Declare variables to store the first letter of the name, the index position, the block start and end, and the array position
  char first_letter;
  int index_pos, block_start, block_end, array_pos;

  // Get the first letter of the name
  first_letter = name[0];

  // Perform a binary search on the index file to find the index position
  int low, high, mid;
  low = 0;
  high = INDEX_SIZE - 1;
  while (low <= high) {
    mid = (low + high) / 2;
    if (first_letter == index_file[mid].first_letter) {
      // Found the index position
      index_pos = mid;
      break;