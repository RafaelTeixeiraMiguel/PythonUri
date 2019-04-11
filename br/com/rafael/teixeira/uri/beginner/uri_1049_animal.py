t1 = input()
t2 = input()
t3 = input()

if (t1.lower() == "vertebrado"):
    if (t2.lower() == "ave"):

        if (t3.lower() == "carnivoro"):
            print("aguia")
        elif (t3.lower() == "onivoro"):
            print("pomba")

    elif (t2.lower() == "mamifero"):

        if (t3.lower() == "onivoro"):
            print("homem")
        elif (t3.lower() == "herbivoro"):
            print("vaca")

elif (t1.lower() == "invertebrado"):
    if (t2.lower() == "inseto"):

        if (t3.lower() == "hematofago"):
            print("pulga")
        elif (t3.lower() == "herbivoro"):
            print("lagarta")

    elif (t2.lower() == "anelideo"):

        if (t3.lower() == "hematofago"):
            print("sanguessuga")
        elif (t3.lower() == "onivoro"):
            print("minhoca")