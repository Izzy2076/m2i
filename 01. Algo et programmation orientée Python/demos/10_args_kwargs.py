def demo_args_kwargs(*args, **kwargs):
    print("Args : ", args) # => tuple
    print("kwargs : ", kwargs) # => clé : valeur
    for key, value in kwargs.items():
        print(f"{key} = {value}")

demo_args_kwargs(10, 20, 30 ,50, "test", nom="toto", age=25, email="toto@email.fr")