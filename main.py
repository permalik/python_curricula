# main.py
"""
python_curricula
"""

import argparse

from algorithm.sort.insertion_sort import insertion_sort_v1
from fundamental.calc.fibonacci import fibonacci_v1


def main():
    # Initialize Parser and Subparser
    parser = argparse.ArgumentParser(description="python_curricula CLI")
    subparsers = parser.add_subparsers(
        dest="category", required=True, help="Select a Category"
    )

    # Category Selection
    # Fundamental
    fun_parser = subparsers.add_parser("fun", help="Fundamental Programs")
    fun_subparsers = fun_parser.add_subparsers(dest="program", required=True)

    # Construct
    con_parser = subparsers.add_parser("con", help="Construct Programs")
    con_subparsers = con_parser.add_subparsers(dest="construct", required=True)

    # Datastructure
    ds_parser = subparsers.add_parser("ds", help="Datastructure Programs")
    ds_subparsers = ds_parser.add_subparsers(dest="ds", required=True)

    # Algorithm
    alg_parser = subparsers.add_parser("alg", help="Algorithm Programs")
    alg_subparsers = alg_parser.add_subparsers(dest="alg", required=True)

    # Fundamental: Calc: Fibonacci V1
    fib_v1_parser = fun_subparsers.add_parser(
        "fibonacci_v1", help="Compute Fibonacci Sequence"
    )
    fib_v1_parser.add_argument(
        "-n", "--iterations", type=int, default=10, help="Number of iterations"
    )
    fib_v1_parser.set_defaults(func=fibonacci_v1)

    # Algorithm: Sort: Insertion Sort V1
    insort_v1_parser = alg_subparsers.add_parser(
        "insertion_sort_v1", help="Sort Integer List"
    )
    insort_v1_parser.add_argument(
        "-n", "--length", type=int, default=10, help="Length of list"
    )
    insort_v1_parser.set_defaults(func=insertion_sort_v1)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
