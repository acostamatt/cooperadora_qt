import os, sys

if sys.platform == "win32":
    path_login = r'../src/views/base/login_base.py'
else:
    path_login = '../src/views/base/login_base.py'

file_content = open(path_login, 'r')
content_data = file_content.read()
content_data = content_data.replace('resources_rc','resources')
file_content.close()
open(path_login, 'w').write(content_data)
