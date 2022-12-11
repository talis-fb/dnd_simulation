from time import sleep
from typing import List
from src.impl.characters import gnoll as gnoll_module
from src.impl.characters import goblin as goblin_module
from src.impl.characters import goblin_boss as goblin_boss_module
from src.impl.characters import devorator_de_mentes as devorator_de_mentes_mod
from src.impl.characters import black_dragon_young as black_dragon_young_mod
from src.impl.characters import kobold_wing as kobold_wing_mod
from src.impl.characters import goblin as goblin_mod

from src.game.game import Game, GameResult, CharacterTestable
import pandas as pd
from src.plots.frequency_win import FrequencyPlot

def main():

    # ---------------
    # Definitions
    # ---------------
    characters_mods = [
        black_dragon_young_mod,
        devorator_de_mentes_mod,
    ]

    character_1 = CharacterTestable(
        name=characters_mods[0].create().summary.name,
        factory=characters_mods[0].create
    )

    character_2 = CharacterTestable(
        name=characters_mods[1].create().summary.name,
        factory=characters_mods[1].create
    )

    resultados: List[GameResult] = []
    game = Game(
        character_1.factory,
        character_2.factory,
    )

    # ---------------
    # Simulation
    # ---------------

    times = 5000
    # times = 20000

    progress = 0
    for _ in range(times):
        game.restart_game()
        while(not game.is_finished):
            game.next_turn()
            game.validate_turn()
            game.run_turn()

        result = game.get_game_results()
        resultados.append(result)

        progress += 1
        if(progress % (times/100 ) == 0):
            print(f'{(progress*100)/times}%')

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

    plot = FrequencyPlot(df, character_1, character_2)
    plot.build()
    plot.show()


if __name__ == "__main__":
    main()
