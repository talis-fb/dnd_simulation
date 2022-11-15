import impl_characters.goblin as goblin

def printf(c):
    # print(c)
    pass

def main():
    goblin1 = goblin.create()
    goblin2 = goblin.create()

    ganhadores = []
    for _ in range(500000):
        goblin1 = goblin.create()
        goblin2 = goblin.create()
        while(goblin1.heath.is_alive() and goblin2.heath.is_alive()):
            printf(f" -------- PRIMEIRO -------")
            goblin1.set_randon_action()

            printf(f" >>> Ação: {type(goblin1.current_action).__name__}")
            goblin1.exec([ goblin2 ])

            if goblin1.current_action.success:
                printf(f" >>> SUCESSO -> {goblin1.current_action.result}")
            else:
                printf(f" {goblin1.current_action.result}")

            ### --------------
            printf(f" -------- SEGUNDO -------")
            goblin2.set_randon_action()

            printf(f" >>> Ação: {type(goblin2.current_action).__name__}")
            goblin2.exec([ goblin1 ])

            if goblin2.current_action.success:
                printf(f" >>> SUCESSO -> {goblin2.current_action.result}")
            else:
                printf(f" {goblin2.current_action.result}")

            printf(f" *** STATUS *** ")
            printf(f"\tHP 1: {goblin1.heath.hp}")
            printf(f"\tHP 2: {goblin2.heath.hp} \n")

        win = 1 if not goblin1.heath.is_alive() else 2
        ganhadores.append(win)

        printf(f" #######################")
        printf(f" ## VENCEDOR: {win} ####")
        printf(f" #######################")

    # printf(ganhadores)
    ganhadores.sort()
    # printf(ganhadores)
    print(ganhadores.count(1))
    print(ganhadores.count(2))

if __name__ == "__main__":
    main()
