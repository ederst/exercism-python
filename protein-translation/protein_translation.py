from itertools import takewhile
from textwrap import wrap

wrap_width = 3

codon_mapping = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine",
    "UUC": "Phenylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGG": "Tryptophan",
}

stoppers = ["UAA", "UAG", "UGA"]

def translate(codon):
    return codon_mapping.get(codon)

def is_no_stopper(codon):
    return codon not in stoppers

def proteins(strand):
    return list(map(translate, takewhile(is_no_stopper, wrap(strand, wrap_width))))
