'''
Two classes - Candidate and Election

Election
 - accepts a list of candidates
 - has a results method computing number of votes

Candidate
- argument is a name str

'''

class Candidate:

    def __init__(self, name):
        self.name = name
        self.votes = 0

    def __iadd__(self, count):
        if not isinstance(count, int):
            return NotImplemented
        
        self.votes += count
        return self # mirrors built-in method


class Election:

    def __init__(self, candidates):
        self.candidates = candidates

    def results(self):
        winner = ""
        max_count = 0
        total = 0


        for c in self.candidates:
            total += c.votes
            print(f"{c.name}: {c.votes} votes")
            if c.votes >= max_count:
                winner = c.name
                max_count = c.votes

        print(f"{winner} won: {max_count / total * 100}% of votes")



mike_jones = Candidate('Mike Jones')
susan_dore = Candidate('Susan Dore')
kim_waters = Candidate('Kim Waters')

candidates = {
    mike_jones,
    susan_dore,
    kim_waters,
}

votes = [
    mike_jones,
    susan_dore,
    mike_jones,
    susan_dore,
    susan_dore,
    kim_waters,
    susan_dore,
    mike_jones,
]

for candidate in votes:
    candidate += 1

election = Election(candidates)
election.results()

'''
Mike Jones: 3 votes
Susan Dore: 4 votes
Kim Waters: 1 votes

Susan Dore won: 50.0% of votes
'''