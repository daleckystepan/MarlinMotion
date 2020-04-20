# Marlin Motion Simulator #

Tool to simulate Marlin motion

![screenshot](https://github.com/daleckystepan/MarlinMotion/raw/master/screenshot.png)

## Usage ##
```
./MarlinMotion.py -h
usage: MarlinMotion.py [-h] [-a AMAX] [-v VMAX] [--dinit DINIT] [-d DMAX]
                       [-j JERK] [-s STEP]

optional arguments:
  -h, --help            show this help message and exit
  -a AMAX, --amax AMAX  Max acceleration (default: 100)
  -v VMAX, --vmax VMAX  Max velocity (default: 15)
  --dinit DINIT         Init displacement (default: 0)
  -d DMAX, --dmax DMAX  Init displacement (default: 0.8)
  -j JERK, --jerk JERK  Jerk (default: 5)
  -s STEP, --step STEP  Init displacement (default: 1e-05)
```


## Example run ##
`./MarlinMotion && gnuplot -p plot.gp`