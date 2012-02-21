from django.contrib import admin
import ideas.ideasm as ideasm

admin.site.register(ideasm.models.Submitter)
admin.site.register(ideasm.models.Idea)
admin.site.register(ideasm.models.KVPairs)

