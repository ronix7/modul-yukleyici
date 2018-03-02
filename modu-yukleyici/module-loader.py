import moduller
import platform
import os
import urllib.request
from subprocess import Popen

bulundugum_dizi = os.getcwd()
# pywin32
def pywin32():
	pywin32 = "https://github.com/ronix7/modul-yukleyici/blob/master/modul-yukleyici/pywin32-223-cp36-cp36m-win32.whl"
	urllib.request.urlretrieve(pywin32,"pywin32-223-cp36-cp36m-win32"+".whl")

def pyHook():
	# pyHook
	pyHook = "https://github.com/ronix7/modul-yukleyici/blob/master/modul-yukleyici/pyHook-1.5.1-cp36-cp36m-win32.whl"
	urllib.request.urlretrieve(pyHook,"pyHook-1.5.1-cp36-cp36m-win32"+".whl")

def moduller():
	print("\nMODULLER\n\n1-pywin32\n2-pyHook")

def aciklamalar():
	print(">>>>>>>>> Modul Yukleyici\n\nYuklemek istediginiz modulu rakam ile belirtiniz")
	secim =int(input("\nSecim :"))
	moduller()
	if secim ==1:
		pywin32()
		pywin32_kur = Popen("pywin32.bat", cwd = bulundugum_dizi)
		stdout, stderr = p.communicate()
	elif secim ==2:
		pyHook()

aciklamalar()