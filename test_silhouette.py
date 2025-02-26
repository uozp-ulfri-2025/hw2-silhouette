import unittest

from silhouette import silhouette, silhouette_average


dataS4 = {"X": [1, 1],
          "Y": [0.9, 1],
          "Z": [1, 0],
          "Z1": [0.8, 0],
          "A": [0.5, 0.5],
          "A1": [0.6, 0.7],
          "A2": [0.4, 0.3],
          "A3": [0.8, 0.7],
          "B": [0.2, 0.1],
          "B2": [0.4, 0.5],
          }


dataS2 = {"X": [1, 1],
          "Y": [0.9, 1],
          "Z": [1, 0],
          "Z1": [0.8, 0]}


class SilhouetteTest(unittest.TestCase):

    def test_silhouette_basic(self):
        data = {"X":[1, 1],
                "Y": [0.9, 1],
                "Z": [1, 0]}

        s1 = silhouette("X", [["X", "Y"], ["Z"]], data)
        self.assertTrue(0.5 < s1 < 1)

    def test_silhouette_average_basic(self):
        data = {"X": [1, 1],
                "Y": [0.9, 1],
                "Z": [1, 0]}

        s1 = silhouette_average(data, [["X", "Y"], ["Z"]])  # boljše skupine
        s2 = silhouette_average(data, [["X", "Z"], ["Y"]])  # slabše skupine
        s3 = silhouette_average(data, [["Y", "Z"], ["X"]])  # še slabše skupine
        self.assertLess(s2, s1)
        self.assertLess(s3, s2)

    def test_silhouette1(self):
        data = dataS2
        self.assertAlmostEqual(silhouette("X", [["X"], ["Z", "Z1"]], data), 0.0)  # 0 by definition
        self.assertAlmostEqual(silhouette("Z", [["X"], ["Z", "Z1"]], data), 0.8, places=5)

    def test_silhouette2_mean(self):
        data = dataS2
        s1 = silhouette_average(data, [["X", "Y"], ["Z", "Z1"]])  # boljše skupine
        s2 = silhouette_average(data, [["X", "Z"], ["Y", "Z1"]])  # slabše skupine
        s3 = silhouette_average(data, [["Y", "Z"], ["X", "Z1"]])  # še slabše skupine
        self.assertAlmostEqual(s1, 0.851105768704104, places=5)
        self.assertAlmostEqual(s2, -0.42024432102251297, places=5)
        self.assertAlmostEqual(s3, -0.43077817395149687, places=5)

    def test_silhouette2(self):
        data = dataS2
        self.assertAlmostEqual(silhouette("X", [["X", "Y"], ["Z", "Z1"]], data), 0.9009804864072152, places=5)
        self.assertAlmostEqual(silhouette("Y", [["X", "Y"], ["Z", "Z1"]], data), 0.9004962809790011, places=5)
        self.assertAlmostEqual(silhouette("Z", [["X", "Y"], ["Z", "Z1"]], data), 0.800497515516439, places=5)
        self.assertAlmostEqual(silhouette("Z1", [["X", "Y"], ["Z", "Z1"]], data), 0.8024487919137608, places=5)

        self.assertAlmostEqual(silhouette("X", [["X", "Z"], ["Y", "Z1"]], data), -0.44009804864072155, places=5)
        self.assertAlmostEqual(silhouette("Y", [["X", "Z"], ["Y", "Z1"]], data), -0.4502481404895006, places=5)
        self.assertAlmostEqual(silhouette("Z", [["X", "Z"], ["Y", "Z1"]], data), -0.39750621894395555, places=5)
        self.assertAlmostEqual(silhouette("Z1", [["X", "Z"], ["Y", "Z1"]], data), -0.39312487601587404, places=5)

    def test_silhouette4(self):
        data = dataS4
        cl1 = [["X", "Y"], ["Z", "Z1"], ["A", "A1", "A2", "A3"], ["B", "B2"]]
        cl2 = [["Z", "Z1"], ["A", "A1", "A2", "A3"], ["X", "Y"], ["B", "B2"]]
        self.assertAlmostEqual(silhouette("X", cl1, data), 0.8393326749789924, places=5)
        self.assertAlmostEqual(silhouette("Y", cl1, data), 0.8215111850702933, places=5)
        self.assertAlmostEqual(silhouette("A", cl1, data), 0.10247919661515911, places=5)
        self.assertAlmostEqual(silhouette("B2", cl1, data), -0.42418101867909697, places=5)
        self.assertAlmostEqual(silhouette("X", cl2, data), 0.8393326749789924, places=5)
        self.assertAlmostEqual(silhouette("Y", cl2, data), 0.8215111850702933, places=5)
        self.assertAlmostEqual(silhouette("A", cl2, data), 0.10247919661515911, places=5)
        self.assertAlmostEqual(silhouette("B2", cl2, data), -0.42418101867909697, places=5)

