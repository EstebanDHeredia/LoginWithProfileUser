from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.


class Interest(models.Model):
    name = models.CharField(max_length=80, unique=True, verbose_name='Nombre')

    class Meta:
        verbose_name = 'Interés'
        verbose_name_plural = 'Intereses'
        ordering = ['name']

    def __str__(self) -> str:
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(
        default='users/default_profile_pict.jpeg', upload_to='users/')
    location = models.CharField(max_length=80, null=True, blank=True)
    bio = models.TextField(max_length=400, null=True, blank=True)
    interests = models.ManyToManyField(Interest, verbose_name="Intereses")

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
        ordering = ['-id']

# Función que crea el profile
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # Si el usuario fue creado --> creo un perfil para ese usuario
        Profile.objects.create(user=instance)

# Función que graba el profile
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()  # Grabo el profile

# Ahora conecto estas funciones con la señal de post_save y User
post_save.connect(create_user_profile, sender=User)
post_save.connect(save_user_profile, sender=User)