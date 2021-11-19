import sys


def nadiSveLance(bridovi, trenutni, posjeceno, sviPutovi):
    posjeceno.append(trenutni)
    if trenutni in bridovi.keys():
        for vrh in bridovi.get(trenutni):
            if vrh not in posjeceno:
                nadiSveLance(bridovi, vrh, posjeceno.copy(), sviPutovi)
    sviPutovi.append(posjeceno)


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

    sviLanci = []
    for vrh in bridovi.keys():
        nadiSveLance(bridovi, vrh, [], sviLanci)

    najveciLanac = 0
    for lanac in sviLanci:
        duljina = len(lanac) - 1
        if duljina > najveciLanac:
            najveciLanac = duljina

    print(najveciLanac)


main()
