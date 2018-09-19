import numpy as np
from csv import DictReader
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def extract_cols(lst, keys):
    new_lst = []
    for i, d in enumerate(lst):
        row = []
        for key in keys:
            row.append(d[key])
        new_lst.append(row)

    return np.array(new_lst)

def visualize_perceptron(feature_names, X, y, w, b, fig=None):
    d = len(feature_names)
    if d not in (2, 3):
        print("Visualize 2d can only take 2 or 3 features at once!")
        return

    is_sf = np.where(y == 1)
    is_nyc = np.where(y == 0)

    X_sf = np.take(X, is_sf, axis=0).reshape(-1, d)
    X_nyc = np.take(X, is_nyc, axis=0).reshape(-1, d)

    if fig is None:
        fig = plt.figure()

    # visualize 2d
    if d == 2:
        ax = fig.gca()

        h_min, h_max = X[:,0].min(), X[:,0].max()
        slope = -w[0]/w[1]
        y_int = -b/w[1]
        ax.plot([h_min, h_max], [y_int, y_int + slope*(h_max - h_min)], '-', label='decision boundary')
        v_min, v_max = X[:,1].min(), X[:,1].max()

        ax.scatter(X_sf[:,0], X_sf[:,1], label='sf', c='red')
        ax.scatter(X_nyc[:,0], X_nyc[:,1], label='nyc')
        ax.set_xlabel(feature_names[0])
        ax.set_ylabel(feature_names[1])
        ax.legend()
        ax.set_xlim(h_min, h_max)
        ax.set_ylim(v_min, v_max)
        ax.set_title("Visualization of Housing SF vs NYC Classification")
        fig.show()

    # visualize 3d
    elif d == 3:
        ax = fig.add_subplot(111, projection='3d')

        ax.scatter(X_sf[:,0], X_sf[:,1], X_sf[:,2], c='r', label='sf')
        ax.scatter(X_nyc[:,0], X_nyc[:,1], X_nyc[:,2], c='b', label='nyc')

        xx_min, xx_max = X[:,0].min(), X[:,0].max()
        xx_range = abs(xx_max - xx_min)
        yy_min, yy_max = X[:,1].min(), X[:,1].max()
        yy_range = abs(yy_max - yy_min)

        xx, yy = np.meshgrid(np.linspace(xx_min, xx_max, 3), np.linspace(yy_min, yy_max, 3))
        z = (-w[0] * xx -w[1] * yy - b) / w[2]

        ax.plot_surface(xx, yy, z, label='decision boundary', alpha=0.2)
        ax.set_xlabel(feature_names[0])
        ax.set_ylabel(feature_names[1])
        ax.set_zlabel(feature_names[2])
        ax.set_xlim(xx_min - 0.1*xx_range, xx_max + 0.1*xx_range)
        ax.set_ylim(yy_min - 0.1*yy_range, yy_max + 0.1*yy_range)
        ax.set_zlim(X[:,2].min(), X[:,2].max())
        ax.set_title("Visualization of Housing SF vs NYC Classification")
        fig.show()            

def visualize_linear_regression(feature_names, X, y, w, b):
    d = len(feature_names)

    if d not in (1, 2):
        print("Can only visualize 1 or 2 features at a time.")
        return

    if d == 1:
        x_min, x_max = X.min(), X.max()

        fig = plt.figure()
        ax = fig.gca()
        ax.scatter(X.reshape(-1,1), y)
        plt.plot([x_min, x_max], [b, b + w*(x_max - x_min)], '-', label='prediction')
        plt.xlabel(feature_names[0])
        plt.ylabel("Price")
        plt.legend()
        plt.title("Visualization of Housing Price Regression")
        fig.show()

    elif d == 2:

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        ax.scatter(X[:,0], X[:,1], y)

        xx_min, xx_max = X[:,0].min(), X[:,0].max()
        yy_min, yy_max = X[:,1].min(), X[:,1].max()

        xx, yy = np.meshgrid(np.linspace(xx_min, xx_max, 2), np.linspace(yy_min, yy_max, 2))
        z = w[0] * xx + w[1] * yy + b

        ax.plot_surface(xx, yy, z, alpha=0.2)
        ax.set_xlabel(feature_names[0])
        ax.set_ylabel(feature_names[1])
        ax.set_zlabel("Price")
        plt.title("Visualization of Housing Price Regression")
        fig.show()

def load_data():
    # loading housing data
    all_data = []
    with open('housing.csv', 'r') as f:
        reader = DictReader(f)
        for row in reader:
            all_data.append({
                    'year_built': int(row['year_built']),
                    'price_per_sqft': int(row['price_per_sqft']),
                    'bath': float(row['bath']),
                    'beds': float(row['beds']),
                    'elevation': int(row['elevation']),
                    'price': int(row['price']),
                    'in_sf': int(row['in_sf'])
                })
    # shuffling data
    np.random.shuffle(all_data)

    # separating features from labels for classification exercises
    features_c = []
    labels_c = []
    for data in all_data:
        data = data.copy()
        labels_c.append(data.pop('in_sf', None))
        features_c.append(data)

    # separating features from labels for regression exercises
    features_r = []
    labels_r = []
    for data in all_data:
        data = data.copy()
        labels_r.append(data.pop('price', None))
        features_r.append(data)

    return all_data, features_c, labels_c, features_r, labels_r
