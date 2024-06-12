package Facade_pattern;
// Step 1 is to : Design the Interface This is the Interface that not be known to Customer class
public interface IAccount{
    public void deposit(BigDecimal amount);
    public void withdraw(BigDecimal amount);
    public void transfer(BigDecimal amount);
    public int getAccountNumber();

}

//  In this Example we are using only one Interface to hide Informationi but in Practality we wil Ecapsulate or wrap all the interfaces and class for subsystem.
// Step 2 : Implementing the Interface with one or more classes
public class Chequing implements IAccount{....} // This are the Subtypes of the main class
public class Saving implements IAccount{....}
public class Investment implements IAccount{....}

// Here is the FAcade class which wil Wrap up everything

public class BankService{
    private Hashtable<int,IAccount> bankAccounts;
    public BankService(){
        this.bankAccounts = new Hashtable<int, IAccount>;
    }

    public int createNewAccount(String type , BigDecimal initamount){
        IAccont newAccount = null;
        switch(type){
            case "chequing":
                newAccount = new Chequing(initamount);
            case "saving" :
                new    
        }
    }
}