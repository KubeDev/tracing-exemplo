import logging
from jaeger_client import Config
from flask_opentracing import FlaskTracing


def init_tracer(service):
    logging.getLogger('').handlers = []
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)

    config = Config(
        config={
            'sampler': {
                'type': 'const',
                'param': 1,
            },
            'local_agent': {
                'reporting_host': 'jaeger',
                'reporting_port': '6831'
                #'reporting_port': '5775'
            },            
            'logging': True,
        },
        service_name=service,
    )

    return config.initialize_tracer()

opentracing_tracer = init_tracer("gerador-nome")
tracing = FlaskTracing(opentracing_tracer)