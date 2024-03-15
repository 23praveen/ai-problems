% Define facts and rules

% Known facts
has_symptom(john, fever).
has_symptom(john, cough).
has_symptom(jane, rash).

% Define rules
has_disease(X, flu) :-
    has_symptom(X, fever),
    has_symptom(X, cough).
has_disease(X, measles) :-
    has_symptom(X, fever),
    has_symptom(X, rash).

% Define backward chaining predicate
backward_chaining(Patient, Disease) :-
    has_disease(Patient, Disease),
    format('~w has ~w.~n', [Patient, Disease]).
backward_chaining(Patient, Disease) :-
    % Check if patient has symptom of Disease
    has_symptom(Patient, Symptom),
    % Check if symptom is associated with Disease
    (Disease = flu, (Symptom = fever ; Symptom = cough)) ;
    (Disease = measles, (Symptom = fever ; Symptom = rash)),
    format('~w has ~w.~n', [Patient, Disease]).

% Example queries:
% backward_chaining(john, flu).
% backward_chaining(jane, measles).
