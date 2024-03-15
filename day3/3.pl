% Facts: Define the relationships in the family tree
male(john).
male(bob).
male(mike).
male(tom).

female(susan).
female(lisa).
female(emily).

parent(john, bob).
parent(john, lisa).
parent(susan, bob).
parent(susan, lisa).

parent(bob, mike).
parent(bob, tom).
parent(lisa, emily).

% Rules: Define additional relationships based on facts
father(X, Y) :-
    male(X),
    parent(X, Y).

mother(X, Y) :-
    female(X),
    parent(X, Y).

sibling(X, Y) :-
    parent(Z, X),
    parent(Z, Y),
    X \= Y.

grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).

ancestor(X, Y) :-
    parent(X, Y).
ancestor(X, Y) :-
    parent(X, Z),
    ancestor(Z, Y).

/*output
father(john, bob).
true */
