#!c:\workspace\python_func_samples\azure_pyfuncperf_sample\env\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'memory-profiler==0.55.0','console_scripts','mprof'
__requires__ = 'memory-profiler==0.55.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('memory-profiler==0.55.0', 'console_scripts', 'mprof')()
    )
