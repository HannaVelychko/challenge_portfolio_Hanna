import time
from lib2to3.pgen2 import driver

from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class Dashboard(BasePage):
    expected_title = "Scouts Panel"
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/en'
    header_footbalTeam_Logo_xpath = "//ancestor::header/div/h6"
    button_MainPage_xpath = "//*/div/following-sibling::ul[1]/div[1]"
    button_Players_xpath = "//*/div/following-sibling::ul[1]/div[2]"
    button_Language_xpath = "//*/div/following-sibling::ul[2]/div[1]"
    button_SignOut_xpath = "//*/div/following-sibling::ul[2]/div[2]"
    footballTeam_Logo_xpath = "//*[@title='Logo Scouts Panel']"
    header_ScoutsPanel_xpath = "//ancestor::div/h2"
    paragraph_ScoutsPanel_xpath = "//ancestor::div/p"
    button_Link_DevTeamContact_xpath = "//*[1][name() = 'a']"
    div_Shortcuts_xpath = "//ancestor::main/div[3]/div[2]/div"
    header_Shortcuts_xpath = "//ancestor::div[3]/div[2]/div/div/h2"
    button_Link_AddPlayer_xpath = "//*[2][name()='a']"
    div_Player_Icon_xpath = "//*/div/following-sibling::div[1]/div[1]/div"
    div_Matches_Icon_xpath = "//*/div/following-sibling::div[1]/div[2]/div"
    div_Reports_Icon_xpath = "//*/div/following-sibling::div[2]"
    div_EventsCount_Icon_xpath = "//*/div/following-sibling::div[3]"
    wait = WebDriverWait(driver, 10)
    def title_of_page(self):
        self.wait_for_element_to_be_clicable(self.button_Language_xpath)
        assert self.get_page_title(self.dashboard_url) == self.expected_title
