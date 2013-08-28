Introduction
============

This repository is the Research Object for the comparison of sizes between HCGs and the CIGs.

It has the following structure:

    project
	   |
	   +- README.md: This file
	   |
	   +- sql: folder with SQL related-stuff
	   |
	   +- scripts: folder with Python scripts, other
	   |
	   +- workflows: folder with Taverna workflows


Steps to reproduce
==================

1. Run the `create_hcg_table.sql` script to create the HCG data supporting table.
1. Run the `populate_hcg_coordinates.py` script

TODO list
=========

1. Create and run the script for populating the coordinates from Sesame
1. Create and run the script for populating the sizes from Hyperleda