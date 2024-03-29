import requests
import re
import uuid
import argparse
import json
code=[93,["Afghanistan"],
355,["Albania"],
213,["Algeria"],
684,["American Samoa"],
376,["Andorra"],
244,["Angola"],
809,["Anguilla"],
268,["Antigua"],
54,["Argentina"],
374,["Armenia"],
297,["Aruba"],
247,["Ascension Island"],
61,["Australia"],
672,["Australian External Territories"],
43,["Austria"],
994,["Azerbaijan"],
242,["Bahamas"],
246,["Barbados"],
973,["Bahrain"],
880,["Bangladesh"],
375,["Belarus"],
32,["Belgium"],
501,["Belize"],
229,["Benin"],
809,["Bermuda"],
975,["Bhutan"],
284,["British Virgin Islands"],
591,["Bolivia"],
387,["Bosnia and Hercegovina"],
267,["Botswana"],
55,["Brazil"],
284,["British V.I."],
673,["Brunei Darussalm"],
359,["Bulgaria"],
226,["Burkina Faso"],
257,["Burundi"],
855,["Cambodia"],
237,["Cameroon"],
1,["Canada"],
238,["CapeVerde Islands"],
1,["Caribbean Nations"],
345,["Cayman Islands"],
238,["Cape Verdi"],
236,["Central African Republic"],
235,["Chad"],
56,["Chile"],
86,["China (People's Republic)"],
886,["China-Taiwan"],
57,["Colombia"],
269,["Comoros and Mayotte"],
242,["Congo"],
682,["Cook Islands"],
506,["Costa Rica"],
385,["Croatia"],
53,["Cuba"],
357,["Cyprus"],
420,["Czech Republic"],
45,["Denmark"],
246,["Diego Garcia"],
767,["Dominca"],
809,["Dominican Republic"],
253,["Djibouti"],
593,["Ecuador"],
20,["Egypt"],
503,["El Salvador"],
240,["Equatorial Guinea"],
291,["Eritrea"],
372,["Estonia"],
251,["Ethiopia"],
500,["Falkland Islands"],
298,["Faroe (Faeroe) Islands (Denmark)"],
679,["Fiji"],
358,["Finland"],
33,["France"],
596,["French Antilles"],
594,["French Guiana"],
241,["Gabon (Gabonese Republic)"],
220,["Gambia"],
995,["Georgia"],
49,["Germany"],
233,["Ghana"],
350,["Gibraltar"],
30,["Greece"],
299,["Greenland"],
473,["Grenada/Carricou"],
671,["Guam"],
502,["Guatemala"],
224,["Guinea"],
245,["Guinea-Bissau"],
592,["Guyana"],
509,["Haiti"],
504,["Honduras"],
852,["Hong Kong"],
36,["Hungary"],
354,["Iceland"],
91,["India"],
62,["Indonesia"],
98,["Iran"],
964,["Iraq"],
353,["Ireland (Irish Republic; Eire)"],
972,["Israel"],
39,["Italy"],
225,["Ivory Coast (La Cote d'Ivoire)"],
876,["Jamaica"],
81,["Japan"],
962,["Jordan"],
7,["Kazakhstan"],
254,["Kenya"],
855,["Khmer Republic (Cambodia/Kampuchea)"],
686,["Kiribati Republic (Gilbert Islands)"],
82,["Korea, Republic of (South Korea)"],
850,["Korea, People's Republic of (North Korea)"],
965,["Kuwait"],
996,["Kyrgyz Republic"],
371,["Latvia"],
856,["Laos"],
961,["Lebanon"],
266,["Lesotho"],
231,["Liberia"],
370,["Lithuania"],
218,["Libya"],
423,["Liechtenstein"],
352,["Luxembourg"],
853,["Macao"],
389,["Macedonia"],
261,["Madagascar"],
265,["Malawi"],
60,["Malaysia"],
960,["Maldives"],
223,["Mali"],
356,["Malta"],
692,["Marshall Islands"],
596,["Martinique (French Antilles)"],
222,["Mauritania"],
230,["Mauritius"],
269,["Mayolte"],
52,["Mexico"],
691,["Micronesia (F.S. of Polynesia)"],
373,["Moldova"],
33,["Monaco"],
976,["Mongolia"],
473,["Montserrat"],
212,["Morocco"],
258,["Mozambique"],
95,["Myanmar (former Burma)"],
264,["Namibia (former South-West Africa)"],
674,["Nauru"],
977,["Nepal"],
31,["Netherlands"],
599,["Netherlands Antilles"],
869,["Nevis"],
687,["New Caledonia"],
64,["New Zealand"],
505,["Nicaragua"],
227,["Niger"],
234,["Nigeria"],
683,["Niue"],
850,["North Korea"],
1670,["North Mariana Islands (Saipan)"],
47,["Norway"],
968,["Oman"],
92,["Pakistan"],
680,["Palau"],
507,["Panama"],
675,["Papua New Guinea"],
595,["Paraguay"],
51,["Peru"],
63,["Philippines"],
48,["Poland"],
351,["Portugal (includes Azores)"],
1787,["Puerto Rico"],
974,["Qatar"],
262,["Reunion (France)"],
40,["Romania"],
7,["Russia"],
250,["Rwanda (Rwandese Republic)"],
670,["Saipan"],
378,["San Marino"],
239,["Sao Tome and Principe"],
966,["Saudi Arabia"],
221,["Senegal"],
381,["Serbia and Montenegro"],
248,["Seychelles"],
232,["Sierra Leone"],
65,["Singapore"],
421,["Slovakia"],
386,["Slovenia"],
677,["Solomon Islands"],
252,["Somalia"],
27,["South Africa"],
34,["Spain"],
94,["Sri Lanka"],
290,["St. Helena"],
869,["St. Kitts/Nevis"],
508,["St. Pierre &(et) Miquelon (France)"],
249,["Sudan"],
597,["Suriname"],
268,["Swaziland"],
46,["Sweden"],
41,["Switzerland"],
963,["Syrian Arab Republic (Syria)"],
689,["Tahiti (French Polynesia)"],
886,["Taiwan"],
7,["Tajikistan"],
255,["Tanzania (includes Zanzibar)"],
66,["Thailand"],
228,["Togo (Togolese Republic)"],
690,["Tokelau"],
676,["Tonga"],
1868,["Trinidad and Tobago"],
216,["Tunisia"],
90,["Turkey"],
993,["Turkmenistan"],
688,["Tuvalu (Ellice Islands)"],
256,["Uganda"],
380,["Ukraine"],
971,["United Arab Emirates"],
44,["United Kingdom"],
598,["Uruguay"],
1,["USA"],
7,["Uzbekistan"],
678,["Vanuatu (New Hebrides)"],
39,["Vatican City"],
58,["Venezuela"],
84,["Viet Nam"],
1340,["Virgin Islands"],
681,["Wallis and Futuna"],
685,["Western Samoa"],
381,["Yemen (People's Democratic Republic of)"],
967,["Yemen Arab Republic (North Yemen)"],
381,["Yugoslavia (discontinued)"],
243,["Zaire"],
260,["Zambia"],
263,["Zimbabwe"]]
def token():
    req=requests.get('https://www.instagram.com/').text
    token=re.search('"csrf_token":"(.*?)",',req).group(1)
    return token
