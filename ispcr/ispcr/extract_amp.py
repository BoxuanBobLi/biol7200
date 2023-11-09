import subprocess

def examp(hit_pairs: list[tuple[list[str]]], assembly_file: str) -> str:
    """
    Filter the BLASTN results for full length hits with percent identity >= 80%.
    """
    cmd = ["mktemp"]
    result = subprocess.run(cmd, capture_output=True, text=True)
 
    temp_bed_path = result.stdout.strip()  # Capture the path to the created temporary file

    try:
        # Write the BED content to the temporary file
        with open(temp_bed_path, 'w') as temp_bed:
            for pair in hit_pairs:
                forward_hit = pair[0]
                reverse_hit = pair[1]

                contig = forward_hit[1]  # Assuming column 2 of BLAST output is the subject id (contig)

                # Adjust positions for BED format and to exclude primer sequences
                start = int(forward_hit[9]) 
                end = int(reverse_hit[9]) -1
                
                temp_bed.write(f"{contig}\t{start}\t{end}\n")

        # Use subprocess to run seqtk with the temporary BED file
        cmd = ["seqtk", "subseq", assembly_file, temp_bed_path]
        result = subprocess.run(cmd, capture_output=True, text=True)

        return result.stdout

    finally:
        # Clean up by removing the temporary file using rm command via subprocess
        cmd = ["rm", temp_bed_path]
        subprocess.run(cmd)
