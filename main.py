import impl_characters.goblin as goblin

def main():
    goblin1 = goblin.create()
    goblin2 = goblin.create()

    for i in range(10):
        while(not goblin1.heath.is_dead() and not goblin2.heath.is_dead()):
            print(f" -------- PRIMEIRO -------")
            goblin1.set_randon_action()

            print(f" >>> Ação: {type(goblin1.current_action).__name__}")
            goblin1.exec([ goblin2 ])

            if goblin1.current_action.success:
                print(f" >>> SUCESSO -> {goblin1.current_action.result}")
            else:
                print(f" {goblin1.current_action.result}")

            ### --------------
            print(f" -------- SEGUNDO -------")
            goblin2.set_randon_action()

            print(f" >>> Ação: {type(goblin2.current_action).__name__}")
            goblin2.exec([ goblin1 ])

            if goblin2.current_action.success:
                print(f" >>> SUCESSO -> {goblin2.current_action.result}")
            else:
                print(f" {goblin2.current_action.result}")

            print(f" *** STATUS *** ")
            print(f"\tHP 1: {goblin1.heath.hp}")
            print(f"\tHP 2: {goblin2.heath.hp} \n")

        win = 1 if not goblin1.heath.is_dead() else 2

        # print(f" __VENCEDOR: {win} ___")

if __name__ == "__main__":
    main()
