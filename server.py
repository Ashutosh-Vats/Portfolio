from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)


@app.route("/")
def my_home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Did not save to database.'
    else:
        return 'Something went wrong. Try again!'


'''''

@app.route("/index.html")
def home():
    return render_template('index.html')

@app.route("/about.html")
def about():
    return render_template('about.html')

@app.route("/works.html")
def work():
    return render_template('works.html')

@app.route("/contact.html")
def contacts():
    return render_template('contact.html')




@app.route("/components.html")
def component():
    return render_template('components.html')



@app.route("/work.html")
def about():
    return render_template('work.html')

@app.route("/contact.html")
def about():
    return render_template('contact.html')



@app.route("/about.html")
def about():
    return render_template('about.html')


@app.route("/blog")
def blog():
    return "<p>These are my thought on blog!</p>"

@app.route("/blog/2024/dogs")
def blog2():
    return "<p>This is my dog</p>"
#flask --app server --debug run
#flask --app server run
#flask --env development
#https://flask.palletsprojects.com/en/3.0.x/quickstart/
#https://flask.palletsprojects.com/en/3.0.x/cli/
#https://docs.python.org/fr/3/library/venv.html
#pip3 install Flask
# Web_Server/Scripts/activate.bat
'''''
