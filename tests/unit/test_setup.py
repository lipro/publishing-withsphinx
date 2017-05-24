# -*- coding: utf-8 -*-
#
# Copyright (c) 2017 Stephan Linz
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# How to write tests: http://docs.python-guide.org/en/latest/writing/tests/
#

'''
test_setup
~~~~~~~~~~

This module contains basic units tests for the setup sequence of the
package publishing.withsphinx.

:copyright: Copyright 2014-2017 by Li-Pro.Net, see AUTHORS.
:license: MIT, see LICENSE for details.
'''

from __future__ import absolute_import

from tests import util


class TestSetup(util.TestCasePublishingSphinx):

    @classmethod
    def setUpClass(self):
        self.message = "Method should be called. Called {times} times!"

    def test_package_has_setup(self):
        '''
        UNIT TEST: package has setup
        '''
        import publishing.withsphinx as pws
        self.assertTrue(callable(pws.setup))

    @util.mock.patch('publishing.withsphinx.backports.sphinx15')
    def test_package_has_setup_backports(self, mock_backports_sphinx15):
        '''
        UNIT TEST: package has setup calling backports from Sphinx 1.5
        '''
        import publishing.withsphinx as pws
        app = util.mock.MagicMock()
        pws.setup(app)
        self.assertTrue(mock_backports_sphinx15.called,
                        self.message.format(times=mock_backports_sphinx15.call_count))
        mock_backports_sphinx15.assert_called_with(app)

    @util.mock.patch('publishing.withsphinx.required.extensions')
    def test_package_has_setup_required(self, mock_required_extensions):
        '''
        UNIT TEST: package has setup calling required extensions
        '''
        import publishing.withsphinx as pws
        app = util.mock.MagicMock()
        pws.setup(app)
        self.assertTrue(mock_required_extensions.called,
                        self.message.format(times=mock_required_extensions.call_count))
        mock_required_extensions.assert_called_with(app)


if __name__ == "__main__":
    util.main()
