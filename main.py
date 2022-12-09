from time import sleep
from typing import List
from src.impl.characters import gnoll as gnoll_module
from src.impl.characters import goblin as goblin_module
from src.impl.characters import goblin_boss as goblin_boss_module
from src.game.game import Game, GameResult, CharacterTestable
import pandas as pd
from src.plots.frequency_win import FrequencyPlot

def main():

    # ---------------
    # Definitions
    # ---------------
    goblin_boss = CharacterTestable(
        name=goblin_boss_module.create().summary.name,
        factory=goblin_boss_module.create
    )

    gnoll = CharacterTestable(
        name=gnoll_module.create().summary.name,
        factory=gnoll_module.create
    )

    resultados: List[GameResult] = []
    game = Game(
        goblin_boss.factory,
        gnoll.factory,
    )

    # ---------------
    # Simulation
    # ---------------
    times = 5000
    for _ in range(times):
        # print(f'>>>> {_}')
        # print(f'PRE RESTART')
        # print(f'{game.characters[0].heath.hp} / {game.characters[0].heath.hp_max}')
        # print(f'{game.characters[1].heath.hp} / {game.characters[1].heath.hp_max}')
        game.restart_game()
        # print(f'RESTART')
        # print(f'{game.characters[0].heath.hp} / {game.characters[0].heath.hp_max}')
        # print(f'{game.characters[1].heath.hp} / {game.characters[1].heath.hp_max}')
        while(not game.is_finished):
            # print(f'BEGIN TURN -> {game.current_character}')
            # print(f'{game.characters[0].heath.hp} / {game.characters[0].heath.hp_max}')
            # print(f'{game.characters[1].heath.hp} / {game.characters[1].heath.hp_max}')
            game.next_turn()
            game.validate_turn()
            game.run_turn()
            # print(f'END TURN')
            # print(f'{game.characters[0].heath.hp} / {game.characters[0].heath.hp_max}')
            # print(f'{game.characters[1].heath.hp} / {game.characters[1].heath.hp_max}')
            # sleep(0.5)

        result = game.get_game_results()
        resultados.append(result)
        # print(result.winner_name)
        # print(result.diff_hp)
        # print(resultados[ len(resultados)-10 : len(resultados) ])
        # print('-----------------------------------------')

    # ---------------
    # Plot
    # ---------------
    winners_list = []
    diff_hp_list = []
    for n in resultados:
        winners_list.append(n.winner_name)
        diff_hp_list.append(n.diff_hp)

    df = pd.DataFrame({
        'winners': winners_list,
        'diff_hp': diff_hp_list
    })
    print(df)
    df.to_csv("result.csv")

    plot = FrequencyPlot(df, goblin_boss, gnoll)
    plot.build()
    plot.show()


if __name__ == "__main__":
    main()
