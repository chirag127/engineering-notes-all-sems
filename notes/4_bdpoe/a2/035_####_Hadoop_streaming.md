 Here is the content in markdown format on the topic #### Hadoop streaming:

#### Hadoop Streaming

Hadoop Streaming is a utility which allows users to create and run Map/Reduce jobs with any executable or script as the mapper and/or the reducer.

-   This allows you to use any programming language (like Python, Perl, Ruby, etc.) to write the Map and Reduce jobs. This is very useful when the required operations are not available in the Java API.
-   The streamed jobs read input from standard input (stdin) and emit output to standard output (stdout).
-   The utility runs the user-provided executable in parallel on each node of the cluster.
-   The executable should read the input from standard input (line by line) and emit the output to standard output.

Advantages:

-   Allows usage of any scripting/programming language to write Mapper and Reducer.
-   Useful when Java API does not provide the required functionality.
-   Easy to debug as standard streams are used.

Disadvantages:

-   The processing is less efficient as compared to the Java API as additional processes are spawned to run the user executable.
-   Limited access to Hadoop APIs. The jobs have to be self-contained.

Examples:

-   Word count in Python - The mapper will emit a word count for each line. The reducer will aggregate the counts for each word.
-   Grep - Emit only those lines from the input that match a certain pattern.

Applications:

-   Processing data using scripts/tools in languages other than Java.
-   Prototyping Map Reduce jobs.
-   Integrating existing scripts/tools with Hadoop.

Mnemonics/Learning tricks:

-   Think of Hadoop Streaming as a utility to run user programs/scripts on Hadoop, with inputs from stdin and outputs to stdout.
-   The utility is useful when you want to use a language other than Java to write Map Reduce jobs or integrate existing scripts/tools with Hadoop.
-   Remember the advantages of using standard streams and disadvantages of spawning additional processes.