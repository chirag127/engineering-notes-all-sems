### Private and Public Members for the Notes of the Unit 6 - Objects and Classes in the Subject of Object Oriented System Design

Below are some key points to keep in mind when considering private and public members in objects and classes:

#### Public Members
- Public members are accessible to all parts of the program.
- Public members can be accessed and modified outside the class.
- Public members are typically used to provide an interface to the outside world.

#### Private Members
- Private members are only accessible within the class itself.
- Private members cannot be accessed or modified outside the class.
- Private members are typically used to store data that should not be directly manipulated by external code.

#### Access Modifiers
- Access modifiers determine the level of accessibility of a member.
- The `public` keyword is used to make a member public.
- The `private` keyword is used to make a member private.
- There are also two other access modifiers, `protected` and `internal`, which are not covered in this topic.

#### Example Code
Here is an example of how to use private and public members in a class:

```csharp
public class Person
{
    private string name;
    public int age;

    public void SetName(string newName)
    {
        // This method can access the private member 'name'
        name = newName;
    }

    public string GetName()
    {
        // This method can also access the private member 'name'
        return name;
    }
}
```

In the above code, `name` is a private member and `age` is a public member. The `SetName` and `GetName` methods are public methods that can access the private member `name`.