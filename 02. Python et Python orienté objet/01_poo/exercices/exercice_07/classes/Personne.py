class Personne:
    def __init__(self, prenom, tel, email):
        self._prenom = prenom
        self._tel = tel
        self._email = email

    @property
    def prenom(self):
        return self._prenom

    @prenom.setter
    def prenom(self, value):
        if isinstance(value, str):
            self._prenom = value
        else:
            raise ValueError

    @property
    def tel(self):
        return self._tel

    @tel.setter
    def tel(self, value):
        if isinstance(value, str):
            self._tel = value
        else:
            raise ValueError

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if isinstance(value, str):
            self._email = value
        else:
            raise ValueError
        
    def __str__(self):
        return f"Nom : {self.prenom}, email : {self.email}, tel : {self.tel}"
