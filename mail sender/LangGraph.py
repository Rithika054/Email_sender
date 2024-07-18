from flask import Flask,request
from flask_mail import Mail, Message 

app = Flask(__name__)

app.config['MAIL_SERVER']='sandbox.smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = '00b5ed9d5cfa30'
app.config['MAIL_PASSWORD'] = 'd01f9615243841'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)


@app.route("/",methods=['POST'])
def index():
  data = request.get_json()
  print(data)
  subject = data['subject']
  message = data['message']
  sender = data['sender']
  recipients = data['recipients']
  msg = Message(subject, sender =  sender, recipients = [recipients])
  msg.body = message
  mail.send(msg)
  return data

if __name__ == '__main__':
   app.run(debug = True)