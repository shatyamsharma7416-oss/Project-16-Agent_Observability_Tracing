import time, uuid


spans = []
span_stack = []

class track_span:
    def __init__(self, name):
        self.name = name


    def __enter__(self):
        self.span_id = str(uuid.uuid4())[:8]
        self.parent_id = span_stack[-1] if span_stack else None
        self.start = time.time()
        span_stack.append(self.span_id)
        return self

    def __exit__(self, exc_type, exc, tb):
        span_stack.pop()
        spans.append({
            "span_id":self.span_id,
            "parent_id":self.parent_id,
            "name":self.name,
            "duration_ms": round((time.time() - self.start) * 1000, 1),
            "error": str(exc) if exc else None,
        })


