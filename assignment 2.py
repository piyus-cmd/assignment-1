import sys
import getpass 
import random
import string

student_data = {}
logged_in_reg_no = None


def get_next_reg_no():
    """Generates a simple, sequential registration number."""
    if not student_data:
        return "LNCT001"
    
    # Get all existing Reg Nos
    reg_numbers = sorted(student_data.keys())
    
    # Find the last number used
    try:
        last_reg_no = reg_numbers[-1]
        # Assuming the format is LNCTXXX, extract the number part
        last_number = int(last_reg_no.replace("LNCT", ""))
        new_number = last_number + 1
    except:
        # Fallback if the keys are somehow non-standard or empty
        new_number = 1
        
    return f"LNCT{new_number:03d}"

def is_username_unique(username):
    """Checks if a username is already used by any student."""
    for student in student_data.values():
        if student.get('username') == username:
            return False
    return True

# --- APPLICATION FUNCTIONS ---

def register():
    """
    Handles new student registration, collecting 11 fields and storing them as a dictionary.
    """
    print("\n--- Student Registration (11 Fields Required) ---")
    
    # 1. Registration Number (Auto-generated)
    reg_no = get_next_reg_no()
    print(f"Your unique Registration Number is: {reg_no}")

    # 2. Username
    while True:
        username = input("1. Enter a unique Username: ").strip()
        if not username:
            print("Username cannot be empty.")
            continue
        if not is_username_unique(username):
            print("Username already taken. Please try another.")
        else:
            break

    # 3. Password
    try:
        password = getpass.getpass("2. Enter a Password: ").strip()
    except Exception:
        password = input("2. Enter a Password: ").strip()
        
    if not password:
        print("Password cannot be empty. Registration cancelled.")
        return
    
    print("\n--- Remaining Profile Details ---")
    # 4. Full Name
    name = input("3. Full Name: ").strip()

    # 5. Date of Birth (DOB)
    dob = input("4. Date of Birth (DD/MM/YYYY): ").strip()

    # 6. Phone Number
    phone = input("5. Phone Number: ").strip()

    # 7. Email
    email = input("6. Email Address: ").strip()

    # 8. Program/Course
    program = input("7. Program/Course (e.g., B.Tech CSE): ").strip()

    # 9. Academic Year
    year = input("8. Academic Year (e.g., 1st, 2nd): ").strip()

    # 10. Permanent Address
    address = input("9. Permanent Address: ").strip()
    
    # 11. Guardian/Parent Name
    guardian = input("10. Guardian/Parent Name: ").strip()
    
    # Create the student dictionary and save to the data store
    new_student = {
        'reg_no': reg_no,
        'username': username,
        'password': password,
        'name': name,
        'dob': dob,
        'phone': phone,
        'email': email,
        'program': program,
        'year': year,
        'address': address,
        'guardian': guardian
    }
    student_data[reg_no] = new_student
    
    print(f"\n SUCCESS! {name} registered with Reg No: {reg_no}")

def login():
    """Authenticates the user and sets the global logged_in_reg_no."""
    global logged_in_reg_no
    
    if logged_in_reg_no:
        current_user = student_data[logged_in_reg_no]['username']
        print(f"\nINFO: Already logged in as {current_user}.")
        return

    print("\n--- Student Login ---")
    username = input("Username: ").strip()
    try:
        password = getpass.getpass("Password: ").strip()
    except Exception:
        password = input("Password: ").strip()

    # Search through all student dictionaries for a match
    for reg_no, student in student_data.items():
        if student.get('username') == username and student.get('password') == password:
            logged_in_reg_no = reg_no
            print(f"\n🥳 WELCOME! Logged in as {student['name']}.")
            return

    print("\n ERROR: Invalid username or password.")

