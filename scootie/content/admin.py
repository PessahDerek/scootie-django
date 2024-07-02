from django.contrib import admin

from content.models import Content, Review, Video, Faq, Contact

# Register your models here.
admin.site.register(Content)
admin.site.register(Contact)
admin.site.register(Review)
admin.site.register(Faq)
admin.site.register(Video)
