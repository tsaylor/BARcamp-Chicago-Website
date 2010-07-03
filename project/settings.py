import os
from django.conf import global_settings
# Django settings for project project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = '/home/eviljoel/Desktop/BARcamp Chicago 2010/premiumWebsiteSqlite/sqliteDb'             # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = '/home/eviljoel/Desktop/BARcamp Chicago 2010/premiumWebsite/media/'
MEDIA_SERVE = True

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/admin/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'l;kjasd on9;fu890 ;2LKSJD;IOU FOP9;U2kl*&(*&*()sjdfliuei jlisja l92u '

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',

    'sphene.community.groupaware_templateloader.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',

    'sphene.community.middleware.ThreadLocals',
    'sphene.community.middleware.GroupMiddleware',
)

ROOT_URLCONF = 'project.urls'

TEMPLATE_DIRS = ( "/home/eviljoel/Desktop/BARcamp Chicago 2010/premiumWebsite/website/templates"
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
)

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'sphene.community.context_processors.navigation',
    'django.core.context_processors.request',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',

    'mptt',
    'tagging',
    'tinymce',
#    'filebrowser',

    'feincms',
#    'feincms.module.blog',
    'feincms.module.page',

    'sphene.sphwiki',
    'sphene.community',

    'website',
)

FEINCMS_ADMIN_MEDIA = '/media/feincms/'

TINYMCE_JS_URL = MEDIA_URL + 'tinymce/jscripts/tiny_mce/tiny_mce.js'
TINYMCE_JS_ROOT = MEDIA_ROOT + 'tinymce/jscripts/tiny_mce'
TINYMCE_SPELLCHECKER = False
TINYMCE_FILEBROWSER = False
TINYMCE_DEFAULT_CONFIG = {
    'theme': "advanced", 
    'relative_urls': False,
    'theme_advanced_toolbar_location' : "top",
    'theme_advanced_toolbar_align' : "left",
    'plugins' : "table",
    'plugins' : "paste",
    'theme_advanced_buttons3_add' : "tablecontrols",
    'document_base_url': "http://barcampchicago.com/",
    'theme_advanced_resizing': True,
    'theme_advanced_statusbar_location' : "bottom",
    'theme_advanced_styles' : "Header 1=header1;Header 2=header2;Header 3=header3;Table Row=tableRow1",
    'theme_advanced_buttons3_add' : "pastetext,pasteword,selectall",
    'gecko_spellcheck' : True,
}

FILEBROWSER_URL_FILEBROWSER_MEDIA = MEDIA_URL + 'filebrowser/'
FILEBROWSER_PATH_MEDIA = MEDIA_ROOT + 'filebrowser/'
FILEBROWSER_URL_TINYMCE = TINYMCE_JS_URL[:TINYMCE_JS_URL.rfind('/')] + '/'
FILEBROWSER_PATH_TINYMCE = TINYMCE_JS_ROOT
FILEBROWSER_DEBUG = True

try:
    from settings_local import *
except:
    pass
