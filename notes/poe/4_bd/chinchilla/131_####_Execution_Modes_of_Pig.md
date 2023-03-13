#### Execution Modes of Pig

Apache Pig is a high-level platform for creating MapReduce programs. Pig enables developers to write complex MapReduce tasks using a simple scripting language called Pig Latin. Pig supports three execution modes, which are as follows:

1. Local Mode:
   - In Local mode, Pig executes on a single machine using the local file system.
   - This mode is useful for testing and debugging small scripts.
   - To run a Pig script in local mode, the command is as follows:
     ```
     pig -x local <script_name>
     ```

2. MapReduce Mode:
   - In MapReduce mode, Pig jobs run on a Hadoop cluster.
   - Pig translates the Pig Latin script into MapReduce jobs, which are then executed on the Hadoop cluster.
   - This mode is useful for processing large datasets.
   - To run a Pig script in MapReduce mode, the command is as follows:
     ```
     pig <script_name>
     ```

3. Tez Mode:
   - In Tez mode, Pig jobs run on a Hadoop cluster using Apache Tez as the execution engine.
   - Tez is a more efficient execution engine than MapReduce, as it reduces the overhead of launching multiple MapReduce jobs for a single Pig script.
   - This mode is useful for processing large datasets with complex data flows.
   - To run a Pig script in Tez mode, the command is as follows:
     ```
     pig -x tez <script_name>
     ```

Mnemonics and learning tricks:
- Local mode is for Local testing and debugging.
- MapReduce mode is for Massive processing on a Hadoop cluster.
- Tez mode is for Efficient processing with complex data flows.