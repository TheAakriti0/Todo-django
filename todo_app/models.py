from django.db import models

# create table todo(
# id serial primary key,
# title varchar(255)
# );

# If there is nay change in models.py, run following:
# python manage.py makemigrations
# python manage.py migrate

class Todo(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    


