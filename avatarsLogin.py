import pyautogui
import time

#auto logon em avatars habbo

class ScreenController:
    
    def __init__(self, loadCheckPoint, checkPointColor, backButtonPoint, selectButtonPosition, numOfAvatars = 10, offset = -175):

        self.loadCheckPoint = loadCheckPoint
        self.checkPointColor = checkPointColor
        self.backButtonPoint = backButtonPoint
        self.selectButtonPosition = selectButtonPosition
        self.currentScrollTranslation = 0
        self.numOfAvatars = numOfAvatars
        self.offset = offset

        self.setupMouse()

    def setupMouse(self):
        x, y = self.selectButtonPosition
        pyautogui.moveTo(x, y)
        pyautogui.click()
        pyautogui.scroll(self.currentScrollTranslation)
    
    def scrollOverAvatars(self, sleep = 1):
        for i in range(self.numOfAvatars):
            pyautogui.scroll(self.offset)
            self.currentScrollTranslation += self.offset

            self.handleCurrentAvatar()
            
            time.sleep(sleep)
            
    def handleCurrentAvatar(self):
        pyautogui.click()
        time.sleep(6)
        self.undoScroll()
        self.goToHotel()
        time.sleep(60)
        self.backToHome()
        time.sleep(1)
        self.setupMouse()

    def undoScroll(self):
        pyautogui.scroll(-self.offset*self.numOfAvatars)

    def goToHotel(self):
        pyautogui.moveTo(1188, 167)
        pyautogui.click()
        self.waitLoading()

    def backToHome(self):
        x, y = self.backButtonPoint
        pyautogui.moveTo(x, y)
        pyautogui.click()

    def waitLoading(self):
        continueChecking = True
        while(continueChecking):
            time.sleep(1)
            screenShot = pyautogui.screenshot()
            checkPointCurrentColor = screenShot.getpixel(self.loadCheckPoint)
            if checkPointCurrentColor == self.checkPointColor:
                continueChecking = False
            


pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1

screenController = ScreenController((167, 108), (239, 212, 32), (38, 92), (646, 665), numOfAvatars = 11)

screenController.scrollOverAvatars()
