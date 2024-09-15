

# Login System
class LogInSystem:
    def __init__(self, filename="users.txt"):
        self.filename = filename
    def user_SignUp(self):
        input_username = str(input("Enter username: "))
        input_password = str(input("Enter password: "))
        input_name = str(input("Enter name: "))
        input_number = str(input("Enter phone number: "))
        input_gender = str(input("Enter gender (Male/Female): "))
        input_address = str(input("Enter address: "))
        input_email = str(input("Enter email: "))
        
        with open(self.filename, 'a') as f:
            f.write(f'{input_username},{input_password},{input_name},{input_number},{input_gender},{input_address},{input_email},member\n')
            print("Your account has been registered successfully")
    def user_login(self, username, password):
        try:
            with open(self.filename, 'r') as f:
                for line in f:
                    found_username, found_password, *_ = line.split(',')
                    if found_username == username and found_password == password:
                        return True                    
        except FileNotFoundError:
            print("file not found")
        return False

# Admin Functions
class Admin:
    def __init__(self, filename="users.txt"):
        self.filename = filename
    def add_member(self):
        LogInSystem.user_SignUp(self)
    def view_all_members(self):
        print(f"{'Username':<15} {'Name':<20} {'Phone':<12} {'Gender':<10} {'Address':<20} {'Email':<25} {'Role':<10}")
        print("=" * 120)
        try:
            with open(self.filename, 'r') as f:
                for line in f:
                    if not line.strip():
                        continue
                    info_username, info_password, info_name, info_number, info_gender, info_address, info_email, role = line.strip().split(',')
                    if role == 'member':
                        print(f"{info_username:<15} {info_name:<20} {info_number:<12} {info_gender:<10} {info_address:<20} {info_email:<25} {role:<10}")
                    else:
                        continue
            print("=" * 120)
        except FileNotFoundError:
            print("file not found")
    def search_member(self):
        search_key = input("Enter the keyword to search : ").lower()
        print(f"{'Username':<15} {'Name':<20} {'Phone':<12} {'Gender':<10} {'Address':<20} {'Email':<25} {'Role':<10}")
        print("=" * 120)
        try:
            with open(self.filename, 'r') as f:
                for line in f:
                    if not line.strip():
                        continue
                    info_username, info_password, info_name, info_number, info_gender, info_address, info_email, role = line.strip().split(',')
                    if (search_key in info_username.lower() or 
                        search_key in info_password.lower() or 
                        search_key in info_name.lower() or 
                        search_key in info_number.lower() or 
                        search_key in info_gender.lower() or 
                        search_key in info_address.lower() or 
                        search_key in info_email.lower() or 
                        search_key in role.lower()):
                        print(f"{info_username:<15} {info_name:<20} {info_number:<12} {info_gender:<10} {info_address:<20} {info_email:<25} {role:<10}")
                    else:
                        continue
        except:
            print("Nothing was found")