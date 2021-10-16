from django.contrib import admin
from .models import Poll,Vote,PollOption

admin.site.register(Poll)
admin.site.register(PollOption)
admin.site.register(Vote)

