from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50)),
                ('cnpj', models.CharField(db_index=True, max_length=50)),
                ('mail', models.CharField(db_index=True, max_length=50)),
                ('address', models.CharField(db_index=True, max_length=50)),
                ('data_created', models.DateTimeField(auto_now_add=True)),
                ('data_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
