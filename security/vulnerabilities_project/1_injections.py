from flask import Flask, session, request

app = Flask(__name__)

# As soon as your application accepts some kind of user data,
# that's a potential door to attackers.

# Run this Flask application and try submitting some message of your choice
# in the text input before submitting. You should see your message displayed on the next page.

# Now, try entering the following into the input text:
# <script>alert("I am an attacker!")</script>
# 
# Now submit again. What happens?

# Then, go to the next file

@app.route('/')
def index():
    return '''<form method="POST" action="/submit">
        <input type="text" name="message" value='<script>alert("I am an attacker!")</script>' />
        <input type="submit" />
    </form>'''


@app.route('/submit', methods=['POST'])
def submit():
    return '<h1>You submitted: ' + request.form['message'] + '</h1>'

if __name__ == '__main__':
    app.run()