# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-06-29 17:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import otree.db.models
import otree_save_the_change.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('otree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_subsession', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ind_info_group', to='otree.Session')),
            ],
            options={
                'db_table': 'ind_info_group',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_group', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_payoff', otree.db.models.CurrencyField(default=0, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_gbat_arrived', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('_gbat_grouped', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('ratemo_1', otree.db.models.StringField(choices=[('全くあてはまらない', '全くあてはまらない'), ('あまりあてはまらない', 'あまりあてはまらない'), ('どちらともいえない', 'どちらともいえない'), ('少しあてはまる', '少しあてはまる'), ('非常にあてはまる', '非常にあてはまる')], max_length=10000, null=True, verbose_name='たいていの人より，ものごとを論理的に解決するのが上手である．')),
                ('ratemo_2', otree.db.models.StringField(choices=[('全くあてはまらない', '全くあてはまらない'), ('あまりあてはまらない', 'あまりあてはまらない'), ('どちらともいえない', 'どちらともいえない'), ('少しあてはまる', '少しあてはまる'), ('非常にあてはまる', '非常にあてはまる')], max_length=10000, null=True, verbose_name='直観に頼らなければならない状況は好きではない．')),
                ('ratemo_3', otree.db.models.StringField(choices=[('全くあてはまらない', '全くあてはまらない'), ('あまりあてはまらない', 'あまりあてはまらない'), ('どちらともいえない', 'どちらともいえない'), ('少しあてはまる', '少しあてはまる'), ('非常にあてはまる', '非常にあてはまる')], max_length=10000, null=True, verbose_name='自分の予感を信じることにしている．')),
                ('ratemo_4', otree.db.models.StringField(choices=[('全くあてはまらない', '全くあてはまらない'), ('あまりあてはまらない', 'あまりあてはまらない'), ('どちらともいえない', 'どちらともいえない'), ('少しあてはまる', '少しあてはまる'), ('非常にあてはまる', '非常にあてはまる')], max_length=10000, null=True, verbose_name='論理的な考えの持ち主だ．')),
                ('ratemo_5', otree.db.models.StringField(choices=[('全くあてはまらない', '全くあてはまらない'), ('あまりあてはまらない', 'あまりあてはまらない'), ('どちらともいえない', 'どちらともいえない'), ('少しあてはまる', '少しあてはまる'), ('非常にあてはまる', '非常にあてはまる')], max_length=10000, null=True, verbose_name='ものごとを注意深く理論的に解決するのは，得意ではない．')),
                ('ratemo_6', otree.db.models.StringField(choices=[('全くあてはまらない', '全くあてはまらない'), ('あまりあてはまらない', 'あまりあてはまらない'), ('どちらともいえない', 'どちらともいえない'), ('少しあてはまる', '少しあてはまる'), ('非常に当てはまる', '非常に当てはまる')], max_length=10000, null=True, verbose_name='簡単な問題より複雑な問題の方が好きだ．')),
                ('ratemo_7', otree.db.models.StringField(choices=[('全くあてはまらない', '全くあてはまらない'), ('あまりあてはまらない', 'あまりあてはまらない'), ('どちらともいえない', 'どちらともいえない'), ('少しあてはまる', '少しあてはまる'), ('非常にあてはまる', '非常にあてはまる')], max_length=10000, null=True, verbose_name='なぜだか理由を説明できないが，その人が正しいか間違っているかを，感じとることができる．')),
                ('ratemo_8', otree.db.models.StringField(choices=[('全くあてはまらない', '全くあてはまらない'), ('あまりあてはまらない', 'あまりあてはまらない'), ('どちらともいえない', 'どちらともいえない'), ('少しあてはまる', '少しあてはまる'), ('非常に当てはまる', '非常に当てはまる')], max_length=10000, null=True, verbose_name='分析的に考える方ではない．')),
                ('ratemo_9', otree.db.models.StringField(choices=[('全くあてはまらない', '全くあてはまらない'), ('あまりあてはまらない', 'あまりあてはまらない'), ('どちらともいえない', 'どちらともいえない'), ('少しあてはまる', '少しあてはまる'), ('非常にあてはまる', '非常にあてはまる')], max_length=10000, null=True, verbose_name='私にはすごい直観力はない．')),
                ('ratemo_10', otree.db.models.StringField(choices=[('全くあてはまらない', '全くあてはまらない'), ('あまりあてはまらない', 'あまりあてはまらない'), ('どちらともいえない', 'どちらともいえない'), ('少しあてはまる', '少しあてはまる'), ('非常にあてはまる', '非常にあてはまる')], max_length=10000, null=True, verbose_name='考えることは，楽しいことだと思わない．')),
                ('ratemo_11', otree.db.models.StringField(choices=[('全くあてはまらない', '全くあてはまらない'), ('あまりあてはまらない', 'あまりあてはまらない'), ('どちらともいえない', 'どちらともいえない'), ('少しあてはまる', '少しあてはまる'), ('非常にあてはまる', '非常にあてはまる')], max_length=10000, null=True, verbose_name='直観は問題を解決するのに役立つ方法だろう．')),
                ('ratemo_12', otree.db.models.StringField(choices=[('全くあてはまらない', '全くあてはまらない'), ('あまりあてはまらない', 'あまりあてはまらない'), ('どちらともいえない', 'どちらともいえない'), ('少しあてはまる', '少しあてはまる'), ('非常にあてはまる', '非常にあてはまる')], max_length=10000, null=True, verbose_name='感情に基づいて重要な決定をするのは，愚かなことだと思う．')),
                ('ratemo_13', otree.db.models.StringField(choices=[('全くあてはまらない', '全くあてはまらない'), ('あまりあてはまらない', 'あまりあてはまらない'), ('どちらともいえない', 'どちらともいえない'), ('少しあてはまる', '少しあてはまる'), ('非常にあてはまる', '非常にあてはまる')], max_length=10000, null=True, verbose_name='行動を決める時，直観に頼ることが多い．')),
                ('ratemo_14', otree.db.models.StringField(choices=[('全くあてはまらない', '全くあてはまらない'), ('あまりあてはまらない', 'あまりあてはまらない'), ('どちらともいえない', 'どちらともいえない'), ('少しあてはまる', '少しあてはまる'), ('非常にあてはまる', '非常にあてはまる')], max_length=10000, null=True, verbose_name='私にとって，新しい考え方を学ぶことは，とても魅力的である．')),
                ('ratemo_15', otree.db.models.StringField(choices=[('全くあてはまらない', '全くあてはまらない'), ('あまりあてはまらない', 'あまりあてはまらない'), ('どちらともいえない', 'どちらともいえない'), ('少しあてはまる', '少しあてはまる'), ('非常にあてはまる', '非常にあてはまる')], max_length=10000, null=True, verbose_name='複雑な問題を解決するのは，得意ではない．')),
                ('ratemo_16', otree.db.models.StringField(choices=[('全くあてはまらない', '全くあてはまらない'), ('あまりあてはまらない', 'あまりあてはまらない'), ('どちらともいえない', 'どちらともいえない'), ('少しあてはまる', '少しあてはまる'), ('非常にあてはまる', '非常にあてはまる')], max_length=10000, null=True, verbose_name='知的な挑戦が好きだ．')),
                ('ratemo_17', otree.db.models.StringField(choices=[('全くあてはまらない', '全くあてはまらない'), ('あまりあてはまらない', 'あまりあてはまらない'), ('どちらともいえない', 'どちらともいえない'), ('少しあてはまる', '少しあてはまる'), ('非常にあてはまる', '非常にあてはまる')], max_length=10000, null=True, verbose_name='直観に頼って重要な決定をするのは，いい考えだと思わない．')),
                ('ratemo_18', otree.db.models.StringField(choices=[('全くあてはまらない', '全くあてはまらない'), ('あまりあてはまらない', 'あまりあてはまらない'), ('どちらともいえない', 'どちらともいえない'), ('少しあてはまる', '少しあてはまる'), ('非常にあてはまる', '非常にあてはまる')], max_length=10000, null=True, verbose_name='もし私が直観に頼るならば，間違いをおかすことが多くなるだろう．')),
                ('ratemo_19', otree.db.models.StringField(choices=[('全くあてはまらない', '全くあてはまらない'), ('あまりあてはまらない', 'あまりあてはまらない'), ('どちらともいえない', 'どちらともいえない'), ('少しあてはまる', '少しあてはまる'), ('非常にあてはまる', '非常にあてはまる')], max_length=10000, null=True, verbose_name='直観的な印象に頼るのが好きだ．')),
                ('ratemo_20', otree.db.models.StringField(choices=[('全くあてはまらない', '全くあてはまらない'), ('あまりあてはまらない', 'あまりあてはまらない'), ('どちらともいえない', 'どちらともいえない'), ('少しあてはまる', '少しあてはまる'), ('非常にあてはまる', '非常にあてはまる')], max_length=10000, null=True, verbose_name='一生懸命考えなければならないような問題を解決するのが好きだ．')),
                ('ratemo_21', otree.db.models.StringField(choices=[('全くあてはまらない', '全くあてはまらない'), ('あまりあてはまらない', 'あまりあてはまらない'), ('どちらともいえない', 'どちらともいえない'), ('少しあてはまる', '少しあてはまる'), ('非常にあてはまる', '非常にあてはまる')], max_length=10000, null=True, verbose_name='答えを見つけるために直観に従って，うまくいかなかったことはほとんどない．')),
                ('ratemo_22', otree.db.models.StringField(choices=[('全くあてはまらない', '全くあてはまらない'), ('あまりあてはまらない', 'あまりあてはまらない'), ('どちらともいえない', 'どちらともいえない'), ('少しあてはまる', '少しあてはまる'), ('非常にあてはまる', '非常にあてはまる')], max_length=10000, null=True, verbose_name='人生や生活上のいろんな問題を考えるとき，直観的にやるとうまくいく．')),
                ('ratemo_23', otree.db.models.StringField(choices=[('全くあてはまらない', '全くあてはまらない'), ('あまりあてはまらない', 'あまりあてはまらない'), ('どちらともいえない', 'どちらともいえない'), ('少しあてはまる', '少しあてはまる'), ('非常にあてはまる', '非常にあてはまる')], max_length=10000, null=True, verbose_name='注意深く論理的な分析が必要とされる問題を解決するのは，得意ではない．')),
                ('ratemo_24', otree.db.models.StringField(choices=[('全くあてはまらない', '全くあてはまらない'), ('あまりあてはまらない', 'あまりあてはまらない'), ('どちらともいえない', 'どちらともいえない'), ('少しあてはまる', '少しあてはまる'), ('非常にあてはまる', '非常にあてはまる')], max_length=10000, null=True, verbose_name='いろいろ考えるのは好きではない．')),
                ('big5_1', otree.db.models.StringField(choices=[('1.全く違うと思う', '1.全く違うと思う'), ('2.おおよそ違うと思う', '2.おおよそ違うと思う'), ('3.少し違うと思う', '3.少し違うと思う'), ('4.どちらでもない', '4.どちらでもない'), ('5.少しそう思う', '5.少しそう思う'), ('6.まあまあそう思う', '6.まあまあそう思う'), ('7.強くそう思う', '7.強くそう思う')], max_length=10000, null=True, verbose_name='活発で，外向的だと思う')),
                ('big5_2', otree.db.models.StringField(choices=[('1.全く違うと思う', '1.全く違うと思う'), ('2.おおよそ違うと思う', '2.おおよそ違うと思う'), ('3.少し違うと思う', '3.少し違うと思う'), ('4.どちらでもない', '4.どちらでもない'), ('5.少しそう思う', '5.少しそう思う'), ('6.まあまあそう思う', '6.まあまあそう思う'), ('7.強くそう思う', '7.強くそう思う')], max_length=10000, null=True, verbose_name='他人に不満をもち，もめごとを起こしやすいと思う')),
                ('big5_3', otree.db.models.StringField(choices=[('1.全く違うと思う', '1.全く違うと思う'), ('2.おおよそ違うと思う', '2.おおよそ違うと思う'), ('3.少し違うと思う', '3.少し違うと思う'), ('4.どちらでもない', '4.どちらでもない'), ('5.少しそう思う', '5.少しそう思う'), ('6.まあまあそう思う', '6.まあまあそう思う'), ('7.強くそう思う', '7.強くそう思う')], max_length=10000, null=True, verbose_name='しっかりしていて，自分に厳しいと思う')),
                ('big5_4', otree.db.models.StringField(choices=[('1.全く違うと思う', '1.全く違うと思う'), ('2.おおよそ違うと思う', '2.おおよそ違うと思う'), ('3.少し違うと思う', '3.少し違うと思う'), ('4.どちらでもない', '4.どちらでもない'), ('5.少しそう思う', '5.少しそう思う'), ('6.まあまあそう思う', '6.まあまあそう思う'), ('7.強くそう思う', '7.強くそう思う')], max_length=10000, null=True, verbose_name='心配性で，うろたえやすいと思う')),
                ('big5_5', otree.db.models.StringField(choices=[('1.全く違うと思う', '1.全く違うと思う'), ('2.おおよそ違うと思う', '2.おおよそ違うと思う'), ('3.少し違うと思う', '3.少し違うと思う'), ('4.どちらでもない', '4.どちらでもない'), ('5.少しそう思う', '5.少しそう思う'), ('6.まあまあそう思う', '6.まあまあそう思う'), ('7.強くそう思う', '7.強くそう思う')], max_length=10000, null=True, verbose_name='新しいことが好きで，変わった考えをもつと思う')),
                ('big5_6', otree.db.models.StringField(choices=[('1.全く違うと思う', '1.全く違うと思う'), ('2.おおよそ違うと思う', '2.おおよそ違うと思う'), ('3.少し違うと思う', '3.少し違うと思う'), ('4.どちらでもない', '4.どちらでもない'), ('5.少しそう思う', '5.少しそう思う'), ('6.まあまあそう思う', '6.まあまあそう思う'), ('7.強くそう思う', '7.強くそう思う')], max_length=10000, null=True, verbose_name='ひかえめで，おとなしいと思う')),
                ('big5_7', otree.db.models.StringField(choices=[('1.全く違うと思う', '1.全く違うと思う'), ('2.おおよそ違うと思う', '2.おおよそ違うと思う'), ('3.少し違うと思う', '3.少し違うと思う'), ('4.どちらでもない', '4.どちらでもない'), ('5.少しそう思う', '5.少しそう思う'), ('6.まあまあそう思う', '6.まあまあそう思う'), ('7.強くそう思う', '7.強くそう思う')], max_length=10000, null=True, verbose_name='人に気をつかう，やさしい人間だと思う')),
                ('big5_8', otree.db.models.StringField(choices=[('1.全く違うと思う', '1.全く違うと思う'), ('2.おおよそ違うと思う', '2.おおよそ違うと思う'), ('3.少し違うと思う', '3.少し違うと思う'), ('4.どちらでもない', '4.どちらでもない'), ('5.少しそう思う', '5.少しそう思う'), ('6.まあまあそう思う', '6.まあまあそう思う'), ('7.強くそう思う', '7.強くそう思う')], max_length=10000, null=True, verbose_name='だらしなく，うっかりしていると思う')),
                ('big5_9', otree.db.models.StringField(choices=[('1.全く違うと思う', '1.全く違うと思う'), ('2.おおよそ違うと思う', '2.おおよそ違うと思う'), ('3.少し違うと思う', '3.少し違うと思う'), ('4.どちらでもない', '4.どちらでもない'), ('5.少しそう思う', '5.少しそう思う'), ('6.まあまあそう思う', '6.まあまあそう思う'), ('7.強くそう思う', '7.強くそう思う')], max_length=10000, null=True, verbose_name='冷静で，気分が安定していると思う')),
                ('big5_10', otree.db.models.StringField(choices=[('1.全く違うと思う', '1.全く違うと思う'), ('2.おおよそ違うと思う', '2.おおよそ違うと思う'), ('3.少し違うと思う', '3.少し違うと思う'), ('4.どちらでもない', '4.どちらでもない'), ('5.少しそう思う', '5.少しそう思う'), ('6.まあまあそう思う', '6.まあまあそう思う'), ('7.強くそう思う', '7.強くそう思う')], max_length=10000, null=True, verbose_name='発想力に欠けた，平凡な人間だと思う')),
                ('q_gender', otree.db.models.StringField(choices=[('男性', '男性'), ('女性', '女性'), ('その他', 'その他')], max_length=10000, null=True, verbose_name='あなたの性別を教えてください．')),
                ('q_age', otree.db.models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30), (31, 31), (32, 32), (33, 33), (34, 34), (35, 35), (36, 36), (37, 37), (38, 38), (39, 39), (40, 40), (41, 41), (42, 42), (43, 43), (44, 44), (45, 45), (46, 46), (47, 47), (48, 48), (49, 49), (50, 50), (51, 51), (52, 52), (53, 53), (54, 54), (55, 55), (56, 56), (57, 57), (58, 58), (59, 59), (60, 60), (61, 61), (62, 62), (63, 63), (64, 64), (65, 65), (66, 66), (67, 67), (68, 68), (69, 69), (70, 70), (71, 71), (72, 72), (73, 73), (74, 74), (75, 75), (76, 76), (77, 77), (78, 78), (79, 79), (80, 80), (81, 81), (82, 82), (83, 83), (84, 84), (85, 85), (86, 86), (87, 87), (88, 88), (89, 89), (90, 90), (91, 91), (92, 92), (93, 93), (94, 94), (95, 95), (96, 96), (97, 97), (98, 98), (99, 99), (100, 100), (101, 101), (102, 102), (103, 103), (104, 104), (105, 105), (106, 106), (107, 107), (108, 108), (109, 109), (110, 110), (111, 111), (112, 112), (113, 113), (114, 114), (115, 115), (116, 116), (117, 117), (118, 118), (119, 119), (120, 120), (121, 121), (122, 122), (123, 123), (124, 124)], null=True, verbose_name='あなたの年齢を教えてください．')),
                ('q_country', otree.db.models.StringField(choices=[('北海道', '北海道'), ('青森県', '青森県'), ('岩手県', '岩手県'), ('宮城県', '宮城県'), ('秋田県', '秋田県'), ('山形県', '山形県'), ('福島県', '福島県'), ('茨城県', '茨城県'), ('栃木県', '栃木県'), ('群馬県', '群馬県'), ('埼玉県', '埼玉県'), ('千葉県', '千葉県'), ('東京都', '東京都'), ('神奈川県', '神奈川県'), ('新潟県', '新潟県'), ('富山県', '富山県'), ('石川県', '石川県'), ('福井県', '福井県'), ('山梨県', '山梨県'), ('長野県', '長野県'), ('岐阜県', '岐阜県'), ('静岡県', '静岡県'), ('愛知県', '愛知県'), ('三重県', '三重県'), ('滋賀県', '滋賀県'), ('京都府', '京都府'), ('大阪府', '大阪府'), ('兵庫県', '兵庫県'), ('奈良県', '奈良県'), ('和歌山県', '和歌山県'), ('鳥取県', '鳥取県'), ('島根県', '島根県'), ('岡山県', '岡山県'), ('広島県', '広島県'), ('山口県', '山口県'), ('徳島県', '徳島県'), ('香川県', '香川県'), ('愛媛県', '愛媛県'), ('高知県', '高知県'), ('福岡県', '福岡県'), ('佐賀県', '佐賀県'), ('長崎県', '長崎県'), ('熊本県', '熊本県'), ('大分県', '大分県'), ('宮崎県', '宮崎県'), ('鹿児島県', '鹿児島県'), ('沖縄県', '沖縄県')], max_length=10000, null=True, verbose_name='あなたのおすまいの地域を教えてください．')),
                ('q_aca', otree.db.models.StringField(choices=[('中学校卒業', '中学校卒業'), ('高校中退', '高校中退'), ('高校卒業', '高校卒業'), ('専門学校（短期大学）中退', '専門学校（短期大学）中退'), ('専門学校（短期大学）卒業', '専門学校（短期大学）卒業'), ('大学中退', '大学中退'), ('大学卒業', '大学卒業'), ('大学院修士課程（博士前期課程）中退', '大学院修士課程（博士前期課程）中退'), ('大学院修士課程（博士前期課程）修了', '大学院修士課程（博士前期課程）修了'), ('大学院博士課程（博士後期課程）中退', '大学院博士課程（博士後期課程）中退'), ('大学院博士課程（博士後期課程）修了', '大学院博士課程（博士後期課程）修了')], max_length=10000, null=True, verbose_name='あなたの最終学歴を教えてください．')),
                ('q_INK', otree.db.models.StringField(choices=[('0円', '0円'), ('1円〜200万円未満', '1円〜200万円未満'), ('200万円以上〜400万円未満', '200万円以上〜400万円未満'), ('400万円以上〜600万円未満', '400万円以上〜600万円未満'), ('600万円以上〜800万円未満', '600万円以上〜800万円未満'), ('800万円以上〜1,000万円未満', '800万円以上〜1,000万円未満'), ('1,000万円以上〜1,200万円未満', '1,000万円以上〜1,200万円未満'), ('1,200万円以上〜1,500万円未満', '1,200万円以上〜1,500万円未満'), ('1,500万円以上〜2,000万円未満', '1,500万円以上〜2,000万円未満'), ('2,000万円以上', '2,000万円以上'), ('わからない', 'わからない')], max_length=10000, null=True, verbose_name='あなたの個人収入(額面)を教えてください．')),
                ('q_INS', otree.db.models.StringField(choices=[('0円', '0円'), ('1円〜200万円未満', '1円〜200万円未満'), ('200万円以上〜400万円未満', '200万円以上〜400万円未満'), ('400万円以上〜600万円未満', '400万円以上〜600万円未満'), ('600万円以上〜800万円未満', '600万円以上〜800万円未満'), ('800万円以上〜1,000万円未満', '800万円以上〜1,000万円未満'), ('1,000万円以上〜1,200万円未満', '1,000万円以上〜1,200万円未満'), ('1,200万円以上〜1,500万円未満', '1,200万円以上〜1,500万円未満'), ('1,500万円以上〜2,000万円未満', '1,500万円以上〜2,000万円未満'), ('2,000万円以上', '2,000万円以上'), ('わからない', 'わからない')], max_length=10000, null=True, verbose_name='あなたの世帯収入(額面)を教えてください．')),
                ('q_MAR', otree.db.models.StringField(choices=[('未婚', '未婚'), ('既婚', '既婚')], max_length=10000, null=True, verbose_name='あなたは結婚されていますか？それとも結婚されていませんか？')),
                ('q_CHI', otree.db.models.StringField(choices=[('子どもなし', '子どもなし'), ('子どもあり', '子どもあり')], max_length=10000, null=True, verbose_name='あなたは子どもがいますか？いませんか？')),
                ('crt_bat', otree.db.models.PositiveIntegerField(null=True)),
                ('crt_widget', otree.db.models.PositiveIntegerField(null=True)),
                ('crt_lake', otree.db.models.PositiveIntegerField(null=True)),
                ('crt_1st', otree.db.models.StringField(choices=[('あてはまらない', 'あてはまらない'), ('どちらかといえばあてはまらない', 'どちらかといえばあてはまらない'), ('どちらかといえばあてはまる', 'どちらかといえばあてはまる'), ('あてはまる', 'あてはまる')], max_length=10000, null=True, verbose_name='日常生活の中で，自分の行動は「自分自身」に見られていると思うことがある．')),
                ('crt_2nd', otree.db.models.StringField(choices=[('あてはまらない', 'あてはまらない'), ('どちらかといえばあてはまらない', 'どちらかといえばあてはまらない'), ('どちらかといえばあてはまる', 'どちらかといえばあてはまる'), ('あてはまる', 'あてはまる')], max_length=10000, null=True, verbose_name='日常生活の中で，自分の行動は「直接誰か（人間）」に見られていると思うことがある．')),
                ('crt_3rd', otree.db.models.StringField(choices=[('あてはまらない', 'あてはまらない'), ('どちらかといえばあてはまらない', 'どちらかといえばあてはまらない'), ('どちらかといえばあてはまる', 'どちらかといえばあてはまる'), ('あてはまる', 'あてはまる')], max_length=10000, null=True, verbose_name='日常生活の中で，自分の行動は「監視カメラ等を通じて誰か（人間）」に間接的に見られていると思うことがある．')),
                ('crt_sup', otree.db.models.StringField(choices=[('あてはまらない', 'あてはまらない'), ('どちらかといえばあてはまらない', 'どちらかといえばあてはまらない'), ('どちらかといえばあてはまる', 'どちらかといえばあてはまる'), ('あてはまる', 'あてはまる')], max_length=10000, null=True, verbose_name='日常生活の中で，自分の行動は「お天道様や神様，仏様などの超自然的な存在」に見られていると思うことがある．')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ind_info.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ind_info_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ind_info_player', to='otree.Session')),
            ],
            options={
                'db_table': 'ind_info_player',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ind_info_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'ind_info_subsession',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.AddField(
            model_name='player',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ind_info.Subsession'),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ind_info.Subsession'),
        ),
    ]
