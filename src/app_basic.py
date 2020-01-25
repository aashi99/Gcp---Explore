import os
import ocr
import translate
from flask import Flask, render_template, request
l = []
app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/image")
def image():
    import click1
    img_nam = click1.click2()
    destination = "/home/aashi/Downloads/GoogleApi_Project/src"+ img_nam
    print("printing destination......")
    print(destination)
    l = ocr.detect_text(destination)
    print(str(l))
    trans = translate.translate_text("HOW TO WRITE ALT TEXT AND IMAGE DESCRIPTIONS FOR THE VISUALLY IMPAIRED")

    return render_template("complete.html", output=l, op = trans )


    # return render_template("index.html")
    # return '<h1>' + 'Image Clicked' +'</h1>'

@app.route("/upload", methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    print("target =     ",target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print("file =     ",file)
        filename = file.filename
        destination = "/".join([target, filename])
        print("destination =    ",destination)
        file.save(destination)
    l = ocr.detect_text(destination)
    print(str(l))
    trans = translate.translate_text("HOW TO WRITE CORRECTLY")

    return render_template("complete.html", output=l, op = trans )

if __name__ == "__main__":
    app.run(port=4555, debug=True)
