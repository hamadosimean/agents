from django.db import models
from django.contrib.auth import get_user_model
import uuid
from general_settings.utils import TimeStampedModel
# Create your models here.

User = get_user_model()


# --------------------------------
# Question model
# --------------------------------
class Question(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.TextField()

    def __str__(self):
        return self.question


# --------------------------------
# Answer model
# --------------------------------
class Answer(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField()

    def __str__(self):
        return self.answer


# --------------------------------
# Knowledge model
# --------------------------------
class Knowledge(TimeStampedModel):
    """
    This model is used to store the knowledge of the assistant.
    It would retreive the knowledge from the file and use it to answer the questions.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to="knowledge/%Y/%m/%d/")

    def __str__(self):
        return self.name
