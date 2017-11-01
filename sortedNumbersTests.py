import unittest
import datetime
import Genetic


def get_fitness(genes):
    fitness = 1
    for i in range(1, len(genes)):
        if genes[i] > genes[i - 1]:
            fitness += 1
    return fitness


def display(candidate, startTime):
    timeDiff = datetime.datetime.now() - startTime
    print("{0}\t=> {1}\t{2}".format(', '.join(map(str, candidate.Genes)),
          candidate.Fitness,
          str(timeDiff)))



class SortedNumbersTests(unittest.TestCase):
    def test_sort_10_numbers(self):
        self.sort_numbers(10)

    def sort_numbers(self, totalNumbers):
        geneset = [i for i in range(100)]
        startTime = datetime.datetime.now()

        def fnDisplay(candidate):
            display(candidate, startTime)

        def fnGetFitness(genes):
            return get_fitness(genes)

        optimalFitness = totalNumbers
        best = Genetic.get_best(fnGetFitness, totalNumbers, optimalFitness, geneset, fnDisplay)
        self.assertTrue(not optimalFitness > best.Fitness)

class Fitness:
    NumbersInSequenceCount = None
    TotalGap = None

    def __int__(self, numbersInSequenceCount, totalGap):
        self.NumbersInSequenceCount = numbersInSequenceCount
        self.TotalGap = totalGap

    def __gt__(self, other):