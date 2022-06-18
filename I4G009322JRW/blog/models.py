from django.db import models
from django.contrib.auth import get_user_model



STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

user = get_user_model()

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(user, on_delete=models.CASCADE)
    #created_date = models.DateTimeField(auto_now_add=True)
    #published_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    #def publish(self):
    #    self.published_date = timezone.now()
    #    self.save()
    # class Meta:
    #     ordering = ['-created_date']

    def __str__(self):
        return self.title + ' created by ' + str(self.author)