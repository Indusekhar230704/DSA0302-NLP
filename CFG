import nltk
from nltk.parse.generate import generate
from nltk import CFG

grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N
Det -> 'the' | 'a'
N -> 'cat' | 'dog' | 'house'
VP -> V NP
V -> 'chased' | 'saw'
""")

parser = nltk.ChartParser(grammar)
sentence = "the cat chased a dog"
tokens = sentence.split()

for tree in parser.parse(tokens):
    tree.pretty_print()

parse_trees = list(parser.parse(tokens))
