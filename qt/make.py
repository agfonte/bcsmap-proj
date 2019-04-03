from pathlib import WindowsPath
import os


dir_ = WindowsPath(os.getcwd())
par_ = dir_.parent
out_ = par_.joinpath('app\\synchro\\uiforms')

for child in filter(lambda f : f.is_file(), dir_.iterdir()):
    if child.suffix == '.ui':
        cmd_ = 'pyuic5 -o "{}" "{}"'.format(out_.joinpath(child.with_suffix('.py').name), child)
        os.system(cmd_)