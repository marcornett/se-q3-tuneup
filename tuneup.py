#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment

Use the timeit and cProfile libraries to find bad code.
"""

__author__ = 'marcornett'

import cProfile
import pstats
import functools
import timeit


def profile(func):
    """A cProfile decorator function that can be used to
    measure performance.
    """
    # Be sure to review the lesson material on decorators.
    # You need to understand how they are constructed and used.

    # create inner function(*args, **kwargs)
    def wrapper(*args, **kwargs):
        # create cprofile object
        pr = cProfile.Profile()
        # enable cprofile
        pr.enable()
        # invoke func(*args, **kwargs)
        result = func(*args, **kwargs)
        # disable cprofile
        pr.disable()
        # sort stats by 'cumulative' time to see functions costing most time
        sort_by = pstats.SortKey.CUMULATIVE
        # use pstats, create stats object to collect statistics from cprofile
        ps = pstats.Stats(pr).sort_stats(sort_by)
        # print_stats() using stats object print function
        ps.print_stats()
        return result
    return wrapper


def read_movies(src):
    """Returns a list of movie titles."""
    print(f'Reading file: {src}')
    with open(src, 'r') as f:
        return f.read().splitlines()


# def is_duplicate(title, movies):
#     """Returns True if title is within movies list."""
#     for movie in movies:
#         if movie.lower() == title.lower():
#             return True
#     return False


@profile
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list."""
    movies = read_movies(src)
    duplicates = []
    while movies:
        movie = movies.pop()
        if movie in movies:
            # if is_duplicate(movie, movies):
            duplicates.append(movie)
    return duplicates


def timeit_helper(func):
    """Part A: Obtain some profiling measurements using timeit."""
    t = timeit.Timer(stmt=func, setup='pass')
    run_times = 10
    result = t.repeat(repeat=7, number=run_times)
    average = min(result) / run_times
    # average:.11f
    print(
        f'Best time across {7} repeats of {10} runs per repeat: {average:.11f} sec')


def main():
    """Computes a list of duplicate movie entries."""
    result = find_duplicate_movies('movies.txt')
    print(f'Found {len(result)} duplicate movies:')
    print('\n'.join(result))


if __name__ == '__main__':
    main()

# timeit_helper('main()')
