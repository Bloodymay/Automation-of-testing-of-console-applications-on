"""
Задание 2. (повышенной сложности)

Доработать функцию из предыдущего задания таким образом, чтобы у неё появился дополнительный режим работы,
в котором вывод разбивается на слова с удалением всех знаков пунктуации
(их можно взять из списка string.punctuation модуля string). В этом режиме должно проверяться наличие слова в выводе.

"""
import subprocess
import re
if __name__ == "__main__":
    def test_func(command, text, mode=None):
        print(punctuation)
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding="utf-8")
        out = result.stdout
        if mode == None:
            if text in out and result.returncode == 0:
                return True
            else:
                return False
        elif mode == "strip_punct":
            lst = re.findall(r'\w+',out)
            print(lst)
            if text in lst and result.returncode == 0:
                return True
            else:
                return False

    print(test_func("cat /etc/os-release","jammy", mode="strip_punct"))