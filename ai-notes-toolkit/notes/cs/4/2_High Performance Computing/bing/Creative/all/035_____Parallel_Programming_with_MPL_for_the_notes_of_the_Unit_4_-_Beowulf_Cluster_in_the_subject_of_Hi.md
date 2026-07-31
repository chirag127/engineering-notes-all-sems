# Parallel Programming with MPL

MPL is a compiler for parallel programming on shared-memory multicore machines. The MPL language is essentially Standard ML (SML) with extensions for parallelism. MPL generates executables with excellent multicore performance, utilizing a novel approach to memory management based on the theory of disentanglement    .

## Features of MPL

- MPL supports nested (fork-join) parallelism, which allows the programmer to express parallel computations as a tree of tasks that can be executed concurrently by different cores.
- MPL provides a parallel version of the SML library, which includes parallel data structures, parallel algorithms, and parallel I/O operations.
- MPL implements a space-efficient garbage collector that avoids copying or moving data between cores, and ensures that each core only accesses its own local memory regions.
- MPL uses a type-and-effect system to statically check the parallelism and locality properties of the program, and to optimize the code generation and runtime system accordingly.
- MPL supports interoperability with C, allowing the programmer to call C functions from MPL and vice versa.

## Example of MPL

The following code snippet shows a parallel implementation of the quicksort algorithm in MPL:

```sml
fun quicksort [] = []
  | quicksort (x::xs) =
    let
      val (lesser, greater) = List.partition (fn y => y < x) xs
      val (sorted_lesser, sorted_greater) =
        par (quicksort lesser, quicksort greater)
    in
      sorted_lesser @ [x] @ sorted_greater
    end
```

The `par` construct creates two parallel tasks, one for sorting the `lesser` list and one for sorting the `greater` list, and waits for both tasks to finish before concatenating the results. The `List.partition` function is also parallelized by MPL, using a divide-and-conquer strategy.

## References

: Disentanglement: A New Approach to Space-Efficient Parallel Functional Programming. Umut A. Acar, Arthur Charguéraud, Mike Rainey, and Filip Sieczkowski. In Proceedings of the 2020 ACM SIGPLAN International Conference on Functional Programming (ICFP 2020), pages 1–29, 2020.

: Disentanglement: A New Approach to Space-Efficient Parallel Functional Programming (Extended Version). Umut A. Acar, Arthur Charguéraud, Mike Rainey, and Filip Sieczkowski. Technical Report, 2020.

: Disentanglement: A New Approach to Space-Efficient Parallel Functional Programming (Slides). Umut A. Acar, Arthur Charguéraud, Mike Rainey, and Filip Sieczkowski. Presented at ICFP 2020, 2020.

: Disentanglement: A New Approach to Space-Efficient Parallel Functional Programming (Video). Umut A. Acar, Arthur Charguéraud, Mike Rainey, and Filip Sieczkowski. Presented at ICFP 2020, 2020.

: Disentanglement: A New Approach to Space-Efficient Parallel Functional Programming (Website). Umut A. Acar, Arthur Charguéraud, Mike Rainey, and Filip Sieczkowski. https://mpl.cis.upenn.edu/, 2020.