from impl_characters import goblin 

def main():
    for i in range(20):
        goblin.goblin.set_randon_action()
        goblin.goblin.exec( 
            goblin.goblin,
            [ goblin.goblin2 ],
        )

        print(goblin.goblin.atbs)
        print(goblin.goblin2.atbs)

        goblin.goblin2.set_randon_action()
        goblin.goblin2.exec( 
            goblin.goblin2,
            [ goblin.goblin ],
        )

        print(goblin.goblin.atbs)
        print(goblin.goblin2.atbs)

if __name__ == "__main__":
    main()
