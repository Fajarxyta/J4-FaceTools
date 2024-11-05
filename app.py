from Tools.imports import *
from Tools.Login import LOGIN
from Tools.GetUserData import UserData

headers = {
  'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
  'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
  'cache-control': "max-age=0",
  'dpr': "2.75",
  'viewport-width': "980",
  'sec-ch-ua': "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
  'sec-ch-ua-mobile': "?0",
  'sec-ch-ua-platform': "\"Linux\"",
  'sec-ch-ua-platform-version': "\"\"",
  'sec-ch-ua-model': "\"\"",
  'sec-ch-ua-full-version-list': "\"Not-A.Brand\";v=\"99.0.0.0\", \"Chromium\";v=\"124.0.6327.4\"",
  'sec-ch-prefers-color-scheme': "light",
  'upgrade-insecure-requests': "1",
  'sec-fetch-site': "same-origin",
  'sec-fetch-mode': "navigate",
  'sec-fetch-user': "?1",
  'sec-fetch-dest': "document",
  'accept-language': "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
}

headers_post = {
  'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
  #'Accept-Encoding': "gzip, deflate, br, zstd",
  'Content-Type': "application/x-www-form-urlencoded",
  'sec-ch-ua-full-version-list': "\"Chromium\";v=\"130.0.6723.86\", \"Google Chrome\";v=\"130.0.6723.86\", \"Not?A_Brand\";v=\"99.0.0.0\"",
  'sec-ch-ua-platform': "\"Linux\"",
  'sec-ch-ua': "\"Chromium\";v=\"130\", \"Google Chrome\";v=\"130\", \"Not?A_Brand\";v=\"99\"",
  'x-fb-friendly-name': "ProfileCometAppCollectionListRendererPaginationQuery",
  'sec-ch-ua-mobile': "?0",
  'sec-ch-ua-model': "\"\"",
  'x-asbd-id': "129477",
  'x-fb-lsd': "DG_Tiuh1s5bAhY31tuKNIv",
  'sec-ch-prefers-color-scheme': "light",
  'sec-ch-ua-platform-version': "\"\"",
  'origin': "https://web.facebook.com",
  'sec-fetch-site': "same-origin",
  'sec-fetch-mode': "cors",
  'sec-fetch-dest': "empty",
  'accept-language': "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
}
class Main:
    def __init__(self) -> None:
        pass
    
    def menu(self):
        os.system('clear')
        username, userid = None, None
        try:
            cookie = json.loads(open('Data/Cookie.json', 'r').read())['Cookie']
            userid, username = LOGIN().cookiesvalidasi(cookie)
        except Exception as e:
            console.print(f' [bold red]#[bold white]) Cookies Invalid Silahkan Login Kembali\n [bold red]#[bold white]) [bold red]{str(e)}[bold white]')
            time.sleep(1.5)
            LOGIN().LoginCookies()
        
        console.print(f' [bold green]#[bold white]) Userid: [bold green]{userid}[bold white] | Name: [bold green]{username[:6]}[bold white]')
        console.print(""" [bold green]1[bold white]) Dump from firends list\n [bold green]2[bold white]) Dump from members group\n [bold green]3[bold white]) Dump from search name\n [bold green]4[bold white]) Crack ulang hasil checkpoint\n [bold red]5[bold white]) Remove Cookies\n [bold red]6[bold white]) Exit Tools\n""")
        pilihan = console.input(" [bold green]#[bold white]) Pilih (1-6): ")
        if pilihan == '1' or pilihan == '01':
            console.print(" [bold green]#[bold white]) Masukan ID Target Gunakan Tanda Koma Sebagai Pemisah (,)")
            user = console.input(" [bold green]#[bold white]) Userid: ")
            for userID in user.split(','):
                GraphQlDump().Dumpteman(userID, cookie)
                
            if len(DUMP) < 50:
                console.print(" [bold green]#[bold white]) [bold red]userid terlalu sedikit!!!")
                exit()
            else:
                console.print(" [bold green]#[bold white]) Jumlah ID terkumpul [bold green]{len(DUMP)}[bold white]")
                Setting
                
        elif pilihan == '2' or pilihan == '02':
            pass
        elif pilihan == '3' or pilihan == '03':
            pass
        
class GraphQlDump:
    def __init__(self):
        pass
    
    def Dumpteman(self, userid, cookie):
        try:
            with requests.Session() as r:
                params = {'id': userid, 'sk': "friends"}
                response = r.get("https://web.facebook.com/profile.php", params = params, cookies = {'cookie':cookie}, headers=headers).text
                userID = re.search('"tab_key":"friends_all","id":"(.*?)"', str(response)).group(1)
                end_cursor = re.search('"page_info":{"end_cursor":"(.*?)","has_next_page":true}', response).group(1)
                data = UserData().dataGraphQL(response)
                self.NextDumpTeman(userid, userID, cookie, data, end_cursor)
        except Exception as e:
            console.print(f" [bold green]#[bold white]) {str(e).upper()}", end='\r')
            time.sleep(5.0)
            return("Dump error")
    
    def NextDumpTeman(self, ids, userid, cookie, data, cursor):
        try:
            with requests.Session() as r:
                data.update({
                    'fb_api_req_friendly_name':'ProfileCometAppCollectionListRendererPaginationQuery',
                    'variables': json.dumps({"count":8,"cursor":cursor,"scale":3,"search":None,"id":userid}),
                    'server_timestamps':True,
                    'doc_id':'8512257125510319'
                })
                headers_post.update({
                     'referer': f"https://web.facebook.com/profile.php?id={ids}&sk=friends",
                    'x-fb-friendly-name': "ProfileCometAppCollectionListRendererPaginationQuery",
                    'x-fb-lsd': data["lsd"],
                    'priority': "u=1, i",
                    'cookie': cookie
                })
                post = r.post('https://web.facebook.com/api/graphql/', data=data, cookies={'cookie':cookie}, headers=headers_post)
                json_data = json.loads(post.text)
                for kyta in json_data["data"]["node"]["pageItems"]["edges"]:
                    try:
                        usrID = kyta["node"]["actions_renderer"]["action"]["client_handler"]["profile_action"]["restrictable_profile_owner"]["id"]
                        name = kyta["node"]["actions_renderer"]["action"]["client_handler"]["profile_action"]["restrictable_profile_owner"]["name"]
                        if str(name) in str(DUMP):
                            continue
                        else:
                            DUMP.append(f'{usrID}|{name}')
                            console.print(f" [bold green]#[bold white]) {usrID}|{name[:6]} => {len(DUMP)}", end='\r')
                    except (IndexError, TypeError):
                        continue
                if json_data["data"]["node"]["pageItems"]["page_info"]["has_next_page"]:
                    next = json_data["data"]["node"]["pageItems"]["page_info"]["end_cursor"]
                    self.NextDumpTeman(ids, userid, cookie, data, next)
                else:
                    return ("Dump berhasil")
        except (KeyboardInterrupt):
            Console().print(f"                                                               ", end='\r')
            time.sleep(1.5)
            return ("Dump berhasil")
            

if __name__ == '__main__':
    Start = Main()
    Start.menu()