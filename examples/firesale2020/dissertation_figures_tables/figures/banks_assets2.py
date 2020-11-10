import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rc
#rc('font',**{'family':'sans-serif','sans-serif':['Arial']})
plt.rcParams['text.usetex'] = True
plt.rcParams['text.latex.unicode'] = True
# Load the example iris dataset
#iris = sns.load_dataset("iris")
df = pd.read_excel('/Users/Tina/Dropbox/phd/projects/banking_spillovers_contagion/python_plotting/comp.xlsx')

   #one plot 

#print(Test.to_string())
#val = ["Loans and advances", "m1 Cash and gold reserves", 'Assets held for investment', "m23 Non financial assets"]
#test_v = Test[Test.variable.isin(val)]
sns.set(style="whitegrid", palette="muted")

f, ax = plt.subplots(figsize=(8, 8), ncols=1, nrows=2)
#plt.suptitle('SA banks asset values', fontsize=16)
ax[0].set_xticklabels(df.Name, rotation=90, fontsize=12)

sns.set_color_codes("muted")
ax[0].bar(df.Name, df.Loans, width=.9, color="b", align="center", label="Loan book")
sns.set_color_codes("pastel")
ax[0].bar(df.Name, df.Investments, width=.65, color="b", align="center", label="Trading book")
sns.set_color_codes("muted")
ax[0].bar(df.Name, df.Cash, width=.6, color="r", align="center", label="Cash")
sns.set_color_codes("pastel")
ax[0].bar(df.Name, df.Nonfi, width=.4, color="y", align="center", label="Non-Financial")
ax[0].xaxis.grid(False)
 #sns.despine(left=True)
ax[0].set_title('Absolute values in ZAR', fontsize=12)
ax[0].legend( loc="center", fontsize=12, frameon=True, ncol=2)

ax[0].tick_params(axis='x', labelsize=10)
ax[0].tick_params(axis='y', labelsize=12)
#print(Test.to_string())
#val = ["Loans and advances", "m1 Cash and gold reserves", 'Assets held for investment', "m23 Non financial assets"]
#test_v = Test[Test.variable.isin(val)]
sns.set_color_codes("muted")
#plt.suptitle('SA banks asset values', fontsize=16)

ax[1].bar(df.Name, df.loan_book, width=.9, color="b", align="center", label="Loan Book")
sns.set_color_codes("pastel")
ax[1].bar(df.Name, df.trading_book, width=.65, color="b", align="center", label="Trading Book")
sns.set_color_codes("muted")
ax[1].bar(df.Name, df.cash_w, width=.6, color="r", align="center", label="Cash")
sns.set_color_codes("pastel")
ax[1].bar(df.Name, df.nf_w, width=.4, color="y", align="center", label="Non-Financial")
ax[1].xaxis.grid(False)
#sns.despine(left=True)
# ax[1].legend(ncol=2, loc=1, frameon=True)
ax[1].set_title('Relative values in \% of banks\' total assets', fontsize=12)
ax[1].set_ylim(0,1.1)
ax[1].set_xticklabels(df.Name, rotation=90, fontsize=10)
ax[1].xaxis.grid(False)

ax[1].tick_params(axis='x', labelsize=10)
ax[1].tick_params(axis='y', labelsize=12)
#f.set_size_inches(18.5, 10.5)
 

plt.subplots_adjust(left=0.125, bottom=0.13, right=0.9, top=None,wspace=0.4, hspace=0.6)
#                
plt.show()