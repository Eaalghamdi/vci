# black --line-length 150 .
# flake8 --max-line-length=150 .
from utilitiespackage.standard import *

from collections import Iterable as __Iterable, Mapping as __Mapping, Sequence as __Sequence

# we import * this namespace, so might as well
# grab partial, aget, mcall, and iget while we're at it
# ignore pyflakes, we mean to import this to rexport
from functools import reduce  # NOQA
from functools import partial  # NOQA
from operator import attrgetter as aget, itemgetter as iget, methodcaller as mcall  # NOQA  # NOQA  # NOQA


def gensym():
    "Generates a unique symbol that is a valid python identifier"
    from uuid import uuid4

    return str(uuid4()).replace("-", "_")


def isa(value, target):
    "True if value is a target via ==, issubclass, or isinstance"
    # equality
    if value == target:
        return True

    # instance vs type
    if issubclass(type(value), type):
        if issubclass(type(target), type):
            return issubclass(value, target)
        else:
            return False
    else:
        if issubclass(type(target), type):
            return isinstance(value, target)
        return False


class MultiFn(object):
    def __init__(self, dispatch):
        self.dispatch = dispatch
        self.dispatch_alist = []
        self.dispatch_prefers = []
        self.default_func = None

    def __call__(self, *args, **kwargs):
        value = self.dispatch(*args, **kwargs)
        return self.invoke(value, args, kwargs)

    def invoke(self, value, args, kwargs):
        "Invoke the appropriate function from dispatch_alist for value"

        # handle registered preferences
        def do_maybe_preferred(target, func):
            preferred = self.prefers_over(target)
            if preferred is not None:
                return self.invoke(preferred, args, kwargs)
            else:
                return func(*args, **kwargs)

        # equality
        for target, func in self.dispatch_alist:
            if value == target:
                return do_maybe_preferred(target, func)

        # inheritance
        for target, func in self.dispatch_alist:
            if isa(value, target):
                return do_maybe_preferred(target, func)

        # default to default_func or throwing if default_func isn't setup
        if self.default_func is not None:
            return self.default_func(*args, **kwargs)
        else:
            raise Exception("No default value provided!")

    def register_method(self, target, f):
        "Helper to register a new method for a given dispatch target"
        # make sure we unregister any other methods of the same target
        self.unregister_method(target)
        # register the new method in the assoc list
        self.dispatch_alist.append((target, f))

    def method(self, target):
        "Decorator to register a new method for a dispatch target"

        def decorator(f):
            self.register_method(target, f)
            return f

        return decorator

    def register_default(self, f):
        "Helper to registers the default function"
        self.default_func = f

    def default(self, f):
        "Decorator to register the default method"
        self.register_default(f)
        return f

    def unregister_method(self, target):
        "Unregisters a dispatch target"
        # remove target from dispatch_alist
        self.dispatch_alist = [x for x in self.dispatch_alist if x[0] != target]
        # remove target from dispatch_prefers
        self.dispatch_prefers = [x for x in self.dispatch_prefers if target not in x]

    def unregister_default(self):
        "Unregisters the default method"
        self.default_method = None

    def prefers_over(self, target):
        "Returns a class that is preferred over target or None"
        for c1, c2 in self.dispatch_prefers:
            if target == c2:
                return c1

    def prefer(self, class1, class2):
        "Prefers class1 over class2"
        if class1 == class2:
            raise ValueError("class1 cannot == class2")
        # search for class1 and class2 in dispatch_alist
        p1 = False
        p2 = False
        for t, _ in self.dispatch_alist:
            if t == class1:
                p1 = True
            elif t == class2:
                p2 = True
            if p1 and p2:
                break
        if not p1:
            raise ValueError("class1 is not registered!")
        if not p2:
            raise ValueError("class2 is not registered!")
        # register the preference
        self.dispatch_prefers.append((class1, class2))

    def stop_prefer(self, class1, class2):
        p = (class1, class2)
        self.dispatch_prefers = [x for x in self.dispatch_prefers if x != p]


def interleave(*args):
    """ Takes any number of iterables and interleaves them in a generator. """
    iterators = [iter(x) for x in args]
    while iterators:
        for i, x in enumerate(iterators):
            try:
                yield x.next()
            except StopIteration:
                try:
                    iterators.pop(i)
                except IndexError:
                    break


def merge_with(f, *dicts):
    """ Merges dicts using f(old, new) when encountering collision. """
    r = {}
    sentinel = object()
    for d in filter(None, dicts):
        for k, v in d.iteritems():
            tmp = r.get(k, sentinel)
            if tmp is sentinel:
                r[k] = v
            else:
                r[k] = f(tmp, v)
    return r


