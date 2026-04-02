def translate_dna(dna):
  dna=dna.upper() #convert the sequence to uppercase
  codon_table={"TTT": "Phe", "TTC": "Phe","TTA": "Leu", "TTG": "Leu",
    "CTT": "Leu", "CTC": "Leu", "CTA": "Leu", "CTG": "Leu",
    "ATT": "Ile", "ATC": "Ile", "ATA": "Ile",
    "ATG": "Met","GTT": "Val", "GTC": "Val", "GTA": "Val", "GTG": "Val",
    "TCT": "Ser", "TCC": "Ser", "TCA": "Ser", "TCG": "Ser",
    "CCT": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro",
    "ACT": "Thr", "ACC": "Thr", "ACA": "Thr", "ACG": "Thr",
    "GCT": "Ala", "GCC": "Ala", "GCA": "Ala", "GCG": "Ala",
    "TAT": "Tyr", "TAC": "Tyr","TAA": "Stop", "TAG": "Stop", "TGA": "Stop",
    "CAT": "His", "CAC": "His",
    "CAA": "Gln", "CAG": "Gln",
    "AAT": "Asn", "AAC": "Asn",
    "AAA": "Lys", "AAG": "Lys",
    "GAT": "Asp", "GAC": "Asp",
    "GAA": "Glu", "GAG": "Glu",
    "TGT": "Cys", "TGC": "Cys",
    "TGG": "Trp",
    "CGT": "Arg", "CGC": "Arg", "CGA": "Arg", "CGG": "Arg",
    "AGT": "Ser", "AGC": "Ser",
    "AGA": "Arg", "AGG": "Arg",
    "GGT": "Gly", "GGC": "Gly", "GGA": "Gly", "GGG": "Gly"}
  print("=" * 40)
  print("   CODON TRANSLATION REPORT")
  print("=" * 40)
    
  for i in range(0, len(dna), 3):  # finding codon and its respective amino acid in loop fuction
        codon = dna[i:i+3]
        amino_acid = codon_table.get(codon)
        print(codon + " → " + str(amino_acid))
        if amino_acid == "Stop":  # print stopcodon found when "Stop" found in codon table
          print("Stop codon reached! 🛑")
          break

  print("=" * 40)
  print("End")
  print("=" * 40)

translate_dna("atgcttaagctagctaaatag")