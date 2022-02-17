# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/13_export.ipynb (unless otherwise specified).

__all__ = ['mq_ouput_files', 'mod_translation', 'remove_mods', 'ap_to_mq_sequence', 'prepare_ap_results']

# Cell

mq_ouput_files = ['allPeptides.txt', 'evidence.txt', 'matchedFeatures.txt', 'modificationSpecificPeptides.txt', 'ms3Scans.txt', 'msms.txt', 'msmsScans.txt', 'mzRange.txt', 'Oxidation (M)Sites.txt', 'parameters.txt', 'peptides.txt', 'proteinGroups.txt', 'summary.txt', 'tables.pdf']

# Cell

# TODO: Acetyl (Protein N-term cannot be easily converted as we don't know the protein end.)
mod_translation = {}
mod_translation['oxM'] = 'Oxidation (M)'
mod_translation['cC'] = None
mod_translation['aM'] = None

# Cell

from .fasta import parse

def remove_mods(sequence):
    return ''.join([_ for _ in sequence if _.isupper()])

def ap_to_mq_sequence(sequence, mod_translation):
    """
    Converts AlphaPept sequence format to MaxQuant Format
    returns naked_sequence, len_sequence, modifications_, mq_sequence

    """
    # Add leading and trailing modification
    naked_sequence = remove_mods(sequence)
    parsed_sequence = parse(sequence)

    mq_sequence = '_'

    modifications = {}

    for idx, AA in enumerate(parsed_sequence):

        mq_sequence += naked_sequence[idx]
        if len(AA) != 1:
            if mod_translation[AA] is not None:
                if mod_translation[AA] in modifications:
                    modifications[mod_translation[AA]] += 1
                else:
                    modifications[mod_translation[AA]] = 1

                mq_sequence += f"({mod_translation[AA]})"

    if len(modifications) == 0:
        modifications_ = 'Unmodified'
    else:
        modifications_ = ''

        for mod in modifications.keys():
            count = modifications[mod]
            if count == 1:
                count_ = ''
            else:
                count_ = str(count)+' '

            if modifications_ == '':
                sep = ''
            else:
                sep = ', '

            modifications_ += sep + count_ + mod

    mq_sequence += '_'

    n_AA = len(naked_sequence)

    return naked_sequence, n_AA, modifications_, mq_sequence


# Cell
import os
import numpy as np

def prepare_ap_results(ref_ap):

    if 'type' not in ref_ap.columns:

        ref_ap['type'] = 'None'

    remove_path = ref_ap['filename'].apply(lambda x: os.path.splitext(os.path.split(x)[1])[0])

    ref_ap['mq_rawfile'] = remove_path.apply(lambda x: x[:-8] if x.endswith('.ms_data') else x)


    ref_ap['reverse'] = np.nan
    ref_ap.loc[ref_ap['decoy'],'reverse'] = '+'

    # Undefined yet:

    ref_ap['undefined'] = np.nan

    ref_ap['contaminant'] = np.nan
    ref_ap.loc[ref_ap['protein_group'].str.contains('CON__'),'contaminant'] = '+'

    ref_ap['id'] = ref_ap.index

    naked_sequence, nAA, mq_modifications, mq_sequence = zip(*ref_ap['sequence'].apply(lambda x: ap_to_mq_sequence(x, mod_translation)))

    ref_ap['naked_sequence'] = naked_sequence
    ref_ap['n_AA'] = nAA
    ref_ap['mq_modifications'] = mq_modifications
    ref_ap['mq_sequence'] = mq_sequence

    return ref_ap