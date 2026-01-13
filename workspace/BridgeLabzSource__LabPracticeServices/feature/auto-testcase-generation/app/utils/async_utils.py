import asyncio

_global_loop = None

def get_event_loop():
    global _global_loop
    if _global_loop is None or _global_loop.is_closed():
        _global_loop = asyncio.new_event_loop()
    return _global_loop

def run_async(func, *args, **kwargs):
    loop = get_event_loop()
    return loop.run_until_complete(func(*args, **kwargs))