def show_profile():
    """Displays the profile of the currently logged-in student."""
    if not logged_in_reg_no:
        print("\n ERROR: Please login first to view your profile.")
        return
        
    student = student_data[logged_in_reg_no]
        
    profile_output = f"""
        --- Student Profile ---
        Registration No: {student['reg_no']}
        Name: {student['name']}
        Username: {student['username']}
        Program: {student['program']} ({student['year']} Year)
        -----------------------
        1. Date of Birth: {student['dob']}
        2. Phone: {student['phone']}
        3. Email: {student['email']}
        4. Address: {student['address']}
        5. Guardian Name: {student['guardian']}
    """
    print(profile_output)

def update_profile():
    """Allows the logged-in student to update key fields."""
    if not logged_in_reg_no:
        print("\n ERROR: Please login first to update your profile.")
        return
        
    student = student_data[logged_in_reg_no]
    print(f"\n--- Update Profile for {student['name']} ({student['reg_no']}) ---")
    print("What would you like to update?")
    print(f"1. Phone Number (Current: {student['phone']})")
    print(f"2. Email Address (Current: {student['email']})")
    print(f"3. Permanent Address (Current: {student['address']})")
    print("4. Password")
    print("0. Cancel")
    
    choice = input("Select option (1/2/3/4/0): ").strip()
    
    if choice == '1':
        student['phone'] = input("Enter new Phone Number: ").strip()
        print(" Phone number updated.")
    elif choice == '2':
        student['email'] = input("Enter new Email Address: ").strip()
        print(" Email address updated.")
    elif choice == '3':
        student['address'] = input("Enter new Permanent Address: ").strip()
        print(" Address updated.")
    elif choice == '4':
        try:
            old_pass = getpass.getpass("Enter current Password for verification: ").strip()
        except Exception:
            old_pass = input("Enter current Password for verification: ").strip()
            
        if old_pass == student['password']:
            try:
                student['password'] = getpass.getpass("Enter NEW Password: ").strip()
            except Exception:
                student['password'] = input("Enter NEW Password: ").strip()
                
            print(" Password updated.")
        else:
            print(" Verification failed. Current password was incorrect.")
    elif choice == '0':
        print("Update cancelled.")
    else:
        print("Invalid choice.")

def logout():
    """Clears the logged_in_reg_no variable."""
    global logged_in_reg_no
    if not logged_in_reg_no:
        print("\nINFO: No user is currently logged in.")
        return
        
    username = student_data[logged_in_reg_no]['username']
    print(f"\n Logging out {username}. Goodbye!")
    logged_in_reg_no = None

def terminate():
    """Exits the application gracefully."""
    print("\n Thank you for using the LNCT Student System. Exiting...")
    sys.exit()

# --- MAIN MENU LOOP ---

def main():
    """The primary execution loop for the application menu."""
    print(" Welcome to LNCT Student Management System (Function-Based) ⭐")
    
    while True:
        # Determine current status for the menu header
        if logged_in_reg_no:
            status = student_data[logged_in_reg_no]['username']
        else:
            status = '(Not Logged In)'
        
        menu_prompt = f'''
        \n--- Main Menu ---
        STATUS: {status}
        
        Choose option:
        1. Registration
        2. Login
        3. Profile
        4. Update profile
        5. Logout
        7. Exit

            select option 1/2/3/4/5/7: '''
            
        response = input(menu_prompt).strip()

        if response == '1':
            register()
        elif response == '2':
            login()
        elif response == '3':
            show_profile()
        elif response == '4':
            update_profile()
        elif response == '5':
            logout()
        elif response == '7':
            terminate()
        else:
            print(" Invalid Choice, Please select a correct option (1, 2, 3, 4, 5, or 7).")

if __name__ == '__main__':
    # Add a sample student for easy testing (11 fields in a dictionary)
    student_data["LNCT000"] = {
        'reg_no': "LNCT000",
        'username': "testuser",
        'password': "password123",
        'name': "Aarav Sharma",
        'dob': "01/01/2004",
        'phone': "9876543210",
        'email': "aarav.s@lnct.in",
        'program': "B.Tech CSE",
        'year': "3rd",
        'address': "Bhopal, MP",
        'guardian': "Rajesh Sharma"
    }
    
    main()
