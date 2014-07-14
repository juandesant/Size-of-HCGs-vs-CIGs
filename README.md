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

1. Create Table 'HCGgalaxies' (See HCGgalaxies_table.sql)
2. Fill Table 'HCGgalaxies' (use: datasets/inputs/preprocessing/sample_selection/galaxy-names-hcg-ned-output-cut.csv)
3. Add new columns to HCGgalaxies table and calculate new values (See HCGgalaxies_table.sql)
1. remove this step[Run the `create_hcg_table.sql` script to create the HCG data supporting table.]
1. remove this step [Run the `populate_hcg_coordinates.py` script]

Todo list
=========

1. TODO: Create and run the script for populating the sizes from Hyperleda
2. TODO: Obtain galaxies coordinates and velocity from sextractor
3. Get group sizes from Hyperleda
4. Download Images 

Dependencies
============
1. Sextractor software
2. curl command line tool
3. Taverna 2.4 + Astrotaverna plugin or Taverna 2.5 Astronomy Edition. It requires the inclusion of stil.jar in taverna lib folder

Comments on sloan images
========
1. HCG74  returns only a image for g-band ---> removed from the workflow
2. HCG26  galaxies are not in sdr9 ---> removed from the workflow.
3. HCG77 returns only a image for g-band ---> removed from the workflow
4. HCG53 and HCG54 are very close. Is that a problem? --> I suppose it is not. 
5. HCG5, HCG36, HCG47 images were to small but this is fixed by including bigger sizes for those groups.
6. HCG10, HCG16, HCG31, HCG41, HCG59, HCG61, HCG72 images were too small

