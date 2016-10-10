#!/usr/bin/python

import smtplib
import os
from datetime import datetime
from email.mime.text import MIMEText
import speedtest_cli as stc

result = stc.speedtest()
ping = result["ping"]["latency"]
download = (result["download"]/1000000) * 8
upload = (result["upload"]/1000000) * 8
time = datetime.now()

passpath = os.environ["HOME"] + "/path/to/email/password/text/file/"
fp = open(passpath, 'r')
# Create a text/plain message
passw = fp.read()
fp.close()
stats = "%s\nPing:\n%s\nDownload:\n%s\nUpload:\n%s" % (time, ping, download, upload)

msg = MIMEText(stats, 'plain')

me = "the sender's email address"
you = "the recipient's email address"

##    The recipients email address will be their phone number
##    and a specific domain, depending on the carrier:
##    AT&T: number@txt.att.net
##    T-Mobile: number@tmomail.net
##    Verizon: number@vtext.com
##    Sprint: number@messaging.sprintpcs.com or number@pm.sprint.com
##    Virgin Mobile: number@vmobl.com
##    Tracfone: number@mmst5.tracfone.com
##    Metro PCS: number@mymetropcs.com
##    Boost Mobile: number@myboostmobile.com
##    Cricket: number@sms.mycricket.com
##    Ptel: number@ptel.com
##    Republic Wireless: number@text.republicwireless.com
##    Suncom: number@tms.suncom.com
##    Ting: number@message.ting.com
##    U.S. Cellular: number@email.uscc.net
##    Consumer Cellular: number@cingularme.com
##    C-Spire: number@cspire1.com
##    Page Plus: number@vtext.com

msg['Subject'] = "Speedtest"
msg['From'] = me
msg['To'] = you

s = smtplib.SMTP('smtp.gmail.com:587')
s.starttls()
s.login(me, passw)
s.sendmail(me, you, msg.as_string())
s.quit()
