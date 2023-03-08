 Here is the content in markdown format for the topic ### built-in control structures for the notes of the Unit 10 - SCALA in the subject of Big Data:

### Built-in Control Structures

#### 1. If-else
- If-else is used to execute code based on a certain condition.
- Syntax:
if (condition) {
  // code to execute if condition is true
} else {
  // code to execute if condition is false
}
- Example:
if (x > 0) {
  println("Positive number")
} else {
  println("Non-positive number")
}

#### 2. Match
- Match is used to match a value against a series of patterns and execute code based on the first matched pattern.
- Syntax:
match value {
  case pattern1 => code1
  case pattern2 => code2
  case _ => default code  // used if no pattern matches
}
- Example:
match status {
  case "Ready" => println("Proceed with the action")
  case "In Progress" => println("Please wait...")
  case _ => println("Invalid status")
}

#### 3. For
- For loop is used to iterate over a range of values or a collection.
- Syntax:
for (element <- collection) {
  // code to execute for each element
}
- Example:
for (i <- 1 to 5) {  // iterates from 1 to 5
  println(i)
}

for (word <- wordsList) {  // iterates over a list of words
  println(word)
}

[Detailed explanations, codes, diagrams, advantages, disadvantages, applications, etc can be added here for the points as required.]