import pytest
import requests
from Api_Tests.jsons import json_data
from Api_Tests.Config import GLOBAL_LINK
from Api_Tests.enums.global_enum_errors import GlobalErrorMessages
from Api_Tests.base.basedresponse import Response
from Api_Tests.pydantic.post import Post_Create, Post_Register, Post_Login
from Api_Tests.pydantic.Put import Put_Update
from Api_Tests.pydantic.Patch import Patch_Update

@pytest.mark.post
class Test_Post():
    def test_post_create(self, get_url):
        user = {"name" : "johns", "job": "leader"}
        responses = requests.post(get_url(GLOBAL_LINK , "/api/users"), json=user)
        response = Response(responses)
        response.assert_statuse_code(201).valid(Post_Create)
        print(responses.json())

    def test_post_register_successfull(self, get_url):
        new_user = {"email": "eve.holt@reqres.in","password": "pistol"}
        responses = requests.post(get_url(GLOBAL_LINK , "/api/users"), json=new_user)
        response = Response(responses)
        response.assert_statuse_code(201).valid(Post_Register)
        print(responses.json())
    @pytest.mark.xfail(reason="required field for register is empty")
    def test_post_register_unsuccessfull(self, get_url):
        new_user = {"email": "eve.holt@reqres.in"}
        responses = requests.post(get_url(GLOBAL_LINK , "/api/users"), json=new_user)
        response = Response(responses)
        response.assert_statuse_code(201).valid(Post_Register)
        print(responses.json())

    def test_post_login_successfull(self, get_url):
        new_user = { "email": "eve.holt@reqres.in","password": "cityslicka"}
        responses = requests.post(get_url(GLOBAL_LINK , "/api/login"), json=new_user)
        response = Response(responses)
        response.assert_statuse_code(200).valid(Post_Login)
        print(responses.json())

    @pytest.mark.xfail(reason="required field for login is empty")
    def test_post_login_unsuccessfull(self, get_url):
        new_user = { "email": "eve.holt@reqres.in"}
        responses = requests.post(get_url(GLOBAL_LINK , "/api/login"), json=new_user)
        response = Response(responses)
        response.assert_statuse_code(200).valid(Post_Login)
        print(responses.json())