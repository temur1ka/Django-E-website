# Generated by Django 4.2.5 on 2023-11-08 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_checkout_session_id', models.CharField(blank=True, max_length=220, null=True)),
                ('completed', models.BooleanField(default=False)),
                ('stripe_price', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]