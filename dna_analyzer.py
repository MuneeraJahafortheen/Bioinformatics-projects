def analyze_dna(sequence):
    # Normalize input
    sequence = sequence.upper()
    
    # Basic information
    print("=" * 40)
    print("   DNA SEQUENCE ANALYSIS REPORT")
    print("=" * 40)
    print("Sequence: " + sequence)
    print("Length:   " + str(len(sequence)) + " bases")
    print("\n--- Base Composition ---")
    print("A: " + str(sequence.count("A")))
    print("T: " + str(sequence.count("T")))
    print("G: " + str(sequence.count("G")))
    print("C: " + str(sequence.count("C")))
    gc = (sequence.count("G") + sequence.count("C")) / len(sequence) * 100
    print("\n--- GC Content ---")
    print("GC Content: " + str(round(gc, 2)) + "%")
    rna = sequence.replace("T", "U")
    print("\n--- Transcription ---")
    print("DNA: " + sequence)
    print("RNA: " + rna)
    # Start codon check
    print("\n--- Codon Analysis ---")
    if "ATG" in sequence:
        print("Start codon ATG: ✅ Found at position " + str(sequence.find("ATG")))
    else:
        print("Start codon ATG: ❌ Not found")
     # Codon extraction
    print("\nCodons:")
    for i in range(0, len(sequence), 3):
        codon = sequence[i:i+3]
        print("  " + codon)
    
    print("=" * 40)
    
analyze_dna("ATGGGGTAG")