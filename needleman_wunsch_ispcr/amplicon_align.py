#!/usr/bin/env python3

import argparse
from magnumopus import ispcr, needleman_wunsch

def parse_arguments():
    parser = argparse.ArgumentParser(description='Perform in-silico PCR on two assemblies and align the amplicons')
    # Add 'dest' to each argument to give it a proper variable name
    parser.add_argument('-1', dest='assembly1', metavar='ASSEMBLY1', required=True, help='Path to the first assembly file')
    parser.add_argument('-2', dest='assembly2', metavar='ASSEMBLY2', required=True, help='Path to the second assembly file')
    parser.add_argument('-p', dest='primers', metavar='PRIMERS', required=True, help='Path to the primer file')
    parser.add_argument('-m', dest='max_amplicon_size', metavar='MAX_AMPLICON_SIZE', type=int, required=True, help='maximum amplicon size for ispcr')
    parser.add_argument('--match', type=int, required=True, help='match score to use in alignment')
    parser.add_argument('--mismatch', type=int, required=True, help='mismatch penalty to use in alignment')
    parser.add_argument('--gap', type=int, required=True, help='gap penalty to use in alignment')
    return parser.parse_args()

def remove_header(seq):
    lines = seq.split('\n')
    sequence = ''.join(lines[1:])
    return sequence

def reverse_complement(seq):
    complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G', 'N': 'N'}
    return ''.join(complement[base] for base in reversed(seq))

def amplicon_align():
    args = parse_arguments()
    
    # Perform ispcr on both assemblies using the proper variable names
    header_amplicon1 = ispcr(args.primers, args.assembly1, args.max_amplicon_size)
    header_amplicon2 = ispcr(args.primers, args.assembly2, args.max_amplicon_size)
    
    amplicon1 = remove_header(header_amplicon1)
    amplicon2 = remove_header(header_amplicon2)
    
    # Check if any amplicon was not found
    if not amplicon1 or not amplicon2:
        print("No amplicon produced from one or both of the assemblies with the given primers.")
        return

    # Align the two sequences in both orientations to find the best alignment
    aln1, score1 = needleman_wunsch(amplicon1, amplicon2, args.match, args.mismatch, args.gap)
    aln2, score2 = needleman_wunsch(amplicon1, reverse_complement(amplicon2), args.match, args.mismatch, args.gap)
    
    # Determine which orientation gives the best alignment score
    if score1 >= score2:
        aln = aln1
        score = score1
    else:
        aln = aln2
        score = score2

    # Print the best alignment and its score
    print("\n".join(aln))
    print(score)

amplicon_align()

