### Sorting and Order Statistics - Shell Sort

- Shell sort is a generalization of insertion sort that allows the exchange of items that are far apart.
- The idea is to arrange the list of elements so that, starting anywhere, considering every hth element gives a sorted list.
- Such a list is said to be h-sorted. It can also be thought of as h interleaved lists, each individually sorted.
- By performing insertion sort on each of the h sublists, the total number of exchanges required by insertion sort can be reduced.
- The final step of shell sort is a plain insertion sort, but by then, the list of elements is guaranteed to be almost sorted.
- The running time of shell sort depends on the choice of the increment sequence, which is a series of values for h that ends in 1.
- One common choice is h_k = 2^k, for k = floor(log_2 n), k-1, ..., 1, 0. This gives a worst-case running time of O(n^(3/2)).
- Another common choice is h_k = 3^k - 1 / 2, for k such that h_k < n / 3. This gives a worst-case running time of O(n^(3/2)) as well, but performs better in practice.
- The best known worst-case running time for shell sort with a specific increment sequence is O(n log^2 n), but the best increment sequence is not known.