import json
import os
import re
import time
from selenium.webdriver.common.by import By
from get_chrome_driver import GetChromeDriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from create import store_into_database

class Twitter:

    def __init__(self, user_name, user_email, user_password):
        self.user_name = user_name
        self.user_email = user_email
        self.user_password = user_password

    def login(self, driver):
        time.sleep(5)
        # entering email
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.r-fdjqy7')))
        log_In_input = driver.find_element(By.CSS_SELECTOR, '.r-fdjqy7')
        time.sleep(3)
        log_In_input.send_keys(self.user_email)
        time.sleep(3)
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.r-1f1sjgu+ .r-13qz1uu')))
        btn_next = driver.find_element(By.CSS_SELECTOR, '.r-1f1sjgu+ .r-13qz1uu')

        time.sleep(3)
        btn_next.click()
        time.sleep(3)

        # entering user name
        try:
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.r-fdjqy7')))
            log_In_input = driver.find_element(By.CSS_SELECTOR, '.r-fdjqy7')
            time.sleep(3)
            log_In_input.send_keys(self.user_name)
            time.sleep(3)
            try:
                next_css = '.css-18t94o4.css-1dbjc4n.r-1m3jxhj.r-42olwf.r-sdzlij.r-1phboty.r-rs99b7.r-19yznuf.r-64el8z.r-1ny4l3l.r-1dye5f7.r-o7ynqc.r-6416eg.r-lrvibr'
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, next_css)))
                btn_next = driver.find_element(By.CSS_SELECTOR, next_css)
            except:
                next_css = '.css-1dbjc4n.r-pw2am6 div[role=button]'

                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, next_css)))
                btn_next = driver.find_element(By.CSS_SELECTOR, next_css)

            time.sleep(3)
            btn_next.click()
            time.sleep(3)

        except Exception as e:
            print(e)

        # entering password
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                        '.r-30o5oe.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-1dz5y72.r-fdjqy7.r-13qz1uu')))
        pas_element = driver.find_element(By.CSS_SELECTOR,
                                          '.r-30o5oe.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-1dz5y72.r-fdjqy7.r-13qz1uu')
        time.sleep(3)
        pas_element.send_keys(self.user_password)
        time.sleep(3)

        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                        '.css-18t94o4.css-1dbjc4n.r-sdzlij.r-1phboty.r-rs99b7.r-19yznuf.r-64el8z.r-1ny4l3l.r-1dye5f7.r-o7ynqc.r-6416eg.r-lrvibr')))
        btn_log_in = driver.find_element(By.CSS_SELECTOR,
                                         '.css-18t94o4.css-1dbjc4n.r-sdzlij.r-1phboty.r-rs99b7.r-19yznuf.r-64el8z.r-1ny4l3l.r-1dye5f7.r-o7ynqc.r-6416eg.r-lrvibr')

        time.sleep(3)
        btn_log_in.click()
        time.sleep(3)

    def login_after(self, driver):
        try:
            login_css = '.css-1dbjc4n.r-1awozwy.r-1pz39u2.r-18u37iz.r-16y2uox a'
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, login_css)))
            login_btn = driver.find_element(By.CSS_SELECTOR, login_css)

            time.sleep(2)
            login_btn.click()
            time.sleep(3)

            # entering email
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.r-fdjqy7')))
            log_In_input = driver.find_element(By.CSS_SELECTOR, '.r-fdjqy7')
            time.sleep(3)
            log_In_input.send_keys(self.user_email)
            time.sleep(3)
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.r-1f1sjgu+ .r-13qz1uu')))
            btn_next = driver.find_element(By.CSS_SELECTOR, '.r-1f1sjgu+ .r-13qz1uu')

            time.sleep(3)
            btn_next.click()
            time.sleep(3)

            # entering user name
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.r-fdjqy7')))
            log_In_input = driver.find_element(By.CSS_SELECTOR, '.r-fdjqy7')
            time.sleep(3)
            log_In_input.send_keys(self.user_name)
            time.sleep(3)
            try:
                next_css = '.css-18t94o4.css-1dbjc4n.r-1m3jxhj.r-42olwf.r-sdzlij.r-1phboty.r-rs99b7.r-19yznuf.r-64el8z.r-1ny4l3l.r-1dye5f7.r-o7ynqc.r-6416eg.r-lrvibr'
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, next_css)))
                btn_next = driver.find_element(By.CSS_SELECTOR, next_css)
            except:
                next_css = '.css-1dbjc4n.r-pw2am6 div[role=button]'

                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, next_css)))
                btn_next = driver.find_element(By.CSS_SELECTOR, next_css)

            time.sleep(3)
            btn_next.click()
            time.sleep(3)

            # entering password
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                            '.r-30o5oe.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-1dz5y72.r-fdjqy7.r-13qz1uu')))
            pas_element = driver.find_element(By.CSS_SELECTOR,
                                              '.r-30o5oe.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-t60dpp.r-1dz5y72.r-fdjqy7.r-13qz1uu')
            time.sleep(3)
            pas_element.send_keys(self.user_password)
            time.sleep(3)

            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                            '.css-18t94o4.css-1dbjc4n.r-sdzlij.r-1phboty.r-rs99b7.r-19yznuf.r-64el8z.r-1ny4l3l.r-1dye5f7.r-o7ynqc.r-6416eg.r-lrvibr')))
            btn_log_in = driver.find_element(By.CSS_SELECTOR,
                                             '.css-18t94o4.css-1dbjc4n.r-sdzlij.r-1phboty.r-rs99b7.r-19yznuf.r-64el8z.r-1ny4l3l.r-1dye5f7.r-o7ynqc.r-6416eg.r-lrvibr')
            time.sleep(3)
            btn_log_in.click()
            time.sleep(3)

        except Exception as e:
            print(e)

    def get_posts(self, driver):
        post_selector = ".css-1dbjc4n.r-1loqt21.r-18u37iz.r-1ny4l3l.r-1udh08x.r-1qhn6m8.r-i023vh.r-o7ynqc.r-6416eg"
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, post_selector)))
        posts = driver.find_elements(By.CSS_SELECTOR, post_selector)

        no_new_posts = 0
        posts_len = len(posts)
        while len(posts) < 20:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)
            posts = driver.find_elements(By.CSS_SELECTOR, post_selector)
            if posts_len == len(posts):
                no_new_posts+=1
            if no_new_posts>5:
                break
            posts_len = len(posts)

        if len(posts) > 20:
            posts = posts[:20]
        return posts

    def relogin(self, driver):
        try:
            dont_miss = driver.find_element(By.CSS_SELECTOR,
                                            '.css-901oao.r-jwli3a.r-37j5jr.r-1blvdjr.r-b88u0q.r-vrz42v.r-bcqeeo.r-qvutc0').text
            if dont_miss == 'Don’t miss what’s happening':
                self.login_after(driver)
        except Exception as e:
            print('failed to re login')

    def scrape_comment(self, comment_element):
        comment_field = {'n_comments': None, 'n_retweets': None, 'n_like': None, 'post_url': None, 'post_time': None,
                'post_text': None}
        try:
            comments_retweets_likes = comment_element.find_element(By.CSS_SELECTOR,
                                                     '.css-1dbjc4n.r-1ta3fxp.r-18u37iz.r-1wtj0ep.r-1s2bzr4.r-1mdbhws').get_attribute(
                "aria-label")
            comments_retweets_likes = comments_retweets_likes.lower()
            repl = re.findall(r'(\d+) repl', comments_retweets_likes)
            if repl:
                comment_field["n_comments"] = int(repl[0])
        except Exception as e:
            print('failed to scrape n_comments')

        try:
            retw = re.findall(r'(\d+) retweet', comments_retweets_likes)
            if retw:
                comment_field["n_retweets"] = int(retw[0])
        except Exception as e:
            print('failed to scrape n_comments')

        try:
            like = re.findall(r'(\d+) like', comments_retweets_likes)
            if like:
                comment_field["n_like"] = int(like[0])
        except Exception as e:
            print('failed to scrape n_comments')

        try:
            post_url = comment_element.find_element(By.CSS_SELECTOR, '.css-1dbjc4n.r-18u37iz.r-1q142lx a').get_attribute("href")
            comment_field["post_url"] = post_url
        except Exception as e:
            print('failed to scrape n_comments')

        try:
            post_time = comment_element.find_element(By.CSS_SELECTOR, 'time').get_attribute("datetime")
            comment_field["post_time"] = post_time
        except Exception as e:
            print('failed to scrape n_comments')

        try:
            post_text = comment_element.find_element(By.CSS_SELECTOR,
                                       '.css-901oao.r-18jsvk2.r-37j5jr.r-a023e6.r-16dba41.r-rjixqe.r-bcqeeo.r-bnwqim.r-qvutc0').text
            comment_field["post_text"] = post_text
        except Exception as e:
            print('failed to scrape n_comments')

        return comment_field

    def click_more(self, driver):
        try:
            see_more = '.r-16dba41.r-q4m81j'
            while True:
                try:
                    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, see_more)))
                    more_btn = driver.find_element(By.CSS_SELECTOR, see_more)
                    driver.execute_script("arguments[0].scrollIntoView(true);", more_btn)
                    time.sleep(3)
                    more_btn.click()
                    time.sleep(3)
                except Exception as e:
                    break
        except Exception as e:
            print("No more buttons")

    def scrape_comments(self, driver):
        comments_data = []
        time.sleep(5)
        try:
            comment_selector = '.r-i023vh.r-6416eg'
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, comment_selector)))
            comments = driver.find_elements(By.CSS_SELECTOR, comment_selector)

            for comment in comments:
                comment_data = {'commenter_profile_url': None, 'commenter_name': None, 'comment_time': None, 'comment_text': None}
                try:
                    commenter_profile = comment.find_element(By.CSS_SELECTOR, '.css-1dbjc4n.r-1wbh5a2.r-dnmrzs.r-1ny4l3l a')
                    comment_data["commenter_profile_url"] = commenter_profile.get_attribute("href")
                    comment_data["commenter_name"] = commenter_profile.text
                    comment_data["comment_time"] = comment.find_element(By.CSS_SELECTOR, 'time').get_attribute("datetime")
                    comment_data["comment_text"] = comment.find_element(By.CSS_SELECTOR,
                                                                        '.css-901oao.r-18jsvk2.r-37j5jr.r-a023e6.r-16dba41.r-rjixqe.r-bcqeeo.r-bnwqim.r-qvutc0').text
                except Exception as e:
                    print(e)
                comments_data.append(comment_data)
        except Exception as e:
            print("no comments")

        return comments_data

    def scrape_retweets(self, driver):
        retweets_data = []
        try:
            retweets_selector = '.css-18t94o4.css-1dbjc4n.r-1ny4l3l.r-ymttw5.r-1f1sjgu.r-o7ynqc.r-6416eg'
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, retweets_selector)))
            retweets = driver.find_elements(By.CSS_SELECTOR,retweets_selector)

            for retweet in retweets:
                retweet_data = {'retweeter_name': None, 'retweeter_profile_url': None, 'retweet_text': None}
                try:
                    Who_Retweets = retweet.find_element(By.CSS_SELECTOR, '.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1wtj0ep a')
                    retweet_data["retweeter_name"] = Who_Retweets.text
                    retweet_data["retweeter_profile_url"] = Who_Retweets.get_attribute("href")
                except Exception as e:
                    print("no retweet Who_Retweets")

                try:
                    retweet_data["retweet_text"] = retweet.find_element(By.CSS_SELECTOR,'.css-901oao.r-18jsvk2.r-37j5jr.r-a023e6.r-16dba41.r-rjixqe.r-bcqeeo.r-1h8ys4a.r-1jeg54m.r-qvutc0').text
                except Exception as e:
                    print("no retweet text")
                retweets_data.append(retweet_data)
        except Exception as e:
            print("no retweet")

        return retweets_data

