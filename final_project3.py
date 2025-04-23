import pandas as pd

from Person_class import Person
from Student_class import Student
from Employee_class import Employee
from MenuOption_class import MenuOption

user_stats = {"total_age": 0, "user_count": 0}

# Map types to classes
type_to_class = {
    "Person": Person,
    "Student": Student,
    "Employee": Employee
}

def get_menu():
    menu = """
1. Save a new entry
2. Search by ID
3. Print ages average
4. Print all names
5. Print all IDs
6. Print all entries
7. Print entry by index
8. Save all data
9. Exit
Please enter your choice: """
    return menu

def get_option():
    option = """
1. Add Person
2. Add Student
3. Add Employee
Please choose an option: """
    return option

def save_new_entry(user_dict: dict, user_type: str, user: list):
    if user_type not in type_to_class:
        print("Unknown user type.")
        return
    
    user_id = user[0]
    new_entry = type_to_class[user_type](*user)
    user_dict[user_id] = new_entry
    
    user_age = user[2]
    user_stats["total_age"] += user_age
    user_stats["user_count"] += 1
        
def search_entry_by_id(user_dict: dict, user_id: int):
    if user_id in user_dict:
        return user_dict[user_id]
    return None

def print_ages_average(user_dict: dict):
    if not user_dict:
        print("No users in the database.\nThe ages average is: 0")
        return
    
    average = user_stats["total_age"] / user_stats["user_count"]
    print("The ages average is: " + str(average))

def print_all_names(user_dict: dict):
    if not user_dict:
        print("No users in the database.")
        return
   
    for index, person in enumerate(user_dict.values()):
        print(str(index) + ". " + person.getName())
        
def print_all_ids(user_dict: dict):
    if not user_dict:
        print("No users in the database.")
        return
   
    for index, user_id in enumerate(user_dict):
        print(str(index) + ". " + str(user_id))

def print_all_entries(user_dict: dict):
    if not user_dict:
        print("No users in the database.")
        return

    for index, (user_id, person) in enumerate(user_dict.items()):
      print(str(index) + ". " + person.getMyselfString())

def print_entry_by_index(user_dict: dict, entry_index: int, keys_list: list):
    if len(user_dict) == 0:
        print("No users in the database.")  
        return
    
    if entry_index < 0 or entry_index > (len(user_dict) - 1):
        print("Index out of range. The maximum index allowed is " + str(len(user_dict) - 1))
        return
    user_id = keys_list[entry_index]
    print_entry(user_dict,user_id)

def print_entry(user_dict: dict, user_id: int):
    person = user_dict[user_id]
    person.printMyselfString()

def error_not_number_msg(value: str, name_of_entry: str):
        print("Error: " + name_of_entry + " must be number. " + value + " is not a number")
  
def get_valid_integer_input(msg_for_user_input: str, label: str):
    while True:
        value = input(msg_for_user_input).strip()
        if value.isdigit() is True:
            return int(value)
        error_not_number_msg(value, label)

def pause(msg: str = "Press Enter to continue "):
    input(msg)

def get_user_data(user_choice: int):
    user_id = get_valid_integer_input("ID: ", "ID")
    user_name = input("Name: ")
    user_age = get_valid_integer_input("Age: ", "Age")
    
    if user_choice == 2:  # Student
        field_of_study = input("Field Of Study: ")
        year_of_study = get_valid_integer_input("Year of study: ", "Year")
        score_avg = get_valid_integer_input("Average score: ", "Score")
        return "Student", [user_id, user_name, user_age, field_of_study, year_of_study, score_avg]

    elif user_choice == 3:  # Employee
        field_of_work = input("Field Of Work: ")
        salary = get_valid_integer_input("Salary: ", "Salary")
        return "Employee", [user_id, user_name, user_age, field_of_work,salary]
    else:  # Person
        return "Person", [user_id, user_name, user_age]

