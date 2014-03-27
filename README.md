> Work in progress! This GitHub repository contains an in-progress Research Object (see [http://www.researchobject.org/](http://www.researchobject.org/)), and as such, all of its content, including this README file, can be in an incoherent state while this notice remains in display.

Introduction
============

This repository is the [Research Object (RO)](http://www.researchobject.org/ "Research Object portal") for the comparison of sizes between HCGs and the CIGs.

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
	   |
	   +- datasets: input data and result data for different steps of the experiment
	   |
	   +- config: configuration files to be able to run the workflows and scripts


Steps to reproduce
==================

1. Run the `create_hcg_table.sql` script to create the HCG data supporting table.
1. Run the `populate_hcg_coordinates.py` script

Todo list
=========

1. TODO: Create and run the script for populating the coordinates from Sesame
1. TODO: Create and run the script for populating the sizes from Hyperleda

Dependencies
============
1. Sextractor software
2. curl command line tool
3. Taverna 2.4 + Astrotaverna plugin or Taverna 2.5 Astronomy Edition. It requires the inclusion of stil.jar in taverna lib folder

Comments on sloan images
========
1. HCG74  returns only a image for g-band ---> removed from the workflow
2. HCG26  the images seems to be incomplete ---> need to verify this.
