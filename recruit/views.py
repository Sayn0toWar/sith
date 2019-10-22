from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Recruit, Planet, Question, Answer, Sith
from django.utils.text import slugify
from django.urls import reverse
import smtplib
from email.mime.text import MIMEText


def index(request):
    return render(request, 'index.html', context={
    })


def recruit_1(request):
    planets = Planet.objects.all()
    recruits = Recruit.objects.all()

    return render(request, 'recruit-1.html', context={
        'planets': planets,
        'recruits': recruits,
    })


def recruit_2(request):
    available_questions = Question.objects.all()
    if request.method == 'POST':
        try:
            request.POST.get('recruit-input-planet')
        except (KeyError, request.POST.get('recruit-input-planet').DoesNotExist):
            pass
        else:
            name = request.POST.get('recruit-input-name')
            slug = slugify(name, allow_unicode=False)
            age = request.POST.get('recruit-input-age')
            planet = Planet.objects.get(slug=request.POST.get('recruit-input-planet'))
            email = request.POST.get('recruit-input-email')

            Recruit.objects.get_or_create(name=name, slug=slug, age=age, planet=planet, email=email)

    return render(request, 'recruit-2.html', context={
        'available_questions': available_questions,
        'name': name,
    })


def recruit_quest(request):
    if request.method == 'POST':
        available_questions = Question.objects.all()
        recruit_name = request.POST.get('recruit-name')
        recruit_answers = ''
        for i, question in enumerate(available_questions):
            print(i+1, question.content)
            if request.POST.get('question-' + str(i+1)) == 'on':
                user_answer = True
            else:
                user_answer = False
            recruit_answers += str(question.content) + ':' + str(user_answer) + ', '
        Answer.objects.get_or_create(recruit_name=recruit_name, answers=recruit_answers)

        return HttpResponseRedirect(reverse('index'))

    return HttpResponseRedirect(reverse('index'))


def sith_choice(request):
    sith_list = Sith.objects.all()
    return render(request, 'sith-choice.html', context={
        'sith_list': sith_list,
    })


def sith_page(request, slug):
    sith = Sith.objects.get(slug=slug)
    all_siths = Sith.objects.all()
    recruits_tested = zip(Recruit.objects.all(), Answer.objects.all())

    return render(request, 'sith-page.html', context={
        'sith': sith,
        'all_siths': all_siths,
        'recruits_tested': recruits_tested,
    })


def shadow_hand(request):
    shadow_hand_user = request.POST.get('shadow-hand-user')
    shadow_hand_user_obj = Sith.objects.get(slug=shadow_hand_user)
    try:
        recruit_slug = request.POST.get('recruit-shadow-handed')
    except (KeyError, request.POST.get('recruit-shadow-handed').DoesNotExist):
        pass
    else:
        if shadow_hand_user_obj.shadowhand_used < 3:
            shadow_hand_user_obj.shadowhand_used += 1
            shadow_hand_user_obj.save()

            recruit = Recruit.objects.get(slug=recruit_slug)
            recruit.got_shadowhand = True
            recruit.save()

            mail_from = 'sith-order@tempr.email'
            mail_to = str(recruit.email)
            smtp_server = 'smtp.mail.ru'
            msg = MIMEText('Сообщение от ордена Ситхов')
            msg['Subject'] = 'Сообщение от ордена Ситхов'
            msg['From'] = mail_from
            msg['To'] = mail_to
            server = smtplib.SMTP(smtp_server)
            try:
                server.login('Sith-order', '123empirerules')
                server.sendmail(mail_from, [mail_to], msg.as_string())
            except Exception:
                server.quit()
            else:
                pass

    return HttpResponseRedirect(reverse('sith-page', args=(shadow_hand_user,)))
