'''2) Take country name as input from user e.g India, australia, us,uk
India 1.1.1.2
uk 1.3.4.5.6.7
us 1.898.98.09.4
australia 3.5.7.8.698.6
'''

#This code will determine the IP address as per country

print("Please input your country name below")
print(" \n")

country=input("What country are you from: ")
if(country=="India"):
    print("Your IP address is " + "1.1.1.2")
    if(country=="UK"):
        print("Your IP address is " + "1.3.4.5")
    if(country=="US"):
        print("Your IP address is " + "1.8.9.8")
    if(country=="Australia"):
        print("Your IP address is "+ "3.5.7.8")
else:
    print("Sorry we do not recognise your country")
