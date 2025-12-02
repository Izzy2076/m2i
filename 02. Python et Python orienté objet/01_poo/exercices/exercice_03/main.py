from classes.WaterTank import WaterTank

wt1 = WaterTank(1000.0, 500.0, 50.0)
wt2 = WaterTank(1500.0, 1000.0, 550.0)

print(f"Niveau total : {WaterTank.all_watertanks}L")

wt1.remplir(300.0)
print(f"Niveau total : {WaterTank.all_watertanks}L")

print(wt1.poids_total())
wt1.vider(400.0)
print(f"Niveau total : {WaterTank.all_watertanks}L")

