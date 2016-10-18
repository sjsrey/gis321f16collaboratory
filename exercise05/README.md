# Exercise 05: Geospatial Functions and Modules with Python

**GIS 321: Principles of Programming for GIScience**  
**Instructor: Dr. Sergio Rey**

![airports](/home/serge/Dropbox/g/GIS321/F16/collaboratory/exercise04/figures/airportosm.png  "Aiports and Open Street Map Layer")

In this exercise you will extend our points module to include distance based functions to carry out some analysis of the point pattern distribution.

You will be working on the [airports.csv](airports.csv) dataset we introduced in [exercise 2][e2]. Only now you will use Python to complete the following analyses.


1. In your `points/distance.py` module add a function to calculate the nearest neighbor distance (using Euclidean distance) for each airport and have it return a list of tuples with each tuple being of the following form `(origin_id, nn_id, distance)` where `origin_id` is the id of the origin airport, `nn_id` is the id of the nearest neighbor airport for `origin_id` and `distance` is the nearest neighbor distance.
2. Find the most isolated airport using Euclidean distance.
3. Find the pair of airports that are separated by the largest distance.
4. Repeat steps 1-3 but  now using an implementation of the [Haversine](https://en.wikipedia.org/wiki/Haversine_formula) formula in place of Euclidean Distance. Add your implementation of the Haversine function to your `distance.py` module.
5. Report any major descrepancies between your answers using Euclidean distance and Great Circle Distance.


Submit your finished, and fully commented, Jupyter notebook as a pull request to the collaboratory repository on GitHub.

*Hints:* You should revisit the lecture notebooks on [functions][functions] and [modules][modules] for ideas on how to implement your solutions.


[e2]: https://github.com/sjsrey/gis321f16collaboratory/blob/master/exercise02/exercise02.md
[functions]: https://github.com/sjsrey/gis321f16/blob/master/content/partI/lecture_functions.ipynb
[modules]: https://github.com/sjsrey/gis321f16/blob/master/content/partI/lecture_modules.ipynb
