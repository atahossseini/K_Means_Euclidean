import pprint
from random import randint
from math import sqrt

# Read the file

file_path = 'C:\\Users\\ata\\Downloads\\Telegram Desktop\\points.txt'


class KMeans:
    """
    KMeans class to represent k-means clustering algorithm and filter file
    input file path and kind of methode kmeans clustering and number of clusters
    output a dictionary with kmeans clustering results and number of clusters
    """

    def __init__(self, path_file, kind, k_in):
        self.path_file = path_file
        self.kind = kind
        self.k_in = k_in

    def read_file(self):
        point = list()
        with open(self.path_file, 'r') as f:
            while f.readline():
                point.append(f.readline().rstrip().split(','))
        return point

    def clean_file(self):
        point = self.read_file()
        point_list = list()

        for i in range(len(point)):
            try:
                z = [float(j) for j in point[i]]

            except ValueError as error:
                print("Wrong data found and deleted \n")
            else:
                if len(z) < 3:
                    continue
                point_list.append(z)
        return point_list

    def distance(self, p1, p2) -> float:
        if self.kind == 0:
            return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2)
        else:
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) + abs(p1[2] - p2[2])

    def k_means(self, points, centers):
        result = [
            {
                "center": center,
                "points": [],

            }
            for center in centers]

        for point in points:
            index, minimum = 0, self.distance(point, centers[0])

            i = 1

            while i < len(centers):
                d = self.distance(point, centers[i])
                if d < minimum:
                    index, minimum = i, d

                i += 1

            result[index]["points"].append(point)

        return result

    def center_appoint(self):
        centers = [(randint(-10, 10), randint(-10, 10), randint(-10, 10)) for _ in range(self.k_in)]
        while True:
            clusters = self.k_means(self.clean_file(), centers)
            new_centers = []
            for cluster in clusters:
                x, y, z = zip(*cluster["points"])
                new_centers.append(
                    (
                        sum(x) / len(x),
                        sum(y) / len(y),
                        sum(z) / len(z),
                    )
                )

            if new_centers == centers:
                break

            centers = new_centers

        return clusters


if __name__ == '__main__':
    k_input = input("please enter a number for numbers of list sorting = ")
    while True:
        try:
            k_input = int(k_input)
            break
        except ValueError as error:
            print("error, try again")
            k_input = input("please enter a number for numbers of list sorting = ")

    kind_input = input(
        "what method of distance would you like to use ? for menhattan enter m and for Euclidean enter e : \n")
    while kind_input.lower() not in ["e", "m"]:
        kind_input = input("wrong !! enter again --> M or E : \n")
    kind = 0 if kind_input.lower() == 'e' else 1

    final_list = KMeans(file_path, kind, k_input)

    pprint.pprint(final_list.center_appoint())
