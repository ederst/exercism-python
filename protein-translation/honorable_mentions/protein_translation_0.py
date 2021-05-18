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
    "UAA": "Stop",
    "UAG": "Stop",
    "UGA": "Stop"
}

def translate(codon):
    return codon_mapping.get(codon)

def chunkify(strand, chunk_size=3):
    return [strand[i : i + chunk_size] for i in range(0, len(strand), chunk_size)]

def proteins(strand):
    translated_strand = list(map(translate, chunkify(strand)))

    try:
        first_stop = translated_strand.index("Stop")
    except ValueError:
        first_stop = None

    return translated_strand[:first_stop]

