# We need to add some data into our model to make it "real" now. The official tutorial goes on a lengthy tangent into the Django shell at this point. However to beginners--and even professional programmers--the graphical Django admin is a more intuitive approach. That's what we'll use here.

# But first we need to update snippets/admin.py so the app will actually appear! Just as with the INSTALLED_APPS setting, apps must be explicitly added to the admin.
# snippets/admin.py
from django.contrib import admin
from .models import Snippet

admin.site.register(Snippet)

# Now create a superuser account for log in. Follow all the prompts for setting a username, email, and password. I've used admin, admin@email.com, and testpass123.