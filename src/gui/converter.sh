#!/usr/bin/env bash
rm main_window.py
rm information.py
rm moon_rc.py

pyuic5 main_window.ui -o main_window.py
pyuic5 information.ui -o information.py
pyrcc5 moon.qrc -o moon_rc.py
