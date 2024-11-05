from Tools.imports import *

class UserData:
    
    def dataGraphQL(self, req):
        return {
            "av": re.search('"actorID":"(\d+)"', str(req)).group(1),

            "__aaid": "0",

            "__user": re.search('"actorID":"(\d+)"', str(req)).group(1),
            "__a": str(random.randrange(1, 6)),
            "__req": "12",
            "__hs": re.search('"haste_session":"(.*?)"', str(req)).group(1),
            "dpr": "3",
            "__ccg": re.search('"connectionClass":"(.*?)"', str(req)).group(1),
            "__rev": re.search('"__spin_r":(\d+),', str(req)).group(1),
            "__s": "",
            "__hsi": re.search(r'"hsi":"(\d+)"', str(req)).group(1),
            "__dyn": "",
            "__csr": "",
            "__comet_req": re.search('__comet_req=(\d+)', str(req)).group(1),
            "fb_dtsg": re.search('\\["DTSGInitialData",\\[\\],{"token":"(.*?)"}', req).group(1),#re.search(r'\"DTSGInitialData\",\[(.*?)\],\{\"token\":\"(.*?)\"', str(req)).group(2),
            "jazoest": re.search('jazoest=(.*?)"', str(req)).group(1),
            "lsd": re.search('"LSD",\[\],{"token":"(.*?)"}', str(req)).group(1),
            "__spin_r": re.search('"__spin_r":(\d+),', str(req)).group(1),
            "__spin_b": "trunk",
            "__spin_t": re.search('"__spin_t":(\d+),', str(req)).group(1),
            'fb_api_caller_class': 'RelayModern'
        }