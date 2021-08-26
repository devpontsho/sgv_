__author__ = 'Pontsho Maseko'
__version__ = 1.0

import sys
import os
import shutil
import subprocess


def _copy_to(src: str, dest: str):

    # Try to delete if folder if does exist
    '''
    if not os.path.isdir(dest):
        try:
            os.remove(dest)
        except:
            raise PermissionError(f'[Build Remove] - Failed to delete - {dest}')
    '''

    # Try to copy to install path
    try:
        shutil.copytree(src, dest)
    except:
        raise ValueError(f'[Build Copy] - Failed to copy [{src}] to [{dest}]')


def _get_environment_value(name: str):

    value = os.environ.get(name)
    if value is None:
        raise ValueError(f'Environment Variable does not exist : {name}')
    
    return value

def build():

    print('Building SVG TO QT ...')

    # Install path
    install_path = _get_environment_value('REZ_BUILD_INSTALL_PATH')
    bin_install_dir = os.path.join(install_path, 'bin')
    py_package_install_dir = os.path.join(install_path, 'svg_to_qt', 'svg_to_qt')

    # Source Dir
    source_path = _get_environment_value('REZ_BUILD_SOURCE_PATH')

    source_content = os.listdir(source_path)
    for item in source_content:

        path = os.path.join(source_path, item)
        if item == 'bin':
            _copy_to(path, bin_install_dir)

        if item == 'svg_to_qt':
            _copy_to(path, py_package_install_dir)

    pipe = subprocess.Popen(
        f'chmod +x {bin_install_dir}/svg_to_qt', 
        shell=True,
        stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE
    )
    print(pipe.communicate(0))


if __name__ == '__main__':
    build()
