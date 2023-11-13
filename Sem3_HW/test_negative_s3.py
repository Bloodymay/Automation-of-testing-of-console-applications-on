
import subprocess
import yaml
import pytest
from checkers import checkout_negative

with open('config.yaml') as f:
    # читаем документ YAML
    data = yaml.safe_load(f)


class TestNegative:

    def test_step1(self, make_bad_arx):
        result1 = checkout_negative('cd {}; 7z e bad_arx.{} -o{} -y'.format(data["folder_out"],data["arx_type"], data["folder_ext"]), 'ERRORS')
        assert result1, 'test2 Fail'

    def test_step2(self):
        assert checkout_negative('cd {}; 7z t bad_arx.{}'.format(data["folder_out"], data["arx_type"]), 'ERRORS'), 'test2 Fail'
