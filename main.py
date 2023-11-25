from Veiculo import Carro, Mota, Bicicleta

#vamos criar uma lista de veiculos
frota = []
#vamos criar um veiculo de cada tipo
a = Carro()
b = Carro()
c = Carro()
d = Mota()
e = Mota()
f = Bicicleta()
g = Bicicleta()

frota.append(a)
frota.append(b)
frota.append(c)
frota.append(d)
frota.append(e)
frota.append(f)
frota.append(g)


if __name__ == '__main__':
    # vamos criar um for para percorrer a lista de frota
    for v in frota:
        v.display()

    # Menu de opções
    flag = True
    while flag:
        match(input()):
            case "1":
                print("Hello")
                break
            case "2":
                flag = False
                break


