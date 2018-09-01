import pyautogui
import time
import faker

#criar avatars com nomes aleatorios

class ScreenController:
    
    def __init__(self, adressBar, createButton, backButtonPoint, numOfAvatars = 5):
        self.createButton = createButton
        self.checkPointColor = backButtonPoint
        self.numOfAvatars = numOfAvatars
        self.faker = faker.Faker()
        self.screenSize = pyautogui.size()
        self.adressBar = adressBar
        
    def createAvatars(self):
        for avatar in range(self.numOfAvatars):
            self.setupMouse()
            self.typeAvatarName()
            self.submit()
            time.sleep(10)
            self.backToAvatarsScreen()
            time.sleep(10)
        
    def setupMouse(self):
        x, y = self.createButton
        pyautogui.moveTo(x, y)
        pyautogui.click()
    
    def typeAvatarName(self):
        pyautogui.moveTo(10,10)
        name = self.faker.name().replace(' ', '')
        pyautogui.typewrite(name)

    def submit(self):
        submitFrame = pyautogui.locateOnScreen('createButton.png')
        
        submitCenterX, submitCenterY = pyautogui.center(submitFrame)

        pyautogui.moveTo(submitCenterX, submitCenterY)
        pyautogui.click()
        
    def backToAvatarsScreen(self):
        x, y = self.adressBar
        pyautogui.moveTo(x, y)
        pyautogui.click()
        pyautogui.typewrite("https://www.habbo.com.br/settings/avatars")
        pyautogui.press('enter')

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1

screenController = ScreenController((589, 46), (782, 442), (38, 92), numOfAvatars = 10)

screenController.createAvatars()

