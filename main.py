from src.impl.characters import goblin
from src.impl.characters import gnoll
from src.impl.characters import goblin_boss
from src.game.game import Game
import time

def print_roll(character, hp, result):
    print(f'[{character} / {hp}] => {result}')
    pass

def printf(c):
    print(c)
    pass

def main():

    ganhadores = []
    game = Game(
        goblin_boss.create,
        gnoll.create,
    )

    times = 100
    for _ in range(times):
        game.restart_game()
        while(not game.is_finished):
            game.next_turn()
            game.validate_turn()
            game.run_turn()
            game.log_turn_results()
            # time.sleep(0.20)
            # print_roll(game.attacker.summary.name, game.attacker.heath.hp, game.results)
            # printf(f'[{game.attacker.summary.name}]')
            # printf(f'{game.last_roll} => {game.results}   ||   {game.characters[0].heath.hp}, {game.characters[1].heath.hp} \n')


        win = game.get_game_results()["winner"]
        # printf("\nWINNER")
        # printf(win)
        # printf(game.get_game_results())
        ganhadores.append(win)
        game.log_game_results()
        # printf('--------------------------------------------------------------------------------------------------')

    win_goblin = ganhadores.count('Chefe Goblin')
    win_gnoll = ganhadores.count('Gnoll       ') 
    print(f'GOBLIN: {win_goblin}   {win_goblin / (win_goblin+win_gnoll)}')
    print(f'GNOLL:  {win_gnoll}   {win_gnoll / (win_goblin+win_gnoll)}')
    print(len(ganhadores))

if __name__ == "__main__":
    main()
