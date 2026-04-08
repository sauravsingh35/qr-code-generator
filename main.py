import qrcode
qr=qrcode.make("https://nietcloud.niet.co.in/login.htm;jsessionid=0BADC21CE56CF807549306C1149D5FCF")
qr.save("qrcode.png")
print("qr code genrated")
