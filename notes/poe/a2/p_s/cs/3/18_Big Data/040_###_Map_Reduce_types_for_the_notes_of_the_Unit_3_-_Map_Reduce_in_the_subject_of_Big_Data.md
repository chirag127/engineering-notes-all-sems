 Here is the content in markdown format for the topic ### Map Reduce types for the notes of the Unit 3 - Map Reduce in the subject of Big Data:

### Map Reduce types

The two main types of Map Reduce are:

1.  #### Mapper only
    -   In this type, only the Mapper phase is executed.
    -   The input data is processed by the Mapper and the output is generated.
    -   Reducer phase is not executed.
    -   This type is used when reduction is not required and aggregation can be done in the Mapper itself.
    -   Example: Finding the maximum temperature from the sensor data. Here aggregation (finding max) can be done in the Mapper itself, so Reducer is not required.

2.  #### Complete Map Reduce
    -   In this type, both Mapper and Reducer phases are executed.
    -   The input is first processed by the Mapper and the output intermediate key-value pairs are sent to the Reducer.
    -   The Reducer further processes the intermediate data and generates the final output.
    -   This is the most commonly used type and is suitable for most of the use cases.
    -   Examples: Word count, aggregation calculations, joins, etc.

Some key points to remember:

-   The input data is split into chunks and processed in parallel by the Mapper.
-   The intermediate key-value pairs from the Mapper are sorted and aggregated by the Reducer.
-   The framework takes care of the distribution and coordination between the Mappers and Reducers.
-   The number of Mappers and Reducers can be configured based on the size and type of the input data.
-   Map Reduce provides fault tolerance using replication and by maintaining backup copies of the data.

[Detailed diagrams and examples can be added here if required.]