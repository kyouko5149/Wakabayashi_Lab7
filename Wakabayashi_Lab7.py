
name = input("Enter your name: ").capitalize()
section = input("Enter your section: ").capitalize()
prelim_grade = float(input("Enter your prelim grade: "))
midterm_grade = float(input("Enter your midterm grade: "))
finals_grade = float(input("Enter your finals grade: "))
finalgrade = (prelim_grade*0.3333) + (midterm_grade*0.3333) + (finals_grade*0.3333)
sumgrade = round(finalgrade)

if (40 <= prelim_grade <= 100) or (40 <= midterm_grade <= 100) or (40 <= finals_grade <= 100):
    if sumgrade >= 75 and sumgrade <= 77:
        print(f"Greetings {name}! Your Final Grade is {sumgrade} and Your GPA: 3.00")
    elif sumgrade >= 78 and sumgrade <= 80:
        print(f"Greetings {name}! Your Final Grade is {sumgrade} and Your GPA: 2.75")
    elif sumgrade >= 81 and sumgrade <= 83:
        print(f"Greetings {name}! Your Final Grade is {sumgrade} and Your GPA: 2.50")
    elif sumgrade >= 84 and sumgrade <= 86:
        print(f"Greetings {name}! Your Final Grade is {sumgrade} and Your GPA: 2.25")
    elif sumgrade >= 87 and sumgrade <= 89:
        print(f"Greetings {name}! Your Final Grade is {sumgrade} and Your GPA: 2.00")
    elif sumgrade >= 90 and sumgrade <= 92:
        print(f"Greetings {name}! Your Final Grade is {sumgrade} and Your GPA: 1.75")
    elif sumgrade >= 93 and sumgrade <= 95:
        print(f"Greetings {name}! Your Final Grade is {sumgrade} and Your GPA: 1.50")
    elif sumgrade >= 96 and sumgrade <= 98:
        print(f"Greetings {name}! Your Final Grade is {sumgrade} and Your GPA: 1.25")
    elif sumgrade >= 99 and sumgrade <= 100:
        print(f"Greetings {name}! Your Final Grade is {sumgrade} and Your GPA: 1.00")
else:
    print("Invalid grade")