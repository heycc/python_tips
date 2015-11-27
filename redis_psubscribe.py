#!/usr/bin/env python
# -*- coding: utf-8 -*-

import redis

if __name__ == "__main__":
    r = redis.StrictRedis()
    sub = r.pubsub()
    # ``sub.psubscribe("*")`` this won't work
    sub.psubscribe("**")
