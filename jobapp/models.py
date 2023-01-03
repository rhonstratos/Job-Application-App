from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.db.models.signals import post_save, post_init
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from twilio.rest import Client
User = get_user_model()


from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager


JOB_TYPE = (
    ('1', "Full time"),
    ('2', "Part time"),
    ('3', "Internship"),
)

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Job(models.Model):

    user = models.ForeignKey(User, related_name='User', on_delete=models.CASCADE) 
    title = models.CharField(max_length=300)
    description = RichTextField()
    tags = TaggableManager()
    location = models.CharField(max_length=300)
    job_type = models.CharField(choices=JOB_TYPE, max_length=1)
    category = models.ForeignKey(Category,related_name='Category', on_delete=models.CASCADE)
    salary = models.CharField(max_length=30, blank=True)
    company_name = models.CharField(max_length=300)
    company_description = RichTextField(blank=True, null=True)
    company_image = models.ImageField(blank=True, null=True, verbose_name='Company Image', upload_to='companyImage', default='profileImages/no-profile-picture-icon.webp')
    url = models.URLField(max_length=200)
    last_date = models.DateField()
    is_published = models.BooleanField(default=False)
    is_closed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


@receiver(post_init, sender=Job)
def remember_previous_state(sender, instance, **kwargs):
	instance.previous_state = instance.is_published

@receiver(post_save, sender=Job)
def send_notifcation(sender, instance, **kwargs):
	if instance.previous_state != instance.is_published:
		if instance.is_published:
			users = User.objects.filter(category=instance.category).values()
			account_sid = settings.TWILIO_ACCOUNT_SID
			auth_token = settings.TWILIO_AUTH_TOKEN
			client = Client(account_sid, auth_token)

			for singleuser in list(users):
				message = f"Hello {singleuser.get('first_name')} {singleuser.get('last_name')}! you might want to take a look at this newly posted job: {instance.title} located in {instance.location}."
				if singleuser.get('updateViaEmail'):
					send_mail(
						'New job posted on JobApp200',
						message,
						settings.EMAIL_HOST_USER,
						[singleuser.get('email')],
						fail_silently=False,
					)

				if singleuser.get('updateViaPhoneNumber'):
					sms=client.messages.create(
									body=message,
									from_='+18454421980',
									to=singleuser.get('phoneNumber')
								)
					print(sms.sid)
 

class Applicant(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)


    def __str__(self):
        return self.job.title


  

class BookmarkJob(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)


    def __str__(self):
        return self.job.title