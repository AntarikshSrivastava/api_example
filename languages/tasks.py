from celery import shared_task


@shared_task
def mul():
    return "mul called"
