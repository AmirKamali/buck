#!/usr/bin/env python3
# Copyright (c) Facebook, Inc. and its affiliates.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from asyncio import StreamReader, subprocess

from buck_result import BuckResult


class BuckProcess:
    """ Instiates a BuckProcess object with a new process """

    def __init__(self, process: subprocess.Process) -> None:
        self._process = process

    async def wait(self) -> BuckResult:
        """ Returns a BuckResult with a finished process """
        stdout, stderr = await self._process.communicate()
        return BuckResult(self._process, stdout, stderr)

    def get_stderr(self) -> StreamReader:
        """ Returns the standard error of the Buck Process instance. """
        assert self._process.stderr is not None
        return self._process.stderr
        ###################################################################
        # Exception is thrown if stderr is None, but should never
        # return None with expectation that stderr=asyncio.subprocess.PIPE
        # when creating a subprocess.Process
        ###################################################################

    def get_stdout(self) -> StreamReader:
        """
        Returns the standard error that is redirected into
        standard output of the Buck Process instance.
        """
        assert self._process.stdout is not None
        return self._process.stdout
        ###################################################################
        # Exception is thrown if stdout is None, but should never
        # return None with expectation that stdout=asyncio.subprocess.PIPE
        # when creating a subprocess.Process
        ###################################################################