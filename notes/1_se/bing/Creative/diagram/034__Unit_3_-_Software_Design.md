There are several tools and methods to draw ASCII diagrams. One of them is Asciidoctor Diagram, which is a Ruby gem that allows you to create and embed plain-text diagrams in AsciiDoc documents. You can use different syntaxes to describe different types of diagrams, such as flowcharts, sequence diagrams, ER diagrams, etc. Asciidoctor Diagram will convert them into image files and insert them into your document.

To use Asciidoctor Diagram, you need to install the gem and the Graphviz software, which is used to render some of the diagram types. You also need to use the asciidoctor-diagram script instead of the asciidoctor command to process your document. You can find more details and examples on the Asciidoctor website.

Here is an example of how to draw a basic architecture diagram for Unit 3 - Software Design using Asciidoctor Diagram and the PlantUML syntax:

## Unit 3 - Software Design

[plantuml, unit-3-architecture, png]
----
@startuml
skinparam monochrome true
skinparam componentStyle uml2

package "User Interface" {
  [View]
  [Controller]
}

package "Business Logic" {
  [Model]
}

package "Data Access" {
  [Repository]
}

[View] ..> [Controller] : user input
[Controller] ..> [Model] : business operations
[Model] ..> [Repository] : data operations
[Repository] ..> [Database] : CRUD
[Database] - [Repository] : data
@enduml
----

The following diagram illustrates the basic architecture of Unit 3 - Software Design:

![Unit 3 Architecture](unit-3-architecture.png)