from app.core.celery_app import celery

@celery.task
def send_email_task(email:str):
    print(f"Sending email to {email}")
    return "Email sent"