import pytest
import requests
from Api_Tests.jsons import json_data
from Api_Tests.Config import GLOBAL_LINK
from Api_Tests.enums.global_enum_errors import GlobalErrorMessages
from Api_Tests.base.basedresponse import Response
from Api_Tests.pydantic.post import Post_Create, Post_Register, Post_Login
from Api_Tests.pydantic.Put import Put_Update
from Api_Tests.pydantic.Patch import Patch_Update

@pytest.mark.patch
class Test_Patch():
    def test_patch_update(self, get_url):
        user_update = {"name": "olly", "job": "coder"}
        responses = requests.patch(get_url(GLOBAL_LINK , "/api/users/2"), json=user_update)
        response = Response(responses)
        response.assert_statuse_code(200).valid(Patch_Update)
        print(responses.json())