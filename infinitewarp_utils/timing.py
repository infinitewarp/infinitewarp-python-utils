"""Time related helpers."""
import functools
from timeit import default_timer


def timed(func):
    """Decorate function to print elapsed time upon completion."""
    @functools.wraps(func)
    def wrap(*args, **kwargs):
        t1 = default_timer()
        result = func(*args, **kwargs)
        t2 = default_timer()
        print('func:{} args:[{}, {}] took: {:.4f} sec'.format(
            func.__name__, args, kwargs, t2 - t1))
        return result
    return wrap


class Timer(object):
    """Timing context manager."""

    def __init__(self, verbose=False, action=None):
        """
        Initialize a new Timer.

        Args:
            verbose (bool): if True, print elapsed time on exit
            action (str): optional description to include in str output
        """
        self.verbose = verbose
        self.action = action
        self.timer = default_timer
        self.elapsed = None

    def start(self):
        """Start the Timer."""
        self.start = self.timer()

    def __enter__(self):
        """Start the Timer upon entering as a context manager."""
        self.start()
        return self

    def stop(self):
        """Save the elapsed time."""
        self.elapsed = self._calculate()

    def __exit__(self, *args):
        """Save the elapsed time upon exiting as a context manager."""
        self.stop()
        if self.verbose:
            print(str(self))

    def _calculate(self):
        end = self.timer()
        return end - self.start

    def __str__(self):
        """Get printable representation of the Timer."""
        if not self.elapsed:
            return f'still timing; currently {self._calculate():.4f} sec'
        message = f'{self.elapsed:.4f} sec'
        if self.action:
            message = f'{message} for {self.action}'
        return message
