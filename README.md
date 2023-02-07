# Task 1: Software configuration

## Subtask 1: Why did I choose to participate in the Dare IT Challenge?

Hi there! My name is Hanna. I chose to participate in the Dare IT Challenge because I'm willing to learn something new and do my upskill. 
The opportunity to work remotely and to get good salary is the main motivating thing.
My goal is become a good professional. 

# TASK 2 : Selectors

## Subtask 1: Searching for selectors on the login page

Scots_Panel_Xpath
1. //*[@id="_next"]/form/div/div[1]/h5
2. //h5[text()="Scouts PAnel"]
3. //*[contains(@class, "MuiTypography-root MuiTypography-h5")]
4. //html/body/div/form/div/div[1]/h5
5. //child::div[1]//h5

Login_Label_Xpath
1. //*[@id="login_label"]
2. //html/body/div/form/div/div[1]/div[1]/label
3. //*[text()="Login"]
4. //child::div[1]//label
5. //*[contains(@class, "MuiFormLabel-root MuiInputLabel-root MuiInputLabel-formControl")]

Input_Login_XPath
1. /html/body/div/form/div/div[1]/div[1]/div/input
2. //*[@id="login"]
3. //input[@id="login]
4. //*[contains(@class, "MuiInputBase-input MuiInput-input")]
5. //child::div[1]//input

Password_Label_XPath
1. //*[@id="password-label"]
2. /html/body/div/form/div/div[1]/div[2]/label
3. //*[text()="Password"]
4. //child::div[2]//label

Input_Password_XPath
1. //*[@id="password"]
2. /html/body/div/form/div/div[1]/div[2]/div/input
3. //child::div[2]//input
4. //input[(@id="password")]
5. //*[(@name="password")]

Button_SignIn_Label_XPath
1. //*[@id="__next"]/form/div/div[2]/button/span[1]
2. /html/body/div/form/div/div[2]/button/span[1]
3. //ancestor::div[2]/button/span

Button_SignIn_XPath
1. //*[@id="__next"]/form/div/div[2]/button
2. /html/body/div/form/div/div[2]/button
3. //ancestor::div[2]/button

Change_Language_Label_XPAth
1. //*[@id="__next"]/form/div/div[2]/div/div
2. /html/body/div/form/div/div[2]/div/div
3. //child::div[2]/div/div

Change_language_Input_Xpath
1. //*[@id="__next"]/form/div/div[2]/div/input
2. /html/body/div/form/div/div[2]/div/input
3. //*[contains(@class, "MuiSelect-nativeInput")] 

ChangeLanguage_SVG_List_Xpath
1. //*[@id="__next"]/form/div/div[2]/div/svg
2. /html/body/div/form/div/div[2]/div/svg
