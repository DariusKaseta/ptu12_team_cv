# Generated by Django 4.2.2 on 2023-06-19 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ptu12_cv', '0002_remove_cv_country_code_remove_cv_extention_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='degree',
            field=models.CharField(db_index=True, default='---', max_length=100, verbose_name='degree'),
        ),
        migrations.AlterField(
            model_name='cv',
            name='scope',
            field=models.CharField(choices=[('IT', 'IT'), ('Marketing', 'Marketing'), ('Book_Keeping', 'Book Keeping'), ('Medicine', 'Medicine'), ('Human Resources', 'Human Resources'), ('Education', 'Education'), ('Economy', 'Economy'), ('Banking', 'Banking'), ('Engineering', 'Engineering'), ('Agro Culture', 'Agro Culture'), ('Biology', 'Biology'), ('Linguistics', 'Linguistics'), ('Service_Management', 'Service Management'), ('Graphic Design', 'Graphic Design'), ('Other', 'Other')], db_index=True, max_length=50, verbose_name='scope'),
        ),
        migrations.AlterField(
            model_name='education',
            name='school',
            field=models.CharField(choices=[('Middle', 'Middle School'), ('High', 'High School'), ('Home Schooling', 'Home Schooling'), ('Vocational', 'Vocational School'), ('University/College', 'University/College')], db_index=True, default='middle', max_length=100, verbose_name='school'),
        ),
    ]
