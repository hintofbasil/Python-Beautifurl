#!/usr/bin/env python

import pytest
rv = pytest.main(['/home/will/Workspace/beautiful_url',
                  '--ignore=env', '--verbose'])
exit(rv)
