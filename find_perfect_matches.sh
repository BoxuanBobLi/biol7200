# Bash script
# Make sure the blast is activated
# Input file paths
query_file="$1"
subject_file="$2"
output_file="$3"

# Perform BLAST search and output results in tabular format
blastn -query "$query_file" -subject "$subject_file" -outfmt "6 qseqid sseqid qlen slen length pident" -out temp_blast_results.txt

# Filter and write perfect matches to the output file
awk '$6 == 100 && $3 == $5 {print}' temp_blast_results.txt > "$output_file"

# Count the number of perfect matches
perfect_match_count=$(wc -l < "$output_file")

# Clean up temporary files
rm temp_blast_results.txt

# Print the number of perfect matches to stdout
echo "Number of perfect matches: $perfect_match_count"
