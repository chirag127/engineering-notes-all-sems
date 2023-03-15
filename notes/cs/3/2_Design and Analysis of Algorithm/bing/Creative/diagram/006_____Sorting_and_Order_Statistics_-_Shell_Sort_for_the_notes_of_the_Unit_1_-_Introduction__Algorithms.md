# Sorting and Order Statistics - Shell Sort

- Shell sort is a highly efficient sorting algorithm that is based on the insertion sort algorithm    .
- Shell sort avoids large shifts of elements, as in insertion sort, where the smaller value is on the far right and must be moved to the far left .
- Shell sort works by sorting elements that are far apart from each other and successively reducing the interval between the elements to be sorted .
- The interval between the elements is reduced based on the sequence used. The sequence can be different for different implementations of shell sort  .
- Shell sort is an in-place comparison sort, which means it does not require extra space to store the sorted elements.
- Shell sort is not a stable sort, which means it does not preserve the relative order of equal elements.
- Shell sort has an average time complexity of O(n^1.5^), where n is the number of elements to be sorted.
- Shell sort is suitable for sorting medium-sized arrays that are not too large or too small .