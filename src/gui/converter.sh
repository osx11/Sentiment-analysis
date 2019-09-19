rm main_window.py
rm information.py
rm mountains_rc.py

pyuic5 main_window.ui -o main_window.py
pyuic5 information.ui -o information.py
pyrcc5 mountains.qrc -o mountains_rc.py
