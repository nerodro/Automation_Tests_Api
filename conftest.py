import pytest
import requests
from Api_Tests.Config import GLOBAL_LINK

@pytest.fixture
def get_url():
    return _url


def _url(global_link, input):
    return global_link + input