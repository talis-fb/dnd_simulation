from time import sleep
from typing import List
from src.core.character import Character
from src.impl.characters import gnoll as gnoll_module
from src.impl.characters import goblin_boss as goblin_boss_module
from src.impl.characters import devorator_de_mentes as devorator_de_mentes_mod
from src.impl.characters import black_dragon_young as black_dragon_young_mod
from src.impl.characters import kobold_wing as kobold_wing_mod
from src.impl.characters import goblin as goblin_mod

from src.game.game import Game, GameResult, CharacterTestable
import pandas as pd
from src.plots.frequency_win import FrequencyPlot

from rich.progress import track
import inquirer

def main():

    all_characters = [
        black_dragon_young_mod,
        devorator_de_mentes_mod,
        gnoll_module,
        goblin_boss_module,
        goblin_mod,
        kobold_wing_mod,
    ]

    # ---------------
    # Input
    # ---------------
    options_characters_input = {}
    for ch in all_characters:
        character:Character = ch.create()
        options_characters_input[character.summary.name] = ch

    questions = [
      inquirer.List('character_1',
                    message="Qual o primeiro personagem voce deseja que começe?",
                    choices=options_characters_input.keys(),
                ),
      inquirer.List('character_2',
                    message="E o segundo?",
                    choices=options_characters_input.keys(),
                ),
        inquirer.Text('times',
                      message="Quantas um numero que indica quantas vezes essa simulação deve ser executada (padrão: 100k):",
                ),
    ]

    answers = inquirer.prompt(questions)
    
    # Validation 
    if answers == None:
        return 0

    if answers['times'] == '':
        answers['times'] = 100_000
    print(answers)

    print(r"""

 _                 )      ((   ))     (
(@)               /|\      ))_((     /|\                 _
|-|`\            / | \    (/\|/\)   / | \               (@)
| | ------------/--|-voV---\`|'/--Vov-|--\--------------|-|
|-|                  '^`   (o o)  '^`                   | |
| |                        `\Y/'                        |-|
|-|                                                     | |
| |                 Agora é só aguardar                 |-|
|_|_____________________________________________________| |
(@)       l   /\ /         ( (       \ /\   l         `\|-|
          l /   V           \ \       V   \ l           (@)
          l/                _) )_          \I
                            `\ /'
                              `

          """)


    # ---------------
    # Definitions
    # ---------------
    characters_mods = [
        options_characters_input[ answers['character_1'] ],
        options_characters_input[ answers['character_2'] ],
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

    times = int(answers['times'])

    for _ in track(range(times)):
        game.restart_game()
        while(not game.is_finished):
            game.next_turn()
            game.validate_turn()
            game.run_turn()

        result = game.get_game_results()
        resultados.append(result)

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
