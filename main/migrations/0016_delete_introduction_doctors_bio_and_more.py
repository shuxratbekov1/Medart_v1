# Generated by Django 4.0.6 on 2022-09-13 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_rename_aboutus_block_aboutus_blog_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Introduction',
        ),
        migrations.AddField(
            model_name='doctors',
            name='bio',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='operationg_attented',
            name='participating_doctors',
            field=models.ManyToManyField(blank=True, null=True, to='main.doctors'),
        ),
    ]