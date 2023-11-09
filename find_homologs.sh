# Assign arguments to variables
QUERY_FILE=$1
SUBJECT_FILE=$2
OUTPUT_FILE=$3

# Perform the TBLASTN search
tblastn -query $QUERY_FILE -subject $SUBJECT_FILE -outfmt "6 qseqid sseqid pident length qlen" -out results.blast

# Filter the results and save to the output file
awk '($3 > 30) && ($4/$5 > 0.9) {print $0}' results.blast > $OUTPUT_FILE

# Print the number of matches identified
MATCH_COUNT=$(wc -l < $OUTPUT_FILE)
echo "Number of matches identified: $MATCH_COUNT"

# Clean up temporary files
rm results.blast