from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
print(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return render_template('/thankyou.html')
        except:
            return 'didnt save to database'
    else:
        return 'something went wrong'



@app.route('/back_to_main', methods=['POST', 'GET'])
def back_to_main():
    return hello_world()


def write_to_csv(data):
    write = open("database.csv", "a", newline='')
    email = data['email']
    subject = data['subject']
    message = data['message']
    csv_writer = csv.writer(write, delimiter=',', quotechar="'", quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow([email, subject, message])
    pass
