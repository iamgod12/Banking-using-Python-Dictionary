#%reload_ext nb_black
import random #for random number generator
import string #to string.digits

ch = """  
    Press 1: To create account
    Press 2: To check balance
    Press 3: To deposit
    Press 4 To withdraw
    Press 5 To exit
"""
print(ch) #print choices
users = [] # empty list for holding values


def rannumber(): # function to generate random number
    return "".join(random.choices(string.digits, k=5)) 
# "" to combine number without space
#.join to join them and random. choices pic any number from string.digits of length 5 

def view(): # function to print details of account
    n = input("Please Enter Your Account Number: ") # ask user acc number
    found = False # initialize flag with false
    for i in users: # loop in users where all the name,amount and acc number are stored 
        if i["no"] == n: #if acc number match with in dict. account number section 
            found = True # flah become true and procced
            print("Welcome back {}!!!\n".format(i["naam"])) #print name 
            print("Your Acc Bal:", i["am"]) #print acc number
    if found == False: # if flag become false
        print("No user exists with this Account Number: ") #display 


def dip(): # function to deposite amount in account
    found = False
    n = input("Please Enter Your Account Number: ")

    for i in users:
        if n == i["no"]:
            found = True
            print("Welcome back {}!!!\n".format(i["naam"]))
            paise = int(input("Enter amount to deposit: ")) # ask user to enter amount 
            print("Your account credited with: {}, Cureent balance: {}".format(paise, int(i["am"]) + paise))
            # convert string i["am"] to integer and then add with the amount entered
    if found == False:
        print("No user exists with this Account Number: ")


def deb(): #with draw from account
    found = False
    n = input("Please Enter Your Account Number: ")
    for i in users:
        if n == i["no"]: # run if account exits
            found = True
            print("Welcome back {}!!!\n".format(i["naam"]))
            paise = int(input("Enter amount to Withdraw: "))
            if int(i["am"]) > paise: # if entered amount is more than the balance
                print("No Sufficient Balance") #display insuffecient balance
            
            print("Your account debited with: {}, Cureent balance: {}".format(paise, int(i["am"]) - paise)) 
            # else withdraw from saving 
    if found == False:
        print("No user exists with this Account Number: ")


while True:
    ch = input("Enter Your Choice: ")
    if ch == "1":
        name = input("Enter Your Name: ")
        amount = input("Enter Initial Amount: \n")
        a = rannumber() # calling random function
        data = {"naam": name, "am": amount, "no": a}
        users.append(data) # add data to the dict. like name, initial money , and acc number
        print("Dear {},Yours Account Created Successfully, Acc No: {}".format(name, a),"\n",)
    elif ch == "2":
        view() # calling view function
    elif ch == "3":
        dip() # calling deposite function
    elif ch == "4":
        deb() # calling withdraw function
    elif ch == "5":
        break # program will stop if enter 5
    else:
        print("invalid Choice")
