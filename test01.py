import pytest
import logging

log=logging.basicConfig(level=logging.INFO)

class Test01Android():
    @pytest.mark.parametrize('os', ['android'])
    def test_01(self, os):
        log.info(f"mark value is {os}")
        #log.info("mark value is {s},{d}".format(s=os, d="12"))
        #log.info("mark value is %s" % os)
    @classmethod
    def setup_class(cls):
        log.info("setup_class")

    @classmethod
    def teardown_class(cls):
        log.info("teardown_class")

    def setup_method(self):
        log.info("setup_method")

    def teardown_method(self):
        log.info("teardown_method")
