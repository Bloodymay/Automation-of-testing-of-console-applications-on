"""
Задание 1.

Условие:
Дополнить проект тестами, проверяющими команды вывода списка файлов (l) и разархивирования с путями (x).

*Задание 2. *

• Установить пакет для расчёта crc32
sudo apt install libarchive-zip-perl
• Доработать проект, добавив тест команды расчёта хеша (h). Проверить, что хеш совпадает с рассчитанным командой crc32.

"""

import subprocess

test = '/home/user/Test_arch/test'
out = '/home/user/Test_arch/out'
folder1 = '/home/user/Test_arch/Folder1'
folder2 = '/home/user/Test_arch/Folder2'


def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False


def checkhash(cmd):
    result = subprocess.run(f'{cmd} {out}/arx2.7z', shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    return result.stdout


def test_step1():
    result1 = checkout('cd {}; 7z a {}/arx2'.format(test, out), 'Everything is Ok')
    result2 = checkout('cd {}; ls'.format(out), 'arx2.7z')
    assert result1 and result2, 'test1 Fail'


# HW_2 start
def test_cmd_l():
    assert checkout(f'cd {out}; 7z l arx2.7z', '2 files'), 'test_cmd_l Fail'


def test_cmd_x():
    result1 = checkout(f'cd {out}; 7z x arx2.7z -o{folder1} -y', 'Everything is Ok'),
    result2 = checkout('cd {}; ls'.format(folder1), 'qwe')
    result3 = checkout('cd {}; ls'.format(folder1), 'rty')
    assert result1 and result2 and result3, 'test_cmd_x Fail'


def test_hash():
    result1 = checkhash('crc32')
    print(result1)
    result2 = checkhash('7z h')
    assert result1 in result2.lower(), 'test_hash Fail'
# HW_2 end

def test_step2():
    result1 = checkout('cd {}; 7z e arx2.7z -o{} -y'.format(out, folder1), 'Everything is Ok')
    result2 = checkout('cd {}; ls'.format(folder1), 'qwe')
    result3 = checkout('cd {}; ls'.format(folder1), 'rty')
    assert result1 and result2 and result3, 'test2 Fail'


def test_step3():
    assert checkout('cd {}; 7z t arx2.7z'.format(out), 'Everything is Ok'), 'test3 Fail'


def test_step4():
    assert checkout('cd {}; 7z u {}/arx2.7z'.format(test, out), 'Everything is Ok'), 'test4 Fail'


def test_step5():
    assert checkout('cd {}; 7z d arx2.7z'.format(out), 'Everything is Ok'), 'test5 Fail'