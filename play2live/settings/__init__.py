try:
    from .dev import *
except Exception:
    print('Incorrect settings file. You should set dev setting file or use "settings" parameter in console')
