from dataclasses import dataclass
from src.game.game import CharacterTestable
from src.plots.abstracts import Plot
from matplotlib import pyplot as plt
import pandas as pd

@dataclass
class FrequencyPlot(Plot):
    df: pd.DataFrame
    character_1:CharacterTestable
    character_2:CharacterTestable

    color_ch1 = 'blue'
    color_ch2 = 'red'


    def build(self):
        df_character_1 = self.df[self.df['winners'] == self.character_1.factory().summary.name]
        data_series_ch_1 = df_character_1[[ 'diff_hp' ]].value_counts()

        df_character_2 = self.df[self.df['winners'] == self.character_2.factory().summary.name]
        data_series_ch_2 = df_character_2[[ 'diff_hp' ]].value_counts()

        # print('--Character1')
        # print(data_series_ch_1.to_string())
        # print('--Character2')
        # print(data_series_ch_2.to_string())

        self.df = pd.concat([ data_series_ch_1, data_series_ch_2 ], keys=[ self.character_1.name, self.character_2.name ], axis=1 ).sort_values(by='diff_hp')
        
        print('--DADOS para imprimir')
        print(self.df)

        # self.df = self.df.sample(n=50)

        # WARNING: Metodo interpolate() cria valores lineares entre pontos sem dados (NaN). Nao é possivel destacar
        #  esses pontos dos demais de maneira facil. Está sendo usado para nao gerar um grafico estranho
        # self.df.interpolate().plot(kind='line', marker='o', color=[self.color_ch1, self.color_ch2])
        self.df.plot(kind='line', marker='o', color=[self.color_ch1, self.color_ch2])


    def show(self):
        # Grid and labels
        ch1 = self.character_1.factory()
        ch2 = self.character_2.factory()

        maximun_value = len(self.df.index)

        values_registred = [ n[0] for n in self.df.index.to_list() ]

        # ADD Legend e labels
        plt.legend([ch1.summary.name, ch2.summary.name])
        plt.ylabel('Frequência vitória', fontsize=12)
        plt.xlabel('HP do vencedor ao fim', fontsize=12)
        plt.title(f'{ch1.summary.name} VS {ch2.summary.name}', fontsize=16)

        # Lines with max HP of each character
        hp_max_ch1 = ch1.heath.hp_max
        if hp_max_ch1 in values_registred:
            plt.axvline(values_registred.index(hp_max_ch1), color=self.color_ch1, linestyle='dashed')

        hp_max_ch2 = ch2.heath.hp_max
        if hp_max_ch2 in values_registred:
            plt.axvline(values_registred.index(hp_max_ch2), color=self.color_ch2, linestyle='dashed')

        # Each point
        indexs_to_handle = list(range(maximun_value))
        plt.xticks(indexs_to_handle, values_registred)

        plt.grid()

        plt.show()
