# ./test_case/test_func.py

from func import *

class TestFunc:
	def test_add_by_class(self):
		assert add(2,3) == 5,f'2+3=5正确'


def test_add_by_func_aaa():
	assert add(3,3) == 5, f"3+3应该等于6"

'''
============================= test session starts =============================
platform win32 -- Python 3.7.0, pytest-5.3.4, py-1.8.1, pluggy-0.13.1 -- D:\Python3.7\python.exe
cachedir: .pytest_cache
rootdir: D:\Python3.7\project\pytest, inifile: pytest.ini
plugins: allure-pytest-2.8.9, rerunfailures-8.0
collecting ... collected 2 items

test_case/test_func.py::TestFunc::test_add_by_class PASSED               [ 50%]
test_case/test_func.py::test_add_by_func_aaa FAILED                      [100%]

================================== FAILURES ===================================
____________________________ test_add_by_func_aaa _____________________________

    def test_add_by_func_aaa():
    
>   	assert add(3,3) == 5, "3+3应该等于6"
E    AssertionError: 3+3应该等于6
E    assert 6 == 5
E      -6
E      +5

test_case\test_func.py:14: AssertionError
========================= 1 failed, 1 passed in 0.09s =========================
[Finished in 1.4s]
'''











