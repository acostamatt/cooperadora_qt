#!/bin/bash
pyrcc5 -o ../src/resources.py ../qrc/resources.qrc 
pyuic5 ../ui/form_alumno_update.ui -o ../src/views/alumno/form_alumno_update.py
pyuic5 ../ui/form_socio_update.ui -o ../src/views/socio/form_socio_update.py 
pyuic5 ../ui/form_socio_base.ui -o ../src/views/socio/form_socio_base.py 
pyuic5 ../ui/form_window_default.ui -o ../src/views/main_window/form_window_default.py
pyuic5 ../ui/login_base.ui -o ../src/views/login/login_base.py

pyuic5 ../ui/main_window_base.ui -o ../src/views/main_window/main_window_base.py
pyuic5 ../ui/table_view_alumno.ui -o ../src/views/alumno/table_view_alumno.py
pyuic5 ../ui/table_view_socio.ui -o ../src/views/socio/table_view_socio.py

python replace_script.py
#sed -i -e 's/resources_rc/resources/g' ../src/views/login/login_base.py
