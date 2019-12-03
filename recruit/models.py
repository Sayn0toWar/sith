from django.db import models


class Planet(models.Model):
    name = models.CharField(unique=True, max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Recruit(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=100)
    age = models.PositiveSmallIntegerField(default=0)
    planet = models.ForeignKey(Planet, to_field='name', on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)
    got_shadowhand = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Sith(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=100)
    planet = models.ForeignKey(Planet, to_field='name', on_delete=models.CASCADE)
    shadowhand_used = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class Question(models.Model):
    content = models.CharField(max_length=120)


class ShadowHand(models.Model):
    order_key = models.CharField(max_length=120)
    question_list = models.ManyToManyField(Question)

    def display_question_list(self):
        return ', '.join([question.content for question in self.question_list.all()])
    display_question_list.short_description = 'questions'


class Answer(models.Model):
    recruit_name = models.CharField(max_length=100)
    answers = models.TextField()

    def get_recruit_answers(self):
        return self.answers

