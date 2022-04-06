# Codigo de la subasta silenciosa



from art import logo

print(logo)

diccionary = {}
aux = {}
valor = "yes"
while valor == "yes":
    name = input("What is your name?: ")
    bid = input("What's your bid?: ")
    valor = input("Are there any other bidders? Type 'yes' or 'no'. ")
    diccionary[name] = bid


for name in diccionary:
    for name2 in diccionary:
        if diccionary[name] > diccionary[name2]:
            ganador = name
            valor = diccionary[name]
aux[ganador] = valor

for name in diccionary:
    if diccionary[ganador] == diccionary[name]:
        aux[name] = diccionary[name]

print(f"El o los ganadores son:")
for ganadores in aux:
    print(f"{ganadores} con la cantidad de {aux[ganadores]}")