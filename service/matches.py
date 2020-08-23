import pattern.object_factory as object_factory
import domain.x01_match as x01_match
import domain.darts_match as darts_match


factory = object_factory.ObjectFactory()
factory.register_builder('X01', x01_match.X01MatchBuilder())

x01 = factory.create('X01')
match = darts_match.DartsMatch('Alice', 'Kalifa')
x01.set_match(match)

response = x01.process_visit('Alice', ('S20', 'T20', 'S5'))
print(response)

response = x01.process_visit('Kalifa', ('S1', 'S5', 'S20'))
print(response)

response = x01.process_visit('Alice', ('S20', 'T20', 'T20'))
print(response)

response = x01.process_visit('Kalifa', ('S20', 'S1', 'S0'))
print(response)

response = x01.process_visit('Kalifa', ('S20', 'S1', 'S0'))
print(response)