# Parallel Programming with MPL for the notes of the Unit 4 - Beowulf Cluster in the subject of High Performance Computing

- Beowulf clusters are built to address particular computational requirements by and for researchers with parallel programming experience.
- The most popular programming model for Beowulf is the message passing model.
- In the message passing model, each node in the cluster runs standard serial code (C or Fortran) which is usually called a process.
- These processes then coordinate (synchronize or exchange data) through the message passing library.
- Beowulf clusters have also been built and used by programmers with little or no parallel programming experience.
- Components for building a Beowulf cluster to run pMatlab and MatlabMPI are relatively cheap and widely available.