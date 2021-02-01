
::set /P package="Input package name or input command: "
@echo off

set base_path=%~dp0
set pack_path=Lib\site-packages\pip-man\__init__.py
set pack=%base_path:~0,-8%%pack_path%
echo %pack%

python %pack% %1 %2 %3