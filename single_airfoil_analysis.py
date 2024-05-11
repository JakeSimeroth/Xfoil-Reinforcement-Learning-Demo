# single airfoil analysis
# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# plot airfoil from data


def plot_airfoil_from_data(x_upper, y_upper, x_lower, y_lower):
    x_coords = x_upper + x_lower
    y_coords = y_upper + y_lower

    plt.figure(figsize=(10, 5))
    plt.plot(x_coords, y_coords, 'b-o', label='Airfoil Shape')
    plt.title('Airfoil Shape')
    plt.xlabel('X-coordinate')
    plt.ylabel('Y-coordinate')
    plt.grid(True)
    plt.axis('equal')
    plt.legend()
    plt.show()

# extract the camber and max thickness of the airfoil


def extract_airfoil_features(x, y):
    max_thickness = max(y) - min(y)
    camber = max(y[:len(y)//2]) - min(y[len(y)//2:])
    return camber, max_thickness

# load and plot airfoil from data


def load_and_plot_airfoil(dat_file_path):
    # read the data from the file
    with open(dat_file_path, 'r') as file:
        lines = file.readlines()

    # extract the coordinates of the airfoil from .dat file and plot the airfoil
    coordinates = [line.strip() for line in lines if line.strip()
                   and not line.strip().startswith('#')]
    if not coordinates[0][0].isdigit():
        coordinates = coordinates[1:]

    x = [float(line.split()[0]) for line in coordinates]
    y = [float(line.split()[1]) for line in coordinates]

    half = len(x) // 2
    x_upper = x[:half]
    y_upper = y[:half]
    x_lower = x[half:][::-1]
    y_lower = y[half:][::-1]

    plot_airfoil_from_data(x_upper, y_upper, x_lower, y_lower)
    return extract_airfoil_features(x, y)


# usage here
dat_file_path = 'ag04.dat'
camber, max_thickness = load_and_plot_airfoil(dat_file_path)
