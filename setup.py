import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"  # Если вы хотите, чтобы ваше приложение запускалось без консоли

setup(
    name="my_program",
    version="0.1",
    description="My Description",
    executables=[Executable("UXUI.py", base=base)],  # Укажите свой основной скрипт
)