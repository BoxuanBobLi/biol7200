# Assign input and output files
query_seqs="$1"
genome_assembly="$2"
bed_file="$3"
outfile="$4"

# Temporary files for tblastn results and gene names
tmp_file="tblastn_tmp_results.txt"
genes_tmp="genes_tmp.txt"

# Run tblastn
tblastn \
    -query "$query_seqs" \
    -subject "$genome_assembly" \
    -outfmt '6 std qlen' \
    -task tblastn-fast \
| awk '$3>30 && $4>0.9*$13' > "$tmp_file"

# Loop through the BED file and tblastn results to find which genes contain the domains
while read -r qseqid sseqid pident length mismatch gapopen qstart qend sstart send evalue bitscore qlen; do
    while read -r chrom start end name rest; do
        # Check boundaries
        if [[ "$sstart" -ge "$start" && "$send" -le "$end" ]]; then
            echo "$name" >> "$genes_tmp"
        fi
    done < "$bed_file"
done < "$tmp_file"

# Write the unique gene names to the output file
sort "$genes_tmp" | uniq > "$outfile"

# Cleanup and display number of matches
rm "$tmp_file" "$genes_tmp"
echo "$(wc -l "$outfile") gene matches found in $genome_assembly"
