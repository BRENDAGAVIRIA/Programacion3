from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html', page='main')

@app.route('/accordion')
def accordion():
    return render_template('components-accordion.html')

@app.route('/alerts')
def alerts():
    return render_template('components-alerts.html')

@app.route('/badges')
def badges():
    return render_template('components-badges.html')
