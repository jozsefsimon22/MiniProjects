public class Project {

    // Attributes of the class
    int number;
    String name;
    String type;
    String address;
    int erfNumber;
    int totalCost;
    int amountPaid;
    String deadline;
    boolean status;
    Contractor contractor;
    Customer customer;
    Architect architect;

    // Constructors
    public Project(int number, String name, String type, String address, int erfNumber, int totalCost, int amountPaid,
            String deadline, boolean status, Contractor contractor, Customer customer, Architect architect) {
        this.number = number;
        this.name = name;
        this.type = type;
        this.address = address;
        this.erfNumber = erfNumber;
        this.totalCost = totalCost;
        this.amountPaid = amountPaid;
        this.deadline = deadline;
        this.status = status;
        this.contractor = contractor;
        this.customer = customer;
        this.architect = architect;
    }

    // This method is called with a string value and updates the deadline of the
    // project object
    public void setDeadline(String deadline) {
        this.deadline = deadline;
    }

    // This method is called with a string value and updates the total amount paid
    // of the project object
    public void setAmountPaid(int amountPaid) {
        this.amountPaid = amountPaid;
    }

    // This method is called without an input and updates the object's status to
    // 'true'
    public void completeProject() {
        this.status = true;
    }

    // Returns the project object's details in a string format
    public String toString() {
        String output = "\nNumber: " + number;
        output += "\nName: " + name;
        output += "\nType: " + type;
        output += "\nAddress: " + address;
        output += "\nERF Number: " + erfNumber;
        output += "\nTotal Cost: " + totalCost;
        output += "\nAmount Paid: " + amountPaid;
        output += "\nDeadline: " + deadline;
        output += "\nProject Completed: " + status;
        output += "\nContractor's name: " + contractor.name;
        output += "\nCustomer's name: " + customer.name;
        output += "\nArchitect's name: " + architect.name;

        return output;
    }
}