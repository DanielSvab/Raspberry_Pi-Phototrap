import smtplib
from datetime import datetime
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
from email.MIMEMultipart import MIMEMultipart


frm = 'czechbery@gmail.com'
to = 'danielswab@gmail.com'
psw = '*******'
#ImgFileName je promena pro cestu k obrazkum ktere chci poslat
def SendMail(ImgFileName):
    msg = MIMEMultipart()
    msg['Subject'] = 'Motion'
    msg['From'] = frm
    msg['To'] = to

    body = 'Alert!! Motion Detected!!\nTime: %s' % str(datetime.now())
    msg.attach(MIMEText(body, 'plain'))

#    msgText = MIMEText('<b>Some <i>HTML</i> text</b> and an image.<br><img src="cid:image1"><br>Nifty!', 'html')
#    msgAlternative.attach(msgText)

    fp = open(ImgFileName,'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Content-Disposition','attachment; filename="image.jpg"$
    msg.attach(msgImage)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(frm, psw)
    s.sendmail(frm, to, msg.as_string())
    s.quit()
