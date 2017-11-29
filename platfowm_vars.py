import os



def init_platform_vars():
    from sys import platform as _platform
    global dir_sep
    if _platform == "linux" or _platform == "linux2":
        # linux
        dir_sep = '/'
    # elif _platform == "darwin":
    #     # MAC OS X
    #     pass
    elif _platform == "win32":
        # Windows
        dir_sep = "\\"
    elif _platform == "win64":
        # Windows 64-bit
        dir_sep = "\\"
    else:
        raise OSError("OS not detected")


ROOTDIR = os.path.dirname(os.path.realpath(__file__))
dir_sep = ''
init_platform_vars()