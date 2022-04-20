import Banco as banco
from time import sleep


def mostrar():
    if len(banco.contact) > 1:
        for c in range(1, len(banco.contact)):
            print(f'\n'
                  f'-------Contato {c}-------\n'
                  f'Nome:{banco.contact[c][0]}\n'
                  f'Sobrenome:{banco.contact[c][1]}\n'
                  f'telefones:{banco.contact[c][2]}\n'
                  f'endereço: {banco.contact[c][3]}\n'
                  f'----------------------\n')
            sleep(1)
    else:
        print("Você não adicionou nenhum contato.")
        sleep(1)


def adicionar():
    phones = []
    while True:
        name = str(input("Nome: "))
        if banco.checkname(name):
            print('contato já existe, tente novamente')
        else:
            break
    surname = str(input("Sobrenome: "))

    while True:
        phone = int(input("Telefone: "))
        phones.append(phone)
        condicao = input("Deseja Adicionar mais um?[S ou N]").upper()
        if condicao == "N":
            break

    adress = input("Endereço: ")
    banco.add(name, surname, phones, adress)


def remover():
    name = str(input("Nome: "))
    if banco.checkname(name):
        check = str(input("Deseja realmente apagar? [S or N]")).upper()
        if check == 'S':
            banco.delete(name)
    else:
        print("Esse nome não consta na nos contatos.")


def mudar():
    name = str(input("Nome: "))
    newname = newsurname = newadress = ""
    newphones = []
    if banco.checkname(name):
        if input("Deseja alterar o nome e sobrenome? [S ou N] ").upper() == "S":
            while True:
                newname = str(input("Nome: "))
                if banco.checkname(newname):
                    print("Esse contato já existe")
                else:
                    newsurname = str(input("Sobrenome: "))
                    break
        if input("Deseja alterar os telefones?[S ou N] ").upper():
            while True:
                phone = int(input("Telefone: "))
                newphones.append(phone)
                if input("Deseja Adicionar mais um?[S ou N] ").upper() == 'N':
                    break
        if input("Deseja alterar o endereço?[S ou N] ").upper():
            newadress = str(input("Endereço: "))

        banco.update(name, newname, newsurname, newphones, newadress)

    else:
        print("Esse nome não consta na nos contatos.")
