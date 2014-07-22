import argparse
import datetime
import time
from os import linesep

import psutil


def system_stats(duration):
    for _ in range(duration):
        now = datetime.datetime.isoformat(datetime.datetime.utcnow())
        cpu = psutil.cpu_percent()
        mem = psutil.virtual_memory().percent
        net = psutil.net_io_counters()
        
        yield now, cpu, mem, net.bytes_sent, net.bytes_recv
        time.sleep(1)

def main(duration=60, outfile='systemstats.csv', quiet=False):
    with open(outfile, 'wb') as f:
        line = 'time,cpu_usage,memory_usage,bytes_sent,bytes_received'
        if not quiet: 
            print line
        f.write(line + linesep)

        for snapshot in system_stats(duration):
            line = '{},{},{},{},{}'.format(*snapshot)
            if not quiet:
                print line
            f.write(line + linesep)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Gather data about the system and record it in a file')
    parser.add_argument('-d','--duration', default=60, type=int)
    parser.add_argument('--output-file', default='systemstats.csv')
    parser.add_argument('-q', '--quiet', default=False, type=bool)
    args = parser.parse_args()
    main(args.duration, args.output_file, args.quiet)

