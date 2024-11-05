from Tools.imports import *

class DUMP:
    def __init__(self) -> None:
        pass
    
    def DumpFriend(self, cookie):
        try:
            with requests.Session() as r:
                user = console.input()
                response = r.get(f'https://web.facebook.com/profile.php?id={userid}&sk=friends')
        except Exception, e:
            raise e