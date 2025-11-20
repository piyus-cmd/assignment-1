print("Name - Piyush Kushwaha")
print("Enrollment no. - 0157CY231079")
print("Batch - 5")
print("Batch time - 10:30\n")
print("question numbers range is from 1 to 40")
question_no = int(input("enter question no."))
#1. Write a program to check whether a number is positive, negative, or zero.
if(question_no == 1):
    print("check for +ve,-ve or zero")
    c = int(input("enter no."))
    if(c>0):
        print("no. is positive")
    elif(c<0):
        print("no. is negative")
    else:
        print("no. is zero")

#2. Write a program to check whether a number is even or odd.
elif(question_no == 2):
    print("odd even checker")
    c = int(input("enter no."))
    if(c%2==0):
        print("even")
    else:
        print("odd")

#3. Write a program to check if a given year is a leap year or not.
elif(question_no == 3):
    print("check if given year is a leap year")
    c = int(input("year="))
    if(c%4==0 or c%400==0):
        print("its leap year")
    else:
        print("it is not leap year")

#4. Write a program to find the greatest of two numbers.
elif(question_no == 4):
    print("which is the greatest no.")
    c1 = int(input("1st number"))
    c2 = int(input("2nd number"))
    if(c1>c2):
        print("1st no. is greater :")
    elif(c2>c1):
        print("2nd no. is greater :")
    else:
        print("both are same")

#5. Write a program to check whether a person is eligible to vote (age >= 18).
elif(question_no == 5):
    print("to check person is eligible to vote ")
    c = int(input("enter your age: "))
    if(c>=18):
        print("you are eligible to vote")
    else:
        print("not eligible")

#6. Write a program to check whether a given character is a vowel or consonant.
elif(question_no == 6):
    print("to check given character is vowel or consonant ")
    c = (input("enter character: "))
    c = c.lower()
    if(c=='a' or c=='e' or c=='i' or c=='o' or c=='u'):
        print("entered character is vowel")
    else:
        print("entered character is consonant")

#7. Write a program to check if a number is divisible by 5.
elif(question_no == 7):
    print("a program to check if a number is divisible by 5")
    c = int(input("enter number: "))
    if(c%5==0):
        print(f"%s number is divisible by 5"%(c))
    else:
        print(f"%s number is not divisible by 5"%c)

#8. Write a program to determine whether a given number is a single-digit, two-digit, or more than two-digit number.
elif(question_no == 8):
    print(" a program to determine whether a given number is a single-digit, two-digit, or more than two-digit number")
    c = int(input("enter number: "))
    if(c<-99 or c>99):
        print(f"%s is more than 2 digit number "%c)
    elif(c<-9 or c>9):
        print(f"%s is  2 digit number "%c)
    else:
        print(f"%s is one digit number"%c)

#9. Write a program to check whether a student has passed or failed (passing marks = 40).
elif(question_no == 9):
    print(" a program to check whether a student has passed or failed (passing marks = 40).")
    c = int(input("enter your marks: "))
    if(c >= 40):
        print("hurray you passed the exam")
    else:
        print("Fail..")

#10. Write a program to find whether the entered number is a multiple of both 3 and 7.
elif(question_no == 10):
    print("a program to find whether the entered number is a multiple of both 3 and 7.")
    c = int(input("enter number: "))
    if(c%3==0 and c%7==0):
        print("the entered number is a multiple of both 3 and 7")
    else:
        print("the entered number is not a multiple of both 3 and 7")

#11. Write a program to find the greatest among three numbers.
elif(question_no == 11):
    print("a program to find the greatest among three numbers.")
    a = int(input("a= "))
    b = int(input("b= "))
    c = int(input("c= "))

    if(a>b and a>c):
        print("%s is greatest"%a)
    elif(b>a and b>c):
        print(f"%s is greatest"%b)
    else:
        print(f"%s is greatest"%c)

#12. Write a program to classify a person based on age: Child (<13), Teenager (13-19), Adult (20-59), Senior (60+).
elif(question_no == 12):
    print("a program to classify a person based on age: Child (<13), Teenager (13-19), Adult (20-59), Senior (60+).")
    age = int(input("enter age: "))
    if(age<13 and age>-1):
        print("lalla ho tum abhi")
    elif(age>=13 and age<=19):
        print("teenager")
    elif(age>19 and age <60):
        print("")
    

#13 a program to assign grades based on marks
elif(question_no == 13):
    print("a program to assign grades based on marks")
    marks = int(input("enter marks: "))
    grade = '';
    if(marks>89 and marks<101):
        grade = 'A';
        print(grade);
    elif(marks>74 and marks<90):
        grade = 'B'
        print(grade)
    elif(marks>49 and marks <75):
        grade = 'C';
        print(grade)
    elif(marks>34 and marks<50):
        grade = 'D'
        print(grade)
    elif(marks>-1 and marks<35):
        grade = 'Fail'
        print(grade)
    else:
        print("invalid marks")

