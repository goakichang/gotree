from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants


class Introduction(Page):
    timeout_seconds = 100

    def is_displayed(self):
        return self.round_number == 1


class Decision(Page):
    form_model = models.Player
    form_fields = ['decision']


class ResultsWaitPage(WaitPage):
    body_text = '他のプレイヤーの意思決定が終わるまでお待ち下さい．／Waiting for the other participant to choose.'

    def after_all_players_arrive(self):
        for p in self.group.get_players():
            p.set_payoff()


class Results(Page):
    def vars_for_template(self):
        self.player.set_payoff()

        return {
            'my_decision': self.player.decision.lower(),
            'other_player_decision': self.player.other_player().decision.lower(),
            'same_choice': self.player.decision == self.player.other_player().decision,
        }


page_sequence = [
    Introduction,
    Decision,
    ResultsWaitPage,
    Results
]
