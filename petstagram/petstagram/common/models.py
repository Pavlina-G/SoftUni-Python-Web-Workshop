from django.db import models

from petstagram.photos.models import Photo

'''
The field Comment Text is required:
•	Comment Text - it should consist of a maximum of 300 characters
An additional field should be created:
•	Date and Time of Publication - when a comment is created (only), the date of publication is automatically generated
One more thing we should keep in mind is that the comment should relate to the photo 
'''


class PhotoComment(models.Model):
    MAX_TEXT_LENGTH = 300

    text = models.CharField(
        max_length=MAX_TEXT_LENGTH,
        null=False,
        blank=False,
    )

    publication_date_and_time = models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=True,
    )

    photo = models.ForeignKey(
        Photo,
        on_delete=models.RESTRICT,
        null=False,
        blank=True,
    )


class PhotoLike(models.Model):
    # field in relation is {NAME_OF_THIS_MODEL}_set - photo.photolike_set for PhotoLike, photo.photocomment_set for PhotoComment

    photo = models.ForeignKey(
        Photo,
        on_delete=models.RESTRICT,
        null=False,
        blank=True,
    )

# Later when there are users:
# user = models.ForeignKey(
#     User
# )
