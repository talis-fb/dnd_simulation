from dataclasses import dataclass
from src.game.game import CharacterTestable
from src.plots.abstracts import Plot
from matplotlib import pyplot as plt
import pandas as pd

@dataclass
class FrequencyPlot(Plot):
    character_1:CharacterTestable
    character_2:CharacterTestable

    color_ch1 = 'blue'
    color_ch2 = 'red'

    df = pd.DataFrame()

    def build(self):
        df_character_1 = self.df[self.df['winners'] == self.character_1.factory().summary.name]
        data_series_ch_1 = df_character_1[[ 'diff_hp' ]].value_counts()

        df_character_2 = self.df[self.df['winners'] == self.character_2.factory().summary.name]
        data_series_ch_2 = df_character_2[[ 'diff_hp' ]].value_counts()

        self.df = pd.concat([ data_series_ch_1, data_series_ch_2 ], keys=[ self.character_1.name, self.character_2.name ], axis=1 ).sort_values(by='diff_hp')#.fillna(0)
        
        print('--1')
        print(data_series_ch_1)
        print('--2')
        print(data_series_ch_2)
        print('--FINAL')
        print(self.df)

        # WARNING: Metodo interpolate() cria valores lineares entre pontos sem dados (NaN). Nao é possivel destacar
        #  esses pontos dos demais de maneira facil. Está sendo usado para nao gerar um grafico estranho
        # ax = plt.gca()
        self.df.plot(kind='line', marker='o', color=[self.color_ch1, self.color_ch2])


    def show(self):
        # Grid and labels
        ch1 = self.character_1.factory()
        ch2 = self.character_2.factory()

        maximun_value = len(self.df.index)

        indexs_to_handle = list(range(maximun_value))
        range_hp_axis = list(range(1, maximun_value+1))

        plt.xticks(indexs_to_handle, range_hp_axis)
        plt.grid()

        # ADD Legend e labels
        plt.legend([ch1.summary.name, ch2.summary.name])
        plt.ylabel('Frequência vitória', fontsize=12)
        plt.xlabel('HP do vencedor ao fim', fontsize=12)
        plt.title('Goblins VS Gnolls', fontsize=16)

        # Lines
        plt.axvline(ch1.heath.hp_max - 1, color=self.color_ch1, linestyle='dashed')
        plt.axvline(ch2.heath.hp_max - 1, color=self.color_ch2, linestyle='dashed')


        plt.show()
