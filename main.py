from flask import Flask, request, render_template
from google.cloud import firestore

app = Flask(__name__)
db = firestore.Client()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        doc_ref = db.collection('train_data').document()
        doc_ref.set({
            'instruction': request.form['instruction'],
            'code': request.form['code']
        })
        return 'Data submitted successfully!'
    return render_template('form.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
