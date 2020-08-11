from unittest import skipIf

    fcntl = None  # type: ignore[assignment]

try:
    from twisted.internet.process import (
        ProcessReader, ProcessWriter, PTYProcess)
except ImportError:
    process = None  # type: ignore[misc,assignment]
    ProcessReader = object  # type: ignore[misc,assignment]
    ProcessWriter = object  # type: ignore[misc,assignment]
    PTYProcess = object  # type: ignore[misc,assignment]
from twisted.python.compat import networkString, bytesEnviron
pyExe = FilePath(sys.executable).path
properEnv = dict(os.environ)
properEnv["PYTHONPATH"] = os.pathsep.join(sys.path)
    programName = b""  # type: bytes
            self, pyExe, [pyExe, "-u", "-m", self.programName] + argv,
        environBytes = b''.join(chunks)
        if not environBytes:
        environb = iter(environBytes.split(b'\0'))
                k = next(environb)
                v = next(environb)
@skipIf(not interfaces.IReactorProcess(reactor, None),
        "reactor doesn't support IReactorProcess")
            badUnicode.encode(sys.stdout.encoding)
@skipIf(runtime.platform.getType() != 'win32',
        "Only runs on Windows")
@skipIf(not interfaces.IReactorProcess(reactor, None),
        "reactor doesn't support IReactorProcess")
@skipIf(runtime.platform.getType() != 'posix',
        "Only runs on POSIX platform")
@skipIf(not interfaces.IReactorProcess(reactor, None),
        "reactor doesn't support IReactorProcess")

@skipIf(runtime.platform.getType() != 'posix',
        "Only runs on POSIX platform")
@skipIf(not interfaces.IReactorProcess(reactor, None),
        "reactor doesn't support IReactorProcess")
    @skipIf(runtime.platform.isMacOSX(),
            "Test is flaky from a Darwin bug. See #8840.")

class DumbProcessWriter(ProcessWriter):
    """
    A fake L{ProcessWriter} used for tests.
    """

    def startReading(self):
        Here's the faking: don't do anything here.

class DumbProcessReader(ProcessReader):
    """
    A fake L{ProcessReader} used for tests.
    """

    def startReading(self):
        Here's the faking: don't do anything here.

class DumbPTYProcess(PTYProcess):
    """
    A fake L{PTYProcess} used for tests.
    """

    def startReading(self):
        Here's the faking: don't do anything here.
@skipIf(runtime.platform.getType() != 'posix',
        "Only runs on POSIX platform")
@skipIf(not interfaces.IReactorProcess(reactor, None),
        "reactor doesn't support IReactorProcess")
@skipIf(runtime.platform.getType() != 'posix',
        "Only runs on POSIX platform")
@skipIf(not interfaces.IReactorProcess(reactor, None),
        "reactor doesn't support IReactorProcess")
@skipIf(runtime.platform.getType() != 'win32',
        "Only runs on Windows")
@skipIf(not interfaces.IReactorProcess(reactor, None),
        "reactor doesn't support IReactorProcess")
        if os.supports_bytes_environ:
            env = dict(os.environb)
        else:
            env = bytesEnviron()
        pyExe = FilePath(sys.executable).path
@skipIf(runtime.platform.getType() != 'win32',
        "Only runs on Windows")
@skipIf(not interfaces.IReactorProcess(reactor, None),
        "reactor doesn't support IReactorProcess")
    def test_AsciiEncodeableUnicodeEnvironment(self):
        C{os.environ} (inherited by every subprocess on Windows)
        contains Unicode keys and Unicode values which can be ASCII-encodable.
        os.environ['KEY_ASCII'] = 'VALUE_ASCII'
        self.addCleanup(operator.delitem, os.environ, 'KEY_ASCII')

        p = GetEnvironmentDictionary.run(reactor, [], os.environ)

        def gotEnvironment(environb):
            self.assertEqual(environb[b'KEY_ASCII'], b'VALUE_ASCII')
        return p.getResult().addCallback(gotEnvironment)


    @skipIf(sys.stdout.encoding != sys.getfilesystemencoding(),
            "sys.stdout.encoding: {} does not match "
            "sys.getfilesystemencoding(): {} .  May need to set "
            "PYTHONUTF8 and PYTHONIOENCODING environment variables.".format(
            sys.stdout.encoding, sys.getfilesystemencoding()))
    def test_UTF8StringInEnvironment(self):
        """
        L{os.environ} (inherited by every subprocess on Windows) can
        contain a UTF-8 string value.
        """
        envKey = 'TWISTED_BUILD_SOURCEVERSIONAUTHOR'
        envKeyBytes = b'TWISTED_BUILD_SOURCEVERSIONAUTHOR'
        envVal = "Speciał Committór"
        os.environ[envKey] = envVal
        self.addCleanup(operator.delitem, os.environ, envKey)

        p = GetEnvironmentDictionary.run(reactor, [], os.environ)

        def gotEnvironment(environb):
            self.assertIn(envKeyBytes, environb)
            self.assertEqual(environb[envKeyBytes],
                             "Speciał Committór".encode(sys.stdout.encoding))
@skipIf(runtime.platform.getType() != 'win32',
        "Only runs on Windows")
@skipIf(not interfaces.IReactorProcess(reactor, None),
        "reactor doesn't support IReactorProcess")

        pyExe = FilePath(sys.executable).path
@skipIf(runtime.platform.getType() != 'win32',
        "Only runs on Windows")
@skipIf(not interfaces.IReactorProcess(reactor, None),
        "reactor doesn't support IReactorProcess")
@skipIf(not interfaces.IReactorProcess(reactor, None),
        "reactor doesn't support IReactorProcess")

            if runtime.platform.isWindows():
                self.assertIn(b"OSError", errput)
                self.assertIn(b"22", errput)
                self.assertIn(b'BrokenPipeError', errput)