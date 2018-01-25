import os
import dj_database_url
from decouple import config

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', default=True, cast=bool)

# django-compress
COMPRESS_ENABLED = True
COMPRESS_OFFLINE = False
COMPRESS_STORAGE = "django.contrib.staticfiles.storage.CachedStaticFilesStorage"

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

ALLOWED_HOSTS = ['.localhost', '.herokuapp.com']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'compressor',
    'social_django',

    'core.rh',
    'core.servico',
    'core.tag',
    'core.galeria',
    'core.comentario',
    'core.anexo',
    'core.post',
    'dashboard',
    'widget_tweaks'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

    'social_django.middleware.SocialAuthExceptionMiddleware',
    'core.rh.middleware.user_type.UserTypeMiddleware',
)

ROOT_URLCONF = 'project.urls'

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
# 
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]


AUTHENTICATION_BACKENDS = (
    # 'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.open_id.OpenIdAuth',  # for Google authentication
    'social_core.backends.google.GoogleOpenId',  # for Google authentication
    'social_core.backends.google.GoogleOAuth2',  # for Google authentication
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/



LOGIN_URL = 'login'
LOGOUT_URL = '/'
LOGIN_REDIRECT_URL = 'perfil'

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
    'social_core.pipeline.social_auth.associate_by_email',
    # 'apps.users.pipeline.get_avatar'
)

SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['username', 'first_name', 'last_name', 'email']

SOCIAL_AUTH_TWITTER_KEY = 'gi8pAoPKh9Qw46pzAeG8b5JWv'
SOCIAL_AUTH_TWITTER_SECRET = 'Dhdy944oZ26XcWT0JDlEOwcvcy0rFUXMdgPaBnbADS048hiK16'

SOCIAL_AUTH_FACEBOOK_KEY = '541656296181952'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = 'cca5eb11728456aa5fc92f150e8d6d0f'  # App Secret
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id,name,email', 
}

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '1095358520833-cmssjplolkklq006l5baivg5b183id26.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'NZrPLLL8wVp6caLiUB7-l_tq'

SOCIAL_AUTH_GOOGLE_OAUTH2_IGNORE_DEFAULT_SCOPE = True
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
'https://www.googleapis.com/auth/userinfo.email',
'https://www.googleapis.com/auth/userinfo.profile'
]
# Google+ SignIn (google-plus)
SOCIAL_AUTH_GOOGLE_PLUS_IGNORE_DEFAULT_SCOPE = True
SOCIAL_AUTH_GOOGLE_PLUS_SCOPE = [
'https://www.googleapis.com/auth/plus.login',
'https://www.googleapis.com/auth/userinfo.email',
'https://www.googleapis.com/auth/userinfo.profile'
]

# SOCIAL_AUTH_LOGIN_ERROR_URL = '/settings/'
# SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/settings/'
# SOCIAL_AUTH_RAISE_EXCEPTIONS = False

# SOCIAL_AUTH_USER_MODEL = 'rh.Aluno'

TINYMCE_DEFAULT_CONFIG = {
   'theme': 'advanced',
   'theme_advanced_buttons1': 'bold,italic,|justifyleft,justifycenter,justifyright,justifyfull,|,formatselect,fontselect,fontsizeselect',
   'theme_advanced_buttons2': 'cut,copy,paste|,search,replace,|,bullist,numlist,|,outdent,indent,blockquote,|,undo,redo,|,link,unlink,',
   'theme_advanced_buttons3': '',
   'theme_advanced_toolbar_location': 'top',
   'theme_advanced_toolbar_align': 'center',
   'paste_text_sticky': 'true',
   'paste_text_sticky_default': 'true',
   'valid_styles': 'font-weight,font-style,text-decoration',
   'width': "100%",
   'theme_advanced_resizing': "true",
}

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'socialstudentt@gmail.com'
EMAIL_HOST_PASSWORD = 'SocialStudent**'