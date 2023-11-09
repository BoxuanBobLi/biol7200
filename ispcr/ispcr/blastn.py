import subprocess

def run_blastn(primer_file: str, assembly_file: str) -> str:
    """
    Run BLASTN on the primer and assembly files, returning the result.
    """
    output_file = "blastn_output.txt"
    
    cmd = [
        "blastn",
        "-task", "blastn-short",
        "-query", primer_file,
        "-subject", assembly_file,
        "-outfmt", "6 std qlen",
        "-out", output_file
    ]
    
    subprocess.run(cmd, check=True)
    
    return output_file


def filter_blastn_results(blastn_output: str) -> list[list[str]]:
    """
    Filter the BLASTN results for full length hits with percent identity >= 80%.
    """
    filtered_results = []

    with open(blastn_output, 'r') as file:
        for line in file:
            # split the BLAST output
            fields = line.strip().split('\t')
            
            # Extract needed values (convert to int or float for comparison)
            percent_identity = float(fields[2])
            alignment_length = int(fields[3])
            query_length = int(fields[12])

            # Check for full length and percent identity conditions
            if alignment_length == query_length and percent_identity >= 80:
                filtered_results.append(fields)
    
    # Sort the results based on the start position of the hit (9th field)
    filter_results = sorted(filtered_results, key=lambda x: int(x[8]))
    
    return filter_results

