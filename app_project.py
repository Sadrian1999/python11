
#I. Főmenü - követelmények
#A felhasználó eldönti hogy regisztrál vagy belép.
#1-Bejelentkezés
#2-Regisztráció
#Mit szeretne csinálni?
#input

print("1 - Bejelentkezés")
print("2 - Regisztráció")
print("3 - Elfelejtett jelszó")
print("Válasszon a megadott opciók közül!")
user_input : int = int(input())
user_question : str = ""
user_answer : str = ""
db_username : str = "userone"
db_password : str = "bestpass"
db_security_q : str = "Mi volt az első háziállatod neve?"
db_security_a : str = "Bodri"

def password_redeem_email():
    email_address : str = "xd@xd.com"
    new_password : str = "asd456"
    send_email(new_password)
    
def send_email(password : str):
    pass


if user_input == 1: # login
    print("Bejentkezés")
    print("Username: ")
    username : str = input()
    print("Password: ")
    password : str = input()
    if username == db_username and password == db_password:
        print("Sikeres belépés!")
    else:
        print("Sikertelen belépés")
elif user_input == 2: #register
    print("Regisztráció")
    print("Username: ")
    username : str = input()
    print("Password: ")
    password : str = input()
    print("Password újra:")
    password_again : str = input()
    if password == password_again:
        print("Válassz egy biztonsági kérdést")
        print("1 - Mi volt az első háziállatod neve?")
        print("2 - Mi a kedvenc szined?")
        security_q_number : int = int(input())
        if security_q_number == 1:
            user_question = "Mi volt az első háziállatod neve?"
            user_answer = input()
        elif security_q_number == 2:
            user_question = "Mi a kedvenc szined?"
            user_answer = input()
        else:
            print("Hibás kérdésszám, kilépés...")
    else:
        print("Hibás jelszó, kilépés...") 
elif user_input == 3:
    print("Add meg a felhasználó neved:")
    username : str = input() 
    password_redeem_email()
else:
    print("Rossz billentyű lett leütve, program leáll ...")


#jobb megoldás
