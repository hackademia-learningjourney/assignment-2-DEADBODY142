import json 
#try opening file in read mode and load the file in dict_login
try:
    with open('signup.json', 'r') as file:
        dict_login = json.load(file)
#if file is not found, initialize empty dict_login 
except:
    dict_login={
        'username':[],
        'password':[],
        'mobile_number':[]
    }
while True:
    print('--'*10)
    choice=int(input("Enter your choice: \n1. Sign in\n2. Sign up\n3. Exit\n"))

    if choice==1:
        username = input("Enter username: ")
        password = input("Enter password: ")
        mobile_number = input("Enter mobile number: ")
        dict_login['username'].append(username)
        dict_login['password'].append(password)
        dict_login['mobile_number'].append(mobile_number)
        with open('signup.json','w') as f:
            json.dump(dict_login,f)
        
    elif choice==2:
        username = input("Enter username: ")
        password = input("Enter password: ")
        try:
            index=dict_login['username'].index(username)
            if dict_login['password'][index]==password:
                print("Logged in successfully your number is "+dict_login['mobile_number'][index])
            else:
                print("Password incorrect")
        except:
            print("Invalid credentials")
            
    elif choice==3:
        break

