import unittest

import gevent
import gevent_opentracing
from gevent_opentracing.greenlet import TracedGreenlet

from opentracing.mocktracer import MockTracer


class TestApi(unittest.TestCase):
    def test_init(self):
        tracer = MockTracer()
        gevent_opentracing.init_tracing(tracer)
        self.assertEqual(tracer, TracedGreenlet._get_tracer())
