"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from aws_secret_key import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'krrxp*=dxxne+u)8wbag35zl%lkfq1xz%jpl_m3ine!m=t11#z'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'django_extensions',
    'rest_framework',
    'drf_yasg',
    # 'rest_framework_swagger',
    'rest_framework.authtoken',
    'corsheaders',
    'accounts',
    'products',
    'community',
    'django_crontab',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'house_of_today',
        'USER': RDS_MASTER_ID,
        'PASSWORD': RDS_MASTER_PW,
        'HOST': 'house-of-today.cnuxbldx8kex.ap-northeast-2.rds.amazonaws.com',
        'POST': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
AWS_ACCESS_KEY_ID = ADMIN_AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY = ADMIN_AWS_SECRET_ACCESS_KEY

AWS_REGION = 'ap-northeast-2'
AWS_STORAGE_BUCKET_NAME = 'static.house-of-today.jinukk.me'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.%s.amazonaws.com' % (AWS_STORAGE_BUCKET_NAME, AWS_REGION)
# AWS_S3_CUSTOM_DOMAIN = AWS_STORAGE_BUCKET_NAME
AWS_S3_SECURE_URLS = False

AWS_S3_FILE_OVERWRITE = False
# True일 경우 같은 파일을 올렸을 때 덮어씌워진다.
# False를 하면 같은 파일이 올라와도 덮어씌워지지 않게 파일 이름을 자동으로 바꿔줌

# 브라우저가 해당 파일에 접속 했을 때 나타나는 파라미터 값
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}

# 지금올리는 파일의 권한을 지정해줌
AWS_DEFAULT_ACL = 'public-read'

AWS_LOCATION = ''

STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

DEFAULT_FILE_STORAGE = 'config.s3media.MediaStorage'
# STATIC_URL = '/static/'

# Debug Toolbar
INTERNAL_IPS = ['127.0.0.1']

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]

AUTH_USER_MODEL = 'accounts.User'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'accounts.backends.EmailBackend',
    'accounts.backends.SocialLoginBackend',
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    # 'DEFAULT_FILTER_BACKENDS': (
    #     'django_filters.rest_framework.DjangoFilterBackend',
    #     'rest_framework.filters.SearchFilter'
    # )
}

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        "api_key": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header"
        }
    }
}

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True


# python manage.py crontab add 를 통해 실행중인 경우,
# settings.py의 CRONJOBS를 변경하게 되면 무조건 python manage.py crontab remove 후
# 다시 python manage.py crontab add를 해줘야 한다!!!! 안그러면 에러 발생한다!!
CRONJOBS = [
    ('0 0 * * *', 'products.cron.products_todaydeal'),
    ('0 0 * * *', 'community.cron.community_todaystory'),
]


# 환경 변수 추가 : https://cafe.naver.com/plan99/852
# https://brownbears.tistory.com/15
# 실제 만드는 법 : http://greenyant.blogspot.com/2015/04/django-crontab-quick-start-model-check.html

# 한글 출력 관련 확인 명령어 : $ echo $LANG

# 크론탭 실행 : python manage.py crontab show
# 크론탭 추가 : python manage.py crontab add
# 크론탭 삭제 : python manage.py crontab remove

# 등록된 크론탭 확인 명령어 : $ crontab -l
# 크론탭 설정 : $ crontab -e

# ('분 시 일 월 요일 명령어','앱이름.파일명.함수명')
# 첫번째 (분) : 0~59
# 두번째 (시) : 0~23
# 세번째 (일) : 0~31
# 네번째 (월) : 1~12
# 다섯번째 (요일) : 0~7 (0 또는 7 일요일, 1=월요일, 2=화요일, ...)
# 여섯번째 (명령어) : 실행할 명령어를 한줄로 작성.

# Example)
# ('*/1 * * * *', 'products.cron.my_scheduled_job') -> 1분마다 실행
# ('* */0 * * *', 'products.cron.my_scheduled_job') -> 매일 자정 0시마다 실행.

# 로그 관련 파일 남기는 법. 단, 예시가 없어서 아직 미구현 상태.. 시간 될때 봐야할듯 합니다.
# ('*/1 * * * *', 'products.cron.my_scheduled_job', '>> '+BASE_DIR+'/log/log_file.log'),

