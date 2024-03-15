% Facts about fruits and their colors
fruit_color(apple, red).
fruit_color(banana, yellow).
fruit_color(grape, purple).
fruit_color(orange, orange).

% Rules to query for fruits based on color
fruit_of_color(Color, Fruit) :-
    fruit_color(Fruit, Color).

% Rules to query for colors based on fruit
color_of_fruit(Fruit, Color) :-
    fruit_color(Fruit, Color).

/*color_of_fruit(banana, Color).
Color = yellow.*/
