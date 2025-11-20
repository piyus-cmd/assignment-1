import sys
import getpass 
import random
import string
import json
from datetime import datetime
import quiz_data 


DATA_FILE = 'quiz_app_data.json'
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "adminpass"

student_data = {} 
quiz_scores = {} 
logged_in_reg_no = None

quiz_questions = quiz_data.quiz_questions



def load_data():
    """Loads student and score data from the JSON file."""
    global student_data, quiz_scores
    try:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
            student_data.update(data.get('students', {}))
            quiz_scores.update(data.get('scores', {}))
        print(f"\n[INFO] Data loaded successfully from {DATA_FILE}.")
    except FileNotFoundError:
        print()
    except json.JSONDecodeError:
        print(f"\n[ERROR] Error decoding data file ({DATA_FILE}). Starting fresh.")

def save_data():
    """Saves student and score data to the JSON file."""
    data = {
        'students': student_data,
        'scores': quiz_scores
    }
    try:
        with open(DATA_FILE, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"\n[INFO] Data saved successfully to {DATA_FILE}.")
    except Exception as e:
        print(f"\n[ERROR] Failed to save data: {e}")

# --- HELPER FUNCTIONS ---

def get_next_reg_no():
    """Generates a simple, sequential registration number."""
    if not student_data:
        return "LNCT001"
    
    reg_numbers = sorted([r for r in student_data.keys() if r.startswith('LNCT')])
    
    try:
        last_reg_no = reg_numbers[-1]
        last_number = int(last_reg_no.replace("LNCT", ""))
        new_number = last_number + 1
    except (IndexError, ValueError):
        new_number = 1
        
    return f"LNCT{new_number:03d}"

def is_username_unique(username):
    """Checks if a username is already used by any student."""
    for student in student_data.values():
        if student.get('username') == username:
            return False
    # Also check against admin username
    if username == ADMIN_USERNAME:
        return False
    return True



def register():
    """Handles new student registration."""
    print("\n--- Student Registration (11 Fields Required) ---")
    
    # Registration Number (Auto-generated)
    reg_no = get_next_reg_no()
    print(f"Your unique Registration Number is: {reg_no}")

    # Username
    while True:
        username = input("1. Enter a unique Username: ").strip()
        if not username:
            print("Username cannot be empty.")
            continue
        if not is_username_unique(username):
            print("Username already taken or reserved (e.g., admin). Please try another.")
        else:
            break

    # Password
    try:
        password = getpass.getpass("2. Enter a Password: ").strip()
    except Exception:
        password = input("2. Enter a Password: ").strip()
        
    if not password:
        print("Password cannot be empty. Registration cancelled.")
        return
    
    print("\n--- Remaining Profile Details ---")
    name = input("3. Full Name: ").strip()
    dob = input("4. Date of Birth (DD/MM/YYYY): ").strip()
    phone = input("5. Phone Number (Contact): ").strip()
    email = input("6. Email Address: ").strip()
    program = input("7. Program/Course (Branch): ").strip()
    year = input("8. Academic Year: ").strip()
    address = input("9. Permanent Address: ").strip()
    guardian = input("10. Guardian/Parent Name: ").strip()
    
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
    """Authenticates the user (student or admin) and sets the global logged_in_reg_no."""
    global logged_in_reg_no
    
    if logged_in_reg_no:
        status = 'ADMIN' if logged_in_reg_no == 'ADMIN' else student_data[logged_in_reg_no]['username']
        print(f"\n[INFO] Already logged in as {status}.")
        return

    print("\n--- Login (User or Admin) ---")
    user = input("Username: ").strip()
    try:
        password = getpass.getpass("Password: ").strip()
    except Exception:
        password = input("Password: ").strip()

    # 1. Check for Admin Login
    if user == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        logged_in_reg_no = 'ADMIN' # Special identifier for admin
        print("\nWelcome Admin Logged in as Administrator.")
        return

    # 2. Check for Student Login
    for reg_no, student in student_data.items():
        if student.get('username') == user and student.get('password') == password:
            logged_in_reg_no = reg_no
            print(f"\nWELCOME Logged in as {student['name']}.")
            return

    print("\n ERROR: Invalid username or password.")