def deep_merge_with(f, *dicts):
    """ Merges dicts recursively, resolving node conflicts using f """

    def _deep_merge_with(*ds):
        if all([isinstance(d, __Mapping) for d in ds]):
            return merge_with(_deep_merge_with, *ds)
        else:
            return f(*ds)

    return _deep_merge_with(*dicts)


def throw(exception, *args, **kwargs):
    """ Raises an exception (as an expression) """
    raise exception(*args, **kwargs)


def get_in(obj, lookup, default=None):
    """ Walk obj via __getitem__ for each lookup,
    returning the final value of the lookup or default.
    """
    tmp = obj
    for l in lookup:
        try:
            tmp = tmp[l]
        except (KeyError, IndexError, TypeError):
            return default
    return tmp


def get(obj, k, default=None):
    """ Return obj[k] with a default if __getitem__ fails.

    If default is callable, return a call to it passing in obj and k.
    """
    try:
        return obj[k]
    except (KeyError, AttributeError, TypeError, IndexError):
        if callable(default):
            return default(obj, k)
        return default


def is_even(x):
    """ True if obj is even. """
    return (x % 2) == 0


def assoc(obj, *args):
    """Return obj with k1=v1... via __setitem__.

    Expects *args as k1, v1, k2, v2 ...

    Special-cases None to return {k: v} ala Clojure.
    """
    # requires even count of *args
    if not is_even(len(args)):
        raise ValueError("*args count must be even")

    # special case None to work like empty dict
    if obj is None:
        obj = {}

    # iterate args as key value pairs
    for k, v in zip(args[::2], args[1::2]):
        obj[k] = v

    return obj


def assoc_deep(obj, *args):
    """Return a deep copy of obj with k1=v1... via __setitem__.

    Expects *args as k1, v1, k2, v2 ...

    Special-cases None to return {k: v} ala Clojure.
    """
    from copy import deepcopy

    # requires even count of *args
    if not is_even(len(args)):
        raise ValueError("*args count must be even")

    # special case None to work like empty dict
    if obj is None:
        obj = {}
    else:
        obj = deepcopy(obj)

    # iterate args as key value pairs
    for k, v in zip(args[::2], args[1::2]):
        obj[k] = v

    return obj


def assoc_kw(obj, **kwargs):
    """ __setitem__ all kwargs on the new object, return it. """
    # special case None to work like empty dict
    if obj is None:
        obj = {}

    for k, v in kwargs.items():
        obj[k] = v

    return obj


def assoc_deep_kw(obj, **kwargs):
    """ Deep Copy obj and __setitem__ all kwargs on the new object, return it. """
    from copy import deepcopy

    # special case None to work like empty dict
    if obj is None:
        obj = {}
    else:
        obj = deepcopy(obj)

    for k, v in kwargs.items():
        obj[k] = v

    return obj


def assoc_in(obj, keys, v):
    """ Return a copy of obj with v updated at keys.

    Dictionaries are created when keys don't exist.
    """
    k, ks = keys[0], keys[1:]
    if ks:
        return assoc(obj, k, assoc_in(get(obj, k), ks, v))
    return assoc(obj, k, v)


def assoc_deep_in(obj, keys, v):
    """ Return a copy of obj with v updated at keys.

    Dictionaries are created when keys don't exist.
    """
    k, ks = keys[0], keys[1:]
    if ks:
        return assoc_deep(obj, k, assoc_deep_in(get(obj, k), ks, v))
    return assoc_deep(obj, k, v)


def update_in(obj, keys, fn, *args, **kwargs):
    """ Return obj with v updated by
        fn(current_value, *args, **kwargs) at keys.

    Dictionaries are created when keys don't exist.
    """
    k, ks = keys[0], keys[1:]
    if ks:
        return assoc(obj, k, update_in(get(obj, k), ks, fn, *args, **kwargs))
    return assoc(obj, k, fn(get(obj, k), *args, **kwargs))


def update_deep_in(obj, keys, fn, *args, **kwargs):
    """ Return a copy of obj with v updated by
        fn(current_value, *args, **kwargs) at keys.

    Dictionaries are created when keys don't exist.
    """
    k, ks = keys[0], keys[1:]
    if ks:
        return assoc_deep(obj, k, update_deep_in(get(obj, k), ks, fn, *args, **kwargs))
    return assoc_deep(obj, k, fn(get(obj, k), *args, **kwargs))


def is_iterable(obj):
    """ True if obj is iterable """
    return isinstance(obj, __Iterable)


def dissoc(obj, *ks):
    """ Return obj without k """
    for k in ks:
        try:
            del obj[k]
        except (KeyError, IndexError):
            pass
    return obj


