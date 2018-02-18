"""Tests for infinitewarp_utils.timing module."""
from unittest import mock

from infinitewarp_utils import timing


def test_timer_context_manager():
    """Assert timing.Timer behaves as a context manager."""
    with timing.Timer() as timer:
        pass
    assert timer.elapsed is not None


def test_timer_context_manager_check_while_running():
    """Assert timing.Timer gives elapsed time if checked while running."""
    with timing.Timer() as timer:
        expected_print = 'still timing; currently'
        assert str(timer).startswith(expected_print)


def test_timer_context_manager_verbose():
    """Assert timing.Timer as a context manager prints when verbose is True."""
    with mock.patch.object(timing, 'print') as mock_print:
        with timing.Timer(action='foo', verbose=True):
            pass
        expected_print = 'sec for foo'
        mock_print.mock_calls[0][1][0].endswith(expected_print)


def test_timer_object():
    """Assert time.Timer behaves as expected as an object."""
    timer = timing.Timer()
    timer.start()
    timer.stop()
    assert timer.elapsed is not None


def test_timed_decorator():
    """Assert time.timed decorator produces expected output."""
    with mock.patch.object(timing, 'print') as mock_print:
        expected_print = 'func:funky args:[(True,), {\'foo\': \'bar\'}] ' \
                         'took: '

        @timing.timed
        def funky(*args, **kwargs):
            pass

        funky(True, foo='bar')
        mock_print.mock_calls[0][1][0].startswith(expected_print)
