print("Let's practice everything.")
print('You\'d need to know \'bout \'scapes with \\ that do:')
print('\n new lines and \t tabs and \a bells')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\twhere there is none.
"""

print("--------")
print(poem)
print("--------")

five = 5
print("This should be five: {}".format(five))

def secret_formula(started):
    jelly_beans = started*500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000

beans, jars, crates = secret_formula(start_point)

print("Started at {}".format(start_point))
print(f"End up with {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point/10

print("We can also do that this way:")
formula = secret_formula(start_point)

print("We'd have {} beans, {} jars, and {} crates.".format(*formula))

