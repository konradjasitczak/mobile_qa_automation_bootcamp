import pytest
import logging

logging.basicConfig(level=logging.INFO)

class Test01Android():
    @pytest.mark.parametrize('os', ['android'])
    def test_01(self):
        logging.info("test_01 method")

    @classmethod
    def setup_class(cls):
        logging.info("setup_class")

    @classmethod
    def teardown_class(cls):
        logging.info("teardown_class")

    def setup_method(self, method):
        logging.info("setup_method")

    def teardown_method(self, method):
        logging.info("teardown_method")