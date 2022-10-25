import random as rand

Start = 144804
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
        "Kasutusi": 5
    },
    {
        "Sihtkoht": "Suur-Ameerika 51a - Lõõtsa 12 - Peterburi tee 92g",
        "Vahemaa": 30,
        "Eesmärk": "Primend konsultatsioon",
        "Kasutusi": 3
    },
    {
        "Sihtkoht": "Peterburi tee 92g - Lastekodu 46 - Peterburi tee 92g",
        "Vahemaa": 25,
        "Eesmärk": "Arvuti transport",
        "Kasutusi": 100
    },
    {
        "Sihtkoht": "Peterburi tee 92g - Lõõtsa 6 - Peterburi tee 92g",
        "Vahemaa": 24,
        "Eesmärk": "Infovara konsultatsioon",
        "Kasutusi": 100
    },
    {
        "Sihtkoht": "Peterburi tee 92g - Paldiski mnt 102 - Peterburi tee 92g",
        "Vahemaa": 34,
        "Eesmärk": "IT varustus",
        "Kasutusi": 100
    },
]
'''
    {
        "Sihtkoht": "Peterburi tee 92g - Ilmatsalu 3b - Suur-Ameerika 51a",
        "Vahemaa": 362,
        "Eesmärk": "Upin IT Konsultatsioon",
        "Kasutusi": 1
    },
'''
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