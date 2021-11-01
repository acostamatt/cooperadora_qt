#!/bin/bash
mkdir -p ../src/views/base
pyrcc5 -o ../src/resources.py ../qrc/resources.qrc 
pyuic5 ../ui/form_alumno_base.ui -o ../src/views/base/form_alumno_base.py
pyuic5 ../ui/form_socio_base.ui -o ../src/views/base/form_socio_base.py
pyuic5 ../ui/table_window_default.ui -o ../src/views/base/table_window_default.py
pyuic5 ../ui/login_base.ui -o ../src/views/base/login_base.py

pyuic5 ../ui/main_window_base.ui -o ../src/views/base/main_window_base.py
pyuic5 ../ui/table_view_alumno.ui -o ../src/views/base/table_view_alumno.py
pyuic5 ../ui/table_view_socio.ui -o ../src/views/base/table_view_socio.py

python replace_script.py
