from django.contrib import admin
from .models import Sith, Planet, ShadowHand, Question, Recruit, Answer


class SithAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', ), }
    list_display = ('name', 'slug', 'planet', )


admin.site.register(Sith, SithAdmin)


class PlanetAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', ), }
    list_display = ('name', 'slug', )


admin.site.register(Planet, PlanetAdmin)


class ShadowHandAdmin(admin.ModelAdmin):
    list_display = ('order_key', 'display_question_list', )


admin.site.register(ShadowHand, ShadowHandAdmin)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('content', )


admin.site.register(Question, QuestionAdmin)


class RecruitAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'age', 'planet', 'email', 'got_shadowhand', )


admin.site.register(Recruit, RecruitAdmin)


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('recruit_name', 'answers', )


admin.site.register(Answer, AnswerAdmin)
