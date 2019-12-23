# Dictionary of pin and balance of customers
userpin = {"sid":1234, "shubham":2345, "deepa": 3456, "karan": 4567,"harshada":5678,"harshada":6789}
userbal = {"sid":50000, "shubham":20000, "deepa": 5000, "karan": 10000,"harshada":65446,"harshada":900000}
usercur = {"sid":57000, "shubham":40000, "deepa": 500, "karan": 90000,"harshada":46432,"harshada":9867}
useremail ={"sid":'sid913893@gmail.com', "shubham":'Shubham17063@gmail.com', "deepa":'Deepa17063@gmail.com',
            "karan":'karan17063@gmail.com',"harshada":'harshushinde41@gmail.com',"harshada":'harshushinde83@gmail.com' }
# Cash deposition of ATM
print("----------Cashier cash deposition----------\n")
amt2000 = int(input("Enter number of 2000 rupee notes to be filled: "))
amt500 = int(input("Enter number of 500 rupee notes to be filled: "))
amt100 = int(input("Enter number of 100 rupee notes to be filled: "))
amttotal = amt2000*2000 + amt500*500 + amt100*100
print("Total amount in ATM is Rs. {0}\n".format(amttotal))

# Start ATM code here
print("----------WELCOME TO BANK OF RAIT----------\n")
n='machinehackers@1999'

##### import os
import os
import smtplib
import math, random 
# EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
# EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

try:
    f=1
    while f==1:

        # function to generate OTP 
        def generateOTP() : 
            digits = "0123456789"
            OTP = "" 

            for i in range(4) : 
                OTP += digits[math.floor(random.random() * 10)] 
            return OTP 

        #print("OTP of 4 digits:", generateOTP()) 
        gen=int(generateOTP())
        
        
        name=input("ENTER YOUR NAME: ")
        while name not in userpin.keys():   
            name=input("ENTER YOUR CORRECT NAME: ")
        pin=int(input("ENTER YOUR PIN: "))
        while pin != userpin[name]:
            pin=int(input("ENTER YOUR CORRECT PIN: "))
        
        with smtplib.SMTP("smtp.gmail.com",587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
    
            smtp.login('mlclan213a@gmail.com', n)
    
            subject = 'ONE TIME PASSWORD'
            body = int(gen)
            msg = f'Subject: {subject}\n\n{body}'
    
            smtp.sendmail('mlclan213a@gmail.com', useremail[name], msg)
    
    
        otp=int(input("ENTER THE OTP: "))
        if gen == otp:
            s = int(input("Choose your account type: \n 1)Saving account \n 2) Current account \n 3) PIN Chance\n"))

            if s==1:
                op = int(input("Choose the follow oparation \n 1) DEPOSIT money \n 2) BALANCE CHECK \n 3) Withdraw money \n"))
                if op==1:
                    am2000 = int(input("Enter number of 2000 rupee notes to be filled: "))
                    am500 = int(input("Enter number of 500 rupee notes to be filled: "))
                    am100 = int(input("Enter number of 100 rupee notes to be filled: "))
                    amt2000=am2000 + amt2000
                    amt500=am500 + amt500
                    amt100=am100 + amt100
                    amtotal = am2000*2000 + am500*500 + am100*100
                    n= userbal[name]
                    userbal[name]=amtotal+n
                elif op==2:
                    print("--------------------------------------------------------")
                    print("       BALANCE RECEIPT     ")
                    print("YOUR CURRENT BALANCE IS: ",userbal[name])
                    print("--------------------------------------------------------") 
                elif op==3:
                    mny=float(input("ENTER THE AMOUNT: "))
                    if mny < amttotal:
                        if mny < userbal[name] and mny<=10000 :
                            n= userbal[name]
                            userbal[name]=n-mny
                        else:
                            if mny <=10000:
                                print("YOUR BALANCE LIMIT IS: ",userbal[name])
                            else:
                                print("LIMIT TO WITHDRAW THE AMOUNT IS 10K")
                    else:
                        print("we dont have money")
            elif s==2:
                op = int(input("Choose the follow oparation \n 1) DEPOSIT money \n 2) BALANCE CHECK \n 3) Withdraw money \n"))
                if op==1:
                    am2000 = int(input("Enter number of 2000 rupee notes to be filled: "))
                    am500 = int(input("Enter number of 500 rupee notes to be filled: "))
                    am100 = int(input("Enter number of 100 rupee notes to be filled: "))
                    amt2000=am2000 + amt2000
                    amt500=am500 + amt500
                    amt100=am100 + amt100
                    amtotal = am2000*2000 + am500*500 + am100*100
                    n= usercur[name]
                    usercur[name]=amtotal+n
                elif op==2:
                    print("--------------------------------------------------------")
                    print("       BALANCE RECEIPT     ")
                    print("YOUR CURRENT BALANCE IS: ",usercur[name])
                    print("--------------------------------------------------------") 
                elif op==3:
                    mny=float(input("ENTER THE AMOUNT: "))
                    if mny < amttotal:
                        if mny < usercur[name]:
                            n= usercur[name]
                            usercur[name]=n-mny
                        else:
                            print("YOUR BALANCE LIMIT IS: ",userbal[name])
                    else:
                        print("we dont have money")
            elif s==3:
                pin1= int(input("ENTER YOUR PIN: "))
                if pin1 == userpin[name]:
                    pin2=int(input("ENTER YOUR NEW PIN: "))
                    userpin[name]=pin2
            else:
                print("ENTER THE CORRECT NUMBER")
        else:
            print("try again")
except KeyboardInterrupt:
    print("SAVING ACCOUNT BALANCE IS: ",userbal)
    print("CURRENT ACCOUNT BALANCE IS: ",usercur)   
