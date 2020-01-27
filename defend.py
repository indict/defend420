import requests, sys
from threading import Thread

if len(sys.argv) < 3:
    sys.exit(f"Usage: {sys.argv[0]} <target> <username> <password>")

Name = sys.argv[2]
Passwrd = sys.argv[3]

class Turbo:
    csrfTok = "https://www.instagram.com/accounts/login/"
    LoginURL = "https://www.instagram.com/accounts/login/ajax/"
    CheckAlias = "https://www.instagram.com/accounts/edit/"
    def __init__(self, user, passw, target):
        self.username = user
        self.password = passw
        self.target = target 
        self.s = requests.Session()

    def login(self):
        self.s.headers.update({
                'accept': '*/*',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/accounts/login/',
                'user-agent': 'Mozilla/5.0 (Linux; U; Android 2.3.3; en-us; HTC_DesireS_S510e Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
                'x-instagram-ajax': '1',
                'x-requested-with': 'XMLHttpRequest'
        })
        Grab = self.s.get(self.csrfTok)
        self.s.headers.update({"x-csrftoken": Grab.cookies.get_dict()['csrftoken']})
        LoginData = {
            'username': self.username,
            'password': self.password,
            'queryParams': '{}'
        }
        AccLogin = self.s.post(self.LoginURL, data=LoginData)
        if AccLogin.json()['authenticated']:
            self.s.headers.update({"x-csrftoken": AccLogin.cookies.get_dict()['csrftoken']})
            self.LoginStatus = True
            self.CheckAv()
        else:
            print(f"{sys.argv[1]} failed to login")


    def CheckAv(self):
        self.Checks = 0
        while self.LoginStatus:
            CheckData = {
                'first_name': self.target,
                'email': self.target + "@crime.su",
                'username': self.target,
                'phone_number': '{}',
                'biography': 'tommy2fast4u',
                'external_url': '{}',
                'chaining_enabled': 'on'
            }
            GetData = self.s.post(self.CheckAlias, data=CheckData)
            if GetData.json()['status'] == "fail":
                self.Checks += 1
                print(f"{self.Checks}")
            else:
                print(f"Claimed {self.username}")

Dayum = Turbo(Name, Passwrd, sys.argv[1])
Dayum.login()