#14. Write a program to check the type of triangle (equilateral, isosceles, or scalene) based on sides. 
elif(question_no == 14):
    print("a program to check the type of triangle (equilateral, isosceles, or scalene) based on sides.")
    side_a = int(input("length of side a = "))
    side_b = int(input("length of side b = "))
    side_c = int(input("length of side c = "))
    if(side_a == side_b):
        if(side_a == side_c):
            print("this is a equilateral triangle")
        else:
            print("its an isosceles triangle")
    else:
        if(side_b == side_c):
            print("its a isosceles triangle")
        else:
            print("its a scalene triangle")


#15. Write a program to check if a character is uppercase, lowercase, digit, or special symbol.
elif(question_no == 15):
    print("a program to check if a character is uppercase, lowercase, digit, or special symbol.")
    c = (input("enter character: "))
    if(c.isalpha()):
        if(c.isupper()):
            print("character is uppercase")
        else:
            print("character is lowercase")
    else:
        if(c.isdigit()):
            print("character is digit")
        else:
            print("character is symbol")


#16. Write a program to calculate electricity bill based on units: 
#       Up to 100 units: ₹5 per unit, 
#       101–200 units: ₹7 per unit, 
#       Above 200 units: ₹10 per unit. 
elif(question_no == 16):
    print("a program to calculate electricity bill based on units.")
    units = int(input("enter units :"))
    bill = 0
    if(units>200):                   #units = 1000       
        bill = 10*(units-200)        #bill = 10*800
        units = units-(units-200)    #units = 1000-(1000-200) = 200
        bill = bill+(7*(units-100))  #bill = 8000+(7*(200-100)) = 8700 
        units = units-100            #unit = 100
        bill = bill+(5*units)        #bill = 8700+(5*100) = 9200
        print("bill = ",bill)
    else:
        if(units<101):
            bill = 5*units
            print("bill = ",bill)
        else:
            bill = 5*(100) 
            units = units - 100
            bill = bill+(7*units)
            print("bill = ",bill)

#17. Write a program to determine the largest of four numbers using nested if. 
elif(question_no == 17):
    print("a program to determine the largest of four numbers using nested if.")
    a = int(input("enter a = "))
    b = int(input("enter b = "))
    c = int(input("enter c = "))
    d = int(input("enter d = "))
    if(a>b):
        if(a>c):
            if(a>d):
                print(f"%s is greatest"%a)
            else:
                print(f"%s is greatest"%d)
        else:
            if(c>d):
                print(f"%s is greatest"%c)
            else:
                print(f"%s is greatest"%d)

    else:
        if(b>c):
            if(b>d):
                print(f"%s is greatest"%b)
            else:
                print(f"%s is greatest"%d)
        else:
            if(c>d):
                print(f"%s is greatest"%c)
            else:
                print(f"%s is greatest"%d)

#18. Write a program to check if a given year is a century year and also a leap year. 
elif(question_no == 18):
    print("a program to check if a given year is a century year and also a leap year.")
    c = int(input("year="))
    if(c%400==0):
        print("its century year and also a leap year.")
    else:
        print("it is not century year and also a leap year.")

#19. Write a program to classify BMI value: Underweight (<18.5), Normal (18.5-24.9), Overweight (25-29.9), Obese (30+). 
elif(question_no == 19):
    print("a program to classify BMI value: Underweight (<18.5), Normal (18.5-24.9), Overweight (25-29.9), Obese (30+). ")
    BMI = float(input("Enter BMI: "))
    if(BMI<30):
        if(BMI<25):
            if(BMI<18.5 and BMI>=0):
                print("Underweight")
            else:
                print("Normal")
        else:
            print("Overweight")
    else:
        print("Obese")

#20. Write a program to display the smallest number among three using nested if.
elif(question_no == 20):
    print("a program to display the smallest number among three using nested if.")
    a = int(input("enter a= "))
    b = int(input("enter b= "))
    c = int(input("enter c= "))
    if(a>b):
        if(a>c):
            print(f"%s is greatest"%a)
        else:
            print(f"%s is greatest"%c)
    else:
        if(b>c):
            print(f"%s is greatest"%b)
        else:
            print(f"%s is greatest"%c)

