
print("Welcome to Age App\n")
print("Login Below\n")
name= (input("what is your name : "))
print('\n Welcome {} !!!'.format(name))
def aim():
    age= input("\n what is your age: ")
    aimc = int(age)*365*24*60
    aidc = int(age)*365
    aihc= int(age)*365*24
    print("\n You can have the results in - Days(d), - Hours(h) or - Minutes(m) \n")
    choice = input("Please input d/h/m \n ")
    if(choice=='d'):
        print('You are {} days old'.format(aidc))
    if(choice=='h'):
        print("You are {} hours old".format(aihc))
    if(choice=='m'):
        print('You are {} days old'.format(aimc))

aim() 
print("Are you satisfied with this approximation or you want exact figures")
ans=input("Yes or No ")
if(ans=='Yes'):
    print("Thank you for using our app")
if(ans=='No'):
    Year=input("In what year where you born :")
    Month=input("In what month were you born :")
    Day= input("on what day were you born: ")
    dob= Day+' '+ Month+ ' '+Year 
    print(dob)

