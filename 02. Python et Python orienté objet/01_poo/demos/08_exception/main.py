class NombreInvalideException(Exception):
    pass

while True:
    try:
        nb = int(input("Veuillez saisir un nombre entre 1 et 20 : "))

        if nb < 1 or nb > 20:
            raise NombreInvalideException("le nombre doit être entre 1 et 20 !")
        else:
            break
    except ValueError as e:
        print(e)
    except NombreInvalideException as e:
        print(e)
    except Exception as error:
        print(error)


