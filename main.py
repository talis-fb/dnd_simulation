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

    print('MAIN----')
    print(df)
    print('END M---')

    # aa: pd.DataFrame = df['winners']
    # aa.value_counts().plot()

    # df.filter(iter)
    print('------------------------')
    name_goblins = goblin_boss.name
    df_goblins = df[df['winners'] == name_goblins]
    _dd = df_goblins[[ 'diff_hp' ]].value_counts()
    dd = pd.Series(_dd).sort_index()
    print(dd)

    print('---------')

    name_gnoll = gnoll.name
    df_gnolls = df[df['winners'] == name_gnoll]
    _dd2 = df_gnolls[[ 'diff_hp' ]].value_counts()
    dd2 = pd.Series(_dd2).sort_index()
    print(dd2)
    print(dd2.tolist())

    print('------------------------')

    dd.plot(kind='line', sort_columns=True, color='green')
    dd2.plot(kind='line', sort_columns=True)

    # dd.plot(label="Goblin", color="orange")
    # dd2.plot(label="Gnoll")

    # plt.plot(dd, label="Goblin", color="orange")
    # plt.plot(dd2, label="Gnoll", color='blue')

    #add legend
    plt.legend(['Goblins', 'Gnoll'])

    #add axes labels and a title
    plt.ylabel('Sales', fontsize=14)
    plt.xlabel('Time', fontsize=14)
    plt.title('Sales by Group', fontsize=16)

    plt.title('Goblins VS Gnolls')

    max_hp_character = max( goblin_boss.factory().heath.hp_max, gnoll.factory().heath.hp_max )
    range_hp_axis = list(range(max_hp_character))
    plt.xticks(range_hp_axis, range_hp_axis)
    # plt.yticks([5,10,15,20,25,30,35,40,45,50,55])
    plt.grid()

    plt.show()
    


    # win_goblin = ganhadores.count(goblin_boss.summary().name)
    # win_gnoll = ganhadores.count(gnoll.summary().name) 
    # print(f'GOBLIN: {win_goblin}   {win_goblin / (win_goblin+win_gnoll)}')
    # print(f'GNOLL:  {win_gnoll}   {win_gnoll / (win_goblin+win_gnoll)}')
    # print(len(ganhadores))

if __name__ == "__main__":
    main()
