from flask import Flask, render_template, request, redirect, url_for
import subprocess
from email.message import EmailMessage

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def send_email():
    if request.method == 'POST':
        sender_email = 'your_email@example.com'  # Replace with your sender email address
        recipient_email = request.form['recipient']
        subject = request.form['subject']
        message = request.form['message']

        msg = EmailMessage()
        msg.set_content(message)
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = recipient_email

        try:
            p = subprocess.Popen(
                ['/usr/sbin/sendmail', '-t'],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            p.communicate(input=msg.as_string().encode())
            return "Email sent successfully!"
        except Exception as e:
            return f"Error sending email: {e}"

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