def dissoc_deep(obj, *ks):
    """ Return a copy of obj without k """
    from copy import deepcopy

    obj = deepcopy(obj)
    for k in ks:
        try:
            del obj[k]
        except (KeyError, IndexError):
            pass
    return obj


def dissoc_in(obj, keys):
    """ Return obj without k at keys. """
    k, ks = keys[0], keys[1:]
    if ks:
        nextmap = get(obj, k)
        if nextmap is not None:
            newmap = dissoc_in(nextmap, ks)
            if is_iterable(obj):
                return assoc(obj, k, newmap)
            return dissoc(obj, k)
        return obj
    return dissoc(obj, k)


def dissoc_deep_in(obj, keys):
    """ Return a copy of obj without k at keys. """
    k, ks = keys[0], keys[1:]
    if ks:
        nextmap = get(obj, k)
        if nextmap is not None:
            newmap = dissoc_in(nextmap, ks)
            if is_iterable(obj):
                return assoc(obj, k, newmap)
            return dissoc(obj, k)
        return obj
    return dissoc(obj, k)


def select_keys(keys, d, default=None):
    """ Given a list of keys and a collection that supports __getitem__, return
        a dictionary with only those keys.
    """
    r = {}
    for k in keys:
        r[k] = get(d, k, default)
    return r


def select_vals(keys, d, default=None):
    """ Given a list of keys and a collection that supports __getitem__, return
       a list with those keys. """
    return [get(d, k, default) for k in keys]


select_keys_flat = select_vals


def identity(x):
    """ Identity functions x -> x """
    return x


def compose(*fns):
    "compose(foo, bar, baz)(x) = foo(bar(baz(x)))"
    return reduce(lambda f, g: lambda *xs, **ys: f(g(*xs, **ys)), fns)


def pipeline(*fns):
    """
    five = partial(operator.add, 5)
    ten = partial(operator.add, 10)
    one = partial(operator.add, 1)

    pipeline(five,
             ten,
             one)(0)
    = one(ten(five(0))) => 16
    """
    return reduce(lambda f, g: lambda *xs, **ys: g(f(*xs, **ys)), fns)


def thread(*args):
    """ Threads args[0] through the fns args[-1:1].

    an example:
    >>> thread(10, lambda x: x+1, lambda x: x * 2)
    => (lambda x: x*2)((lambda x: x+1)(10))
    """
    return reduce(lambda f, g: g(f), args)


def trap_exception(e, f, default=None):
    """ Call f(), trapping e, default to default (which might be callable) """
    try:
        return f()
    except e:
        if callable(default):
            return default(e)
        else:
            return default


def prepend(v, l):
    """ Given a value, prepend it to an iterable or a list

    Returns a concrete list if given a list and a generator otherwise.

    Ignores None as l
    """
    if isinstance(v, list):
        tmp = [v]
        tmp.extend(l)
        return tmp
    else:

        def generator():
            yield v
            try:
                for x in l:
                    yield x
            except TypeError:
                pass

        return generator()


cons = prepend


def append(l, *vs):
    """ Given an iterable or a list, append values to it.

    Returns a concrete list if given a list, otherwise a generator.

    Ignores None as l
    """
    if isinstance(l, list):
        l.extend(vs)
        return l
    else:

        def generator():
            try:
                for x in l:
                    yield x
            except TypeError:
                pass
            for v in vs:
                yield v

        return generator()


conj = append


def concat(*items):
    """ Expands iterable items (via iteration, this means keys for dicts!)

    Returns a generator
    """
    for item in items:
        if is_iterable(item) and not is_str_or_bytes(item):
            for x in item:
                yield x
        else:
            yield item


flatten1 = compose(list, concat)
flatten1.__doc__ = "Expands iterable items (via iteration, this means keys for dicts) into a concrete list"


def if_let(expression, if_callable, else_callable=None):
    """ (if-let [tmp expression] (if-callable tmp) (else-callable tmp))

    if_callable/else_callable can also be just a value. if it's not callable(),
    then we just return the value.
    """
    if expression:
        if callable(if_callable):
            return if_callable(expression)
        else:
            return if_callable
    elif callable(else_callable):
        return else_callable(expression)
    else:
        return else_callable


def rpartial(func, *args):
    """ partial that returns a fn that concats the args to the funcs with args

        e.g.: rpartial(get, 0) => lambda x: get(x, 0)
    """
    return lambda *xtra: func(*flatten1(xtra, args))


