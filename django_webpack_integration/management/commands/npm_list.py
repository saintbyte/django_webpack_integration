__author__ = 'sb'

from . import NeedPackageJsonCommand

class Command(NeedPackageJsonCommand):
    help = 'npm list available command'

    def handle(self, *args, **options):
        try:
            scripts = self.package_json_obj['scripts']
            for name, cmd in scripts.items():
                self.stdout.write('{}: {}'.format(name,cmd))
        except:
            self.stdout.write(self.style.ERROR('Can\'t find "scripts" section in json from package.json'))
            self.stdout.write(self.style.ERROR('Full package.json path:{}'.format(self.package_json_filepath)))
            quit()