def show_profile():
    """Displays the profile of the currently logged-in student (or a message for admin)."""
    if not logged_in_reg_no:
        print("\n ERROR: Please login first to view your profile.")
        return
        
    if logged_in_reg_no == 'ADMIN':
        print("\n--- Admin Profile ---")
        print("Role: System Administrator")
        print("Note: Admin functionality (e.g., viewing all data) is not implemented here.")
        return
        
    student = student_data[logged_in_reg_no]
        
    profile_output = f"""
        --- Student Profile ---
        Registration No: {student['reg_no']}
        Name: {student['name']}
        Username: {student['username']}
        Program (Branch): {student['program']} ({student['year']} Year)
        -----------------------
        1. Date of Birth: {student['dob']}
        2. Phone (Contact): {student['phone']}
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
        
    if logged_in_reg_no == 'ADMIN':
        print("\n ERROR: Admin cannot update profile through this interface.")
        return
        
    student = student_data[logged_in_reg_no]
    print(f"\n--- Update Profile for {student['name']} ({student['reg_no']}) ---")
    print("Which field would you like to update?")
    print(f"1. Full Name (Current: {student['name']})")
    print(f"2. Email Address (Current: {student['email']})")
    print(f"3. Phone Number (Contact) (Current: {student['phone']})")
    print(f"4. Program/Branch (Current: {student['program']})")
    print(f"5. Academic Year (Current: {student['year']})")
    print("6. Password")
    print("0. Cancel")
    
    choice = input("Select option (1-6/0): ").strip()
    
    if choice == '1':
        student['name'] = input("Enter new Full Name: ").strip()
        print(" Full Name updated.")
    elif choice == '2':
        student['email'] = input("Enter new Email Address: ").strip()
        print(" Email address updated.")
    elif choice == '3':
        student['phone'] = input("Enter new Phone Number: ").strip()
        print(" Phone number updated.")
    elif choice == '4':
        student['program'] = input("Enter new Program/Branch: ").strip()
        print(" Program/Branch updated.")
    elif choice == '5':
        student['year'] = input("Enter new Academic Year: ").strip()
        print(" Academic Year updated.")
    elif choice == '6':
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
        print("\n[INFO] No user is currently logged in.")
        return
        
    status = 'ADMIN' if logged_in_reg_no == 'ADMIN' else student_data[logged_in_reg_no]['username']
    print(f"\n Logging out {status}. Goodbye!")
    logged_in_reg_no = None

# --- QUIZ MODULE FUNCTIONS ---

def attempt_quiz(category):
    """Administers the quiz for the selected category, shuffles questions and options."""
    questions = quiz_questions.get(category)
    if not questions:
        print(f" ERROR: No questions found for category {category}.")
        return

    # Shuffle questions
    random.shuffle(questions)
    
    score = 0
    total_questions = len(questions)
    reg_no = logged_in_reg_no

    print(f"\n--- Starting {category} Quiz ({total_questions} Questions) ---")
    
    for i, (question, options, correct_index) in enumerate(questions):
        print(f"\nQuestion {i + 1}/{total_questions}: {question}")
        option_map = {}
        
        # Shuffle options
        shuffled_options = list(enumerate(options))
        random.shuffle(shuffled_options) 
        
        # Display options
        for j, (original_index, opt) in enumerate(shuffled_options):
            option_letter = chr(65 + j) # A, B, C, D
            print(f"  {option_letter}. {opt}")
            option_map[option_letter.lower()] = original_index
            
        
        # Get user input
        while True:
            answer = input("Your answer (A/B/C/D): ").strip().lower()
            if answer in option_map:
                break
            print(" Invalid input. Please enter A, B, C, or D.")

        # Check answer
        selected_index = option_map[answer]
        if selected_index == correct_index:
            score += 1
            print(" Correct!")
        else:
            # Find the correct letter for display
            correct_letter = ""
            for letter, index in option_map.items():
                if index == correct_index:
                    correct_letter = letter.upper()
                    break
            print(f" Incorrect! The correct answer was {correct_letter}. {options[correct_index]}")

    # Record score
    print("\n--- Quiz Finished! ---")
    print(f"Your final score: {score} out of {total_questions}")
    
    score_record = {
        'category': category,
        'marks': score,
        'total_marks': total_questions,
        'datetime': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    if reg_no not in quiz_scores:
        quiz_scores[reg_no] = []
    
    quiz_scores[reg_no].append(score_record)
    print("Score recorded in your profile.")


def show_scores():
    """Displays the user's quiz score history."""
    if not logged_in_reg_no or logged_in_reg_no == 'ADMIN':
        print("\n ERROR: Please login as a student to view scores.")
        return
    
    reg_no = logged_in_reg_no
    scores = quiz_scores.get(reg_no, [])

    print(f"\n--- Quiz Score History for {student_data[reg_no]['name']} ---")
    
    if not scores:
        print(" No quizzes attempted yet.")
        return
        
    print(f"{'#':<3} | {'Category':<10} | {'Score':<12} | {'Date/Time':<20}")
    print("-" * 50)
    
    for i, record in enumerate(scores, 1):
        score_str = f"{record['marks']}/{record['total_marks']}"
        print(f"{i:<3} | {record['category']:<10} | {score_str:<12} | {record['datetime']:<20}")


