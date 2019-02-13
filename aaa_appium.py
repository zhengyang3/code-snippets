# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time

class Action():
    def __init__(self):
        """
        初始化
        """
        caps = {
            'platformName': 'Android',
            'deviceName': 'OPPO_R9s',
            'appPackage': 'com.offservice.tech',
            'appActivity': '.ui.activitys.WelcomeActivity'
        }

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

    def comments(self):
        driver = self.driver
        time.sleep(10)
        TouchAction(driver).tap(x=286, y=1854).perform()
        time.sleep(3)
        TouchAction(driver).tap(x=301, y=659).perform()
        time.sleep(3)
        TouchAction(driver).tap(x=160, y=1822).perform()
        time.sleep(3)
        TouchAction(driver).tap(x=295, y=1310).perform()
        time.sleep(3)
        TouchAction(driver).tap(x=540, y=1646).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=542, y=1460).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=776, y=1477).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=781, y=1481).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=306, y=1663).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=531, y=1483).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=772, y=1631).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=542, y=1494).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=536, y=1303).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=757, y=1473).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=241, y=863).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=111, y=1496).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=807, y=1327).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=1000, y=1633).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=165, y=1813).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=783, y=1316).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=321, y=1319).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=529, y=1316).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=553, y=1807).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=555, y=1826).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=514, y=1644).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=536, y=1659).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=1000, y=1152).perform()
        time.sleep(1)
        TouchAction(driver).tap(x=568, y=1234).perform()
        time.sleep(1)
        time.sleep(3)
        TouchAction(driver).tap(x=397, y=1865).perform()
        time.sleep(1)
        time.sleep(3)
        time.sleep(1)
        TouchAction(driver).tap(x=833, y=1709).perform()
        time.sleep(3)
        time.sleep(1)
        TouchAction(driver).tap(x=828, y=1707).perform()
        time.sleep(3)
        time.sleep(3)
        time.sleep(1)
        TouchAction(driver)   .press(x=622, y=998)   .move_to(x=625, y=592)   .release()   .perform()
        time.sleep(3)
        time.sleep(1)

    
    def scroll(self):
        while True:
            # 模拟拖动
            # 驱动配置
            FLICK_START_X = 300
            FLICK_START_Y = 300
            FLICK_DISTANCE = 700

            self.driver.swipe(FLICK_START_X, FLICK_START_Y + FLICK_DISTANCE, FLICK_START_X, FLICK_START_Y)
            time.sleep(0.1)
    
    def main(self):
        self.comments()
        self.scroll()


if __name__ == '__main__':
    action = Action()
    action.main()
