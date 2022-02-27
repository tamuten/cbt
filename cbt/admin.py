from django.contrib import admin

from .models import Thought, FeelVariation, Feeling, NewThinking

class NewThinkingInline(admin.StackedInline):
    model = NewThinking
    extra = 1

class FeelingInline(admin.StackedInline):
    model = Feeling
    extra = 2

class ThoughtAdmin(admin.ModelAdmin):
    inlines = [NewThinkingInline, FeelingInline]

admin.site.register(Thought, ThoughtAdmin)
admin.site.register(FeelVariation)
