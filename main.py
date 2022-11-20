from src.impl.characters import goblin
from src.impl.characters import gnoll
from src.impl.characters import goblin_boss

def printf(c):
    # print(c)
    pass

def main():
    goblin1 = goblin_boss.create()
    goblin2 = gnoll.create()

    ganhadores = []
    for _ in range(100000):
        goblin1 = goblin_boss.create()
        goblin2 = gnoll.create()
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

        win = 1 if goblin1.heath.is_alive() else 2
        ganhadores.append(win)

        printf(f" #######################")
        printf(f" ## VENCEDOR: {win} ####")
        printf(f" #######################")

    win_1 = ganhadores.count(1) 
    win_2 = ganhadores.count(2) 
    print(win_1)
    print(win_2)
    print(f'{win_1 / (win_1+win_2)} / {win_2 / (win_1+win_2)}')

if __name__ == "__main__":
    main()
