import sys


# provjera jel susjedi imaju razlicite boje
def provjeraBoja(graf, boja, n):
    for i in range(n):
        for j in range(i + 1, n):
            if j in graf.get(i) and boja.get(i) == boja.get(j):
                return False
    return True


def bojanjeGrafa(graf, n, i, boja):
    # dosli smo do zadnjeg vrha
    if i == n:
        # ako se moze obojati vrati 1
        if provjeraBoja(graf, boja, n):
            return 1
        return 0

    # dodjela boja vrhovima, od 1 do 4
    for j in range(1, 5):
        boja.update({i: j})
        if bojanjeGrafa(graf, n, i + 1, boja):
            return 1
        boja.update({i: 0})
    return 0


def main():
    file_name = sys.argv[1]
    f = open(file_name, 'r')
    i = 0
    n = 0
    matrica = []
    for line in f.readlines():
        if line == '\n':
            continue
        if i == 0:
            n = int(line.strip())
        else:
            v1 = line.split(' ')
            v1 = [int(x) for x in v1]
            matrica.append(v1)
        i += 1
    bridovi = {}
    for i in range(len(matrica)):
        for j in range(len(matrica[i])):
            if matrica[i][j] == 1:
                if i in bridovi.keys():
                    susjedi = bridovi.get(i)
                else:
                    susjedi = set()
                susjedi.add(j)
                bridovi.update({i: susjedi})

    boje = {}
    if bojanjeGrafa(bridovi, n, 0, boje) == 1:
        print(1)
        # print(boje)
    else:
        print(0)


main()
