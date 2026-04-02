def analyze_dna(sequence):
    # Normalize input
    sequence = sequence.upper()
   
    # Basic information
    print("=" * 40)
    print("   DNA SEQUENCE ANALYSIS REPORT")
    print("=" * 40)
    print("Length:   " + str(len(sequence)) + " bases")
    print("\n--- Base Composition ---")
    print("A: " + str(sequence.count("A")))
    print("T: " + str(sequence.count("T")))
    print("G: " + str(sequence.count("G")))
    print("C: " + str(sequence.count("C")))
    gc = (sequence.count("G") + sequence.count("C")) / len(sequence) * 100
    print("\n--- GC Content ---")
    print("GC Content: " + str(round(gc, 2)) + "%")
    # Start codon check
    print("\n--- Codon Analysis ---")
    if "ATG" in sequence:
        print("Start codon ATG: ✅ Found at position " + str(sequence.find("ATG")))
    else:
        print("Start codon ATG: ❌ Not found")
    print("=" * 40)

header = ""
sequence = ""
with open("P53.fasta","r") as f:
    for line in f:
        line=line.strip()
        if line.startswith(">"):
            header = line
        else:
            sequence = sequence + line

    print("Name:"+header)
    print("---")
    analyze_dna(sequence)
        