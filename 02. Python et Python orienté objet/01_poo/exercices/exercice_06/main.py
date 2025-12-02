from classes.Employe import Employe
from classes.Manager import Manager
from classes.Technicien import Technicien

emp1 = Employe("emp1", 1500.0)
emp2 = Employe("emp2", 1700.0)
emp3 = Employe("emp3", 2700.0)

manager = Manager("Manager", 3000.0, [emp1, emp2, emp3])
technicien = Technicien("technicien", 2800.0, "Réseau")

print(emp1.presentation())
emp1.augmenter_salaire(10)
print(emp1.presentation())

manager.ajouter_employe(technicien)
print(manager.presentation())

print(technicien.presentation())
technicien.changer_specialite("dev")
print(technicien.presentation())

def filtre_role(equipe, role: Technicien | Manager):
    return [emp.nom for emp in equipe if isinstance(emp, role)]

print(filtre_role(manager.equipe, Technicien))