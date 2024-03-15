bird(canary).
bird(ostrich).
bird(sparrow).
bird(eagle).
bird(penguin).

can_fly(X) :-
    bird(X),
    \+ (X = ostrich; X = penguin).

/*output
 can_fly(eagle).
true.*/
