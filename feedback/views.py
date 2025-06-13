from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FeedbackForm

def send_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save()
            # Формируем сообщение
            subject = settings.FEEDBACK_EMAIL_SUBJECT
            message = f'''
                Новое сообщение обратной связи:

                Имя: {feedback.name}
                Email: {feedback.email}
                Сообщение: {feedback.message}

                Дата: {feedback.created_at}
            '''

            # Отправляем email
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                settings.FEEDBACK_EMAILS,
                fail_silently=False,
            )
            messages.success(request, 'Ваше сообщение успешно отправлено! Мы свяжемся с вами в ближайшее время.')
            return redirect('main:index')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
    return redirect('main:index')
