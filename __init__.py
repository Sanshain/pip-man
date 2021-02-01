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

import sys
import subprocess
import shutil

from pipfile import find_pipfile, create_pipfile

cmd_dict = {
    'i': {
        'help' : 'install package/packages',
        'shell' : 'install',
        'action' : lambda opt: 0,
        'options' : {
            '-D': 'dev-packages',
            None: 'packages',
        }
    },
    'u': {
        'help' : 'uninstall package/packages',
        'shell' : 'uninstall',
        'action' : lambda opts: 0
    },
    'init': {
        'help' : 'initialize new repozitory',
        'shell' : '',
    },
    'up':{
        'help' : 'update package/packages',
        'shell' : '',
    }
}



def main():
    cmd_arg = sys.argv[1] if len(sys.argv) > 1 else None
    cmd = cmd_dict.get(cmd_arg, None)
    args = sys.argv[2:] if cmd else []

    if not cmd:
        commands = '\n'.join([' '*12 + '- ' + c + f' ({o.get("help", "-")})' for c, o in cmd_dict.items()])
        print(f'''
            Usage: pm COMMAND [ARGS]...

            Commands:\n{commands}
            ''')
    else:
        pipfile, root_path = find_pipfile()

        shell_cmd = cmd.get('shell')
##        print(pipfile)
##        print(root_path)
##        subprocess.call("notepad.exe")
        out = subprocess.getoutput(f'cd {root_path} & pip {shell_cmd} {' '.join(args)}')

        if cmd == 'i':
            pack_mode = cmd.get('options', {}).get(args[-1] if len(args) else None)
            if not pipfile: create_pipfile(root_path)
            with open(pipfile, 'rw') as pen:
                lines = pen.readlines()
                packages_line = lines.index(f'[{pack_mode}]')  # package
                for pack in args:
                    lines.insert(packages_line, pack + ' = "*"')
                pen.writelines(lines)

##        print(sys.argv)


if __name__ == '__main__':
    main()









