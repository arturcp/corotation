# Gaia

The Gaia mission will survey about one billion stars in the Milky Way Galaxy to
create the largest and most accurate three-dimensional map of the Galaxy ever
obtained. In so doing, it will also detect new asteroids and extragalactic
sources such as quasars, find new exoplanets and even provide some tests of
Einstein’s theory of general relativity.

Gaia was approved in 2000 as a European Space Agency Cornerstone Mission within
ESA’s Horizon 2000 Plus science program.

# The Crawler

To integrate the orbit of a star, we need to know the stars first. The
ESA is mapping the Galaxy, so we used Gaia Catalog as a start point in our
project.

However, there is too much data available, and not all of it has all the
information we need. Instead of working manually on the catalog, we decided to
create a simple Python crawler to read data from the catalog and to filter it,
displaying only the objects that we can use.

Here is the repository of the crawler. The two main files are `crawler.rb` (that
should be your entry point) and `cluster.py`.

Have fun ;)
