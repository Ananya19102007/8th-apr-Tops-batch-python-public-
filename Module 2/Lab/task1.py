#banking system
def acopening(*acdata):
    print("Account Number: ",acdata[0])
    print("Account Holder Name: ",acdata[1])
    print("Account Type: ",acdata[2])

accno=input("Enter account number: ")
acchn=input("Enter the Account holder's name: ")
acct=input("Enter the Account type: ")

acopening(accno,acchn,acct)

#===================================================
dep=int(input("Enter the deposit amt: "))
def deposits():
    global dep
    if dep<2000:
        print("Error the minimum deposit amt is 2000")
    else:
        print("successful")
    
deposits()
if dep<2000:
    bal=+dep

#=======================================================

def withdraw():
    amt=int(input("Enter the amount to be withdrawn: "))
    return amt

a=withdraw()
print(a)
bal=bal-a
#========================================================

def statement():
    global accno,acchn,acct
    print("Account Number: ",accno)
    print("Account Holder's Name: ",acchn)
    print("Account Type: ",acct)
    print("Balance: ",bal)

statement()
