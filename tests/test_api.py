import unittest

import gevent
import gevent_opentracing
from gevent_opentracing.greenlet import TracedGreenlet

from .dummies import *


class TestApi(unittest.TestCase):
    def test_init(self):
        tracer = DummyTracer()
        gevent_opentracing.init_tracing(tracer)
        self.assertEqual(tracer, TracedGreenlet._get_tracer())

    def test_init_subtracer(self):
        tracer = DummyTracer(with_subtracer=True)
        gevent_opentracing.init_tracing(tracer)
        self.assertEqual(tracer._tracer, TracedGreenlet._get_tracer())
