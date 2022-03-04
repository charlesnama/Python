#This code is your Facebook Login Page


print("Welcome to Facebook\n")
print("Login below\n")
Username=input("Username: ")
Password=input("Password: ")
Entry_command=input("Please type 'Enter' if you have verified your login credentials:\n")

if(Entry_command=="Enter"):
    print("Loading------->")
    if(Username=="Charles" and Password!="CAN"):
        print("Hi Charles, please verify your password again")
        Password=input("Password: ")
    if(Username=="Charles" and Password=="CAN"):
        print("Welcome back Charles, good to see you!")
    if(Username!="Charles"):
        #print("Please click on the link below to Sign Up")
        print("Please input 'Yes'below to create an account")
        New_Account=input("Want to create a new account?: \n")
        if(New_Account=="Yes"):
            print("Let's go!")
            print(" \n")
            First_Name=input("First Name:")
            Last_Name=input("Last Name:")
            Full_name=(First_Name + " " + Last_Name)
            Year_of_Birth=int(input("Year of Birth:"))
            Birth_Month=input("Month of Birth:")
            Birth_Date=input("Day of Birth:")
            Date_of_Birth=("%s %s %s"%(Birth_Date,Birth_Month,Year_of_Birth))
            Current_year=2019
            current_age=(int(Current_year) - int(Year_of_Birth))
            if(Year_of_Birth> 1989):
                print("Sorry, you are born on %s making you %s"% (Date_of_Birth,current_age))
                print("You are not eligible to join this platform")
            else:
                print("Welcome to Facebook %s" % Full_name)
        else:
            print("Thanks for stopping by, see you next time!")







 

