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
        self._parent_span = None # TracedGreenlet.__tracer.active_span()

    @classmethod
    def _get_tracer(cls):
        return cls.__tracer

    @classmethod
    def _set_tracer(cls, tracer):
        cls.__tracer = tracer

    def run(self):
        """Run the actual greenlet method. Although ``gevent``
        does not support this method being overriden,
        we do so as we are simply decorating it to handle
        active span management.
        """
        #with TracedGreenlet.__tracer.make_active(self._parent_span):
        super(TracedGreenlet, self).run()

    def parent_span(self):
        """
        Return the captured parent ``Span`` for this greenlet, if any.
        """
        return self._parent_span

    def set_parent_span(self, parent_span):
        """
        Manually sets the parent ``Span`` for this greenlet.
        """
        self._parent_span = parent_span
