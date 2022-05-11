from django.test import TestCase

# Create your tests here.
#https://stackoverflow.com/questions/9522759/imagefield-overwrite-image-file-with-same-name/9523400#9523400
class OverwriteStorage(FileSystemStorage):

    def get_available_name(self, name):
        """Returns a filename that's free on the target storage system, and
        available for new content to be written to.
        """
        # If the filename already exists, remove it as if it was a true file system
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name