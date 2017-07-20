import gevent

from .greenlet import TracedGreenlet


__Greenlet = gevent.Greenlet


def init_tracing(tracer):
    '''
    Set our tracer for gevent. Tracer objects from the
    OpenTracing django/flask/pyramid libraries can be passed as well.

    :param tracer: the tracer object.
    '''
    if hasattr(tracer, '_tracer'):
        tracer = tracer._tracer

    _patch_greenlet_class(tracer)


def _patch_greenlet_class(tracer):
    # Set the tracer/activespansource to capture the span by default
    TracedGreenlet._set_tracer(tracer)

    # replace the original Greenlet class with the new one
    gevent.greenlet.Greenlet = TracedGreenlet

    # replace gevent shortcuts
    gevent.Greenlet = TracedGreenlet
    gevent.spawn = TracedGreenlet.spawn
    gevent.spawn_later = TracedGreenlet.spawn_later


__all__ = [
    'init_tracing',
]
