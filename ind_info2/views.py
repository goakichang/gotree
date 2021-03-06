from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants

class CognitiveReflectionTest(Page):

    form_model = models.Player
    form_fields = ['crt_bat',
                  'crt_widget',
                  'crt_lake',
                  'crt_HAP',
                  'crt_1st',
                  'crt_2nd',
                  'crt_3rd',
                  'crt_sup',
                  'crt_shk1',
                   'crt_shk2',
                   'crt_shk3',
                   'crt_shk4',
                   'crt_shk5',
                   'crt_shk6',
                   'crt_shk7',
                   'crt_shk8',
                   'crt_shk9',
                   'crt_shk10',
                   'crt_shk11',
                   'crt_shk12',
                   'crt_shk13',
                   ]

    def before_next_page(self):
        self.player.set_payoff()


class ratemo(Page):

    form_model = models.Player
    form_fields = ['ratemo_1',
                   'ratemo_2',
                   'ratemo_3',
                   'ratemo_4',
                   'ratemo_5',
                   'ratemo_6',
                   'ratemo_7',
                   'ratemo_8',
                   'ratemo_9',
                   'ratemo_10',
                   'ratemo_11',
                   'ratemo_12',
                   'ratemo_13',
                   'ratemo_14',
                   'ratemo_15',
                   'ratemo_16',
                   'ratemo_17',
                   'ratemo_18',
                   'ratemo_19',
                   'ratemo_20',
                   'ratemo_21',
                   'ratemo_22',
                   'ratemo_23',
                   'ratemo_24'

]

    def before_next_page(self):
        self.player.set_payoff()




class Demographics(Page):

    form_model = models.Player
    form_fields = [
                  'q_gender',
                  'q_age',
                  'q_country',
                  'q_aca',
                  'q_INK',
                  'q_INS',
                  'q_MAR',
                  'q_CHI']



    def before_next_page(self):
        self.player.set_payoff()

page_sequence = [
    CognitiveReflectionTest,
    ratemo,
    Demographics,
]
