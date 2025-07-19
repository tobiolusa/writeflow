from tortoise import fields, models

class Blog(models.Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    content = fields.TextField()
    author = fields.CharField(max_length=100)

    def __str__(self):
        return self.title