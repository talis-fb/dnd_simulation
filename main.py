import impl_characters.goblin as goblin

def main():
    goblin1 = goblin.create()
    goblin2 = goblin.create()

    while(goblin1.atbs.hp > 0 and goblin2.atbs.hp>0):
        print(f" TURNO DO PRIMEIRO -------")
        goblin1.set_randon_action()

        print(f" >>> Ação: {type(goblin1.current_action).__name__}")
        goblin1.exec([ goblin2 ])

        if goblin1.current_action.success:
            print(f" >>> SUCESSO -> {goblin1.current_action.result}")
        else:
            print(f" {goblin1.current_action.result}")

        ### --------------
        print(f" TURNO DO 2 -------")
        goblin2.set_randon_action()

        print(f" >>> Ação: {type(goblin2.current_action).__name__}")
        goblin2.exec([ goblin1 ])

        if goblin2.current_action.success:
            print(f" >>> SUCESSO -> {goblin2.current_action.result}")
        else:
            print(f" {goblin2.current_action.result}")

        print(f" *** STATUS *** ")
        print(f"\tHP 1: {goblin1.atbs.hp}")
        print(f"\tHP 2: {goblin2.atbs.hp} \n")

    win = 1 if goblin1.atbs.hp > 0 else 2

    print(f" __VENCEDOR: {win} ___")

if __name__ == "__main__":
    main()
