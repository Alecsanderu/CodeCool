
from flask import Flask, render_template,url_for, request, redirect
import data_manager as dm
import connection as c


app = Flask(__name__)



from flask import Flask, render_template
from flask import request
from flask import redirect
import data_manager as dm
import connection as c

app = Flask(__name__)

def get_question_by_id(id):
    questions = dm.display_info('./sample_data/question.csv')
    for question in questions:
        if question['id'] == id:
            return question


@app.route('/')
@app.route('/list', methods=['GET', 'POST'])
def display_q():
    questions = dm.display_info('./sample_data/question.csv')
    entries = questions
    sort_by = 'submission_time'
    ascdsc = None
    if request.args.get('sort_by') == 'sorted_by' and request.args.get('asc_dsc') == 'asc' or request.args.get('sort_by') == 'sorted_by' and request.args.get('asc_dsc') == 'desc':
        entries = sorted(questions, key=lambda questions: questions[sort_by])
    elif request.args.get('sort_by') is not None and request.args.get('asc_dsc') is not None:
        ascdsc = request.args.get('asc_dsc')
        sort_by = request.args.get('sort_by')
        if ascdsc == 'asc':
            entries = sorted(questions, key=lambda questions: questions[sort_by], reverse=False)
        elif ascdsc == 'desc':
            entries = sorted(questions, key=lambda questions: questions[sort_by], reverse=True)

    return render_template('list.html', questions=entries, sort_by=sort_by, asc_dsc=request.args.get('asc_dsc'))



@app.route('/question/<question_id>')
def display_one_question(question_id):
    question = get_question_by_id(question_id)
    answer = dm.display_anw('./sample_data/answer.csv')
    return render_template('questions.html', question=question, answers=answer)

@app.route('/add-question')
def add_question():
    # question = c.write_to_questions("./sample_data/question.csv", )

    return render_template('add_question.html')

    return render_template('add-question.html')

@app.route('/add-question-to-csv', methods=['GET'])
def add_question_to_csv():
    question = c.write_to_questions("./sample_data/question.csv", request.args.get('title'), request.args.get('text'))
    print(request.args.get('title'))
    return redirect("/list")


@app.route('/add-question-to-csv', methods=['GET', 'POST'])
def add_question_to_csv():
    question = c.write_to_questions("./sample_data/question.csv", request.form.get('title'), request.form.get('text'))
    return redirect("/list")

@app.route('/question/<question_id>/edit', methods=['GET','POST'])
def edit_question(question_id):
    question = get_question_by_id(question_id)
    if request.method == 'POST':
        question = c.write_to_questions("./sample_data/question.csv", request.form.get('title'),
                                        request.form.get('text'))
    return render_template('edit_question.html', question=question)


@app.route('/question/<question_id>/new_answer/', methods=['GET', 'POST'])
def new_answer(question_id):
    if request.method == 'POST':
        c.write_to_answers("./sample_data/answer.csv", request.form.get('text'), question_id)
        return redirect('/question/' + question_id )
    question = get_question_by_id(question_id)
    return render_template('add_answer.html', question=question)


@app.route('/edit-question-to-csv/<question_id>', methods=['GET', 'POST'])
def edit_question_to_csv(question_id):
    c.edit_specif_question("./sample_data/question.csv", request.form.get('title'), request.form.get('message'), question_id)
    return redirect('/question/' + question_id)

@app.route('/question/<question_id>/delete')
def delete_from_csv(question_id):
    c.delete_q(question_id, './sample_data/question.csv')
    return redirect('/list')

@app.route('/answer/<answer_id>/delete')
def delete_from_csv2(answer_id,):
    c.delete_anw(answer_id, './sample_data/answer.csv')
    question = get_question_by_id(answer_id)
    answer = dm.display_anw('./sample_data/answer.csv')
    return render_template('questions.html', question=question, answers=answer)


if __name__ == "__main__":
    app.run (
        threaded=True,
        host = '0.0.0.0',
        debug = True,
        port = 5000
    )
