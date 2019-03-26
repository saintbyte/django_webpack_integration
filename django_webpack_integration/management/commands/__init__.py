__author__ = 'sb'

from django.core.management.base import BaseCommand
from django.conf import settings
import os
import json

class NeedFrontEndDirCommand(BaseCommand):
    def __init__(self, stdout=None, stderr=None, no_color=False):
        super().__init__(stdout, stderr, no_color)
        if not settings.FRONTEND_DIR:
            self.stdout.write(self.style.ERROR('Please set FRONTEND_DIR in settings.py'))
            quit()
        if not os.path.isdir(settings.FRONTEND_DIR):
            self.stdout.write(self.style.ERROR('FRONTEND_DIR not found'))
            self.stdout.write(self.style.ERROR('FRONTEND_DIR is: {}'.format(settings.FRONTEND_DIR)))
            quit()


class NeedPackageJsonCommand(NeedFrontEndDirCommand):
    package_json_filepath = ''
    package_json_obj = {}

    def __init__(self, stdout=None, stderr=None, no_color=False):
        super().__init__(stdout, stderr, no_color)
        self.package_json_filepath = os.path.join(settings.FRONTEND_DIR,'package.json')
        if not os.path.exists(self.package_json_filepath):
            self.stdout.write(self.style.ERROR('File package.json not found in FRONTEND_DIR'))
            self.stdout.write(self.style.ERROR('May should run "npm init" ?'))
            self.stdout.write(self.style.ERROR('Full package.json path:{}'.format(self.package_json_filepath)))
            quit()
        try:
            fh = open(self.package_json_filepath)
            self.package_json_obj = json.load(fh)
            fh.close()
        except:
            self.stdout.write(self.style.ERROR('Can\'t decode json from package.json'))
            self.stdout.write(self.style.ERROR('May should run "npm init" ?'))
            self.stdout.write(self.style.ERROR('Full package.json path:{}'.format(self.package_json_filepath)))
            quit()

