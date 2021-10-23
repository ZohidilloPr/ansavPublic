# Generated by Django 3.2.3 on 2021-10-05 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Ads', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='item_img')),
                ('itemname', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Ads.itemname')),
            ],
        ),
    ]
