from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/theophilus okoye')
def resume():
    return render_template('theophilusokoye.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')