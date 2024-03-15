% Facts representing relationships between students, teachers, and subjects
student(john).
student(lisa).
student(peter).

teacher(mary).
teacher(james).
teacher(susan).

subject(math).
subject(english).
subject(science).

% Relationship between students, teachers, and subjects
teaches(mary, math).
teaches(james, english).
teaches(susan, science).

% Queries to retrieve information about student, teacher, and subject relationships
% Query to find out who teaches a specific subject
teacher_of(Subject, Teacher) :-
    teaches(Teacher, Subject).

% Query to find out which subjects a specific teacher teaches
subjects_taught(Teacher, Subject) :-
    teaches(Teacher, Subject).

% Query to find out which subjects a specific student is enrolled in
enrolled_in(Student, Subject) :-
    student(Student),
    teaches(Teacher, Subject).
