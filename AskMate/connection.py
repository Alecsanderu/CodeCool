import csv
import time



def read_file(filename):
    all_data = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        reader = sorted(reader, key=lambda col: col['submission_time'], reverse=True)
        for row in reader:
            all_data.append(row)
    return all_data

def write_to_questions(filename,title,text):
    new_id = 0
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            new_id += 1

    with open(filename, 'a', newline='') as csvfile:
        fieldnames = ['id','submission_time','view_number','vote_number','title','message','image']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'id': new_id,
                         'submission_time': time.time(),
                         'view_number': 0,
                         'title': title,
                         'message': text,
                         'image': '/img/1.jpg'
                         })

def get_dict(filename):
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
    return reader




def write_to_questions(filename,title,text):
    new_id = 0
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            new_id += 1

    with open(filename, 'a', newline='') as csvfile:
        fieldnames = ['id','submission_time','view_number','vote_number','title','message','image']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'id': new_id,
                         'submission_time': time.time(),
                         'view_number': 0,
                         'vote_number':0,
                         'title': title,
                         'message': text,
                         'image': '/img/1.jpg'
                         })

def write_to_answers(filename,text,question_id):
    new_id = 0
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            new_id += 1

    with open(filename, 'a', newline='') as csvfile:
        fieldnames = ['id','submission_time','vote_number','question_id','message','image']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({'id': new_id,
                         'submission_time': time.time(),
                         'vote_number': 0,
                         'question_id': question_id,
                         'message': text,
                         'image': '/img/1.jpg'
                         })


def read_anwsers(filename):
    all_data = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        reader = sorted(reader, key=lambda col: col['submission_time'], reverse=True)
        for row in reader:
            all_data.append(row)
    return all_data



def edit_specif_question(filename, title, message,question_id):
    all_questions = read_file(filename)
    for dictionary in all_questions:
        if question_id == dictionary['id']:
            dictionary['title'] = title
            dictionary['message'] = message
            dictionary['submission_time'] = time.time()

            break

    with open(filename, 'w') as csvfile:
        fieldnames = ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for dictionary in all_questions:
            writer.writerow({'id': dictionary['id'],
                             'submission_time': dictionary['submission_time'],
                             'view_number': dictionary['view_number'],
                             'vote_number':dictionary['vote_number'],
                             'title': dictionary['title'],
                             'message': dictionary['message'],
                             'image': dictionary['image']})

def delete_q(question_id, filename):
    all_questions = read_file(filename)
    remaning_q = []
    for dictionary in all_questions:
        if int(question_id) != int(dictionary['id']):
            remaning_q.append(dictionary)
    with open(filename, 'w') as csvfile:
        fieldnames = ['id', 'submission_time', 'view_number', 'vote_number', 'title', 'message', 'image']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for dictionary in remaning_q:
            writer.writerow({'id': dictionary['id'],
                             'submission_time': dictionary['submission_time'],
                             'view_number': dictionary['view_number'],
                             'vote_number':dictionary['vote_number'],
                             'title': dictionary['title'],
                             'message': dictionary['message'],
                             'image': dictionary['image']})


def delete_anw(question_id, filename):
    all_questions = read_file(filename)
    remaning_ans = []
    for dictionary in all_questions:
        if question_id != dictionary['id']:
            remaning_ans.append(dictionary)

    with open(filename, 'w') as csvfile:
        fieldnames = ['id', 'submission_time', 'vote_number', 'question_id', 'message', 'image']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for dictionary in remaning_ans:
            writer.writerow({'id': dictionary['id'],
                             'submission_time': dictionary['submission_time'],
                             'vote_number': dictionary['vote_number'],
                             'question_id':dictionary['question_id'],
                             'message': dictionary['message'],
                             'image': dictionary['image']})

