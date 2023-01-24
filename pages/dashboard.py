from pages.base_page import BasePage


class Dashboard(BasePage):
        header_footbalTeam_Logo_xpath = "//ancestor::header/div/h6"
        button_MainPage_xpath = "//*/div/following-sibling::ul[1]/div[1]"
        button_Players_xpath = "//*/div/following-sibling::ul[1]/div[2]"
        button_Language_xpath = "//*/div/following-sibling::ul[2]/div[1]"
        button_SignOut_xpath = "//*/div/following-sibling::ul[2]/div[2]"
        FootbalTeam_Logo_xpath = "//*[@title='Logo Scouts Panel']"
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





pass