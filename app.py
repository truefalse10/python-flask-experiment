from flask import Flask, request, render_template, flash

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        print('form submittet')
        print(request.form['upload'])
        flash('Your form was submittet')
        # execute julias function and return image url
    
    return render_template('index.html');

if __name__ == '__main__':
    app.run(debug=True)
