import pandas as pd
import matplotlib.pyplot as plot

def deleteRedundantPairs(correlations, df):
    """Get diagonal and lower triangular pairs of correlation matrix"""
    correlationsToDrop = set()
    cols = df.columns
    for i in range(0, df.shape[1]):
        for j in range(0, i + 1):
            correlationsToDrop.add((cols[i], cols[j]))
    return correlations.drop(labels=correlationsToDrop)

def getMostCorrelatedColumns(df):
    correlations = df.corr().abs().unstack()
    correlations = deleteRedundantPairs(correlations, df)
    correlations = correlations.sort_values(ascending=False)
    return correlations[0:1]

df = pd.read_csv('ecoli.data')
for col in df.columns:
    if df.dtypes.get(col) == "float64":
        print("Column " + col + ": median=" + str(df[col].median()) + ", min=" + str(df[col].min()) + ", max="
              + str(df[col].max()))
    else:
        print("Column " + col + ": mode=" + str(df[col].mode()[0]))

mostCorrelatedColumns = getMostCorrelatedColumns(df.select_dtypes(include="float64"))

firstCorrelatedColumnName = str(mostCorrelatedColumns).strip().split(" ")[0]
secondCorrelatedColumnName = str(mostCorrelatedColumns).strip().split(" ")[2]

print("Correlation matrix")
print("Top correlation: " + str(mostCorrelatedColumns))

ax = plot.subplot(1, 2, 1)
ax.hist(df[firstCorrelatedColumnName],edgecolor='black')
ax.set_title(firstCorrelatedColumnName)
ax.set_xlabel("value of " + firstCorrelatedColumnName)
ax.set_ylabel("occurrences of value")
ax.set_ylim(0, 100)

ax2 = plot.subplot(1, 2, 2)
ax2.hist(df[secondCorrelatedColumnName],edgecolor='black')
ax2.set_title(secondCorrelatedColumnName)
ax2.set_xlabel("value of " + secondCorrelatedColumnName)
ax2.set_ylabel("occurrences of value")
ax2.set_ylim(0, 100)

plot.tight_layout()
plot.show()