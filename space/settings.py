# typing support for django
import django_stubs_ext

from pathlib import Path
import environ

# Monkey patch stubs
django_stubs_ext.monkeypatch()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Initialize environment variables
# https://alicecampkin.medium.com/how-to-set-up-environment-variables-in-django-f3c4db78c55f
env = environ.Env()

environ.Env.read_env(env_file=Path(BASE_DIR / ".env"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY", default="moonlitsecret_key")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG")

# DEV or PROD environment
PIPLINE = env("PIPLINE", default="development")

if DEBUG:
    ALLOWED_HOSTS = ["*"]
else:
    # eg: .vercel.app 0.0.0.0
    # add space b/w hosts
    ALLOWED_HOSTS = env("DJANGO_ALLOWED_HOSTS").split(" ")

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Apps
    "blog",
    "newsletter",
    # Django hosts
    "django_hosts",
]

MIDDLEWARE = [
    # Django_host middleware
    "django_hosts.middleware.HostsRequestMiddleware",
    # Django_host middleware
    "django.middleware.security.SecurityMiddleware",
    # whitenoice middleware
    "whitenoise.middleware.WhiteNoiseMiddleware",
    # other django's middlewares
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # Django_host middleware
    "django_hosts.middleware.HostsResponseMiddleware",
]

ROOT_URLCONF = "space.urls"

# https://github.com/jazzband/django-hosts?tab=readme-ov-file#installation

ROOT_HOSTCONF = "space.hosts"

DEFAULT_HOST = "www"

# Templates

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # custom context processors
                "space.context_processors.newsletter_form",
            ],
        },
    },
]

WSGI_APPLICATION = "space.wsgi.application"

# Storages

STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases


if PIPLINE == "production":
    DATABASES = {"default": env.db_url("DATABASE_URL")}
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

STATIC_ROOT = Path(BASE_DIR / "staticfiles")

STATICFILES_DIRS = [Path(BASE_DIR / "static")]

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Configure SMTP
EMAIL_BACKEND = env("EMAIL_BACKEND")
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_PORT = env("EMAIL_PORT")
EMAIL_USE_TLS = env.bool("EMAIL_USE_TLS")
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")

DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL")

# Profile configs
PROFILE = {
    "name": env("PROFILE_NAME"),
    "aka": env("PROFILE_AKA"),
    "email": env("PROFILE_EMAIL"),
    "avatar": env(
        "PROFILE_AVATAR",
        default="/static/images/pfp.jpg",
    ),
    "bio": env("PROFILE_BIO"),
    "socials": {
        "github": env("GITHUB"),
        "discord": env("DISCORD"),
        "telegram": env("TELEGRAM"),
        "twitter": env("TWITTER"),
    },
}
