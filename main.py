from app import *

def main():
    user = LogInSystem()
    admin = Admin()
        
    while True:
        print("1. Sign up")
        print("2. Login")
        print("3. Exit")
        choice = int(input("Choose an option: "))

        if choice == 1:
            admin.search_member()
        
        elif choice == 2:
            input_username = str(input("Enter username: "))
            input_password = str(input("Enter password: "))
            if user.user_login(input_username, input_password):
                print("Login Successful!")
            else:
                print("Login Failed!")
        
        elif choice == 3:
            break
        
        else:
            print("Invalid choice!")

main()
    
