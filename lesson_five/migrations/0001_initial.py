# Generated by Django 3.0.3 on 2020-02-27 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Имя автора')),
                ('surname', models.CharField(max_length=200, verbose_name='Фамилия автора')),
                ('city', models.CharField(choices=[('kyiv', 'Киев'), ('chernigov', 'Чернигов'), ('odessa', 'Одесса'), ('lvov', 'Львов')], help_text='Выберите город со списка', max_length=200, verbose_name='Город')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('text', models.TextField(max_length=500, verbose_name='Текст статьи')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lesson_five.Author1', verbose_name='Автор статьи')),
            ],
        ),
    ]
