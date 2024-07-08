import os
from django.db import models
from django.contrib.auth.models import User
# Import the deconstructible decorator to make a class or function serializable for use in migrations.
from django.utils.deconstruct import deconstructible

@deconstructible
class GenerateProfileImagePath(object):
    """
    A callable class to generate file paths for user profile images.
    """
    def __init__(self) -> None:
        # Constructor method (not doing anything here, but necessary for the class definition).
        pass

    def __call__(self, instance, filename) -> str:
        """
        Generates a file path for a user's profile image.
        
        Args:
            instance: The instance of the model where the image is being attached.
            filename: The original filename of the uploaded image.

        Returns:
            str: The generated file path.
        """

        # Extract the file extension from the uploaded file's name.
        ext = filename.split('.')[-1]

        # Define the directory path using the user's ID.
        path = f'media/accounts/{instance.user.id}/images/'

        # Define the new file name with the same extension but a standard name.
        name = f'profile_image.{ext}'

        # Join the directory path and file name to create the full file path.
        return os.path.join(path, name)

# Create an instance of the GenerateProfileImagePath class to use as the upload_to parameter in the ImageField.
user_profile_image_path = GenerateProfileImagePath()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=user_profile_image_path, blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.user.username} Profile'