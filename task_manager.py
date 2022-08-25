# =====importing libraries===========
from datetime import date
from datetime import datetime

# ====Login Section====

# Boolean variables set to 'False' default values
correct_username = False  # Updated to 'True' when user enters a correct username
correct_password = False  # Updated to 'True' when user enters corresponding password
user_logged_in = (
    False  # Updated to 'True' when both username and password entered correctly
)

# Counters used to count the number of attempts remaining updated through the while loops below
wrong_username_counter = 2
wrong_password_counter = 2

# Empty lists which are updated with the usernames/passwords below
stored_usernames = []
stored_passwords = []

# Asks the user to input their username
username_input = input("Please enter your username: ")

# Opens the 'user.txt' file and cast all usernames to the 'stored_usernames' list and passwords to the 'stored_passwords' list
with open("user.txt", "r") as user_data:
    for line in user_data:
        stored_usernames.append(line.split(",")[0])
        stored_passwords.append(line.split()[1])

# While loop until user enters correct username or wrong username entered 3 times
# If correct username is entered it sets 'correct_username' to true, stores the index of the username, and asks the user to enter password
# If incorrect username is entered it repeats the input query 3 times then displays the error message and quits the program, unless a correct username was entered
while correct_username is False:
    if username_input in stored_usernames:
        correct_username = True
        username_index = stored_usernames.index(username_input)
        password_input = input("Please enter your password: ")
    elif wrong_username_counter == 0:
        print(
            "Wrong username entered too many times. Access denied. Please contact your system administrator."
        )
        exit()
    else:
        username_input = input(
            f"Incorrect username, you have {wrong_username_counter} attempt left. Please enter username: "
        )
        wrong_username_counter -= 1

# While loops executes only if a correct username was entered then asks the user for their password
# Checks if the password entered is the corresponding password for the username by using 'username_index', if correct it sets 'correct_password' to 'True'
# If incorrect password is entered it repeats the input query 3 times then displays the error message and quits the program, unless a correct password was entered
while correct_username is True and correct_password is False:
    if password_input == stored_passwords[username_index]:
        correct_password = True
    elif wrong_password_counter == 0:
        print(
            "Wrong password entered too many times. Access denied. Please contact your system administrator."
        )
        exit()
    else:
        password_input = input(
            f"Wrong password entered, you have {wrong_password_counter} attempt left. Please enter password: "
        )
        wrong_password_counter -= 1

# If both the 'correct_username' and 'correct_password' were set to 'True' above, it updates the 'user_logged_in' to 'True'
if correct_username is True and correct_password is True:
    user_logged_in = True

