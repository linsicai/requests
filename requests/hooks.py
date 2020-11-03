# -*- coding: utf-8 -*-

"""
requests.hooks
~~~~~~~~~~~~~~

This module provides the capabilities for the Requests hooks system.

Available hooks:

``response``:
    The response generated from a Request.
"""
HOOKS = ['response']


# 默认钩子
def default_hooks():
    return {event: [] for event in HOOKS}

# TODO: response is the only one


# 触发所有钩子
def dispatch_hook(key, hooks, hook_data, **kwargs):
    """Dispatches a hook dictionary on a given piece of data."""
    # 取钩子
    hooks = hooks or {}
    hooks = hooks.get(key)

    if hooks:
        # 对象转数组
        if hasattr(hooks, '__call__'):
            hooks = [hooks]

        # 触发所有钩子
        for hook in hooks:
            _hook_data = hook(hook_data, **kwargs)
            if _hook_data is not None:
                hook_data = _hook_data

    # 返回最后一个钩子返回的数据
    return hook_data
