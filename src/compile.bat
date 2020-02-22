C:\Users\osx11\AppData\Local\Programs\Python\Python37\python.exe C:\Users\osx11\AppData\Local\Programs\Python\Python37\Scripts\pyinstaller.exe --onefile core.py
del core.spec
rmdir /S /Q build
move dist\core.exe .\SentimentAnalysis.exe
rmdir dist
