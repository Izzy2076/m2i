from classes.Bus import Bus

bus1 = Bus(123456, 40)
bus2 = Bus(85465)
bus3 = Bus(166)

Bus.afficher_statistiques()
Bus.modifier_tarif(1.6)
Bus.modifier_capacite(60)
Bus.afficher_statistiques()

bus1.retirer_passager(30)
bus1.ajouter_passager(20)
