import random
#declaration d'une fonction objective
def foo (x,y,z):
    return 6*x**3+9*y**2+90*z-25
#calcul de fitnesse
def fitness(x,y,z):
    ans = foo(x,y,z)
    if ans ==0 :
        return 9999
    else:
        return abs(1/ans)
# declaration d'un vecteur qui contient population
solutions = []
#ajouter 1000 reels entre 0 et 9999 d'une façon aléatoire dans notre vecteur
for s in range (1000):
    solutions.append( (random.uniform(0,10000),
                      random.uniform(0,10000),
                      random.uniform(0,10000)))


print(solutions[:5])
# trier les fitnesses des reels du solutions dans rankedsolution du plus meilleur au moins
for i in range (10000):
    rankedsolutions=[]

    for s in solutions:
            rankedsolutions.append((fitness(s[0],s[1],s[2]),s))
#trier
    rankedsolutions.sort()
#inverser la resultat de trie
    rankedsolutions.reverse()

    print(f" == Gen {i} best Solution ===")
    print(rankedsolutions[0])
# ne pas dépasser la taille du vecteur
    if rankedsolutions[0][0] > 999 :
        break
#affecter les 100 meilleurs solutions dans 'bestsolution'
    bestsolution = rankedsolutions[:100 ]

    elemnts=[]

    for s in bestsolution:
        elemnts.append(s[1][0])
        elemnts.append(s[1][1])
        elemnts.append(s[1][2])

        newGen=[]
        for _ in range(1000):
            e1=random.choice(elemnts) * random.uniform(0.99,1.01)
            e2=random.choice(elemnts) * random.uniform(0.99,1.01)
            e3=random.choice(elemnts) * random.uniform(0.99,1.01)

            newGen.append((e1,e2,e3))
        solutions = newGen