first = rpartial(get, 0)
second = rpartial(get, 1)
third = rpartial(get, 2)
fourth = rpartial(get, 3)
fifth = rpartial(get, 4)
sixth = rpartial(get, 5)
seventh = rpartial(get, 6)
eighth = rpartial(get, 7)
ninth = rpartial(get, 8)
tenth = rpartial(get, 9)

last = rpartial(get, -1)


def is_str_or_bytes(x):
    """ True if x is str or bytes.
    This doesn't use rpartial to avoid infinite recursion.
    """
    return isinstance(x, (basestring, bytes, bytearray))


def flatten(xs):
    """ Recursively flatten the argument """
    for x in xs:
        if is_iterable(x) and not is_str_or_bytes(x):
            for y in flatten(x):
                yield y
        else:
            yield x


def group_by_and_transform(grouper, transformer, iterable):
    """ Sort & Group iterable by grouper, apply transformer to each group.

        Grouper must be a function that takes an item in the iterable and
        returns a sort key.

        Returns a dictionary of group keys matched to lists.
        """
    from itertools import groupby

    return {key: map(transformer, group) for key, group in groupby(sorted(iterable, key=grouper), key=grouper)}


def group_by(f, i):
    """ Groups i by f, returning a dictionary keyed by f. """
    return group_by_and_transform(f, identity, i)


dedup = compose(list, set)
dedup.__doc__ = """ Remove duplicates in an iterable """


def is_map(x):
    """ True if x is a Mapping (dict-like) """
    return isinstance(x, __Mapping)


def is_seq(x):
    """ True if x is a Sequence (ordered iterable, list-like) """
    return isinstance(x, __Sequence)


def transform_tree(f, t):
    """ Walks a tree (dict of dicts), depth-first, calling f(k, v) to transform

    The function should take two arguments, the key and value,
    and return a 2-tuple with the new key and new value. A sample
    identity is below:

        def f(k, v):
            return (k, v)

    """
    if not is_map(t):
        return t
    d = {}
    for k, v in t.iteritems():
        nk, nv = f(k, transform_tree(f, v))
        d[nk] = nv
    return d


class Reduced(BaseException):
    """ Used to escape from better_reduce-based iteration, returning
    the passed val immediately.

    Inherits from BaseException so normal Exception catches won't accidentally
    catch this.
    """

    def __init__(self, val):
        self.val = val

    def __str__(self):
        return "<Reduced: {}>".format(val)


def reduced(v):
    """ Aborts execution of a better_reduce or better_map and returns then
    passed value immediately. """
    raise Reduced(v)


def better_reduce(f, *xs):
    """ A multi-arity reduce, with initial value being first supporting reduced.

    Supports reduced(val) in the reducer function to return val immediately
    without further processing.

    If no initial value is given `better_reduce(f, coll)`, then
    the collection must contain at least 2 values, which will be
    passed into f to form the initial value.

    If more than one collection is passed, an initial value must
    be given. Each collection is combined lazily, using izip_longest
    with a fill value of None. This means that your reducing function
    should expect an iterable as the second argument. This iterable
    might contain None as values if the collections are not of equal
    length.
    """
    from itertools import izip_longest

    l = len(xs)

    if l == 0:
        raise Exception("No iterable passed!")

    elif l == 1:

        coll = iter(xs[0])
        try:
            x = next(coll)
            y = next(coll)
        except StopIteration:
            raise Exception("No initial value passed and not at least 2 vals in coll")

        try:
            init = f(x, y)
        except (Reduced, r):
            return r.val

        try:
            return reduce(f, coll, init)
        except (Reduced, r):
            return r.val

    elif l == 2:
        init = xs[0]
        coll = xs[1]

        try:
            return reduce(f, coll, init)
        except (Reduced, r):
            return r.val

    else:
        init = xs[0]
        colls = izip_longest(*xs[1:])

        try:
            return reduce(f, colls, init)
        except (Reduced, r):
            return r.val


def better_map(f, *colls):
    "Higher arity version of map implemented via better_reduce"

    def mapper(r, xs):
        return conj(r, f(*xs))

    return better_reduce(mapper, [], *colls)


def new_list(*xs):
    """ Constructor for lists with values passed as varargs"""
    return list(xs)


def new_iter(*xs):
    """ Builds a new iterator for values passed as varargs using a generator"""
    for x in xs:
        yield x


def new_tuple(*xs):
    """ Constructor for tuples with values passed as varargs"""
    return xs


def juxt(*funcs):
    """ Returns a function that juxtposes values onto the passed functions. """

    def juxt_wrapper(*args, **kwargs):
        return [f(*args, **kwargs) for f in funcs]

    return juxt_wrapper


merge_keep_left = partial(merge_with, lambda x, y: x)
merge_keep_right = partial(merge_with, lambda x, y: y)
