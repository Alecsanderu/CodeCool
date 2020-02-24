from flask import Flask, render_template, request, redirect
import data

app = Flask(__name__)



@app.route('/')
def main_page():
    return render_template("index.html")


@app.route('/request-counter', methods = ['GET', 'POST', 'PUT', 'DELETE'])
def count():
    data_method = data.read_file()
    method = request.method
    data_method[method] += 1
    data.write_to_file(data_method)

    return redirect('/')


@app.route('/statistics')
def statics():
    datas = data.read_file()
    return render_template("statistics.html", data1=datas)





if __name__ == "__main__":
    app.run(
        debug=True,
        port=5000
    )
