import os
import subprocess
# from shutil import copyfile, copytree

def find_file(path, filename):
    for root, dirs, files in os.walk(path):
        return True if filename in files else False


def find_dir(path, dirname):
    for root, dirs, files in os.walk(path):
        return True if dirname in files else False


def install_vim():
    print 'installing Vim'
    subprocess.call('sudo apt-get install vim', shell=True)


def update_vim():
    print 'updating Vim'
    subprocess.call('sudo apt-get install vim', shell=True)


def update_install(installed):
    if installed: update_vim(); install_vim()


def absolute_path(path=''):
    return os.path.expanduser('~') + '/' + path


def backup_vimrc():
    print 'backing up .vimrc'
    found_vimrc = find_file(absolute_path(), '.vimrc')
    if found_vimrc: os.rename(absolute_path('.vimrc'), absolute_path('.vimrc.before_vimvim.bak'))


def backup_dotvim():
    print 'backing up .vim file'
    found_dotvim = find_dir(absolute_path(), '.vim')
    if found_dotvim: os.rename(absolute_path('.vim/'), absolute_path('.vim.before_vimvim.bak/'))
    

def main():
    installed = find_file('/usr/bin/', 'vim.basic')
    update_install(installed)
    backup_vimrc()
    backup_dotvim()


if __name__ == '__main__':
    main()
