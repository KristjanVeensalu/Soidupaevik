import random as rand

Start = 142423
Goal_sum = rand.randrange(412, 421, 1)
End = Start + Goal_sum
Traveled = Start

Destinations = [
    {
        "Sihtkoht": "Peterburi tee 92g - Endla 45 - Peterburi tee 92g",
        "Vahemaa": 27,
        "Eesmärk": "Arvuti transport, IT Varustus",
        "Kasutusi": 2
    },
    {
        "Sihtkoht": "Peterburi tee 92g - Endla 46 - Peterburi tee 92g",
        "Vahemaa": 24,
        "Eesmärk": "IT Varustus",
        "Kasutusi": 3
    },
    {
        "Sihtkoht": "Peterburi tee 92g - Rotermanni 7 - Peterburi tee 92g",
        "Vahemaa": 30,
        "Eesmärk": "Bitfiner konsultatsioon",
        "Kasutusi": 2
    },
    {
        "Sihtkoht": "Suur-Ameerika 51a - Lõõtsa 12 - Peterburi tee 92g",
        "Vahemaa": 30,
        "Eesmärk": "Primend konsultatsioon",
        "Kasutusi": 1
    },
    {
        "Sihtkoht": "Peterburi tee 92g - Narva mnt 25 - Suur-Ameerika 51a",
        "Vahemaa": 27,
        "Eesmärk": "Informaatika loeng",
        "Kasutusi": 8
    },
    {
        "Sihtkoht": "Peterburi tee 92g - Lastekodu 46 - Peterburi tee 92g",
        "Vahemaa": 25,
        "Eesmärk": "Arvuti transport",
        "Kasutusi": 100
    },
]

print(Goal_sum)
print("Calculationg for: ", Start, " - ", End, " With step: ", Goal_sum)
print("-" * 50)
stacking = True
DrivenDays = 0


while Traveled <= End:
    RandomIndex = Destinations.index(rand.choice(Destinations))
    Choice = Destinations[RandomIndex]
    if Choice["Kasutusi"] > 0:
        print(Choice["Sihtkoht"], " ", Choice["Eesmärk"])
        print("Odomeetri algnäit: ", Traveled)
        Choice["Kasutusi"] = Choice["Kasutusi"] - 1
        Traveled = Traveled + Choice["Vahemaa"]
        print("Odomeetri lõppnäit: ",Traveled)
        Traveled = Traveled + rand.randrange(3, 7, 1)
        print("-" * 50)
        DrivenDays += 1
print(DrivenDays)