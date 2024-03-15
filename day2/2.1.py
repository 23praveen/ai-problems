class MapColoringCSP:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains
        self.constraints = constraints

    def is_consistent(self, variable, value, assignment):
        for neighbor in self.constraints[variable]:
            if neighbor in assignment and assignment[neighbor] == value:
                return False
        return True

    def backtrack_search(self, assignment):
        if len(assignment) == len(self.variables):
            return assignment

        unassigned_variables = [var for var in self.variables if var not in assignment]
        first_unassigned = unassigned_variables[0]

        for value in self.domains[first_unassigned]:
            if self.is_consistent(first_unassigned, value, assignment):
                assignment[first_unassigned] = value
                result = self.backtrack_search(assignment)
                if result:
                    return result
                del assignment[first_unassigned]

        return None

def main():
    variables = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
    domains = {
        'WA': ['red', 'green', 'blue'],
        'NT': ['red', 'green', 'blue'],
        'SA': ['red', 'green', 'blue'],
        'Q': ['red', 'green', 'blue'],
        'NSW': ['red', 'green', 'blue'],
        'V': ['red', 'green', 'blue'],
        'T': ['red', 'green', 'blue']
    }
    constraints = {
        'WA': ['NT', 'SA'],
        'NT': ['WA', 'SA', 'Q'],
        'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
        'Q': ['NT', 'SA', 'NSW'],
        'NSW': ['SA', 'Q', 'V'],
        'V': ['SA', 'NSW', 'T'],
        'T': ['V']
    }

    csp = MapColoringCSP(variables, domains, constraints)
    solution = csp.backtrack_search({})
    
    if solution:
        print("Solution found:")
        for var, color in solution.items():
            print(f"{var}: {color}")
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
