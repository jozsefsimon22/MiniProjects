import java.util.Scanner;
import java.util.ArrayList;

public class ProjectManager {
    public static void main(String[] args) {
        // Variable is set to true. It's updated within the while loop below.
        boolean running = true;

        // The collection is used to store the project objects
        ArrayList<Project> projects = new ArrayList<Project>();

        // I declared an example of every object used in the exercise. This is purely
        // for demonstration purposes.
        Architect exampleArchitect = new Architect("James", "999666", "architect@example.com", "Edinburgh");
        Customer exampleCustomer = new Customer("Andrea", "555000", "customer@xample.com", "Glasgow");
        Contractor exampleContractor = new Contractor("David", "555000", "david@example.com", "Edinburgh");
        Project example = new Project(05, "Example", "Example", "Example", 555, 555, 555, "Example", false,
                exampleContractor, exampleCustomer, exampleArchitect);

        // Adding the example project object to the 'projects' collection
        projects.add(example);

        while (running) {
            // Presenting the menu to the user
            System.out.print("\nPlease select an option\n1 - Create new project\n2 - View/Edit projects\n0 - Exit\n:");
            Scanner in = new Scanner(System.in);
            int menuOptionSelected = in.nextInt();

            // If the user selects option 1 the 'newProject' method is called to create a
            // new project
            if (menuOptionSelected == 1) {
                projects.add(newProject());
            }

            // If the user selects option 2 the name of every project is printed to the
            // screen along with an index number.Then the user is asked to enter the index
            // number of the project to view its details.
            if (menuOptionSelected == 2) {
                boolean projectDetailsRunning = true;

                for (int i = 0; i < projects.size(); i++) {
                    System.out.print("Index " + i + ": Project Name: " + projects.get(i).name + "\n");
                }
                // Asking the user to enter the index number of the project they want to view
                System.out.print("\nPlease enter the Project index to view project details: ");
                int indexInput = in.nextInt();
                System.out.println(projects.toArray()[indexInput]);

                // Presenting the user with the option to edit the project details or return to
                // the main menu.
                while (projectDetailsRunning) {
                    System.out.print("\nPlease select:\n0 - Return to main menu\n1 - Edit project\n: ");
                    int projectMenuSelected = in.nextInt();

                    // If the user selects option 1 to edit project details they are presented with
                    // a number of option to select which detail of the project they want to edit.
                    if (projectMenuSelected == 1) {
                        boolean editDetailsRunning = true;

                        while (editDetailsRunning) {
                            System.out.print(
                                    "\nPlease select:\n0 - Return to main menu\n1 - Edit project deadline\n2 - Edit total amount paid\n3 - Edit contractor details\n4 - Finalize project\n: ");
                            int detailEditSelect = in.nextInt();

                            // If the user selects option 1 the 'setDeadLine' function of the project class
                            // is called and the user is asked to enter new deadline
                            if (detailEditSelect == 1) {
                                System.out.print("Enter new deadline: ");
                                String newDeadline = in.next();
                                projects.get(indexInput).setDeadline(newDeadline);
                            }

                            // If the user selects option 2 the 'setAmountPaid' function of the project
                            // class is called and the user is asked to enter the new amount.
                            if (detailEditSelect == 2) {
                                System.out.print("Enter new total amount paid: ");
                                int newAmountPaid = in.nextInt();
                                projects.get(indexInput).setAmountPaid(newAmountPaid);
                            }

                            // If the user selects option 3 to edit the contractor's details the user is
                            // presented with options to select which detail they want to edit. With each
                            // detail option selected the user is asked to enter the new value and the
                            // corresponding function of the 'Contractor' class is called to update the
                            // value.
                            if (detailEditSelect == 3) {
                                boolean contractorDetailEditRunning = true;

                                while (contractorDetailEditRunning) {
                                    // Presenting the options to the user.
                                    System.out.print(
                                            "Please select one of the options\n0 - Previous menu\n1 - Update telephone number\n2 - Update email address\n3 - Update address\n:");
                                    int contractorDetailEditInput = in.nextInt();
                                    // If the user selects option 1 the user is asked to enter the new phone number
                                    // and the 'newTelephoneNumber' method of the 'Contractor' class is called.
                                    if (contractorDetailEditInput == 1) {
                                        System.out.print("Please enter new phone number: ");
                                        String inputPhoneNumberUpdate = in.next();
                                        projects.get(indexInput).contractor.newTelephoneNumber(inputPhoneNumberUpdate);
                                    }
                                    // If the user selects option 2 the user is asked to enter the new email address
                                    // and the 'newEmailAddress' method of the 'Contractor' class is called.
                                    if (contractorDetailEditInput == 2) {
                                        System.out.print("Please enter new email address: ");
                                        String inputEmailAddressUpdate = in.next();
                                        projects.get(indexInput).contractor.newEmailAddress(inputEmailAddressUpdate);
                                    }
                                    // If the user selects option 3 the user is asked to enter the new address and
                                    // the 'newAddress' method of the 'Contractor' class is called.
                                    if (contractorDetailEditInput == 3) {
                                        System.out.print("Please enter new address: ");
                                        String inputAddressUpdate = in.next();
                                        projects.get(indexInput).contractor.newAddress(inputAddressUpdate);
                                    }
                                    // If the user selects '0' the while loop stops which returns the user to the
                                    // previous menu.
                                    if (contractorDetailEditInput == 0) {
                                        System.out.print("Return to previous menu: ");
                                        contractorDetailEditRunning = false;
                                    }
                                }
                            }

                            // If the user selects this option the project is marked completed by calling
                            // the 'completeProject' method from the project class.
                            if (detailEditSelect == 4) {
                                System.out.print("\nThe project has been marked as completed!\n");
                                projects.get(indexInput).completeProject();
                            }
                            // If the user selects '0' the boolean values are set to false which returns the
                            // user to the main menu
                            if (detailEditSelect == 0) {
                                editDetailsRunning = false;
                                projectDetailsRunning = false;
                            }
                        }
                    }
                    // If the user selects '0' the boolean value is set to false which returns the
                    // user to the main menu.
                    if (projectMenuSelected == 0) {
                        projectDetailsRunning = false;
                    }

                }

            }

            // If the user chooses '0 - Exit' the program quits
            if (menuOptionSelected == 0) {
                System.out.print("Goodbye!");
                running = false;
                // Closing the scanner
                in.close();
            }

        }
    }

