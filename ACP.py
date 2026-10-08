def shut():
    print("Program is shutting down...")

    choice = input("do you want to shutdown? (yes/no): ")

    if choice == "yes":
        shut()

        else:
     print("Program is still running...")