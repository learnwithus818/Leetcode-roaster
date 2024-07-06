from django.db import models

# Create your models here.

class userChatWithAI(models.Model):
    user = models.CharField(max_length=100)
    query = models.TextField()
    response = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.user) + ' ' + str(self.date)
    
    
