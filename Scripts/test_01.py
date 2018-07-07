import allure,pytest

class Test_01:

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step(title="第一个测试")
    def test_01_1(self):
        allure.attach("这是一个描述", "我是具体内容")
        allure.attach("这是二个描述", "我是内容")
        allure.attach("这是三个描述", "。。。。。")
        assert 0