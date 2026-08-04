import random
numbers = [13, 40, 95, 1, 44, 3, 21, 34, 45, 66, 13, 17]
people = ["Codrin", "Adrian", "John", "Maria", "Tudor", "Maximilian", "Spike"]
picked = random.choice(numbers)

#Creati o functie care returnează: o lista de dicționare, care arată astfel:
#result = { "name": "Codrin", "age": 30, "of_age": True}

def create_list(numbers, people):
    result = []

    for index, name in enumerate(people):
        person = {
            "name": name,
            "age": numbers[index],
            # Unde of_age este true doar daca numărul ales este mai mare de 18 !!
            "of_age": numbers[index] >= 18
        }
        result.append(person)

    return result

print(create_list(numbers, people))

#Creati o altă funcție care filtrează toate persoanele și returnează doar persoanele of_age.
def filtreaza_majori(lista):
    majori = []

    for persoana in lista:
        if persoana["of_age"] == True:
            majori.append(persoana)

    return majori

print(filtreaza_majori(numbers))



#Creați oldest_person, o funcție care returnează cea mai bătrână persoană
#La fel și pentru youngest_person, cea mai tânără

#Printați acel rezultat.