from src.impl.characters import goblin
from src.impl.characters import gnoll
from src.impl.characters import goblin_boss
from src.game.game import Game
import time

def main():

    ganhadores = []
    game = Game(goblin_boss.create, gnoll.create)

    times = 100
    for i in range(times):
        game.restart_game()
        while(not game.is_finished):
            game.next_turn()
            game.validate_turn()
            game.run_turn()
            game.log_turn_results()
            # time.sleep(0.20)
            # print(game.results)
            print(f'[{game.attacker.summary.name}]')
            print(f'{game.last_roll} => {game.results}   ||   {game.attacker.heath.hp}, {game.defender.heath.hp} \n')

        print('--------------------------------------------------------------------------------------------------')

        ganhadores.append(game.get_game_results()["winner"])
        game.log_game_results()

    win_1 = ganhadores.count('Chefe Goblin')
    win_2 = ganhadores.count('Gnoll') 
    print(win_1)
    print(win_2)
    print(len(ganhadores))
    print(f'{win_1 / (win_1+win_2)} / {win_2 / (win_1+win_2)}')

if __name__ == "__main__":
    main()
