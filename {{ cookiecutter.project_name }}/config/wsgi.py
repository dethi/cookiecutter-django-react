"""
WSGI config for {{ cookiecutter.project_name }} project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
import sys
from pathlib import Path

from django.core.wsgi import get_wsgi_application

# This allows easy placement of apps within the interior {{ cookiecutter.project_slug }} directory.
root_path = Path(__file__).resolve().parent.parent
sys.path.append(root_path / '{{ cookiecutter.project_slug }}')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.prod")

application = get_wsgi_application()
