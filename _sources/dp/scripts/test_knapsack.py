from cmath import e
from dataclasses import dataclass
import os

from typing import Callable, List, Union

from _sources.db.scripts.knapsack_memoized import knapsack as knapsack_memoized
from _sources.db.scripts.knapsack_tabular import knapsack as knapsack_tabular

from functools import wraps
from time import time

# taken from https://stackoverflow.com/questions/1622943/timeit-versus-timing-decorator
def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        try:
            result = f(*args, **kw)
        except Exception as e:
            result = str(e).split(':')[0]
        te = time()
        print(result, ',', '":math:`%2.4f\,\\textrm{ms}`"' % ((te-ts) * 1000))
        return result
    return wrap


@dataclass
class KPInstance:
    weights: List[int]
    profits: List[float]
    capacity: int
    size: int
    optimal_selection: List[int] = None
    optimal_value: int = None

    def to_donnerc(self):
        return self.profits, self.weights, self.capacity


def load_kp_instance_likr(
    instance_name: str, path: str = "kp_instances/likr"
) -> KPInstance:
    filename = os.path.join(path, instance_name + ".kp")
    with open(filename, mode="r") as f:
        N = int(f.readline().strip())
        capacity = int(f.readline().strip())
        f.readline()

        weights = [None] * N
        profits = [None] * N

        for i, line in enumerate(f):
            profits[i], weights[i] = [int(x) for x in line.split(" ")]
    instance = KPInstance(weights, profits, capacity, N)
    return instance


def load_kp_instance_johnyortega(
    instance_name: str, size: str, path: str = "kp_instances"
) -> KPInstance:
    filename = os.path.join(path, "johnyortega", size, instance_name)
    with open(filename, mode="r") as f:
        N, capacity = [int(x) for x in f.readline().split(" ")]

        weights = [None] * N
        profits = [None] * N

        for i, line in enumerate(f):
            try:
                profits[i], weights[i] = [int(x) for x in line.split(" ")]
            except Exception as e:
                #print(f"Unable to load line {line}. Skipping ...")
                pass

    instance = KPInstance(weights, profits, capacity, N)
    return instance


def test_knapsack(algo: Callable) -> None:
    johnyortega_instances = {
        "low-dimensional": [
            "f1_l-d_kp_10_269",
            "f2_l-d_kp_20_878",
            "f3_l-d_kp_4_20",
            "f4_l-d_kp_4_11",
            #"f5_l-d_kp_15_375",
            "f6_l-d_kp_10_60",
            "f7_l-d_kp_7_50",
            "f8_l-d_kp_23_10000",
            "f9_l-d_kp_5_80",
            "f10_l-d_kp_20_879",
        ],
        "large_scale": [
            "knapPI_1_100_1000_1",
            "knapPI_1_200_1000_1",
            "knapPI_1_500_1000_1",
            "knapPI_1_1000_1000_1",
            "knapPI_1_2000_1000_1",
            "knapPI_1_5000_1000_1",
            "knapPI_1_10000_1000_1",
        ],

    }

    for size, instances in johnyortega_instances.items():
        for instance_name in instances:
            try:
                instance = load_kp_instance_johnyortega(instance_name, size)
                # print(instance)
                print(f'``{instance_name}``, "{instance.size}", "{instance.capacity}"', end=", ")
                opt_value = algo(*instance.to_donnerc())
                # print(f"Valeur optimale pour instance {instance_name}: {opt_value}")
            except Exception as e:
                print(f"Error loading instance {instance_name}. Error: {str(e)}")
                raise e
                # print("???")


print("Memoized ...")
test_knapsack(timing(knapsack_memoized))
print("Tabular ...")
test_knapsack(timing(knapsack_tabular))
