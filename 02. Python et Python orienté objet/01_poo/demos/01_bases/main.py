from classes.Chien import Chien

rex = Chien(nom="rex", race="Berger allemand", age=12)
toto = Chien(nom="toto", race="Berger suisse", age=5)
chien = Chien("test", 15)

rex.aboyer()
toto.aboyer()

toto.aboyer_sur(rex)
rex.aboyer_sur(toto)
toto.aboyer_sur(toto)