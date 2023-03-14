Code inspection is a type of static testing that reviews the software code and examines it for any errors. It helps in reducing the ratio of defect multiplication and avoids later-stage error detection by simplifying all the initial error detection processes . Code inspection can improve the quality, reliability and efficiency of the software product .

The following diagram illustrates the basic architecture of a code inspection process using ASCII characters:

```
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|    Author      |----->|    Reviewer    |----->|    Moderator   |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
      |                       |                       |
      |                       |                       |
      |                       |                       |
      v                       v                       v
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|   Prepare      |----->|   Inspect      |----->|   Report       |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
```

The code inspection process consists of the following steps:

1. Prepare: The author of the code prepares the code for inspection and selects the reviewer and the moderator.
2. Inspect: The reviewer inspects the code for any defects and provides feedback to the author.
3. Report: The moderator reports the results of the inspection and tracks the resolution of the defects.