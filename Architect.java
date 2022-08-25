public class Architect {

    // Attributes of the class
    String name;
    String telephoneNumber;
    String emailAddress;
    String address;

    // Constructors
    public Architect(String name, String telephoneNumber, String emailAddress, String address) {
        this.name = name;
        this.telephoneNumber = telephoneNumber;
        this.emailAddress = emailAddress;
        this.address = address;
    }

    // This method is called with a string value and updates the telephone number of
    // the architect object
    public void newTelephoneNumber(String telephoneNumber) {
        this.telephoneNumber = telephoneNumber;
    }

    // This method is called with a string value and updates the email address of
    // the architect object
    public void newEmailAddress(String emailAddress) {
        this.emailAddress = emailAddress;
    }

    // This method is called with a string value and updates the address of
    // the architect object
    public void newAddress(String address) {
        this.address = address;
    }

    // Returns the architect object's details in a string format
    public String toString() {
        String output = "\nName: " + name;
        output += "\nTelephone number: " + telephoneNumber;
        output += "\nEmail address: " + emailAddress;
        output += "\nAddress: " + address;

        return output;
    }

}
