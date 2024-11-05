"""
ASGI config for text_extractor project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'text_extractor.settings')

application = get_asgi_application()