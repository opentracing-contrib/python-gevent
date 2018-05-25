import gevent


class TracedGreenlet(gevent.Greenlet):
    """
    ``Greenlet`` class that is used to replace the original ``gevent``
    class. This class is supposed to do parent ``Span`` management.
    When a new greenlet is spawned from the main greenlet, the current
    active ``Span`` is captured. The main greenlet is not affected
    by this behavior.

    There is no need to inherit this class to create or optimize greenlets
    instances, because this class replaces ``gevent.greenlet.Greenlet``
    through the ``init_tracing()`` method. After the patch, extending the gevent
    ``Greenlet`` class means extending automatically ``TracedGreenlet``.
    """

    __tracer = None

    def __init__(self, *args, **kwargs):
        super(TracedGreenlet, self).__init__(*args, **kwargs)
        scope_manager = TracedGreenlet.__tracer.scope_manager
        scope_manager._set_greenlet_scope(scope_manager.active, greenlet=self)

    @classmethod
    def _get_tracer(cls):
        return cls.__tracer

    @classmethod
    def _set_tracer(cls, tracer):
        cls.__tracer = tracer
