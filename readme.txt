Use Python 3.6 or Higher and set it in path, Using Windows 10 x-64 Version
Open Command Prompt
mkdir myadvo
cd myadvo
python -m venv myvenv
myvenv\Scripts\activate
pip install --upgrade pip
pip install django
pip install selenium
Install GeckoDriver for Firefox https://github.com/mozilla/geckodriver/releases/download/v0.16.1/geckodriver-v0.16.1-win64.zip version v0.16.1
Extract the geckodriver.exe and paste in myadvo\myvenv\selenium\webdriver\firefox 
django-admin.py startproject mysite .
Open mysite/settings.py and change 
TIME_ZONE = 'Asia/Kolkata'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com']
python manage.py migrate
python manage.py startapp details_entry
In mysite/settings.py add
INSTALLED_APPS = [
					'details_entry'
				 ]
Create File details_entry/models.py
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
		
python manage.py makemigrations details_entry		

In details_entry/admin.py
from django.contrib import admin
from .models import Post

admin.site.register(Post)

python manage.py createsuperuser
admin
admin@admin.com
pranavchaturvedi

In mysite/urls.py
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('details_entry.urls')),
]

In details_entry/urls.py


In details_enitry/views.py
def post_list(request):
    return render(request, 'blog/post_list.html', {})

In details_entry/templates/details_entry cfreate file post_list.html	