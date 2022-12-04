from dataclasses import dataclass
from src.game.game import CharacterTestable
from src.plots.abstracts import Plot
from matplotlib import pyplot as plt

@dataclass
class FrequencyPlot(Plot):
    character_1:CharacterTestable
    character_2:CharacterTestable

    def build(self):
        df_character_1 = self.df[self.df['winners'] == self.character_1.factory().summary.name]
        final_series_ch_1 = df_character_1[[ 'diff_hp' ]].value_counts().sort_index()

        df_character_2 = self.df[self.df['winners'] == self.character_2.factory().summary.name]
        final_series_ch_2 = df_character_2[[ 'diff_hp' ]].value_counts().sort_index()

        final_series_ch_1.plot(kind='line')
        final_series_ch_2.plot(kind='line')

    def show(self):
        # Grid and labels
        max_hp_character = max(
            self.character_1.factory().heath.hp_max,
            self.character_2.factory().heath.hp_max
        )
        range_hp_axis = list(range(max_hp_character))
        plt.xticks(range_hp_axis, range_hp_axis)
        plt.grid()

        # ADD Legend e labels
        plt.legend(['Goblin Boss', 'Gnoll'])
        plt.ylabel('Frequência vitória', fontsize=12)
        plt.xlabel('HP do vencedor ao fim', fontsize=12)
        plt.title('Goblins VS Gnolls', fontsize=16)

        plt.show()
