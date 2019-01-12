#!/usr/bin/env python
from pathlib import Path
from collections import defaultdict
import json

import numpy as np
import pandas as pd

def get_parser():
    """Build parser object"""
    from argparse import ArgumentParser
    from argparse import RawTextHelpFormatter
    
    parser = ArgumentParser(description='MRIQC-WebAPI: massaging bson dumps',
                            formatter_class=RawTextHelpFormatter)
    parser.add_argument('input_file', action='store', type=Path, help='input')
    parser.add_argument('output_file', action='store', type=Path, help='output')
    return parser

def main():
    args = get_parser().parse_args()

    dictlist = []
    with args.input_file.open() as f:
        for entry in f.readlines():
            entry = entry.strip().replace('+Infinity', '"+Infinity"')
            entry = entry.replace('-Infinity', '"-Infinity"')
            try:
                dictlist += [json.loads(entry.strip())]
            except:
                print("Error reading: ", entry.strip())

    def emptylist():
        """Create an array of NaNs of the same size as currently
        stored entries"""
        return [np.nan] * max(0, len(data.get('md5sum', [])) - 1)

    data = defaultdict(emptylist, {})
    for entry in dictlist:
        md5sum = entry['provenance']['md5sum']
        if not md5sum:
            continue
    
        data['md5sum'] += [md5sum]
        keys = []
        for key, val in entry.items():
            if isinstance(val, dict):
                for subkey, subval in val.items():
                    if subkey == 'md5sum':
                        continue
                    keys.append('_'.join((key, subkey)))
                    data['_'.join((key, subkey))] += [subval]
            else:
                data[key] += [val]
                keys.append(key)

        # Fill with nans existing keys without value in the current record
        missing = list(set(list(data.keys())) - set(keys + ['md5sum']))
        for k in missing:
            data[k] += [np.nan]

    df = pd.DataFrame(data)
    origcols = df.columns.ravel().tolist()
    iqms = list(set(origcols) - set(['md5sum'] + [k for k in origcols if k.startswith('bids') or k.startswith('provenance') or k.startswith('_')]))
    cols = ['md5sum', '_created_$date'] + iqms + list(sorted(
        [k for k in origcols if k.startswith('provenance') or k.startswith('bids')]))
    df = df[cols]
    df.columns = ['created' if k == '_created_$date' else k for k in cols]
    df = df.drop_duplicates(subset=['md5sum'])
    df.to_csv(str(args.output_file), index=None)
    return 0

if __name__ == '__main__':
    main()

