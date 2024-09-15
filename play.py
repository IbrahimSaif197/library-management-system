with open("users.txt", 'r') as f:
    for line in f:
        user = line.split(' ', -1)
        
        print(user)