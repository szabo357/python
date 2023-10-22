import string as strs
import random
def generar_pwd(length:int,upper:bool,adddigits:bool,addsimbols:bool)->str:
    try:
        password = []
        lowers  = strs.ascii_lowercase
        uppers  = strs.ascii_uppercase
        digits  = strs.digits
        symbols = strs.punctuation

        if length < 8 or length > 16 :
            raise Exception("Password Length must be between 8 and 16 characters.")
        else:

            for i in range(length):   
            
                if upper == True :
                    i+=1
                    password.append(uppers[ random.randint(0,  len(uppers)-1 )]) 
                else:
                    i+=1
                    password.append(lowers[ random.randint(0,  len(lowers)-1 )])   

                if adddigits == True:
                    i+=1
                    password.append(digits[ random.randint(0,  len(digits)-1 )])
            
                if addsimbols == True:
                    i+=1
                    password.append(symbols[ random.randint(0, len(symbols)-1 )])
            
                if i >= length:
                    return str(password)

    except ValueError:
        print("Error Generating Password")

    return password

# El generador de passwords aun falla, tiene bugs!!
print(generar_pwd(8,False,True,True))