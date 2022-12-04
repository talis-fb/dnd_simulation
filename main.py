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
        gnoll.factory
    )

    # ---------------
    # Simulation
    # ---------------
    times = 50000
    for _ in range(times):
        game.restart_game()
        while(not game.is_finished):
            game.next_turn()
            game.validate_turn()
            game.run_turn()
            game.log_turn_results()

        result = game.get_game_results()
        resultados.append(result)

    # ---------------
    # Plot
    # ---------------
    df = pd.DataFrame({
        'winners': [ n.winner_name for n in resultados ],
        'diff_hp': [ n.diff_hp for n in resultados ],
    })

    plot = FrequencyPlot(df,goblin_boss, gnoll)
    plot.build()
    plot.show()


if __name__ == "__main__":
    main()
