import pytest
import requests
from Api_Tests.jsons import json_data
from Api_Tests.Config import GLOBAL_LINK
from Api_Tests.enums.global_enum_errors import GlobalErrorMessages
from Api_Tests.base.basedresponse import Response
from Api_Tests.pydantic.post import Post_Create, Post_Register, Post_Login
from Api_Tests.pydantic.Put import Put_Update
from Api_Tests.pydantic.Patch import Patch_Update

@pytest.mark.get
class Test_Get():
    #@pytest.mark.parametrize(['statuse_code', ''])
    def test_get_list(self, get_url):
        response = requests.get(get_url(GLOBAL_LINK, "/api/users?page=2"))
        assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
        assert response.json() == json_data.list_users, GlobalErrorMessages.WRONG_JSON_DATA.value
        print(response.text)

    def test_get_single(self, get_url):
        response = requests.get(get_url(GLOBAL_LINK , "/api/users/2"))
        assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
        assert response.json() == json_data.single_body, GlobalErrorMessages.WRONG_JSON_DATA.value
        print(response.text)

    def test_get_none(self, get_url):
        response = requests.get(get_url(GLOBAL_LINK , "/api/users/23"))
        assert response.status_code == 404, GlobalErrorMessages.WRONG_STATUS_CODE.value
        assert response.json() == {}, GlobalErrorMessages.WRONG_JSON_DATA.value
        print(response.text)

    def test_list_resource(self, get_url):
        response = requests.get(get_url(GLOBAL_LINK , "/api/unknown"))
        assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
        assert response.json() == json_data.resources, GlobalErrorMessages.WRONG_JSON_DATA.value
        print(response.text)

    def test_single_resource(self, get_url):
        response = requests.get(get_url(GLOBAL_LINK , "/api/unknown/2"))
        assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
        assert response.json() == json_data.single_recource, GlobalErrorMessages.WRONG_JSON_DATA.value
        print(response.text)

    def test_unknown_resource(self, get_url):
        response = requests.get(get_url(GLOBAL_LINK , "/api/unknown/23"))
        assert response.status_code == 404, GlobalErrorMessages.WRONG_STATUS_CODE.value
        assert response.json() == {}, GlobalErrorMessages.WRONG_JSON_DATA.value
        print(response.text)

    def test_delay(self, get_url):
        response = requests.get(get_url(GLOBAL_LINK , "/api/users?delay=3"))
        assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value
        assert response.json() == json_data.delay, GlobalErrorMessages.WRONG_JSON_DATA.value
        print(response.text)