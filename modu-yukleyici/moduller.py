pywin32 = "https://github.com/ronix7/modul-yukleyici/blob/master/modul-yukleyici/pywin32-223-cp36-cp36m-win32.whl"
pyHook = "https://github.com/ronix7/modul-yukleyici-/blob/master/Modul%20Yukleyici/pyHook-1.5.1-cp36-cp36m-win32.whl"

# pywin32

def pywin32():
	urllib.request.urlretrieve(moduller.pywin32,"pywin32-223-cp36-cp36m-win32"+".whl")
	pywin32_kur = open("pywin32"+".bat")
	pywin32_kur.read()
	pywin32_kur.close()

# pyHook

def pyHook():
	# pyHook
	urllib.request.urlretrieve(moduller.pywin32,"pyHook-1.5.1-cp36-cp36m-win32"+".whl")
	pyHook_kur = open("pyHook"+".bat")
	pyHook_kur.read()
	pyHook_kur.close()