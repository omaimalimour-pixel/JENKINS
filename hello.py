import sys
print("=" * 40)
print("Bienvenue dans mon premier job Jenkins !")
print("=" * 40)

if len(sys.argv) > 1:
    nom = sys.argv[1]
else:
    nom = "Etudiant Jenkins"

print(f"Bonjour {nom}, ton job Jenkins a reussi !")
a, b = 10, 5
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")

assert a + b == 15, "Le test a echoue !"
print(" [OK] Tous les tests passent avec succès")