def to_rna(dna_strand):
    transcription = str.maketrans("GCTA", "CGAU")
    return dna_strand.translate(transcription)