def quiz_menu():
    """Provides the main menu for the quiz module."""
    if not logged_in_reg_no:
        print("\n ERROR: You must be logged in to access the Quiz Module.")
        return
        
    if logged_in_reg_no == 'ADMIN':
        print("\n ERROR: Admins cannot attempt quizzes.")
        return

    while True:
        print("\n--- Quiz Module Menu ---")
        print("1. Attempt Quiz (Select Category)")
        print("2. View Score History")
        print("3. Show Profile")
        print("4. Update Profile")
        print("5. Logout")
        print("6. Back to Main Menu")
        
        choice = input("Select option (1-6): ").strip()
        
        if choice == '1':
            print("\n--- Select Quiz Category ---")
            categories = list(quiz_questions.keys())
            for i, cat in enumerate(categories, 1):
                print(f"{i}. {cat}")
            print(f"{len(categories) + 1}. Cancel")
            
            cat_choice = input("Enter category number: ").strip()
            
            try:
                cat_index = int(cat_choice) - 1
                if 0 <= cat_index < len(categories):
                    attempt_quiz(categories[cat_index])
                elif cat_index == len(categories):
                    print("Category selection cancelled.")
                else:
                    print(" Invalid category number.")
            except ValueError:
                print(" Invalid input.")
                
        elif choice == '2':
            show_scores()
        elif choice == '3':
            show_profile()
        elif choice == '4':
            update_profile()
        elif choice == '5':
            logout()
            return # Exit quiz menu after logging out
        elif choice == '6':
            print("Returning to Main Menu.")
            break
        else:
            print(" Invalid choice.")

def terminate():
    """Saves data and exits the application gracefully."""
    save_data()
    print("\n Thank you for using the LNCT Student System. Exiting...")
    sys.exit()

# --- MAIN MENU LOOP ---

def main():
    """The primary execution loop for the application menu."""
    # Load data from file first
    load_data()
    
    # Add a sample student/admin if no data was loaded
    if not student_data:
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
        
        
    print("\n Welcome to LNCT Student Management System ")
    
    while True:
        # Determine current status for the menu header
        if logged_in_reg_no == 'ADMIN':
            status = 'ADMIN'
        elif logged_in_reg_no:
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
        5. Quiz Module 
        6. Logout
        7. Exit

            select option 1/2/3/4/5/6/7: '''
            
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
            quiz_menu()
        elif response == '6':
            logout()
        elif response == '7':
            terminate()
        else:
            print(" Invalid Choice. Please select a correct option (1-7).")

if __name__ == '__main__':
    main()
