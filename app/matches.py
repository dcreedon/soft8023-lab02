import pattern.object_factory as object_factory
import app.gameimpl.x01_match as x01_match
import domain.darts_match as darts_match
from datatype.enums import DartMultiplier
from domain import visit

factory = object_factory.ObjectFactory()
factory.register_builder('X01', x01_match.X01MatchBuilder())

config = {'starting_total': 301}

x01 = factory.create('X01', **config)
match = darts_match.DartsMatch()


player1_index = match.register_player('Larkin')
player2_index = match.register_player('Nikral')

x01.set_match(match)

my_visit = visit.Visit([(DartMultiplier.SINGLE, 5), (DartMultiplier.SINGLE, 5), (DartMultiplier.SINGLE, 20)])
result, response = x01.process_visit(player1_index, my_visit)
print(response)

my_visit = visit.Visit([(DartMultiplier.SINGLE, 1), (DartMultiplier.SINGLE, 20), (DartMultiplier.SINGLE, 5)])
result, response = x01.process_visit(player2_index, my_visit)
print(response)

my_visit = visit.Visit([(DartMultiplier.TREBLE, 20), (DartMultiplier.TREBLE, 5), (DartMultiplier.TREBLE, 20)])
result, response = x01.process_visit(player1_index, my_visit)
print(response)

my_visit = visit.Visit([(DartMultiplier.SINGLE, 20), (DartMultiplier.SINGLE, 7), (DartMultiplier.SINGLE, 19)])
result, response = x01.process_visit(player2_index, my_visit)
print(response)

my_visit = visit.Visit([(DartMultiplier.TREBLE, 20), (DartMultiplier.SINGLE, 20), (DartMultiplier.SINGLE, 1)])
result, response = x01.process_visit(player1_index, my_visit)
print(response)

my_visit = visit.Visit([(DartMultiplier.TREBLE, 20), (DartMultiplier.TREBLE, 20), (DartMultiplier.TREBLE, 1)])
result, response = x01.process_visit(player2_index, my_visit)
print(response)

my_visit = visit.Visit([(DartMultiplier.SINGLE, 10), (DartMultiplier.SINGLE, 20), (DartMultiplier.MISS, 0)])
result, response = x01.process_visit(player1_index, my_visit)
print(response)

my_visit = visit.Visit([(DartMultiplier.SINGLE, 20), (DartMultiplier.SINGLE, 18), (DartMultiplier.SINGLE, 20)])
result, response = x01.process_visit(player2_index, my_visit)
print(response)

my_visit = visit.Visit([(DartMultiplier.SINGLE, 9), (DartMultiplier.DOUBLE, 8), (DartMultiplier.SINGLE, 0)])
result, response = x01.process_visit(player1_index, my_visit)
print(response)

# This should trigger an error message and the visit ignored
#my_visit = visit.Visit([(DartMultiplier.SINGLE, 10), (DartMultiplier.DOUBLE, 18), (DartMultiplier.SINGLE, 20)])
#result, response = x01.process_visit(player2_index, my_visit)
#print(response)
