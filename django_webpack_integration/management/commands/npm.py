__author__ = 'sb'

from django.core.management.base import BaseCommand
from django.conf import settings
import os
from django.core.management import call_command
from . import NeedPackageJsonCommand

class Command(NeedPackageJsonCommand):
    help = 'run npm command'
    ignore_patterns = []

    def create_parser(self, prog_name, subcommand):
        parser = super().create_parser(prog_name, subcommand)
        npm_scripts_allow_arr = []
        try:
            scripts = self.package_json_obj['scripts']
            for name, cmd in scripts.items():
                npm_scripts_allow_arr.append(name)
        except:
            self.stdout.write(self.style.ERROR('Can\'t find "scripts" section in json from package.json'))
            self.stdout.write(self.style.ERROR('Full package.json path:{}'.format(self.package_json_filepath)))
            quit()
        parser.add_argument('npm_script', nargs=1, type=str, default='',choices=npm_scripts_allow_arr)
        return parser

    def handle(self, *args, **options):
        call_command('make_django_json')
        os.chdir(settings.FRONTEND_DIR)
        os.system('npm run ' + options['npm_script'][0])
