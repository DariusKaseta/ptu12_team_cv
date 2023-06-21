# Generated by Django 4.2.2 on 2023-06-21 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ptu12_cv', '0005_cv_about_user_delete_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='scope',
            field=models.CharField(choices=[('IT', 'IT'), ('Marketing', 'Marketing'), ('Book Keeping', 'Book Keeping'), ('Medicine', 'Medicine'), ('Human Resources', 'Human Resources'), ('Education', 'Education'), ('Economy', 'Economy'), ('Banking', 'Banking'), ('Engineering', 'Engineering'), ('Agro Culture', 'Agro Culture'), ('Biology', 'Biology'), ('Linguistics', 'Linguistics'), ('Service Management', 'Service Management'), ('Graphic Design', 'Graphic Design'), ('Other', 'Other')], db_index=True, max_length=50, verbose_name='scope'),
        ),
        migrations.AlterField(
            model_name='education',
            name='school',
            field=models.CharField(choices=[('Middle School', 'Middle School'), ('High School', 'High School'), ('Home Schooling', 'Home Schooling'), ('Vocational School', 'Vocational School'), ('University/College', 'University/College')], db_index=True, default='middle', max_length=100, verbose_name='school'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='skill',
            field=models.TextField(max_length=4000, verbose_name='skill'),
        ),
    ]
