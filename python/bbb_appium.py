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
            'appPackage': 'com.farfetch.farfetchshop',
            'appActivity': '.activities.StartActivity'
        }

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

    def comments(self):
        driver = self.driver
        time.sleep(15)

        TouchAction(driver).tap(x=895, y=126).perform()
        time.sleep(4)
        TouchAction(driver).tap(x=521, y=1240).perform()
        time.sleep(4)
        TouchAction(driver).tap(x=513, y=1702).perform()
        time.sleep(4)
        TouchAction(driver).tap(x=513, y=1744).perform()
        time.sleep(4)
        TouchAction(driver).tap(x=252, y=298).perform()
        time.sleep(14)
        
        
        
        "从第一条是丹麦开始滑动"
        TouchAction(driver)   .press(x=542, y=1025)   .move_to(x=555, y=824)   .release()   .perform()
        time.sleep(14)
    
        TouchAction(driver).tap(x=504, y=424).perform()
        time.sleep(14)
        
        TouchAction(driver).tap(x=845, y=1122).perform()
        time.sleep(10)

        
        
        
        "sleep 30s //手动登陆"
        "time.sleep(40)"
        
        
        TouchAction(driver).tap(x=328, y=1828).perform()
        time.sleep(13)
        TouchAction(driver)   .press(x=521, y=1055)   .move_to(x=529, y=958)   .release()   .perform()
        time.sleep(13)
        
    
        TouchAction(driver).tap(x=899, y=416).perform()
        time.sleep(3)
        TouchAction(driver)   .press(x=555, y=1122)   .move_to(x=572, y=794)   .release()   .perform()
        time.sleep(3)



    def scroll(self):
        while True:
            # 模拟拖动
            # 驱动配置
            FLICK_START_X = 300
            FLICK_START_Y = 300
            FLICK_DISTANCE = 1300

            self.driver.swipe(FLICK_START_X, FLICK_START_Y + FLICK_DISTANCE, FLICK_START_X, FLICK_START_Y)
            time.sleep(0.1)
    
    def main(self):
        self.comments()
        self.scroll()


if __name__ == '__main__':
    action = Action()
    action.main()
