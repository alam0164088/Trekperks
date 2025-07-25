from pathlib import Path

# প্রকল্পের মূল ফোল্ডার
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-your-secret-key-here'  # তোমার নিজস্ব সিক্রেট কী দিবে

DEBUG = True

ALLOWED_HOSTS = []  # ডেভেলপমেন্টে খালি রাখো, প্রডাকশনে তোমার ডোমেইন দিবে

# অ্যাপ্লিকেশনগুলো
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',  # DRF
    'loyalty',
    'users',           # তোমার কাস্টম ইউজার অ্যাপ
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# এখানে অবশ্যই প্রকল্পের মূল ফোল্ডারের নাম সঠিক দিতে হবে!
ROOT_URLCONF = 'trekpreks.urls'  

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # আলাদা টেমপ্লেট ফোল্ডার থাকলে এখানে দিবে
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

WSGI_APPLICATION = 'trekpreks.wsgi.application'  # প্রকল্পের মূল ফোল্ডারের নাম ঠিক রাখো

# ডাটাবেস (SQLite দিয়ে সহজে শুরু করার জন্য)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bot',       # তোমার ডাটাবেসের নাম
        'USER': 'postgres',       # ডাটাবেস ইউজারনেম (যেমন: postgres)
        'PASSWORD': 'nazmul13',  # ডাটাবেস পাসওয়ার্ড
        'HOST': 'localhost',          # সাধারণত লোকালহোস্ট হয়
        'PORT': '5432',               # ডিফল্ট পোর্ট, সাধারণত 5432 হয়
    }
}

# পাসওয়ার্ড ভ্যালিডেশন (ডিফল্ট)
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Django REST Framework সেটিংস (প্রয়োজনমতো পরিবর্তন করতে পারো)
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
}
