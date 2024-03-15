% State representation: state(X, Y, HasBanana)
% X and Y represent the monkey's position, HasBanana is 1 if the monkey has the banana, 0 otherwise.

% Define initial state
initial_state(state(1, 1, 0)).

% Define goal state
goal_state(state(4, 3, 1)).

% Define valid moves
move(state(X, Y, _), state(NewX, NewY, 0)) :-
    move_without_banana(X, Y, NewX, NewY).

move(state(X, Y, 1), state(NewX, NewY, 1)) :-
    move_with_banana(X, Y, NewX, NewY).

% Valid moves without banana
move_without_banana(X, Y, NewX, NewY) :-
    move_up(X, Y, NewX, NewY).
move_without_banana(X, Y, NewX, NewY) :-
    move_down(X, Y, NewX, NewY).
move_without_banana(X, Y, NewX, NewY) :-
    move_left(X, Y, NewX, NewY).
move_without_banana(X, Y, NewX, NewY) :-
    move_right(X, Y, NewX, NewY).

% Valid moves with banana
move_with_banana(X, Y, NewX, NewY) :-
    move_up(X, Y, NewX, NewY).
move_with_banana(X, Y, NewX, NewY) :-
    move_down(X, Y, NewX, NewY).
move_with_banana(X, Y, NewX, NewY) :-
    move_left(X, Y, NewX, NewY).
move_with_banana(X, Y, NewX, NewY) :-
    move_right(X, Y, NewX, NewY).

% Define individual movements
move_up(X, Y, X, NewY) :-
    NewY is Y + 1,
    NewY =< 3.
move_down(X, Y, X, NewY) :-
    NewY is Y - 1,
    NewY >= 1.
move_left(X, Y, NewX, Y) :-
    NewX is X - 1,
    NewX >= 1.
move_right(X, Y, NewX, Y) :-
    NewX is X + 1,
    NewX =< 4.

% Define a predicate to solve the problem
solve(State, _, []) :-
    goal_state(State).
solve(State, Visited, [Move | Moves]) :-
    move(State, NextState),
    \+ member(NextState, Visited), % To avoid loops
    solve(NextState, [NextState | Visited], Moves),
    move_description(State, NextState, Move).

% Define move descriptions for printing
move_description(state(X1, Y1, _), state(X2, Y2, _), Move) :-
    X2 > X1,
    Move = 'Move right.'.
move_description(state(X1, Y1, _), state(X2, Y2, _), Move) :-
    X2 < X1,
    Move = 'Move left.'.
move_description(state(X1, Y1, _), state(X2, Y2, _), Move) :-
    Y2 > Y1,
    Move = 'Move up.'.
move_description(state(X1, Y1, _), state(X2, Y2, _), Move) :-
    Y2 < Y1,
    Move = 'Move down.'.

% Predicate to find and print the solution
find_solution :-
    initial_state(InitialState),
    solve(InitialState, [InitialState], Moves),
    print_solution(Moves).

% Predicate to print the solution
print_solution([]).
print_solution([Move | Moves]) :-
    write(Move), nl,
    print_solution(Moves).
