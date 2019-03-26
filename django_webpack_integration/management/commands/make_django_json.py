__author__ = 'sb'

import json

from . import NeedFrontEndDirCommand
from django.conf import settings
import os
from django.contrib.staticfiles.finders import get_finders
import django


class Command(NeedFrontEndDirCommand):
    help = 'create django.json in FRONTEND_DIR'

    def handle(self, *args, **options):
        django_obj_for_json = {}
        django_obj_for_json['VERSION'] = django.VERSION
        django_obj_for_json['static_dirs'] = []
        for finder in get_finders():
            for key in list(finder.storages):
                django_obj_for_json['static_dirs'].append(finder.storages[key].location)
        django_json_file = os.path.join(settings.FRONTEND_DIR, 'django.json')
        fh = open(django_json_file, 'w')
        fh.write(json.dumps(django_obj_for_json))
        fh.close()
