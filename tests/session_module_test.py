import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class SessionModuleTestSuite:

    def __init__(self):
        pass

    def has_passed_test(self, test_purpose, test_succeeded):
        status = "PASSED" if test_succeeded else "FAILED"
        logger.info(f'\t{test_purpose}: {status}')

    def test(self):
        pass


if __name__ == '__main__':
    SessionModuleTestSuite().test()
