from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the trained model from the pickle file
with open('model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

@app.route("/",methods=['GET', 'POST'])
def home():
    return render_template("indexFront.html")

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/input", methods=['GET', 'POST'])
def input():
    if request.method == 'POST':
        raised_hands = int(request.form.get('raised_hands'))  
        visited_resources = int(request.form.get('visited_resources')) 
        announcement_view = int(request.form.get('announcement_view')) 
        discussion = int(request.form.get('discussion'))  
        absent = int(request.form.get('absent')) 

        result = process_data(raised_hands, visited_resources, announcement_view, discussion, absent)
        return render_template('result.html', result=result)
    return render_template('index.html')

def process_data(raised_hands, visited_resources, announcement_view, discussion, absent):
    data = [[raised_hands, visited_resources, announcement_view, discussion, absent]]
    prediction = loaded_model.predict(data)
    if prediction[0] == 1:
        return "Potential Dropout"
    else:
        return "Not a Potential Dropout"
    

if __name__ == '__main__':
    app.run(debug=True)
