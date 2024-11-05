"""
WSGI config for text_extractor project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'text_extractor.settings')

application = get_wsgi_application()