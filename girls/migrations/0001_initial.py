# Generated by Django 3.2.9 on 2021-11-18 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryGirls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=25)),
                ('keywords', models.CharField(blank=True, max_length=150)),
                ('description', models.CharField(blank=True, max_length=150)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Girls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=25)),
                ('last_name', models.CharField(blank=True, max_length=25)),
                ('age', models.IntegerField()),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('color', models.CharField(choices=[(1, 'Choco'), (2, 'Blondinka'), (3, 'Rijinkiy'), (4, 'Jaydari')], default=1, max_length=15)),
                ('figure', models.CharField(choices=[('1', '90*60*90'), ('2', 'va boshqalar')], default='1', max_length=20)),
                ('hair', models.CharField(blank=True, max_length=30)),
                ('image', models.ImageField(upload_to='media/')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='girls.categorygirls')),
            ],
        ),
    ]
