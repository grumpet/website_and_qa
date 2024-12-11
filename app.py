from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy data for pictures
pictures = [
    {"id": 1, "url": "https://via.placeholder.com/150"},
    {"id": 2, "url": "https://via.placeholder.com/150"},
    {"id": 3, "url": "https://via.placeholder.com/150"}
]

@app.route('/')
def home():
    return render_template('home.html', pictures=pictures)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        # Process the sign-up data here
        return redirect(url_for('home'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # Process the login data here
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/terminate', methods=['POST'])
def terminate():
    # Logic to terminate the account
    return redirect(url_for('home'))

@app.route('/add_payment')
def add_payment():
    return render_template('add_payment.html')

@app.route('/add_payment', methods=['POST'])
def add_payment_post():
    # Logic to handle payment method addition
    card_number = request.form['card_number']
    expiry_date = request.form['expiry_date']
    cvv = request.form['cvv']
    # Process the payment method here
    return redirect(url_for('home'))

@app.route('/confirm/<int:picture_id>')
def confirm(picture_id):
    return render_template('confirm.html', picture_id=picture_id)

@app.route('/picture/<int:picture_id>')
def picture(picture_id):
    picture = next((pic for pic in pictures if pic["id"] == picture_id), None)
    if picture:
        return render_template('picture.html', picture=picture)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')