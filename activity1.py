medical_cause = input("Did you have any medical cause? (Y/N): ").strip().upper()
if medical_cause == 'Y':
    print("You are allowed to give the exam.")
else:
    attendance = int(input("Enter your attendance"))
    if attendance >= 75:
        print("You are allowed to give the exam.")
    else:
        print("You are not allowed to give the exam.")
        