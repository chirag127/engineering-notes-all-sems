# Class and Object Diagrams

## Introduction

- Class and object diagrams are two types of structural diagrams in the Unified Modeling Language (UML) that show the static structure of a system.
- Class diagrams describe the classes and interfaces that make up the system, along with their attributes, operations, and relationships.
- Object diagrams show the instances of the classes and interfaces in the system, along with their values, links, and states.
- Class and object diagrams are closely related and can be derived from each other.
- Class and object diagrams can be used for different purposes, such as analysis, design, implementation, and documentation of a system.

## Class Diagrams

- A class diagram consists of a set of classes and interfaces, along with their features and constraints, and the relationships among them.
- A class is a template that defines the common properties and behaviors of a set of objects. A class has a name, attributes, and operations.
- An attribute is a named property of a class that describes the state of an object. An attribute has a name, a type, and optionally a multiplicity and an initial value.
- An operation is a named behavior of a class that defines the actions that an object can perform. An operation has a name, a list of parameters, and optionally a return type and a visibility.
- A class can also have other features, such as constructors, destructors, stereotypes, and tagged values.
- A class can be abstract, meaning that it cannot be instantiated, or concrete, meaning that it can be instantiated. An abstract class is shown with an italic name.
- A class can be active, meaning that it has its own thread of control, or passive, meaning that it does not. An active class is shown with a thicker border.

- An interface is a specification of a set of operations that a class can implement. An interface has a name and a list of operations. An interface is shown as a circle or a rectangle with the keyword «interface».
- A class can implement one or more interfaces, meaning that it provides the definitions for the operations specified by the interfaces. An implementation relationship is shown as a dashed line with a hollow triangle pointing to the interface.
- A class can inherit from another class, meaning that it inherits the features and constraints of the superclass. An inheritance relationship is also called a generalization relationship. It is shown as a solid line with a hollow triangle pointing to the superclass.
- A class can also inherit from multiple classes, forming a multiple inheritance hierarchy. A multiple inheritance relationship is shown as a tree of generalization relationships.
- A class can be composed of other classes, forming a composition relationship. A composition relationship is a strong form of aggregation that implies ownership and exclusive responsibility. It is shown as a solid line with a filled diamond at the end of the container class.
- A class can also be aggregated by other classes, forming an aggregation relationship. An aggregation relationship is a weak form of composition that implies sharing and non-exclusive responsibility. It is shown as a solid line with an empty diamond at the end of the container class.
- A class can be associated with other classes, forming an association relationship. An association relationship is a structural link that describes how objects of different classes are related. It is shown as a solid line with optional role names, multiplicities, and navigabilities at the ends.
- A class can also be linked to itself, forming a reflexive association. A reflexive association is shown as a line that loops back to the same class.
- An association can have a name, a direction, and optionally an association class. An association class is a class that represents the properties and behaviors of an association. It is shown as a class attached to the association by a dashed line.
- An association can also be specialized into subtypes, forming a specialization relationship. A specialization relationship is also called a subtyping relationship. It is shown as a dashed line with a hollow triangle pointing to the supertype.
- An association can also be qualified by another class, forming a qualified association. A qualified association is a form of association that uses a qualifier to distinguish among multiple objects at the end of an association. A qualifier is shown as a small rectangle at the end of the association.

## Object Diagrams

- An object diagram consists of a set of objects and links, along with their values and states, and the relationships among them.
- An object is an instance of a class that has a unique identity, a state, and a behavior. An object has a name, which is underlined, and optionally a classifier, which is the name of the class that the object belongs to.
- A link is