    // This method creates a new project object from user input. Then it returns the
    // new object created.
    public static Project newProject() {
        Scanner in = new Scanner(System.in);
        System.out.print("Creating new project. Please enter project details.\nProject Number: ");
        int numberInput = in.nextInt();
        System.out.print("Name: ");
        String nameInput = in.next();
        System.out.print("Type: ");
        String typeInput = in.next();
        System.out.print("Address: ");
        String addressInput = in.next();
        System.out.print("ERF Number: ");
        int erfNumberInput = in.nextInt();
        System.out.print("Total cost: ");
        int totalCostInput = in.nextInt();
        System.out.print("Amount paid: ");
        int amountPaidInput = in.nextInt();
        System.out.print("Deadline: ");
        String deadlineInput = in.next();
        Contractor contractor = newContractor();
        Customer customer = newCustomer();
        Architect architect = newArchitect();

        Project newProjectObject = new Project(numberInput, nameInput, typeInput, addressInput, erfNumberInput,
                totalCostInput, amountPaidInput, deadlineInput, false, contractor, customer, architect);

        return newProjectObject;

    }

    // This method creates a new contractor object from user input. Then it returns
    // the new object created.
    public static Contractor newContractor() {
        Scanner in = new Scanner(System.in);
        System.out.print("Adding new contractor. Please enter contractor details.\nContractor's name: ");
        String nameInput = in.nextLine();
        System.out.print("Contractor's telephone number: ");
        String telephoneInput = in.nextLine();
        System.out.print("Contractor's email address: ");
        String emailInput = in.nextLine();
        System.out.print("Contractor's address: ");
        String addressInput = in.nextLine();

        Contractor newContractorObject = new Contractor(nameInput, telephoneInput, emailInput, addressInput);

        return newContractorObject;

    }

    // This method creates a new customer object from user input. Then it returns
    // the new object created.
    public static Customer newCustomer() {
        Scanner in = new Scanner(System.in);
        System.out.print("Adding new Customer. Please enter Customer details.\nCustomer's name: ");
        String nameInput = in.nextLine();
        System.out.print("Customer's telephone number: ");
        String telephoneInput = in.nextLine();
        System.out.print("Customer's email address: ");
        String emailInput = in.nextLine();
        System.out.print("Customer's address: ");
        String addressInput = in.nextLine();

        Customer newCustomerObject = new Customer(nameInput, telephoneInput, emailInput, addressInput);

        return newCustomerObject;

    }

    // This method creates a new architect object from user input. Then it returns
    // the new object created.
    public static Architect newArchitect() {
        Scanner in = new Scanner(System.in);
        System.out.print("Adding new Architect. Please enter Architect details.\nArchitect's name: ");
        String nameInput = in.nextLine();
        System.out.print("Architect's telephone number: ");
        String telephoneInput = in.nextLine();
        System.out.print("Architect's email address: ");
        String emailInput = in.nextLine();
        System.out.print("Architect's address: ");
        String addressInput = in.nextLine();

        Architect newArchitectObject = new Architect(nameInput, telephoneInput, emailInput, addressInput);

        return newArchitectObject;

    }

}