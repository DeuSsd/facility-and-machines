from flask import Flask, render_template, request, url_for, flash, redirect
from markupsafe import escape

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234567'


@app.route('/', methods=('GET', 'POST'))
def index():
    """
    Start page to generate machines with configurations or start creating the solution
    ---------------------
    | text:
    | enterBox:
    | Button:
    |
    |
    |
    ---------------------
    """
    if request.method == 'POST':
        # datasetName = request.form['title']
        # content = request.form['content']
        if "solution" in request.form:
            return render_template('result.html')
        elif "create" in request.form:
            pass

        # if not datasetName:
            # Pop-up window
            # flash('DatasetName is required!')
        # else:
        #     return redirect(url_for('index'))

    return render_template('index.html')


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'


@app.route('/<int:post_id>')
def result(post_id):
    post = 1
    # return render_template('post.html', post=post)
    return render_template('base.html', post=post)



if __name__ == '__main__':
    app.run()