% Facts representing properties of planets
planet(mercury, 0.39, 0.24).
planet(venus, 0.72, 0.62).
planet(earth, 1.0, 1.0).
planet(mars, 1.52, 1.88).
planet(jupiter, 5.2, 11.86).
planet(saturn, 9.58, 29.46).
planet(uranus, 19.22, 84.01).
planet(neptune, 30.05, 164.8).

% Query to find the distance of a planet from the sun
distance_from_sun(Planet, Distance) :-
    planet(Planet, Distance, _).

% Query to find the orbital period of a planet
orbital_period(Planet, Period) :-
    planet(Planet, _, Period).

% Query to find all planets with a specific orbital period
planets_with_orbital_period(Period, Planets) :-
    findall(Planet, (planet(Planet, _, Period)), Planets).

% Query to find the average orbital period of all planets
average_orbital_period(Average) :-
    findall(Period, planet(_, _, Period), Periods),
    length(Periods, NumPlanets),
    sum_list(Periods, Total),
    Average is Total / NumPlanets.
