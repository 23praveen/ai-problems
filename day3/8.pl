% Define symptoms
symptom(fever).
symptom(cough).
symptom(rash).
symptom(headache).

% Define diseases and their symptoms
disease(flu, [fever, cough, headache]).
disease(measles, [fever, rash]).

% Define a predicate to check if a patient has a particular disease
has_disease(Patient, Disease) :-
    disease(Disease, Symptoms),
    has_symptoms(Patient, Symptoms).

% Define a predicate to check if a patient has a list of symptoms
has_symptoms(_, []).
has_symptoms(Patient, [Symptom|Symptoms]) :-
    has_symptom(Patient, Symptom),
    has_symptoms(Patient, Symptoms).

% Define a predicate to check if a patient has a particular symptom
has_symptom(Patient, Symptom) :-
    % Code to determine if the patient has the symptom
    % This could involve asking the patient or running tests
    % For simplicity, we'll just ask the user here
    format('Does ~w have ~w? (yes/no): ', [Patient, Symptom]),
    read(Response),
    Response = yes.

% Example query:
% HasDisease(john, flu).
