from django.db import models

from django.contrib.auth import get_user_model

class Comment(models.Model):
  body = models.CharField(max_length=300)

  owner = models.ForeignKey(
    get_user_model(),
    related_name='comments',
    on_delete=models.CASCADE
  )

  post_id = models.ForeignKey('Post', related_name='comments',
  on_delete=models.CASCADE)

  def __str__(self):
    return f"The comment body is {self.body}"

  def as_dict(self):
    """Dictionary version of Comment model"""
    return {
      'id': self.id,
      'body': self.body
    }
