# bash script
# input and output file names
input_file="$1"
output_file="$2"

# extract the filename 
filename=$(basename $input_file .fna)

# modify headers
sed "s/^>/>$filename /" "$input_file" > "$output_file"

echo "Headers modified and saved to '$output_file'."

