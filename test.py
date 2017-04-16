#!/usr/bin/env python

import os
import pytest

path = os.path.dirname(os.path.abspath(__file__))
rv = pytest.main([path, '--ignore=env', '--verbose'])
exit(rv)
