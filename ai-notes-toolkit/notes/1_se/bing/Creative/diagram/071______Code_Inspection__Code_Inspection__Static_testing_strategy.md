Code inspection is a type of static testing which aims in reviewing the software code and examining for any errors in that. It helps in reducing the ratio of defect multiplication and avoids later-stage error detection by simplifying all the initial error detection processes. Static testing is performed to check the defects in software without actually executing the code of the software application. Static testing can be done manually or using automated tools.

A possible diagram for code inspection static testing strategy is:

#### Code Inspection Static Testing Strategy

```
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|  Code Author   |----->|  Code Reviewer |----->|  Code Inspector|
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      |                       |                       |
      v                       v                       v
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|  Code Writing  |      |  Code Checking |      |  Code Fixing   |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
```

The code author writes the code and submits it to the code reviewer. The code reviewer checks the code for any errors, such as syntax, logic, style, or performance issues. The code reviewer then sends the code to the code inspector, who performs a more thorough and formal analysis of the code, using tools or standards. The code inspector identifies any defects or violations in the code and reports them back to the code author. The code author then fixes the code and resubmits it for another round of inspection, until the code is free of errors and meets the quality criteria.