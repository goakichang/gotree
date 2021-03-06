from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


doc = """
2人の買い手と1人の売り手がレモン市場にいる場合の実験です．Akerlof(1970)の枠組みに基づいて，実験を組んでいます．

In a lemon market of
<a href="http://people.bu.edu/ellisrp/EC387/Papers/1970Akerlof_Lemons_QJE.pdf" target="_blank">
    Akerlof (1970)
</a>, 2 buyers and 1 seller interact for 3 periods. The implementation is
based on
<a href="http://people.virginia.edu/~cah2k/lemontr.pdf" target="_blank">
    Holt (1999)
</a>.
"""


class Constants(BaseConstants):
    name_in_url = 'lemon_market'
    players_per_group = 3
    num_rounds = 3

    instructions_template = 'lemon_market/Instructions.html'

    initial_endowment = c(50)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    sale_price = models.CurrencyField()

    seller_id = models.PositiveIntegerField(
        choices=[(i, 'Buy from seller %i' % i) for i in
                 range(1, Constants.players_per_group)] + [
                    (0, 'Buy nothing')],
        widget=widgets.RadioSelect(),
        doc="""0 means no purchase made"""
    )  # seller index

    def set_payoff(self):
        for p in self.get_players():
            p.payoff = Constants.initial_endowment

        if self.seller_id is not 0:
            seller = self.get_seller()
            self.sale_price = seller.seller_proposed_price

            buyer = self.get_player_by_role('買い主／buyer')
            buyer.payoff += seller.seller_proposed_quality + 5 - seller.seller_proposed_price
            seller.payoff += seller.seller_proposed_price - seller.seller_proposed_quality

    def get_seller(self):
        for p in self.get_players():
            if '売り主／seller' in p.role() and p.seller_id() == self.seller_id:
                return p


class Player(BasePlayer):
    # seller
    seller_proposed_price = models.CurrencyField(
        min=0, max=Constants.initial_endowment,
        verbose_name='Please indicate a price (from 0 to %i) you want to sell'
                     % Constants.initial_endowment)

    seller_proposed_quality = models.CurrencyField(
        choices=[
            (30, '高品質／High'),
            (20, '中品質／Medium'),
            (10, '低品質／Low')],
        verbose_name='あなたが生産したい品質の製品を選んで下さい．／Please select a quality grade you want to produce',
        widget=widgets.RadioSelectHorizontal())

    def seller_id(self):
        # player 1 is the buyer, so seller 1 is actually player 2
        return (self.id_in_group - 1)

    def role(self):
        if self.id_in_group == 1:
            return '売り手／buyer'
        return 'seller {}'.format(self.seller_id())