while True:
    while user_logged_in is True:
        # presenting the menu to the user if user is admin
        # making sure that the user input is converted to lower case.
        if username_input == "admin":
            menu = input(
                """Select one of the following Options below:
        r - Registering a user
        a - Adding a task
        va - View all tasks
        vm - View my task
        vs - View statistics
        e - Exit
        : """
            ).lower()

        # presenting the menu to the user if user is not admin
        # making sure that the user input is converted to lower case.
        if username_input != "admin":
            menu = input(
                """Select one of the following Options below:
        a - Adding a task
        va - View all tasks
        vm - View my task
        e - Exit
        : """
            ).lower()

        # If the user selects 'r' it asks to enter the username and password for the new user
        # then it asks the user to confirm password, if the two entry don't match the new password input is repeated until match
        # then it prints the text and writes the details of the new user to the 'user.txt' file
        if menu == "r" and username_input == "admin":
            print("Registering new user")
            new_username = input("Please enter your username: ")
            new_password = input("Please enter your password: ")
            new_password_confirmation = input("Please confirm your password: ")
            while new_password != new_password_confirmation:
                print("Passwords didn't match, please try again.")
                new_password = input("Please enter your password: ")
                new_password_confirmation = input("Please confirm your password: ")
            print("New user added")
            with open("user.txt", "a") as user_data:
                user_data.write(f"\n{new_username}, {new_password}")

        # If user selects 'a' it asks for the details of the new task and writes it to 'tasks.txt' file
        elif menu == "a":
            today_date = datetime.strftime(date.today(), "%d %b %Y")
            new_task_username = input(
                "Please enter the username task of the task owner: "
            ).lower()
            new_task_title = input("Please enter the title of the task: ")
            new_task_description = input("Please enter the description of the task: ")
            new_task_due_date = input("Please enter the due date of the task: ")
            with open("tasks.txt", mode="a") as tasks_data:
                tasks_data.write(
                    f"\n{new_task_username}, {new_task_title},{new_task_description},{today_date}, {new_task_due_date}, No"
                )

        # Reads the tasks from 'task.txt'
        # cast the text of each line into a list then each item of the list is assigned to a variable
        # then it prints the details of each task out formatted as per the assignment requirement
        elif menu == "va":
            with open("tasks.txt", "r") as tasks:
                for line in tasks:
                    task_list = line.replace("\n", "").split(",")
                    task_title = task_list[1].strip()
                    task_owner = task_list[0].strip()
                    task_date_assigned = task_list[3].strip()
                    task_date_due = task_list[4].strip()
                    task_status = task_list[5].strip()
                    task_description = task_list[2].strip()

                    print(f"\nTask:\t\t\t{task_title}")
                    print(f"Assigned to:\t\t{task_owner}")
                    print(f"Date assigned:\t\t{task_date_assigned}")
                    print(f"Due date:\t\t{task_date_due}")
                    print(f"Task complete:\t\t{task_status}")
                    print(f"Task description:\n\t{task_description}")
                    print(
                        "\u2500" * 150
                    )  # The code to print a straight line was found online Reference: https://stackoverflow.com/questions/65561243/print-a-horizontal-line-in-python

        # Reads the tasks from 'task.txt'
        # cast the text of each line into a list then each item of the list is assigned to a variable
        # then checks the username used to login and prints the details of each task assigned to the user formatted as per the assignment requirement
        elif menu == "vm":
            with open("tasks.txt", "r") as tasks:
                for line in tasks:
                    task_list = line.replace("\n", "").split(",")
                    if username_input == task_list[0]:
                        task_title = task_list[1].strip()
                        task_owner = task_list[0].strip()
                        task_date_assigned = task_list[3].strip()
                        task_date_due = task_list[4].strip()
                        task_status = task_list[5].strip()
                        task_description = task_list[2].strip()

                        print(f"\nTask:\t\t\t{task_title}")
                        print(f"Assigned to:\t\t{task_owner}")
                        print(f"Date assigned:\t\t{task_date_assigned}")
                        print(f"Due date:\t\t{task_date_due}")
                        print(f"Task complete:\t\t{task_status}")
                        print(f"Task description:\n\t{task_description}")
                        print(
                            "\u2500" * 150
                        )  # The code to print a straight line was found online Reference: https://stackoverflow.com/questions/65561243/print-a-horizontal-line-in-python

        # If the user is 'admin' it and select 'vs' it prints the total users and tasks out
        elif menu == "vs" and username_input == "admin":
            task_counter = 0
            user_counter = 0
            with open("tasks.txt", "r") as tasks:
                for line in tasks:
                    task_counter += 1
            with open("user.txt", "r") as users:
                for line in users:
                    user_counter += 1
            print(f"\nTotal users:\t{user_counter}")
            print(f"Total tasks:\t{task_counter}\n")

        elif menu == "e":
            print("Goodbye!!!")
            exit()

        # If a non admin user tries to register a new user an error message is returned
        elif menu == "r" and username_input != "admin":
            print("You don't have access to this option, please choose another one.")

        # If a non admin user tries to view statistics an error message is returned
        elif menu == "vs" and username_input != "admin":
            print("You don't have access to this option, please choose another one.")

        else:
            print("You have made a wrong choice, Please Try again")
