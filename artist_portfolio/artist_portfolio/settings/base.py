"""
Base settings for the *artist_portfolio* Django / Wagtail project.

Split‑settings pattern:
• **base.py**  – shared defaults for every environment
• **dev.py**   – development overrides
• **prod.py**  – production overrides (import this in Docker/Render)
"""

from pathlib import Path
import os

from dotenv import load_dotenv

# ────────────────────────────────────────────────────────────────────────────────
# Paths
# ────────────────────────────────────────────────────────────────────────────────
BASE_DIR: Path = Path(__file__).resolve().parent.parent.parent  # repo root
PROJECT_DIR: Path = BASE_DIR / "artist_portfolio"              # project package

# Load key‑value pairs from a local .env file (ignored by Git)
load_dotenv(BASE_DIR / ".env")

# ────────────────────────────────────────────────────────────────────────────────
# Core config & security
# ────────────────────────────────────────────────────────────────────────────────
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "insecure-dev-key-change-me")
DEBUG: bool = os.getenv("DEBUG", "True") == "True"
ALLOWED_HOSTS: list[str] = os.getenv(
    "ALLOWED_HOSTS", "localhost,127.0.0.1"
).split(",")

# ────────────────────────────────────────────────────────────────────────────────
# Applications
# ────────────────────────────────────────────────────────────────────────────────
INSTALLED_APPS: list[str] = [
    # Project apps
    "home",
    "search",
    # Your custom apps – add here
    # "gallery",
    # "contact",
    # Third‑party / Wagtail
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail",
    "modelcluster",
    "taggit",
    # Django core
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE: list[str] = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # static files in prod
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
]

ROOT_URLCONF = "artist_portfolio.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [PROJECT_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    }
]

WSGI_APPLICATION = "artist_portfolio.wsgi.application"

# ────────────────────────────────────────────────────────────────────────────────
# Database
# ────────────────────────────────────────────────────────────────────────────────
default_sqlite_path = BASE_DIR / "db.sqlite3"
DATABASES = {
    "default": {
        "ENGINE": os.getenv("DB_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.getenv("DB_NAME", default_sqlite_path),
        "USER": os.getenv("DB_USER", ""),
        "PASSWORD": os.getenv("DB_PASSWORD", ""),
        "HOST": os.getenv("DB_HOST", ""),
        "PORT": os.getenv("DB_PORT", ""),
    }
}

# ────────────────────────────────────────────────────────────────────────────────
# Authentication & passwords
# ────────────────────────────────────────────────────────────────────────────────
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ────────────────────────────────────────────────────────────────────────────────
# Internationalisation
# ────────────────────────────────────────────────────────────────────────────────
LANGUAGE_CODE = os.getenv("LANGUAGE_CODE", "de-ch")
TIME_ZONE = os.getenv("TIME_ZONE", "Europe/Zurich")
USE_I18N = True
USE_TZ = True

# ────────────────────────────────────────────────────────────────────────────────
# Static & media files
# ────────────────────────────────────────────────────────────────────────────────
STATICFILES_DIRS = [PROJECT_DIR / "static"]  # your source assets
STATIC_ROOT = BASE_DIR / "staticfiles"       # collected by collectstatic
STATIC_URL = "/static/"

MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = "/media/"

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.ManifestStaticFilesStorage",
    },
}

# ────────────────────────────────────────────────────────────────────────────────
# Email (SMTP) – required for contact forms / notifications
# ────────────────────────────────────────────────────────────────────────────────
EMAIL_BACKEND = os.getenv(
    "EMAIL_BACKEND", "django.core.mail.backends.smtp.EmailBackend"
)
EMAIL_HOST = os.getenv("EMAIL_HOST", "smtp.resend.com")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", "587"))
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", "apikey")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", "")
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS", "True") == "True"
DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL", "noreply@example.com")

# ────────────────────────────────────────────────────────────────────────────────
# Wagtail settings
# ────────────────────────────────────────────────────────────────────────────────
WAGTAIL_SITE_NAME = "artist_portfolio"
WAGTAILADMIN_BASE_URL = os.getenv("WAGTAILADMIN_BASE_URL", "http://localhost:8000")

WAGTAILSEARCH_BACKENDS = {
    "default": {
        "BACKEND": "wagtail.search.backends.database",
    }
}

DATA_UPLOAD_MAX_NUMBER_FIELDS = 10_000  # complex StreamFields

# ────────────────────────────────────────────────────────────────────────────────
# Additional security tweaks for production
# ────────────────────────────────────────────────────────────────────────────────
if not DEBUG:
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 60 * 60 * 24 * 30  # 30 days
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
