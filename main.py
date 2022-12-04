from typing import List
from src.impl.characters import gnoll as gnoll_module
from src.impl.characters import goblin_boss as goblin_boss_module
from src.game.game import Game, GameResult, CharacterTestable
import pandas as pd
from matplotlib import pyplot as plt
import time

def print_roll(character, hp, result):
    print(f'[{character} / {hp}] => {result}')
    pass

def printf(c):
    print(c)
    pass

def main():

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

    times = 1000
    for _ in range(times):
        game.restart_game()
        while(not game.is_finished):
            game.next_turn()
            game.validate_turn()
            game.run_turn()
            game.log_turn_results()

        result = game.get_game_results()
        resultados.append(result)

    df = pd.DataFrame({
        'winners': [ n.winner_name for n in resultados ],
        'diff_hp': [ n.diff_hp for n in resultados ],
    })

    def serie_character(df:pd.DataFrame, character:CharacterTestable):
        df_character = df[df['winners'] == character.name]
        series_frequency = df_character[[ 'diff_hp' ]].value_counts()
        return series_frequency.sort_index()

    result_final_goblin = serie_character(df, goblin_boss)
    result_final_gnoll = serie_character(df, gnoll)

    # Create Plot
    result_final_goblin.plot(kind='line', color='green')
    result_final_gnoll.plot(kind='line')

    # Grid and labels
    max_hp_character = max( goblin_boss.factory().heath.hp_max, gnoll.factory().heath.hp_max )
    range_hp_axis = list(range(max_hp_character))
    plt.xticks(range_hp_axis, range_hp_axis)
    plt.grid()

    # ADD Legend e labels
    plt.legend(['Goblins', 'Gnoll'])
    plt.ylabel('Frequência vitória', fontsize=12)
    plt.xlabel('HP do vencedor ao fim', fontsize=12)
    plt.title('Goblins VS Gnolls', fontsize=16)

    plt.show()


if __name__ == "__main__":
    main()
