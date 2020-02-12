# Generated by Django 2.2.9 on 2020-02-12 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invest_game', '0003_auto_20200212_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investment',
            name='multiple_agreement_question_type',
            field=models.CharField(choices=[('control', 'User was presented with the control question'), ('with_immigration', 'User was presented with the immigration option'), ('with_muslim_immigration', 'User was presented with the Muslim immigration option')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='investment',
            name='reached_stage',
            field=models.CharField(choices=[('select_respondent', 'User reached respondent selection stage'), ('user_investment', 'User reached user investment stage'), ('respondent_investment', 'User reached respondent investment stage'), ('question1', 'User reached question 1 stage'), ('question1_5', 'User reached question 1.5 stage'), ('question2', 'User reached question 2 stage'), ('question3', 'User reached question 3 stage'), ('compare', 'User reached compare stage'), ('finish', 'User reached finish stage')], default='select_respondent', max_length=256),
        ),
        migrations.AlterField(
            model_name='investment',
            name='respondent',
            field=models.CharField(choices=[('Ibrahim', 'Respondent is Ibrahim'), ('Sahr', 'Respondent is Sahr'), ('Sahal', 'Respondent is Sahal'), ('Omar', 'Respondent is Omar'), ('Eman', 'Respondent is Eman'), ('Douglas', 'Respondent is Douglas'), ('Christopher', 'Respondent is Christopher'), ('Philip', 'Respondent is Philip'), ('Theresa', 'Respondent is Theresa'), ('Tracy', 'Respondent is Tracy')], default=None, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='investment',
            name='user_bonus',
            field=models.IntegerField(choices=[(2, 'User received a bonus of $2'), (0, 'User received no bonus ($0)')], default=None, null=True),
        ),
    ]