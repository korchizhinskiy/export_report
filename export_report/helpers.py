from collections.abc import Sequence


def get_longest_sequence(collection: Sequence):
    """Return maximum len of collection.
    - Find max of current collection and nested collection by recursive method.

    :param collection: Collection of objects or nested collection of objects and same recursive principle.

    >>> get_longest_sequence([[1, 1], [2], [3, [4, 4, 4]], [5]])
    4
    """
    return max(
        [len(collection)]
        + [
            get_longest_sequence(nested_collection)
            for nested_collection in collection
            if isinstance(nested_collection, Sequence)
        ]
    )
