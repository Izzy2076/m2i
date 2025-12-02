class WrongLoginException(Exception):
    pass

class WrongPasswordException(Exception):
    pass


while True:
    try:
        login = input("Veuillez saisir le login : ")
        if not login.isalpha() or not login.lower():
            raise WrongLoginException("Il ne dois y avoir que des lettres en minuscules dans le login !")
        else:
            break
    except WrongLoginException as error:
        print(error)

while True:
    try:
        password = input("Veuillez saisir le password : ")
        if not password.isdigit():
            raise WrongPasswordException("Le mot de passe ne dois posséder que des nombres !")
        else:
            break
    except WrongPasswordException as error:
        print(error)