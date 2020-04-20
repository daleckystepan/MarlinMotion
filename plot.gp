

set xlabel "Time [s]"
#set xtics 0.01

set ylabel "Displacement [mm], Velocity [mm/s]"
#set ytics 1

set y2label "Acceleration [mm/s^2]"
#set y2range [0:]
set y2tics

plot "plot.dat" using 1:2 with lines title "Displacement", \
             "" using 1:3 with lines title "Velocity", \
             "" using 1:4 with lines title "Acceleration" axis x1y2#, \
             #"" using 1:5 with lines title "jerk"