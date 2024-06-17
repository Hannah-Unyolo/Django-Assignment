# Generated by Django 5.0.6 on 2024-06-14 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('code', models.PositiveBigIntegerField()),
                ('date_of_birth', models.DateField()),
                ('country', models.CharField(max_length=20)),
                ('bio', models.TextField()),
            ],
        ),

        migrations.CreateModel(
            name='Class',
            fields=[
                ('class_name', models.CharField(max_length=100)),
                ('class_code', models.CharField(max_length=20, unique=True)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('day_of_week', models.CharField(max_length=10)),
                ('room_number', models.CharField(max_length=10)),
                ('capacity', models.PositiveIntegerField()),
                ('current_enrollment', models.PositiveIntegerField(default=0)),
                ('teacher', models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True)),
                ('course', models.ForeignKey('Course', on_delete=models.CASCADE)),
                ('semester',models.CharField(max_length=20)),
                ('year', models.PositiveIntegerField()),
                
            ],
        ),




        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_name', models.CharField(max_length=100)),
                ('course_code', models.CharField(max_length=20, unique=True)),
                ('description', models.TextField()),
                ('credits', models.PositiveIntegerField()),
                ('department', models.CharField(max_length=50)),
                ('prerequisites', models.ManyToManyField('self', symmetrical=False, blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('level', models.CharField(max_length=20)),
                ('syllabus', models.FileField(upload_to='syllabi/', null=True, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),

                
            ],
        ),

         migrations.CreateModel(
            name='Teacher',
            fields=[
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(unique=True)),
                ('employee_id', models.CharField(max_length=20, unique=True)),
                ('date_of_birth', models.DateField()),
                ('department', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=15)),
                ('hire_date', models.DateField()),
                ('salary', models.DecimalField(max_digits=10, decimal_places=2)),
                ('education_level',models.CharField(max_length=50)),
                

                
            ],
        ),


    ]
