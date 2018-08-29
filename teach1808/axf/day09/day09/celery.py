from __future__ import absolute_import
from django.conf import settings
import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTING_MODULE",'day09.settings')

app = Celery("hehe")

app.conf.CELERY_TIMEZONE = settings.TIME_ZONE

app.config_from_object("django.conf:settings")
# 如果你想让celery 自动发现你的任务 你就需要在app目录下 新建一个叫tasks.py文件
app.autodiscover_tasks(lambda:settings.INSTALLED_APPS)