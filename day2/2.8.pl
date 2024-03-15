% Database of names and dates of birth (DOB)
dob(john, date(1990, 5, 15)).
dob(lisa, date(1985, 10, 25)).
dob(mary, date(1978, 3, 8)).
dob(peter, date(1995, 8, 12)).
dob(susan, date(2000, 12, 30)).

% Query to retrieve the date of birth (DOB) for a given name
dob_of(Name, DOB) :-
    dob(Name, DOB).

% Query to retrieve the names of individuals born in a specific year
born_in_year(Year, Name) :-
    dob(Name, date(Year, _, _)).

% Query to retrieve the names of individuals born in a specific month
born_in_month(Month, Name) :-
    dob(Name, date(_, Month, _)).

% Query to retrieve the names of individuals born on a specific day
born_on_day(Day, Name) :-
    dob(Name, date(_, _, Day)).