class ScrapingDriver():

    def __init__(self):
        self.chrome_driver_dir = 'chromedriver_linux64'
        self.chrome_driver_file = self.chrome_driver_dir + '/chromedriver'
        self.option = Options()
        self.option.add_argument("--disable-notifications")
        self.option.add_argument('--no-sandbox')
        self.option.add_argument('--disable-dev-shm-usage')
        # self.option.add_argument("--headless")

    def download_deriver(self):
        if not os.path.exists(self.chrome_driver_file):
            download_driver = GetChromeDriver()
            download_driver.auto_download(output_path=self.chrome_driver_dir, extract=True)

    def execute_driver(self):
        driver = webdriver.Chrome(executable_path=self.chrome_driver_file, options=self.option)
        return driver

def main():

    scraping_driver = ScrapingDriver()

    # download chrome driver
    scraping_driver.download_deriver()

    # visiting to twitter login
    driver = scraping_driver.execute_driver()

    driver.get('https://twitter.com/login')
    driver.maximize_window()
    time.sleep(5)

    twitter = Twitter('Your user name', 'Your email', 'password')

    twitter.login(driver)

    # visiting to scrape data from bbcbangla
    time.sleep(5)
    driver.get('https://twitter.com/bbcbangla')

    # relogin if needed
    twitter.relogin(driver)

    # scraping posts fields
    posts = twitter.get_posts(driver)
    post_data = []
    for i in posts:
        try:
            comments_field = twitter.scrape_comment(i)
            post_data.append(comments_field)
        except Exception as e:
            print(e)

    all_posts_field = []
    for post in post_data:
        twitter.relogin(driver)
        driver.get(post["post_url"])
        time.sleep(5)

        # click more comments
        twitter.click_more(driver)

        # scrape comments
        post['comments']= twitter.scrape_comments(driver)

        # scrape retweets
        time.sleep(5)
        driver.get(post["post_url"]+ "/retweets")
        time.sleep(5)

        post['retweets'] = twitter.scrape_retweets(driver)

        store_into_database(post, post['comments'], post['retweets'])

        all_posts_field.append(post)

    with open('DATA.json', 'w') as file:
        json.dump(all_posts_field, file, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    main()
