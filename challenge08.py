import bz2

UN_CRYPT = b"BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084"
PW_CRYPT = b"BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08"

username = bz2.decompress(UN_CRYPT).decode("utf-8")
password = bz2.decompress(PW_CRYPT).decode("utf-8")

print("Click on the link on the insect.  Use the credentials below to authenticate.")
print("(or use this link: http://www.pythonchallenge.com/pc/return/good.html)")
print(f"Username: {username}")
print(f"Password: {password}")
