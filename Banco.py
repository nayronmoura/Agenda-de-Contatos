# padrão do array(Json):
# {
#   {
#       nome: 'Nayron'
#       sobrenome: 'Moura'
#       telefones{
#           '999633024',
#           '40028922'
#       }
#       adress:'Romildo dantas de Queiroz'
#   }
#
# }
contact = [['', '', ['', ''], '']]


def checkname(name):
    if len(contact) > 1:
        for c in range(len(contact)):
            if contact[c][0] == name:
                return True
    else:
        return False


def add(name, surname, phones, adress):
    contact.append([name, surname, phones, adress])


def delete(name):
    if len(contact) > 1:
        for c in range(len(contact)):
            if contact[c][0] == name:
                contact.pop(c)


def update(name, newname, newsurname, newphones, newadress):
    if len(contact) > 1:
        for c in range(len(contact)):
            if contact[c][0] == name:
                if newname != "":
                    contact[c][0] = newname
                if newsurname != "":
                    contact[c][1] = newsurname
                if newphones[0] != 0:
                    contact[c][2] = newphones
                if newadress != "":
                    contact[c][3] = newadress
