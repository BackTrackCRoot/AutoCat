import uiautomator2 as u2
import time

def make_money(d):
    d(text="赚喵币").click()
    time.sleep(3)
    while d(text="去浏览").exists(timeout=5):
        time.sleep(5)
        d(text="去浏览").click()
        d.swipe_ext("up")
        d.swipe_ext("up")
        d(description="任务完成").exists(timeout=20)
        time.sleep(2)
        d.press("back")
    print("make money done.")

def click_cat(d):
     while 1:
         after = d(textStartsWith='我的喵币,').get_text().split(',')[1]
         d(text="我的猫，点击撸猫").click()
         time.sleep(0.5)
         if after <= d(textStartsWith='我的喵币,').get_text().split(',')[1]:
             print("click_cat done.")
             break

if __name__ == "__main__":
    d = u2.connect()
    d.app_stop("com.taobao.taobao") # revert app
    d.app_start("com.taobao.taobao")
    d.app_wait("com.taobao.taobao", timeout=20.0) #wait app to start

    d.xpath('//*[@resource-id="com.taobao.taobao:id/rv_main_container"]/android.widget.FrameLayout[4]/android.widget.FrameLayout[1]').wait(3)
    if d.xpath('//*[@resource-id="com.taobao.taobao:id/rv_main_container"]/android.widget.FrameLayout[4]/android.widget.FrameLayout[1]').exists:
        d.xpath('//*[@resource-id="com.taobao.taobao:id/rv_main_container"]/android.widget.FrameLayout[4]/android.widget.FrameLayout[1]').click()
        # click cat
        click_cat(d)
        # make money of cat
        make_money(d)
    else:
        print("Can not found the activity entry.")
    
    d.app_stop("com.taobao.taobao")