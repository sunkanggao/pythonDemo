from sklearn import datasets
import pandas as pd
from pandas.tools.plotting import andrews_curves

ir = datasets.load_iris()
iris = pd.DataFrame(ir.data, columns=list(ir.feature_names))
iris['species'] = ir.target

color_map = dict(zip(iris.species.unique(), ['blue', 'green', 'red']))


andrews_curves(iris, 'species')