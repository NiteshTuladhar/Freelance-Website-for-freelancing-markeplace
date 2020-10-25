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
	 'Social Login to Django' bookmarked in Django materials

	Changes to be made in that :
	callback url should be : localhost:8000 

	and add SOCIAL_AUTH_GITHUB_SCOPE = ['user : email'] for loggin in github