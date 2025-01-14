# Generated by Django 5.0.4 on 2024-07-07 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_rename_graduates_item_graduate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='Graduate',
            new_name='Baranggay',
        ),
        migrations.AddField(
            model_name='item',
            name='Address',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='Btype',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='College',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='Cstatus',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='Dbirth',
            field=models.DateField(default='2000-01-01', null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='Elementary',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='Email',
            field=models.EmailField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='FatherFN',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='FatherLN',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='FatherMN',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='Fname',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='Graduates',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='Height',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='Lname',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='Mname',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='MotherFN',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='MotherLN',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='MotherMN',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='MotherMaidenN',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='Municipality',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='Phone',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='Secondary',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='Sex',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='Vcourse',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='Weight',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
