CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT
);

CREATE TABLE quizzes (
    id INTEGER PRIMARY KEY,
    subject TEXT,
    number_questions INTEGER,
    quiz_date TEXT
);

CREATE TABLE results (
    id INTEGER PRIMARY KEY,
    student_id INTEGER,
    quiz_id INTEGER,
    score INTEGER
);

INSERT INTO students (first_name, last_name)
VALUES ('John', 'Smith');

INSERT INTO quizzes (subject, number_questions, quiz_date)
VALUES ('Python Basics', 5, '2015-02-05');

INSERT INTO results (student_id, quiz_id, score)
VALUES (1,1,85);