from django.db import models
from django.contrib.auth.models import User
from batches.models import Slots, Month

# Create your models here.
class UserModel(User):
    fullname = models.CharField(max_length=100)
    age = models.IntegerField(null=False)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def get_full_name(self):
        return self.fullname

    def __str__(self):
        return self.get_full_name()


class ProfileModel(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)
    premium = models.BooleanField(default=False)
    batch_slots = models.IntegerField(choices=Slots, default=0)  # 0 for no batch
    batchmonth = models.CharField(choices=Month, max_length=3, default="N/A")
    batch_fee = models.IntegerField(default=500)

    def __str__(self):
        return self.user.username
