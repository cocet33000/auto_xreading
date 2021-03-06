# -*- coding: utf-8 -*-
import time
import os
import argparse

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys


def scroll_end(driver):
    lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    match=False
    while(match==False):
            lastCount = lenOfPage
            time.sleep(1)
            lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
            if lastCount==lenOfPage:
                match=True


if __name__ == "__main__":
    # 環境変数からXreadingアカウントの情報を受け取る
    my_username = os.environ["xreading_username"]
    my_password = os.environ["xreading_password"]
    
    #コマンドライン引数をパース
    parser = argparse.ArgumentParser()
    parser.add_argument("-only")
    args = parser.parse_args()

    if only:=args.only:
        try:
            if only not in ["read", "wait"]:
                raise ValueError(f"args error {only=} is not correct")
            else:
                print(f'start auto xreading only {only}')
        except Exception as e:
            print(e)
    else:
        print('start autoxreading') 

    # 標準入力からBook情報を受け取る
    URL = input('URL?')
    if only != 'read':
        words = int(input('words?'))
        speed = int(input('speed?'))
        # 入力情報から経過すべき時間を計算
        minute = words//speed

    if only != 'read':
        # 非表示設定
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.add_argument('--headless')
    
        # 操作するページを開く
        driver = webdriver.Chrome('Selenium/chromedriver', chrome_options=options)
        driver.get(URL)
        # タブのタイムアウトを防ぐ
        driver.execute_script('javascript:autoclose_booksbyuesrs = function(){console.log("hoge")}')

        print('start wait')
    
        # 60タブ開く(10分程度経過する)
        for i in range(60):
            time.sleep(0.1)
            driver.execute_script("window.open()") #make new tab
            driver.switch_to.window(driver.window_handles[i+1]) #switch new tab
            driver.get(URL)
            time.sleep(0.5)
            # タブのタイムアウトを防ぐ
            driver.execute_script('javascript:autoclose_booksbyuesrs = function(){console.log("hoge")}')

        # 経過時間に合わせてスリープ
        if minute < 10:
            pass
        else:
            time.sleep(minute-10)

        # 終了
        driver.quit()
        print('end wait')

    if only != 'wait':
        # ログイン
        #driver = webdriver.Chrome('Selenium/chromedriver', chrome_options=options)
        driver = webdriver.Chrome('Selenium/chromedriver')
        login_URL = 'https://xreading.com/'

        driver.get(login_URL)

        username = driver.find_element_by_id('UserUsername')
        username.send_keys(my_username)

        password = driver.find_element_by_id('UserPassword')
        password.send_keys(my_password)

        signin = driver.find_element_by_id('SignInButton')
        signin.submit()

        # 読む
        driver.get(URL)

        print('start read')
        while True:
            try:
                wait = WebDriverWait(driver, 30) # 最大30秒

                scroll_end(driver)

                elem = wait.until( expected_conditions.element_to_be_clickable( (By.ID,"myNxtBtn")) )
                elem.click()
            except:
                wait = WebDriverWait(driver, 30) # 最大30秒

                scroll_end(driver)

                elem = wait.until( expected_conditions.element_to_be_clickable( (By.ID,"closeBtn")) )
                elem.click()
                break
        print('end read')

        print('start quiz')
        # クイズ
        time.sleep(1)
        quiz = driver.find_elements_by_class_name('k-button')[2]
        quiz.click()

        time.sleep(1)
        register = driver.find_element_by_id('register_book')
        register.click()

        quiz_URL = driver.current_url
        for i in range(7):
            time.sleep(0.3)
            driver.execute_script("window.open()") #make new tab
            driver.switch_to.window(driver.window_handles[i+1]) #switch new tab
            driver.get(quiz_URL)

        for i in range(7):
            driver.switch_to.window(driver.window_handles[i+1])
            for j in range(5):
                time.sleep(0.3)
                q1 = driver.find_element_by_id('quest_answer_'+str(j+1))
                q1.click()
                b = driver.find_elements_by_class_name('k-button')
                for x in b:
                    try:
                        if j != 4:
                            x.click()
                        break
                    except:
                        pass
        for i in range(7):
            driver.switch_to.window(driver.window_handles[i+1])
            b = driver.find_elements_by_class_name('k-button')
            for x in b:
                try:
                    x.click()
                    break
                except:
                    pass
        print('end quiz')
        driver.quit()
