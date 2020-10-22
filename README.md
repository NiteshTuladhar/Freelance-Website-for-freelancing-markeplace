# Freelance-Website-for-freelancing-markeplace
This is a Website of a marketplace for freelancers


Packages/Library Installed

pip install Pillow

for environment variables:
	pip install django-getenv
	pip install django-environ

for countries:
	pip install django-countries

for languages:
	pip install django-languages-plus

for thumbnai generatiion:
	pip install easy-thumbnails(Add easy_thumbnails to your INSTALLED_APPS setting:)

for Login through social accounts
	pip install social-auth-app-django
	add social_django in setting.py
	then migrate.(This will handle all the OAuth2 applications)

	add in setting.py
	AUTHENTICATION_BACKENDS = [
    		'social.core.backends.github.GithubOAuth2',
    		'social.core.backends.google.GoogleOAuth2',
    		'django.contrib.auth.backends.ModelBackend', //Her django.contrib..... is used as when we use the social backends like the above two the defaut 
							login backend of dajngo does not work so we need to add the normal login backends.
	]

	'social_django.middleware.SocialAuthExceptionMiddlewarre',  add In MIDDLEWARE[]


	'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',  add in TEMPLATES


	 (in url.py)
	from django.conf.urls import url, include  

	url(r'^oauth/', include('social_django.urls', namespace='social')),