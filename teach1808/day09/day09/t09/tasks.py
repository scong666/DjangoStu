import time
from celery import task

@task
def test(n):
    print("税后工资10000")
    time.sleep(n)
    print("税后1000")
    return