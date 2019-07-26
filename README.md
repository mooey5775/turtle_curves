Python Turtle Curves
====================

This repo contains a few example Python Turtle programs, each of which draws a parametric curve from Wolfram Alpha's library of curves.

 - `parametric_converter.py` takes a parametric curve and converts it to valid Python
 - `turtle_template.py` is a blank template for more turtle curve programs
 - All other files are curve examples

Usage
-----

 - Under any Wolfram Alpha curve, click `Plaintext` under Parametric Equations.
 - Copy the `x(t)` section. Run `parametric_converter.py` and paste it in
 - Copy output and place in `x(t)` section of `turtle_template.py`
 - Do the same thing for `y(t)`
 - Check the plotting bounds, usually right under Wolfram Alpha's graph (i.e. `(plotted from 0 to 84π)`)
 - Update the `pi_count` variable in the template
 - Run and adjust scaling or resolution as needed in the template file
