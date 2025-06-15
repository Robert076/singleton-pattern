class AppState:
    instance = None
    
    def __init__(self):
        self.isLoggedIn = False
        
    @staticmethod
    def getAppState():
        if not AppState.instance:
            AppState.instance = AppState()
        return AppState.instance
    
appState1 = AppState.getAppState()
print(appState1.isLoggedIn) # False

appState2 = AppState.getAppState()
appState1.isLoggedIn = True

print(appState1.isLoggedIn) # True
print(appState2.isLoggedIn) # True

# example followed from a NeetCode tutorial