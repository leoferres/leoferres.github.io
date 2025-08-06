import os
import pyreadr
import pandas as pd

# git clone from https://github.com/reconverse/outbreaks.git
# it assumes only one object (dataset) per RData file
# There are a few files that have no objects (datasets) in them, we skip hthose

# Run it from the outbreaks/data directory or modify the indir/outdir vars below
indir = '.'
outdir = '.'
os.makedirs(outdir, exist_ok=True)

for file in os.listdir(indir):
    if file.endswith('.RData'):
        full_path = os.path.join(indir, file)
        result = pyreadr.read_r(full_path)
        if not result:
            continue
        obj = next(iter(result.values()))
        if not isinstance(obj, pd.DataFrame) or obj.empty:
            continue
        outname = os.path.splitext(file)[0] + '.csv'
        obj.to_csv(os.path.join(outdir, outname), index=False)
