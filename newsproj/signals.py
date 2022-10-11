from django.db.models.signals import m2m_changed
from django.dispatch import receiver  # импортируем нужный декоратор
from django.core.mail import EmailMultiAlternatives  # импортируем класс для создание объекта письма с html
from django.template.loader import render_to_string  # импортируем функцию, которая срендерит наш html в текст
from .models import New, Category, NewCategory, Author, SubscribeCategory
from django.contrib.auth.models import Group, User

@receiver(m2m_changed, sender=Category)
def notify_news_create(sender, instance, action, **kwargs):
    # print(instance, '2-gth')
    if action == 'signal_create':
        for cat in instance.post_category.all():
            for subscribe in SubscribeCategory.objects.filter(category=cat):

                msg = EmailMultiAlternatives(
                    subject=instance.headline,
                    body=instance.description,
                    from_email='schersvetlana@yandex.ru',
                    to=[subscribe.subscribeUser.email],
                )

                html_content = render_to_string(
                    'signal_create.html',
                    {
                        'newss': instance.description,
                        'recipient': subscribe.subscribeUser.email,
                        'category_name': subscribe.category_new,
                        'subscriber_user': subscribe.subscribeUser,
                        'pk_id': instance.pk,
                    },
                )

                msg.attach_alternative(html_content, "news/html")
                msg.send()