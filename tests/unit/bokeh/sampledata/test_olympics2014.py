#-----------------------------------------------------------------------------
# Copyright (c) 2012 - 2024, Anaconda, Inc., and Bokeh Contributors.
# All rights reserved.
#
# The full license is in the file LICENSE.txt, distributed with this software.
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Boilerplate
#-----------------------------------------------------------------------------
from __future__ import annotations # isort:skip

import pytest ; pytest

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

# Bokeh imports
from tests.support.util.api import verify_all

# Module under test
#import bokeh.sampledata.olympics2014 as bso # isort:skip

#-----------------------------------------------------------------------------
# Setup
#-----------------------------------------------------------------------------

ALL = (
    'data',
)

#-----------------------------------------------------------------------------
# General API
#-----------------------------------------------------------------------------

Test___all__ = pytest.mark.sampledata(verify_all("bokeh.sampledata.olympics2014", ALL))

@pytest.mark.sampledata
def test_data() -> None:
    import bokeh.sampledata.olympics2014 as bso
    assert isinstance(bso.data, dict)

    # check detail for package data
    assert set(bso.data.keys()) == {"count", "data", "object"}

#-----------------------------------------------------------------------------
# Dev API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Private API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Code
#-----------------------------------------------------------------------------
