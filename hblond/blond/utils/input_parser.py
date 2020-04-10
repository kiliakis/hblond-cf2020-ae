import argparse

parser = argparse.ArgumentParser(description='HBLonD simulation mainfile.')

parser.add_argument('-p', '--particles', type=int,
                    help='Number of macro-particles.')

parser.add_argument('-s', '--slices', type=int,
                    help='Number of slices.')

parser.add_argument('-b', '--bunches', type=int,
                    help='Number of bunches.')

parser.add_argument('-reduce', '--reduce', type=int,
                    help='Number of turns to reduce.')

parser.add_argument('-t', '--turns', type=int,
                    help='Number of simulation turns.')

parser.add_argument('-mtw', '--mtw', type=int,
                    help='Number of turns to keep the wake field in memory.')

parser.add_argument('-beginafter', '--beginafter', type=int,
                    help='Start the approximation after so many turns.')

parser.add_argument('-approx', '--approx', type=int, choices=[0, 1, 2], default=0,
                    help='Which approximation to use: 0 (No approx), 1 (global reduce), 2 (scale histo).')

parser.add_argument('-withtp', '--withtp', type=int, default=0, choices=[0, 1],
                    help='Use task-parallelism. Default: 0')

parser.add_argument('-o', '--omp', type=int, default=1,
                    help='Number of openmp threads to use.'
                    '\nDefault: 1')

parser.add_argument('-l', '--log', type=int, choices=[0,1],
                    help='Log debug messages (1) or not (0).'
                    '\nDefault: Do not log (0).')

parser.add_argument('-logdir', '--logdir', type=str, default='./logs/',
                    help='Directory to store the log files.'
                    '\nDefault: ./logs.')

parser.add_argument('-time', '--time', type=str, choices=['disabled', 'timing', 'tracing'],
                    default='disabled',
                    help='Time the specified regions of interest.'
                    '\nDefault: No timing.')

parser.add_argument('-timedir', '--timedir', type=str, default='./timings/',
                    help='Directory to store the timing reports.'
                    '\nDefault: ./timings')

parser.add_argument('-m', '--monitor', type=int, default=0, choices=[0,1],
                    help='Monitoring interval (0: no monitor).'
                    '\nDefault: 0')

parser.add_argument('-monitorfile', '--monitorfile', type=str, default=None,
                    help='h5 file to store the monitoring data.'
                    '\nDefault: Descriptive name based on simulation config.')

parser.add_argument('-seed', '--seed', type=int, default=0,
                    help='Seed value for the particle distribution generation.'
                    '\nDefault: None')

parser.add_argument('-trace', '--trace', type=int, default=0, choices=[0,1],
                    help='Trace the specified regions of interest (MPE).'
                    '\nDefault: No tracing.')

parser.add_argument('-tracefile', '--tracefile', type=str, default='mpe-trace',
                    help='The file name to save the MPE trace (without the file extension).'
                    '\nDefault: mpe-trace')

parser.add_argument('-lb', '--loadbalance', type=str, choices=['off', 'times', 'interval', 'reportonly'],
                    default=0,
                    help='Load balance policy: off, times, interval, reportonly.'
                    '\nDefault: off ')

parser.add_argument('-lba', '--loadbalancearg', type=int, default=0,
                    help='Additional Load balance argument, used only if lb is times or interval.'
                    '\nDefault: 0 --> 10 times per run or every 1k turns.')


def parse():
    args = parser.parse_args()
    return vars(args)


if __name__ == '__main__':
    args = parser.parse_args()
    print('Parsed arguments: ', args)