#21. Write a program using a for loop to print all Armstrong numbers between 100 and 999. (Armstrong number: 
#    sum of cubes of digits equals the number itself. Example: 153 => 1³+5³+3³ = 153). 
elif(question_no == 21):
    print("a program using a for loop to print all Armstrong numbers between 100 and 999.")
    for a in range(100,999):
        d = (a%10)
        e = ((a//10)%10)
        f = ((a//100)%10)
        c = (d**3)+(e**3)+(f**3)
        if(c==a):
            print(f"%s "%a)

#22. Write a program to generate and display the first n prime numbers using a for loop.
elif(question_no == 22):
    print("a program to generate and display the first n prime numbers using a for loop.")
    n = int(input("enter number= "))
    prime = [1]
    for num in (range(2,n)):
        j = 2
        for i in range(2,num):
            if(num%i==0):
                break
            j=j+1
        prime.append(j)
    li = set(prime)
    li = sorted(li)
    print(li)


#23: Numbers from 1 to 500 divisible by 3 with sum of digits <= 10.
elif(question_no == 23):
    print("23. Numbers divisible by 3 with a digit sum <= 10:")
    found_numbers = []
    for num in range(1, 501):
        if num % 3 == 0:
            # Calculate the sum of digits
            sum_of_digits = sum(int(digit) for digit in str(num))
            if sum_of_digits <= 10:
                found_numbers.append(num)
    print(found_numbers)

#24: Pyramid of stars.
elif(question_no == 24):
    print(f"24. Star pyramid of height {n}:")
    n = int(input("enter n: "))
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)

#25: Pangram checker.
elif(question_no == 25):
    print(f"25. Checking if string is a pangram:")
    s = input("enter string: ")
    s = s.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    is_pangram_status = True
    for char in alphabet:
        if char not in s:
            is_pangram_status = False
            break
    
    if is_pangram_status:
        print("The string is a pangram.")
    else:
        print("The string is not a pangram.")

#26: Twin primes.
elif(question_no == 26):
    print("Twin primes")
    twin_primes = []
    for num in range(1,100):
        # Check if num is prime
        is_prime1 = True
        if num <= 1:
            is_prime1 = False
        else:
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    is_prime1 = False
                    break
    
        # Check if num + 2 is prime
        is_prime2 = True
        num2 = num + 2
        if num2 <= 1:
            is_prime2 = False
        else:
            for i in range(2, int(num2**0.5) + 1):
                if num2 % i == 0:
                    is_prime2 = False
                    break

        if is_prime1 and is_prime2:
            twin_primes.append((num, num + 2))

    print(twin_primes)

#27: Harshad number checker.
elif(question_no == 27):
    print("27. Checking if number is a Harshad number:")
    num = int(input("enter number: "))
    if num <= 0:
        print("A Harshad number must be a positive integer.")
        
    else:
        sum_of_digits = 0
        # Use a for loop to iterate through the digits of the number
        for digit in str(num):
            sum_of_digits += int(digit)

        if num % sum_of_digits == 0:
            print(f"{num} is a Harshad number.")
        else:
            print(f"{num} is not a Harshad number.")

#88: Pascal's Triangle.
elif(question_no == 28):
    n = int(input("enter no.  of rows: "))
    print(f"28. Pascal's Triangle up to n rows:")
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        if i > 1:
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    # Print the triangle
    for row in triangle:
        print(" ".join(map(str, row)).center(n * 3))

#29: Sum of series 1² + 2² + ... + n².
elif(question_no == 29):
    print(f"29. Sum of the series 1² + 2² + ... + n²:")
    n = int(input("enter n: "))
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i ** 2
    
    print(f"The sum is: {total_sum}")


#30: Strong number checker.
elif(question_no == 30):
    print("30. Strong number checker.")
    num = int(input(".Enter a number to check if it's a Strong number: "))


    print(f"Checking if {num} is a Strong number:")
    original_num = num
    sum_of_factorials = 0

    for digit_char in str(num):
        digit = int(digit_char)
        # Inline factorial calculation
        fact = 1
        if digit == 0:
            fact = 1
        else:
            for i in range(1, digit + 1):
                fact *= i
        sum_of_factorials += fact

    if sum_of_factorials == original_num:
        print(f"{original_num} is a Strong number.")
    else:
        print(f"{original_num} is not a Strong number.")


#31: Greatest among three numbers.
elif(question_no == 31):
    print("31. Greatest among three numbers.")
    while True:
        try:
            a = int(input("Enter first number (a): "))
            b = int(input("Enter second number (b): "))
            c = int(input("Enter third number (c): "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    if a > b and a > c:
        print(f"{a} is greatest")
    elif b > a and b > c:
        print(f"{b} is greatest")
    else:
        print(f"{c} is greatest")

#32: Sum of digits of all numbers entered becomes > 100.
elif(question_no == 32):
    print("32. Keep entering numbers until the sum of digits of all numbers entered is > 100.")
    total_digit_sum = 0
    num_count = 0
    while total_digit_sum <= 100:
        while True:
            try:
                num = int(input(f"Enter number #{num_count + 1}: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
        
        current_digit_sum = 0
        temp_num = abs(num)
        while temp_num > 0:
            current_digit_sum += temp_num % 10
            temp_num //= 10
        
        total_digit_sum += current_digit_sum
        num_count += 1
        print(f"Current sum of digits: {total_digit_sum}")

    print(f"The sum of digits exceeded 100 after {num_count} numbers.")


#33: Duck number checker.
elif(question_no == 33):
    print("33. Duck number checker.")
    while True:
        num_str = input("Enter a number to check if it's a Duck number: ")
        if num_str.startswith('0'):
            print("Invalid input. A Duck number cannot start with zero. Please try again.")
        else:
            is_duck = False
            i = 0
            while i < len(num_str):
                if num_str[i] == '0':
                    is_duck = True
                    break
                i += 1
            
            if is_duck:
                print(f"{num_str} is a Duck number.")
            else:
                print(f"{num_str} is not a Duck number.")
            break


#34: Happy number checker.
elif(question_no == 34):
    num = int(input("Enter a number to check if it's a Happy number: "))

    seen = set()
    original_num = num
    while num != 1 and num not in seen:
        seen.add(num)
        
        sum_of_squares = 0
        temp_num = num
        while temp_num > 0:
            digit = temp_num % 10
            sum_of_squares += digit ** 2
            temp_num //= 10
        
        num = sum_of_squares

    if num == 1:
        print(f"{original_num} is a Happy number.")
    else:
        print(f"{original_num} is not a Happy number.")


#35: Largest prime factor.
elif(question_no == 35):
    print("35. Largest prime factor.")
    while True:
        try:
            n = int(input("Enter a number to find its largest prime factor: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    largest_prime = -1
    i = 2
    while i * i <= n:
        while n % i == 0:
            largest_prime = i
            n //= i
        i += 1

    if n > 1:
        largest_prime = n

    print(f"The largest prime factor is: {largest_prime}")


#36: Palindrome string.
elif(question_no == 36):
    print("36. Palindrome string checker.")
    while True:
        s = input("Enter a string: ")
        reversed_s = s[::-1]
        if s == reversed_s:
            print(f"'{s}' is a palindrome. Exiting.")
            break
        else:
            print(f"'{s}' is not a palindrome. Please try again.")

#37: Digital root.
elif(question_no == 37):
    print("37. Digital root.")
    num = int(input("Enter a number to find its digital root: "))
    while num >= 10:
        sum_of_digits = 0
        temp_num = num
        while temp_num > 0:
            sum_of_digits += temp_num % 10
            temp_num //= 10
        num = sum_of_digits

    print(f"The digital root is: {num}")


#38: Collatz sequence.
elif(question_no == 38):
    print("38. Collatz sequence.")
    n = int(input("Enter a starting number for the Collatz sequence: "))

    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        sequence.append(n)

    print("Collatz sequence:")
    print(sequence)

#39: Kaprekar number checker.
elif(question_no == 39):
    print("39. Kaprekar number checker.")
    n = int(input("Enter a number to check if it's a Kaprekar number: "))
    is_kaprekar = False
    if n > 0:
        square = n * n
        s_square = str(square)
        length = len(s_square)
        
        i = 1
        while i < length:
            part1 = int(s_square[:i])
            part2 = int(s_square[i:])
            if part2 != 0 and part1 + part2 == n:
                is_kaprekar = True
                break
            i += 1

    if is_kaprekar:
        print(f"{n} is a Kaprekar number.")
    else:
        print(f"{n} is not a Kaprekar number.")


#40: ATM machine simulation.
elif(question_no == 40):
    print("40. ATM machine simulation.")
    balance = 1000.00
    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            print(f"Your current balance is: ${balance:.2f}")
        elif choice == '2':
            while True:
                try:
                    deposit_amount = float(input("Enter amount to deposit: $"))
                    if deposit_amount > 0:
                        balance += deposit_amount
                        print(f"Successfully deposited ${deposit_amount:.2f}. New balance: ${balance:.2f}")
                        break
                    else:
                        print("Deposit amount must be positive.")
                except ValueError:
                    print("Invalid input. Please enter a valid amount.")
        elif choice == '3':
            while True:
                try:
                    withdraw_amount = float(input("Enter amount to withdraw: $"))
                    if withdraw_amount > 0:
                        if balance >= withdraw_amount:
                            balance -= withdraw_amount
                            print(f"Successfully withdrew ${withdraw_amount:.2f}. New balance: ${balance:.2f}")
                            break
                        else:
                            print("Insufficient balance.")
                            break
                    else:
                        print("Withdrawal amount must be positive.")
                except ValueError:
                    print("Invalid input. Please enter a valid amount.")
        elif choice == '4':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")
    print("-" * 30)
else:
    print("Entered question no. does not exist")















    
