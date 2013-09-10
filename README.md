> Work in progress! This GitHub repository contains an in-progress Research Object (see [http://www.researchobject.org/](http://www.researchobject.org/)), and as such, all of its content, including this README file, can be in an incoherent state while this notice remains in display.

Introduction
============

This repository is the Research Object for the comparison of sizes between HCGs and the CIGs.

It has the following structure:

    project
	   |
	   +- README.md: This file
	   |
	   +- article: folder with the article to be written about this RO
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

Todo list
=========

1. TODO: Create and run the script for populating the coordinates from Sesame
1. TODO: Create and run the script for populating the sizes from Hyperleda