from Tools.imports import *

class LOGIN:
    def __init__(self):
        self.file = 'Data/Cookie.json'
    
    def LoginCookies(self):
        try:
            cookie = console.input(' [bold green]#[bold white]) Cookies: ')
            cookies = self.cookiesvalidasi(cookie)
            if cookies:
                userid, username = cookies
                if 'c_user=' in str(cookie):
                    with open(self.file, 'w') as w:
                        w.write(
                            json.dumps({'Cookie': cookie})
                        )
                    w.close()
                    console.print(f' [bold green]#[bold white]) Login user: [bold green]{username}')
                    time.sleep(2)
                    exit()
                else:
                    console.print(f'[bold red] #[bold white]) [bold red]Login Cookies Gagal Cobalagi..!!!')
                    exit()
            else:
                console.print(f'[bold red] #[bold white]) [bold red]Login Cookies Gagal Cobalagi..!!!')
                exit()
        except Exception as error:
            console.print(f' [bold red]#[bold white]) Login Error: [bold red]{error}[bold white]')
    
    def cookiesvalidasi(self, cokie):
        try:
            with requests.Session() as r:
                req = r.get(f'https://www.facebook.com/profile.php', cookies={'cookie': cokie})
                userID_match = re.search('"actorID":"(.*?)"', req.text)
                username_match = re.search('"NAME":"(.*?)"', req.text)
                if userID_match and username_match:
                    return userID_match.group(1), username_match.group(1)
                else:
                    return False, False
        except Exception as error:
            console.print(f' [bold red]#[bold white]) Validasi Error: [bold red]{error}[bold white]')