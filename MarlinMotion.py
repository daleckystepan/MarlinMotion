#! /usr/bin/env python3

import argparse
import math
from enum import Enum

def integrate(t, state, arg):

    v = arg
    d = state[1]

    return [d, v]

def step(t, state, h, arg):
    k1 = integrate(t, state, arg)  

    k2 = state.copy()
    for i, v in enumerate(k2):
      k2[i] = v + 0.5*h*k1[i]
    k2 = integrate(t + 0.5*h, k2, arg)

    k3 = state.copy()
    for i, v in enumerate(k3):
      k3[i] = v + 0.5*h*k2[i]
    k3 = integrate(t + 0.5*h, k3, arg)

    k4 = state.copy()
    for i, v in enumerate(k4):
      k4[i] = v + h*k3[i]
    k4 = integrate(t + h, k4, arg)

    for i, v in enumerate(state):
      state[i] = v + h*(k1[i] + 2*k2[i] + 2*k3[i] + k4[i])/6.0

    return state

class State(Enum):
    INCRERASING = 1
    CONSTANT = 2
    DECREASING = 3

def main():
    # Parse arguments, default values
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument("-a", "--amax",  help="Max acceleration",   action="store", type=float, default=100)

    #parser.add_argument("--vinit",       help="Init velocity",      action="store", type=float, default=0)
    parser.add_argument("-v", "--vmax",  help="Max velocity",       action="store", type=float, default=15)

    parser.add_argument(      "--dinit", help="Init displacement",  action="store", type=float, default=0)
    parser.add_argument("-d", "--dmax",  help="Init displacement",  action="store", type=float, default=0.8)

    parser.add_argument("-j", "--jerk",  help="Jerk",               action="store", type=float, default=5)

    parser.add_argument("-s", "--step",  help="Init displacement",  action="store", type=float, default=0.00001)

    args = parser.parse_args()

    state = [args.dinit, args.jerk/2]
    a = args.amax

    t = 0

    f = open('plot.dat', 'w')
    f.write("{} {} {} {}\n".format(t, state[0], state[1], a))

    ss = State.INCRERASING
    print("State.INCRERASING")

    while state[0] < args.dmax and state[1] >= 0:
        state = step(t, state, args.step, a)
        t += args.step

        f.write("{} {} {} {}\n".format(t, state[0], state[1], a))

        if ss == State.INCRERASING:
            # We hit the max velocity
            if( state[1] > args.vmax):
                a = 0
                ss = State.CONSTANT
                print("State.CONSTANT")

        if ss == State.INCRERASING or ss == State.CONSTANT:
            tt = state[1]/args.amax
            d_limit = args.dmax - (state[1]*tt - 0.5*args.amax*tt*tt)
            if( state[0] > d_limit):
                a = -args.amax
                ss = State.DECREASING
                print("State.DECREASING")




    f.close()

if __name__ == '__main__':
    main()