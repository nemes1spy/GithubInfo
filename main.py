from colorama import Fore, init
from datetime import datetime
import requests


init(autoreset=True)

class GithubApi(object):
    def __init__(self) -> None:
        self.__url = "https://api.github.com/users/"
        self.banner()
        
    
    def banner(self):
        print(Fore.RED+r"""
                (                           )
          ) )( (                           ( ) )( (
       ( ( ( )  ) )                     ( (   (  ) )(
      ) )     ,,\\\                     ///,,       ) (
   (  ((    (\\\\//                     \\////)      )
    ) )    (-(__//                       \\__)-)     (
   (((   ((-(__||                         ||__)-))    ) )
  ) )   ((-(-(_||           ```\__        ||_)-)-))   ((
  ((   ((-(-(/(/\\        ''; 9.- `      //\)\)-)-))    )
   )   (-(-(/(/(/\\      '';;;;-\~      //\)\)\)-)-)   (   )
(  (   ((-(-(/(/(/\======,:;:;:;:,======/\)\)\)-)-))   )
    )  '(((-(/(/(/(//////:%%%%%%%:\\\\\\)\)\)\)-)))`  ( (
   ((   '((-(/(/(/('uuuu:WWWWWWWWW:uuuu`)\)\)\)-))`    )
     ))  '((-(/(/(/('|||:wwwwwwwww:|||')\)\)\)-))`    ((
  (   ((   '((((/(/('uuu:WWWWWWWWW:uuu`)\)\))))`     ))
        ))   '':::UUUUUU:wwwwwwwww:UUUUUU:::``     ((   )
          ((      '''''''\uuuuuuuu/``````         ))
           ))            `JJJJJJJJJ`           ((
             ((            LLLLLLLLLLL         ))
               ))         ///|||||||\\\       ((
                 ))      (/(/(/(^)\)\)\)       ((
                  ((                           ))
                    ((                       ((
                      ( )( ))( ( ( ) )( ) (()     


                   { @OWNER : Nemesis }

        
""")
        while True:
            print(Fore.LIGHTMAGENTA_EX+"""
    [1] Kullanıcı Bilgi Topla
    [2] Kullanıcı Repolarını Bul
    [3] Kullanıcı Takipçilerini Bul
    [4] Kullanıcının Takip Ettiği Hesapları Bul
    [5] Çıkış Yap
            

    """)
            print("İşlem Numarasını Girin : ", end="")
            self.query = input()

            print(Fore.CYAN+"[-] Kullanıcı adını girin : ", end="")
            self.username = input()

            if self.query == "1": self.getInfo()
            elif self.query == "2": self.getRepos()
            elif self.query == "3": self.getFollowers()
            elif self.query == "4": self.getFollowing()
            elif self.query == "5": exit()
            

        
       


    def getCurrentTime(self) -> str:
        return datetime.now().strftime("%H:%M:%S")


       
    def getInfo(self):
        
            __requests = requests.get(url = self.__url + self.username).json()
            
            print(f"""
                        {Fore.LIGHTYELLOW_EX} * Hesap Bilgileri * {Fore.RESET}
    {Fore.BLUE}[ {self.getCurrentTime()} ]{Fore.RESET} {Fore.LIGHTBLUE_EX}Kullanıcı Adı {Fore.RESET} : {__requests['login']}
    {Fore.BLUE}[ {self.getCurrentTime()} ]{Fore.RESET} {Fore.LIGHTBLUE_EX}İsim          {Fore.RESET} : {__requests['name']}
    {Fore.BLUE}[ {self.getCurrentTime()} ]{Fore.RESET} {Fore.LIGHTBLUE_EX}Şirket        {Fore.RESET} : {__requests['company']}
    {Fore.BLUE}[ {self.getCurrentTime()} ]{Fore.RESET} {Fore.LIGHTBLUE_EX}Blog          {Fore.RESET} : {__requests['blog']}
    {Fore.BLUE}[ {self.getCurrentTime()} ]{Fore.RESET} {Fore.LIGHTBLUE_EX}Yer           {Fore.RESET} : {__requests['location']}
    {Fore.BLUE}[ {self.getCurrentTime()} ]{Fore.RESET} {Fore.LIGHTBLUE_EX}Mail          {Fore.RESET} : {__requests['email']}
    {Fore.BLUE}[ {self.getCurrentTime()} ]{Fore.RESET} {Fore.LIGHTBLUE_EX}Depo Sayısı   {Fore.RESET} : {__requests['public_repos']}
    {Fore.BLUE}[ {self.getCurrentTime()} ]{Fore.RESET} {Fore.LIGHTBLUE_EX}Takipçi Sayısı{Fore.RESET} : {__requests['followers']}
    {Fore.BLUE}[ {self.getCurrentTime()} ]{Fore.RESET} {Fore.LIGHTBLUE_EX}Takip Sayısı  {Fore.RESET} : {__requests['following']}
    {Fore.BLUE}[ {self.getCurrentTime()} ]{Fore.RESET} {Fore.LIGHTBLUE_EX}Biyografi     {Fore.RESET} : {str(__requests['bio']).strip()}
    {Fore.BLUE}[ {self.getCurrentTime()} ]{Fore.RESET} {Fore.LIGHTBLUE_EX}Hesap Oluşturulma Tarihi{Fore.RESET} : {(__requests['created_at'])}
        """)

            


    def getRepos(self):
        __requestsRepos = requests.get(url = self.__url + self.username + "/repos").json()
        for repo in __requestsRepos:
            print(f"""
{Fore.BLUE}[ {self.getCurrentTime()} ]{Fore.RESET} 
{Fore.LIGHTBLUE_EX}İsim {Fore.RESET} : {repo['name']} | 
{Fore.LIGHTBLUE_EX}Link {Fore.RESET} : {repo['html_url']}
{Fore.LIGHTBLUE_EX}Açıklama {Fore.RESET} : {repo['description']}
{Fore.LIGHTBLUE_EX}Oluşturulma Tarihi {Fore.RESET} : {repo['created_at']}
{Fore.LIGHTBLUE_EX}Güncelleme Tarihi {Fore.RESET} : {repo['updated_at']}
{Fore.LIGHTBLUE_EX}Programlama Dili  {Fore.RESET} : {repo['language']}
{Fore.LIGHTBLUE_EX}Durum {Fore.RESET} : {repo['visibility']}

""".strip())

    def getFollowers(self):
        __requestsFollowers = requests.get(url = self.__url + self.username + "/followers").json()
        for followers in __requestsFollowers:
            print(f"""

{Fore.BLUE}[ {self.getCurrentTime()} ]{Fore.RESET}
{Fore.LIGHTBLUE_EX}Kullanıcı Adı {Fore.RESET} : {followers['login']}  
{Fore.LIGHTBLUE_EX}Avatar Url {Fore.RESET} : {followers['avatar_url']}
{Fore.LIGHTBLUE_EX}Kullanıcı Url {Fore.RESET} : {followers['url']}
""".strip())


    def getFollowing(self):
        __requestsFollowing = requests.get(url= self.__url + self.username + "/following").json()
        for followers in __requestsFollowing:
            print(f"""

{Fore.BLUE}[ {self.getCurrentTime()} ]{Fore.RESET}
{Fore.LIGHTBLUE_EX}Kullanıcı Adı {Fore.RESET} : {followers['login']}  
{Fore.LIGHTBLUE_EX}Avatar Url {Fore.RESET} : {followers['avatar_url']}
{Fore.LIGHTBLUE_EX}Kullanıcı Url {Fore.RESET} : {followers['url']}
""".strip())










        

if __name__ == "__main__":
    app = GithubApi()
    app.banner()
