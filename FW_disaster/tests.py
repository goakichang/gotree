from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants
import random

class PlayerBot(Bot):

    def play_round(self):

        yield (views.Demographics, {
            'q_country': 'BS',
            'q_age': 24,
            'q_gender': 'Male'})

        yield (views.FreeWill, {
            'crt_bat': 10,
            'crt_widget': 5,
            'crt_lake': 48
        })

        for value in [
            self.player.crt_bat,
            self.player.q_country,
            self.player.payoff
        ]:
            assert value is not None
