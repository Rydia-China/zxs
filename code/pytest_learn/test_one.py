# .py测试文件必须以“test_”开头（或“_test”结尾）
# 测试方法必须以“test_”开头
# def test_one():
#     name = "测试"
#     assert name == "测试"
#
#
# def test_two():
#     num = 10
#     assert num == 10

# 测试类必须以Test开头，并且不能有init方法
import pytest

class TestCase():
    def test_three(self):
        assert 1 == 1

    def test_four(self):
        assert 2 == 2


if __name__ == '__main__':
    pytest.main()
