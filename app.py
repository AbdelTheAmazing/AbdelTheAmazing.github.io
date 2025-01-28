from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', active_page='home')

@app.route('/about')
def about():
    return render_template('about.html', active_page='about')

@app.route('/menu')
def menu():
    return render_template('menu.html', active_page='menu')

if __name__ == '__main__':
    app.run(debug=True)
