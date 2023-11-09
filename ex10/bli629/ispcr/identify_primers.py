import subprocess

def idfp(sorted_hits: list[str], max_amplicon_size: int) -> list[tuple[list[str]]]:
    """
    Identify valid PCR amplicons based on the BLAST hits.
    """
    valid_amplicons = []

    # Iterate over all pairs of hits
    for i in range(len(sorted_hits)):
        for j in range(i + 1, len(sorted_hits)):  # Start j from i + 1
            primer1 = sorted_hits[i]
            primer2 = sorted_hits[j]

            # Determine 5' and 3' ends for primer1
            primer1_start = int(primer1[8])
            primer1_end = int(primer1[9])
            primer1_5end = min(primer1_start, primer1_end)
            primer1_3end = max(primer1_start, primer1_end)

            # Determine 5' and 3' ends for primer2
            primer2_start = int(primer2[8])
            primer2_end = int(primer2[9])
            primer2_5end = min(primer2_start, primer2_end)
            primer2_3end = max(primer2_start, primer2_end)

            # Check if primers are pointing towards each other
            if primer1_3end < primer2_5end:
                amplicon_size = primer2_5end - primer1_3end
            elif primer2_3end < primer1_5end:
                amplicon_size = primer1_5end - primer2_3end
            else:
                continue

            # Check if amplicon size is valid
            if amplicon_size < max_amplicon_size:
                valid_amplicons.append((primer1, primer2))

    return valid_amplicons