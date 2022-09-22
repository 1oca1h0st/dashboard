# https://github.com/projectdiscovery/subfinder
import os
import re
import shlex
import subprocess
import sys

__author = "loca1h0st <chenjh.network@gmail.com>"
__version__ = "0.0.1"


class SubFiner(object):
    def __init__(
            self,
            subfinder_search_path=(
                    "subfinder",
                    "/usr/bin/subfinder",
                    "/usr/local/bin/subfinder",
                    "/sw/bin/subfinder",
                    "/opt/local/bin/subfinder",
            )
    ):
        self._subfinder_path = ""
        self._subfinder_output = ""
        self._subfinder_version_numer = 0
        self._subfinder_subversion_number = 0
        self._subfinder_revised_number = 0

        for subfinder_path in subfinder_search_path:
            try:
                if sys.platform.startswith("freebsd") \
                        or sys.platform.startswith("linux") \
                        or sys.platform.startswith("darwin"):
                    p = subprocess.Popen(
                        [subfinder_path, "-version"],
                        bufsize=10000,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        stdin=subprocess.PIPE,
                        close_fds=True,
                    )
                else:
                    p = subprocess.Popen(
                        [subfinder_path, "-version"],
                        bufsize=10000,
                        stdout=subprocess.PIPE
                    )
            except OSError:
                pass
            else:
                self._subfinder_path = subfinder_path  # save path
                break
        else:
            raise SubfinderError(
                "subfinder program was not found in path. Get it from: https://github.com/projectdiscovery/subfinder"
            )

        # subfinder version will output to stderr
        self._subfinder_output = p.stderr.read()
        if isinstance(self._subfinder_output, bytes):
            self._subfinder_output = self._subfinder_output.decode('utf-8')
        regex = re.compile(r"Current Version: v([0-9]\.){2}[0-9]")
        for line in self._subfinder_output.split(os.linesep):
            # remove [INF] info
            if regex.match(line[15:]):
                # get subfinder versions
                regex_version = re.compile(r"((?P<version>\d)\.)((?P<subversion>\d)\.)(?P<revised>\d)")
                rv = regex_version.search(line[15:])
                if rv:
                    self._subfinder_version_numer = int(rv.group('version'))
                    self._subfinder_version_numer = int(rv.group('subversion'))
                    self._subfinder_revised_number = int(rv.group('revised'))
                break
        else:
            raise SubfinderError(
                "subfinder program was not found in path. Get it from: https://github.com/projectdiscovery/subfinder")
        return

    def scan(self, host_domains, arguments, timeout=0):
        cmd = (
                [self._subfinder_path, "-oJ", "-silent", "-d"]
                + shlex.split(host_domains)
                + shlex.split(arguments)
        )
        p = subprocess.Popen(
            cmd,
            bufsize=100000,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        if timeout == 0:
            output, err = p.communicate()
        else:
            try:
                output, err = p.communicate(timeout=timeout)
            except subprocess.TimeoutExpired:
                p.kill()
                raise SubFinderTimeout("Timeout from subfinder process")

        # err = bytes.decode(err)
        return output, err

    @property
    def subfinder_version(self):
        return self._subfinder_version_numer, self._subfinder_version_numer, self._subfinder_revised_number


class SubfinderError(Exception):
    """
    Exception error class for PortScanner class

    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

    def __repr__(self):
        return f"SubFinderError exception {self.value}"


class SubFinderTimeout(SubfinderError):
    pass


if __name__ == '__main__':
    domain = "github.com"
    subfinder = SubFiner()
    a = subfinder.scan(domain, "", 0)
    print(a)
