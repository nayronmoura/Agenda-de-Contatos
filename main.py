import Controle

while True:
    print('\n'
          '    -------> Menu <-------\n'
          '    [1] Monstrar contatos;\n'
          '    [2] Adicionar Contato;\n'
          '    [3] Remover;\n'
          '    [4] Modificar.\n'
          '    ----------------------\n'
          '    ')
    chose = int(input("opção: "))
    if 4 >= chose > 0:
        match chose:
            case 1:
                Controle.mostrar()
            case 2:
                Controle.adicionar()
            case 3:
                Controle.remover()
            case 4:
                Controle.mudar()

    else:
        print("Insira um valor válido.")
