from pages.base_page import BasePage


class Matchform(BasePage):
    button_Player_xpath = "//*/div/following-sibling::ul[2]/div[1]"
    button_Matches_xpath = "//*/div/following-sibling::ul[2]/div[2]"
    button_Reports_xpath = "//*/div/following-sibling::ul[2]/div[3]"
    
    div_HeaderTitle_AddMatch_xpath = "//ancestor::main/div[2]/form/div[1]"
    Input_label_MyTeam_xpath = "//child::div[1]//label"
    Input_myTeam_xpath = "//input[@type='text']"

    Input_enemyTeam_xpath = "//input[@name='enemyTeam']"

    Input_Label_MyTeamScore_xpath = "//child::div[3]//label"
    Input_MyTeamScore_xpath = "//input[@name='myTeamScore']"

    Input_tShirt_xpath = "//input[@name='tshirt']"
    Input_League_xpath = "//input[@name='league']"
    