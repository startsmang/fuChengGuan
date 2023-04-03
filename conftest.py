# import pytest
#
# @pytest.fixture(scope="function",params =[1,2,3])
# def my_fixture(request):
#     print("前置")
#     yield
#     print("后置")
#     return  request.param
#
# class TestDemo:
#     def test_demo(self,my_fixture):
#         print("1")
#         print("------------"+str(my_fixture))
#
#     def test_demo2(self):
#         print("2")
#
# if __name__ == '__main__':
#     pytest.main(["-vs" ,"-n == 3"])