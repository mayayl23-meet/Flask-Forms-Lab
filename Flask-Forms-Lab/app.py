from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "MayaYL25"
password = "12345"
facebook_friends=["Ella","Yael","Naama", "Tamari", "Yarin", "Mia", "Lia"]


@app.route('/', methods=['GET', 'POST'])  # '/' for the default page
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		user1 = request.form['username']
		password1 = request.form['password']
		if user1 == username and password1 == password:
			return redirect(url_for('home'))

		else:
			return render_template('login.html')			 
  	
@app.route('/home')
def home():
	return render_template('home.html', friends=facebook_friends)

@app.route('/friend_exists/<string:name>', methods=['GET', 'POST'])
def friend_exists(name):
	if name in facebook_friends:
		return render_template('friend_exists.html', friends=name, person='True')
	else:
		return render_template('friend_exists.html', friends=name, person='False')

if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)