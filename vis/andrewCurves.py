from sklearn import datasets
import pandas as pd
from pandas.tools.plotting import andrews_curves
import matplotlib.pyplot as plt


ir = datasets.load_iris()
iris = pd.DataFrame(ir.data, columns=list(ir.feature_names))
iris['species'] = ir.target

fig = plt.figure()
ax = fig.add_subplot(111)
ax = andrews_curves(iris, 'species', colormap='winter')
plt.show()