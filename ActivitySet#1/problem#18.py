def _is_integer(x):
    """Determine whether some object ``x`` is an
    integer type (int, long, etc). This is part of the 
    ``fixes`` module, since Python 3 removes the long
    datatype, we have to check the version major.

    Parameters
    ----------

    x : object
        The item to assess whether is an integer.


    Returns
    -------

    bool
        True if ``x`` is an integer type
    """
    return (not isinstance(x, (bool, np.bool))) and \
        isinstance(x, (numbers.Integral, int, np.int, np.long, long))  # no long type in python 3 