from django.db import models

from django.contrib.auth import get_user_model
# This method will locate the model that our project is using as the "User"

class Post(models.Model):
  # define the fields
  title = models.CharField(max_length=50)
  text = models.CharField(max_length=200)

  owner = models.ForeignKey(
    get_user_model(),
    related_name='posts',
    on_delete=models.CASCADE
  )

  def __str__(self):
    # Return a string
    return f"The post titled {self.title} has as text {self.text}"

  def as_dict(self):
    """Dictionary version of Post model"""
    return {
      'id': self.id,
      'title': self.title,
      'text': self.text
    }
