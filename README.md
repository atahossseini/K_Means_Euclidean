# K-Means Clustering with Euclidean Distance

This Python project implements the K-Means clustering algorithm with the option to use Euclidean distance for calculating distances between data points and centroids.

## Usage

1. Ensure that the input data file is in the correct format (CSV) and located at the specified file path.

2. Run the kmeans.py script to perform K-Means clustering using Euclidean distance:
   

3. Follow the prompts to input the number of clusters and choose the distance method (Euclidean).

## Class: KMeans

The KMeans class provides the functionality for clustering data using the K-Means algorithm with Euclidean distance. It has methods for reading and cleaning the input data, calculating distances, performing K-Means clustering, and determining cluster centers.

### Methods

1. __init__(self, path_file, kind, k_in): Initializes the KMeans object with the file path, distance method, and number of clusters.

2. read_file(self): Reads the input data from the specified file.

3. clean_file(self): Cleans the input data by removing invalid entries.

4. distance(self, p1, p2): Calculates the Euclidean distance between two data points.

5. k_means(self, points, centers): Performs K-Means clustering on the input points using Euclidean distance.

6. center_appoint(self): Determines the cluster centers using the K-Means algorithm with Euclidean distance.

## Example


## File Format

The input data should be in a CSV file format where each row represents a data point and each column represents a feature.
