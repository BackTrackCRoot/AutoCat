import uiautomator2 as u2
import time

d = u2.connect()
d.app_stop("com.taobao.taobao") # revert app
d.app_start("com.taobao.taobao")
d.app_wait("com.taobao.taobao", timeout=20.0) #wait app to start
d.xpath('//*[@resource-id="com.taobao.taobao:id/rv_main_container"]/android.widget.FrameLayout[4]/android.widget.FrameLayout[1]').click()
time.sleep(5)
d(text="赚喵币").click()
time.sleep(5)
while d(text="去浏览").exists(timeout=5):
    time.sleep(5)
    d(text="去浏览").click()
    d(description="任务完成").exists(timeout=20)
    time.sleep(2)
    d.press("back")
print("Ok.")