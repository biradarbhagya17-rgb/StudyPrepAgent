
# Study Preparation Agent

print("📚 Welcome to Study Prep Agent!")

subject = input("Enter your subject: ")
hours = input("How many hours can you study today? ")

if hours.isdigit() and int(hours) > 0:
    hours = int(hours)

    print("\nYour study plan for", subject)
    print("1. Learn concepts:", hours // 2, "hour(s)")
    print("2. Practice questions:", hours // 4, "hour(s)")
    print("3. Revise important topics:", hours - (hours // 2) - (hours // 4), "hour(s)")

else:
    print("Please enter a valid number of hours.")
    hours = 0

if hours > 0:
    print("\nPractice Question")

    if subject.lower() == "python":
        print("What is the purpose of a Python function?")
        answer = input("Your answer: ").lower()

        if "reuse" in answer or "task" in answer:
            print("Correct! Functions help organize and reuse code.")
        else:
            print("Review Python functions and try again.")

    elif subject.lower() == "java":
        print("Which keyword is used to create a class in Java?")
        answer = input("Your answer: ").lower().strip()

        if answer == "class":
            print("Correct!")
        else:
            print("Incorrect. The answer is 'class'.")

    else:
        print("Write five questions from your", subject, "syllabus.")
        print("Answer them without looking at your notes.")

print("\nKeep practicing every day. Good luck!")
