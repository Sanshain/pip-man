#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     01.02.2021
# Copyright:   (c) User 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os
import shutil
import re

get_parent = lambda path, deep=1: get_parent(os.path.dirname(path), deep - 1) if deep > 0 else path

def find_pipfile():
    root_path = os.path.join(get_parent(__file__, 5))
    pipfile_path = os.path.join(root_path, 'Pipfile')
    if os.path.exists(pipfile_path):
        return pipfile_path, root_path
    else:
        return None, root_path

def create_pipfile(path):
    shutil.copyfile(
        os.path.join(os.path.dirname(__file__), 'Pipfile'),
        os.path.join(path, 'Pipfile')
    )
    require_file = os.path.join(path, 'requirements.txt')
    if os.path.exists(require_file):
        with open(require_file, 'r') as eyes:
            requirements = eyes.readlines()
        with open(pipfile, 'rw') as pen:
            lines = pen.readlines()
            packages_line = lines.index(f'[{pack_mode}]')  # package
            packages_lines = re.sub(r'==([\d\.\*\~]+)', ' = "==$1"', requirements)
            for pack in packages_lines:
                lines.insert(packages_line, pack + ' = "*"')
            pen.writelines(lines)
        return True

