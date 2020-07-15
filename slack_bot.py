import time
import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#### before start - login to load yopur account in cookies
#### before start - delete first line from csv file
#### before start - check your chrome to be up to date

reviewer = 'your_grader@mail.ru'
website = 'link to your app slack'
# csv -> data loading
with open('slack-members.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
            # load cookies
            chrome_options = Options()
            chrome_options.add_argument("--user-data-dir=chrome-data")
            driver = webdriver.Chrome('/usr/local/Caskroom/chromedriver/83.0.4103.39/chromedriver',
                                      options=chrome_options)
            chrome_options.add_argument("user-data-dir=chrome-data")
            driver.implicitly_wait(10)
            driver.get(website)
            # let's do shit

            driver.find_element_by_xpath(
                '/html/body/div[2]/div/div[2]/div[1]/div/nav/div/div[1]/div/div/div[1]/div/div/div[10]/div/div/button').click()
            driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div/div/div/div[2]/button/div').click()
            driver.find_element_by_id('channel-name').send_keys('hw_' + line[0].replace('.', ''))
            driver.find_element_by_id('channel_create_modal_toggle').click()
            driver.find_element_by_xpath('/html/body/div[6]/div/div/div[3]/div[2]/button').click()
            driver.find_element_by_xpath(
                '/html/body/div[6]/div/div/div[2]/div/div[1]/div/div/div/div/div/div/div[1]/div/input').send_keys(
                line[1])
            driver.find_element_by_class_name('c-base_entity__text-contents').click()
            time.sleep(0.5)
            driver.find_element_by_xpath(
                '/html/body/div[6]/div/div/div[2]/div/div[1]/div/div/div/div/div/div/div[1]/div/input').send_keys(
                reviewer)
            driver.find_element_by_id('channel_invite_modal_select_option_0').click()
            driver.find_element_by_xpath("/html/body/div[6]/div/div/div[3]/div/div/button").click()
            driver.quit()
            print('done.')