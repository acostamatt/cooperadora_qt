@echo off
echo Generaremos los archivos .qrc y .ui a .py
pause
if not exist ..\src\views\base mkdir ..\src\views\base
pyrcc5 ..\qrc\resources.qrc -o ..\src\resources.py
pyuic5 ..\ui\form_alumno_base.ui -o ..\src\views\base\form_alumno_base.py
pyuic5 ..\ui\form_socio_base.ui -o ..\src\views\base\form_socio_base.py
pyuic5 ..\ui\table_window_default.ui -o ..\src\views\base\table_window_default.py
pyuic5 ..\ui\login_base.ui -o ..\src\views\base\login_base.py

pyuic5 ..\ui\main_window_base.ui -o ..\src\views\base\main_window_base.py
pyuic5 ..\ui\table_view_alumno.ui -o ..\src\views\base\table_view_alumno.py
pyuic5 ..\ui\table_view_socio.ui -o ..\src\views\base\table_view_socio.py

python replace_script.py
