import pytest
import requests
from Api_Tests.jsons import json_data
from Api_Tests.Config import GLOBAL_LINK
from Api_Tests.enums.global_enum_errors import GlobalErrorMessages
from Api_Tests.base.basedresponse import Response
from Api_Tests.pydantic.post import Post_Create, Post_Register, Post_Login
from Api_Tests.pydantic.Put import Put_Update
from Api_Tests.pydantic.Patch import Patch_Update

@pytest.mark.delete
class Test_Delete():
    def test_delete(self, get_url):
        user_update = {"name": "olly", "job": "coder"}
        responses = requests.delete(get_url(GLOBAL_LINK , "/api/users/2"), json=user_update)
        assert responses.status_code == 204, GlobalErrorMessages.WRONG_STATUS_CODE.value
        assert responses, GlobalErrorMessages.WRONG_JSON_DATA.value
        print(responses.text)