def option_1(user_dict: dict, keys_list: list):
    while True:
        
        user_choice = get_valid_integer_input(get_option(), "Option")
        if user_choice in [1, 2, 3]:
            break
        else:
            print("Please enter a number between 1 and 3.")
            
    user_type, user_data = get_user_data(user_choice)
    user_id = user_data[0]
    if user_id  in user_dict:
        person = user_dict[user_id]
        print("Error: ID already exists: " + person.getMyselfString())
        return 
    
    save_new_entry(user_dict, user_type, user_data)
    print("ID [" + str(user_id) + "] saved successfully.")
    keys_list.append(user_id)

def option_2(user_dict: dict):
    entry_id = get_valid_integer_input("Please enter the ID you want to look for: ","ID")
    result = search_entry_by_id(user_dict, entry_id)
    if result is None:
        print("Error: ID " + str(entry_id) + " is not saved")
    else:
        print_entry(user_dict,entry_id)

def option_3(user_dict: dict):
    print_ages_average(user_dict)
    
def option_4(user_dict: dict):
    print_all_names(user_dict)

def option_5(user_dict: dict):
    print_all_ids(user_dict)
    
def option_6(user_dict: dict):
    print_all_entries(user_dict)
       
def option_7(user_dict: dict, keys_list: list):
    entry_index = get_valid_integer_input("Please enter the index of the entry you want to print: ","Index")
    print_entry_by_index(user_dict, entry_index, keys_list)  

def option_8(user_dict: dict):
    filename = input("Enter filename to save (with .csv): ")
    if not filename.endswith(".csv"):
        print("Invalid file name. It must end with .csv")
        return

    data = []
    for user_id, person in user_dict.items():
        user_type = type(person).__name__
        person_data = {
            "ID": user_id,
            "Name": person.getName(),
            "Age": person.getAge(),
            "Type": user_type
        }

        if user_type == "Student":
            person_data["Field of Study"] = person.getFieldOfStudy()
            person_data["Year of Study"] = person.getYearOfStudy()
            person_data["Average Score"] = person.getScoreAvg()
        elif user_type == "Employee":
            person_data["Field of Work"] = person.getFieldOfWork()
            person_data["Salary"] = person.getSalary()

        data.append(person_data)

    try:
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)
        print("Data saved successfully to " + filename)
    except :
        print("Failed to save file:")

def option_9():
    while True:
        user_input = input("Are you sure? (y/n) ")
        if user_input == "n":
            return False
        elif user_input == "y":
            print("Goodbye!")
            return True
            
def main():
    
    user_dict = {}
    keys_list = []
    
    while True:
        try:
            selected_option = input(get_menu())
            
            try:
                selected_enum = MenuOption(selected_option)
            except ValueError:
                print("Error: Option [" + selected_option + "] does not exist. Please try again")
                pause()
                continue
            
            if  selected_enum == MenuOption.ADD_ENTRY:
                option_1(user_dict, keys_list)
                
            elif selected_enum == MenuOption.SEARCH_BY_ID:
                option_2(user_dict)
                
            elif selected_enum == MenuOption.PRINT_AVERAGE:
                option_3(user_dict)
                
            elif selected_enum == MenuOption.PRINT_NAMES:
                option_4(user_dict)

            elif selected_enum == MenuOption.PRINT_IDS:
                option_5(user_dict)

            elif selected_enum == MenuOption.PRINT_ALL:
                option_6(user_dict)

            elif selected_enum == MenuOption.PRINT_BY_INDEX:
                option_7(user_dict, keys_list)
                
            elif selected_enum == MenuOption.SAVE_TO_CSV:
                if option_8(user_dict) == True:
                    break
            elif selected_enum == MenuOption.EXIT:
                if option_9() == True:
                    break

            pause()
            
        except KeyboardInterrupt:
            print("\nKeyboard interrupt detected. Exiting gracefully.")
            break

if __name__ == "__main__":
    main()