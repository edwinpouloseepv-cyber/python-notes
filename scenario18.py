age = int(input("Enter age: "))
graduation = input("Have you graduated? (yes/no): ")
banned = input("Are you banned? (yes/no): ")
if banned == "yes":
    banned = True
else:
    banned = False

if age >= 21 and graduation == "yes" and not banned:
    print("You are eligible for the job.")
else:
    print("You are not eligible for the job.")