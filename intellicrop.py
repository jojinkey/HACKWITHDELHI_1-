#"C:/Users/jalaj/Downloads/Geek/PYS/Intelli_crop_data.csv"
#"C:/Users/jalaj/VsCodeLiter/PYs/intelligent_crop/Intelli_crop_data.csv"


# Get the current directory
# # current_directory = os.getcwd()
# "C:/Users/jalaj/VsCodeLiter/PYs/intelligent_crop/Intelli_crop_data.csv"
# Join the current directory with the name of your Flask app script
# flask_app_directory = os.path.join(current_directory, 'your_flask_app.py')
# Print the directory containing the Flask app script
# print(flask_app_directory)  that is C:\Users\jalaj\your_flask_app.py
from flask import Flask, render_template, request
import csv
import os
import secrets





template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
app = Flask(__name__, template_folder=template_dir,  static_folder='static')
app.static_url_path = '/static'

app.secret_key = secrets.token_hex(16)




# Specify path to the csv file
csv_file = "C:/Users/jalaj/VsCodeLiter/PYs/intelligent_crop/Intelli_crop_data.csv"






#Read the csv file and store the data in a dictionary
crop_data = {}
with open(csv_file) as f:
    reader = csv.DictReader(f)
    for row in reader:
        crop_name = row.pop('Crop Name')
        crop_data[crop_name] = row




def compute_yield(crop_type, area, avg_yield):
    total_yield = area * avg_yield
    return f"The total yield of {crop_type} is {total_yield} quintals."



@app.route('/')
def index():
    # define the path for index.html file
    return render_template('index.html')

@app.route('/greenhealth')
def storage():
    # define the path for index.html file
    return render_template('ghealth.html')

@app.route('/info')

def info():
    # define the path for index.html file
    return render_template('info.html')

@app.route('/community')
def predictions():
    # define the path for index.html file
    return render_template('info.html')






if __name__ == '__main__':
    app.run()
