
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('due_date', models.DateField(blank=True)),
                ('tags', models.CharField(blank=True, max_length=1000)),
                ('status', models.CharField(choices=[('O', 'OPEN'), ('W', 'WORKING'), ('D', 'DONE'), ('v', 'OVERDUE')], default='O', max_length=2)),
            ],
        ),
    ]
