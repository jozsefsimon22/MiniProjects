public class Customer {

    // Attributes of the class
    String name;
    String telephoneNumber;
    String emailAddress;
    String address;

    // Constructors
    public Customer(String name, String telephoneNumber, String emailAddress, String address) {
        this.name = name;
        this.telephoneNumber = telephoneNumber;
        this.emailAddress = emailAddress;
        this.address = address;
    }

    // This method is called with a string value and updates the telephone number of
    // the customer object
    public void newTelephoneNumber(String telephoneNumber) {
        this.telephoneNumber = telephoneNumber;
    }

    // This method is called with a string value and updates the email address of
    // the customer object
    public void newEmailAddress(String emailAddress) {
        this.emailAddress = emailAddress;
    }

    public void newAddress(String address) {
        this.address = address;
    }

    // Returns the customer object's details in a string format
    public String toString() {
        String output = "\nName: " + name;
        output += "\nTelephone number: " + telephoneNumber;
        output += "\nEmail address: " + emailAddress;
        output += "\nAddress: " + address;

        return output;
    }

}
