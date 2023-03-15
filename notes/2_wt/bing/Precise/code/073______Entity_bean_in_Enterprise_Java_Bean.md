#### Entity bean in Enterprise Java Bean

An entity bean represents a business object in a persistent storage mechanism. Here is an example of an entity bean that represents a bank account:

```java
import javax.persistence.*;

@Entity
public class BankAccount {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Long id;
    private String accountNumber;
    private double balance;

    public BankAccount() {}

    public BankAccount(String accountNumber, double balance) {
        this.accountNumber = accountNumber;
        this.balance = balance;
    }

    public Long getId() {
        return id;
    }

    public String getAccountNumber() {
        return accountNumber;
    }

    public void setAccountNumber(String accountNumber) {
        this.accountNumber = accountNumber;
    }

    public double getBalance() {
        return balance;
    }

    public void setBalance(double balance) {
        this.balance = balance;
    }
}
```
This entity bean uses annotations to specify the mapping between the class and the database table. The `@Entity` annotation specifies that this class is an entity bean. The `@Id` and `@GeneratedValue` annotations specify that the `id` field is the primary key and that its value is automatically generated. The other fields represent the columns in the database table. The getters and setters provide access to the entity's state.
