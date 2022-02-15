import sys

if sys.version_info.major < 3:
    sys.exit("Python 3 required but lower version found. Aborted.")


def is_windows():
    """
    Simple function to return if a host is Windows or not
    """
    return sys.platform.startswith("win")


def is_linux():
    """
    Simple function to return if a host is Linux or not.
    Note for a proxy minion, we need to return something else
    """
    return sys.platform.startswith("linux")


def is_darwin():
    """
    Simple function to return if a host is Darwin (macOS) or not
    """
    return sys.platform.startswith("darwin")


def is_freebsd():
    """
    Simple function to return if host is FreeBSD or not
    """
    return sys.platform.startswith("freebsd")


def is_netbsd():
    """
    Simple function to return if host is NetBSD or not
    """
    return sys.platform.startswith("netbsd")


def is_openbsd():
    """
    Simple function to return if host is OpenBSD or not
    """
    return sys.platform.startswith("openbsd")
