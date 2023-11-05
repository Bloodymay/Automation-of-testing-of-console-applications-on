import subprocess
"""
Задание 1.

Условие:
Написать функцию на Python, которой передаются в качестве параметров команда и текст. Функция должна возвращать True, 
если команда успешно выполнена и текст найден в её выводе и False в противном случае. Передаваться должна только одна 
строка, разбиение вывода использовать не нужно.
"""

if __name__ == "__main__":
    def test_func(command, text):
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding="utf-8")
        out = result.stdout
        if text in out and result.returncode == 0:
            return True
        else:
            return False
    print(test_func("cat /etc/os-release","jammy"))