def getinfo(token,username):
    guid=str(uuid.uuid4())
    deviceid='android-'+guid
    data={'q':username,'directly_sign_in': True,'username':username,'device_id':deviceid,'guid':guid}
    headers={'user-agent':'Mozilla/5.0 (Linux; U; Android 2.2) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','X-csrftoken':token}
    req=requests.post('https://i.instagram.com/api/v1/users/lookup/',headers=headers,data=data).text
    if 'obfuscated_phone' in req:
        info=requests.get('https://www.instagram.com/'+username+'?__a=1').text
        x=json.loads(req)
        req1=x['obfuscated_phone']
        req2=json.loads(info)
        req2=req2['graphql']['user']['edge_owner_to_timeline_media']['count']
        req3=x['user']['is_private']
        req4=x['user_id']
        req5=re.search('"edge_followed_by":{"count":(.*?)},',info).group(1)
        req6=re.search('"edge_follow":{"count":(.*?)},',info).group(1)
        return [req1,req2,req3,req4,req5,req6]
    else:
        
        info=requests.get('https://www.instagram.com/'+username+'?__a=1').text
        x=json.loads(req)
        req1='null'
        req2=json.loads(info)
        req2=req2['graphql']['user']['edge_owner_to_timeline_media']['count']
        req3=x['user']['is_private']
        req4=x['user_id']
        req5=re.search('"edge_followed_by":{"count":(.*?)},',info).group(1)
        req6=re.search('"edge_follow":{"count":(.*?)},',info).group(1)
        return [req1,req2,req3,req4,req5,req6]

def filtter(text,x):
    v=text.index('*')
    result=text[1:v-1]
    result=x.index(int(result))
    return x[result+1][0]
def args():
    arg=argparse.ArgumentParser()
    arg.add_argument('-u','--user',dest='username',help='-u | --user Pass A username')
    return arg.parse_args().username
print('''
       ////////////////////////////////////////
     ///////////////////////////////////////////
   //////////////////////////////////////////////
  /////////////[ Coded By MrVirus ]///////////////
 //////////////[ Instagram : BQBB ]////////////////
///////////////[ Telegram : camera ]/////////////////
   //////////////////////////////////////////////
    ///////////////////////////////////////////
     ////////////////////////////////////////
''')   
if(args()):
    r=getinfo(token(),args())
    if r[0] =='null':
        country=r[0]
        print('Country : '+country+'\nUserID : '+str(r[3])+'\nis_private : '+str(r[2])+'\nFollowers : '+r[4]+'\nFollowing : '+r[5]+'\nusername : '+args()+'\nPosts : '+str(r[1]))
        input('')
    else:
        
        country=filtter(r[0],code)
        print('Country : '+country+'\nUserID : '+str(r[3])+'\nis_private : '+str(r[2])+'\nFollowers : '+r[4]+'\nFollowing : '+r[5]+'\nusername : '+args()+'\nPosts : '+str(r[1]))
        input('')
else:
    argsa=input('username : ')
    r=getinfo(token(),argsa)
    if r[0] =='null':
        country=r[0]
        print('Country : '+country+'\nUserID : '+str(r[3])+'\nis_private : '+str(r[2])+'\nFollowers : '+r[4]+'\nFollowing : '+r[5]+'\nusername : '+argsa+'\nPosts : '+str(r[1]))
        input('')
    else:
        country=filtter(r[0],code)
        print('Country : '+country+'\nUserID : '+str(r[3])+'\nis_private : '+str(r[2])+'\nFollowers : '+r[4]+'\nFollowing : '+r[5]+'\nusername : '+argsa+'\nPosts : '+str(r[1]))
        input('')
