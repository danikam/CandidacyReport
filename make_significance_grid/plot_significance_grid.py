import pandas as pd
import seaborn as sns
import parse
import numpy as np
import matplotlib.pyplot as plt
import json
import ROOT

CLsexp=[]
mZ=[]
ms=[]
with open('SR_ONE_Output_hypotest__1_harvest_list_had_comparison.json') as json_file:
  data = json.load(json_file)
  for i in range(len(data)):
    CLsexp.append(ROOT.RooStats.PValueToSignificance(data[i]['CLsexp']))
    mZ.append(data[i]['mZ'])
    ms.append(data[i]['ms'])

CLsexp = np.asarray(CLsexp)
mZ = np.asarray(mZ)
ms = np.asarray(ms)

df = pd.DataFrame(data={'mzp': mZ, 'ms': ms, 'sig': CLsexp})

df = df.pivot('ms', 'mzp', 'sig')

f, ax = plt.subplots(figsize=(7, 5))
sns.heatmap(df, ax=ax, annot=True, fmt='.1f', cbar_kws={'label': 'expected significance'}, vmin=0.7, vmax=2.8)

# style plot
plt.xlabel("Mediator ($Z'$) mass [GeV]", position=(1., 0.), va='bottom', ha='right')
plt.ylabel('Dark Higgs ($s$) mass [GeV]', position=(0., 1.), va='top', ha='right')
ax.xaxis.set_label_coords(1., -0.10)
ax.yaxis.set_label_coords(-0.18, 1.)
#plt.title(f'{region} {category}')
plt.gca().invert_yaxis()
# drawATLASLabel(0.65, 0.15, ax, 'int', energy='13 TeV', lumi=36.1)
plt.tight_layout()
plt.savefig('Plots/Significance.png')
