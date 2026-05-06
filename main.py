from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def face_detect():
    return render_template("QR_Reader.html")

if __name__ == '__main__':
    app.run()