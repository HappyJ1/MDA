def codon_task(codons):
    # Count the number of times 'AUG' appears
    aug_count = codons.count('AUG')
    
    # Find the index of the first occurrence of 'UGA'
    try:
       uga_first = codons.index('UGA')
    except:
       uga_first = "UGA NOT Found"

    # Replace all 'GCU' with 'GCA'
    new_codons = tuple('GCA' if codon == 'GCU' else codon for codon in codons)
    
    return aug_count, uga_first, new_codons

# Example input
codons = ('AUG', 'UUU', 'GUU', 'UAA', 'AUG', 'GUU')

# Call the function
result = codon_task(codons)

# Print the results
print("Count of 'AUG':", result[0])
print("Index of first 'UGA':", result[1])
print("New tuple with 'GCU' replaced by 'GCA':", result[2])