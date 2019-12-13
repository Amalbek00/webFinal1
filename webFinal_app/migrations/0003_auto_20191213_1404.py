# Generated by Django 2.2.6 on 2019-12-13 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webFinal_app', '0002_auto_20191208_1850'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='carcase',
        ),
        migrations.RemoveField(
            model_name='car',
            name='transmission',
        ),
        migrations.RemoveField(
            model_name='car',
            name='type_of_drive',
        ),
        migrations.RemoveField(
            model_name='car',
            name='volume',
        ),
        migrations.AddField(
            model_name='car',
            name='about_car',
            field=models.TextField(default='foobar'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='email_of_user',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.CreateModel(
            name='Characteristics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volume_of_car', models.IntegerField()),
                ('type_of_drive', models.CharField(max_length=200)),
                ('transmission', models.CharField(max_length=50)),
                ('carcase', models.CharField(max_length=100)),
                ('cars', models.ForeignKey(on_delete='CASCADE', to='webFinal_app.Car')),
            ],
        ),
    ]
