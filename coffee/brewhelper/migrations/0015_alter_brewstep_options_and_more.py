# Generated by Django 5.0 on 2024-01-15 04:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brewhelper', '0014_recipe_reference_alter_brewstep_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brewstep',
            options={'ordering': ['brew_step_id']},
        ),
        migrations.RenameField(
            model_name='brewstep',
            old_name='step_id',
            new_name='brew_step_id',
        ),
        migrations.RemoveField(
            model_name='brewmethod',
            name='recipes',
        ),
        migrations.RemoveField(
            model_name='brewstep',
            name='description',
        ),
        migrations.RemoveField(
            model_name='brewstep',
            name='recipeID',
        ),
        migrations.AddField(
            model_name='recipe',
            name='methods',
            field=models.ManyToManyField(related_name='recipes', to='brewhelper.brewmethod'),
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step_id', models.PositiveIntegerField()),
                ('description', models.TextField(default='')),
                ('recipe', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='steps', to='brewhelper.recipe')),
            ],
            options={
                'ordering': ['step_id'],
            },
        ),
        migrations.AddField(
            model_name='brewstep',
            name='step',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='brewhelper.step'),
        ),
    ]
