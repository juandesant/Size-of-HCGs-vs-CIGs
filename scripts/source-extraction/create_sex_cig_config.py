#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Open data file with CIG properties
CIG_data_file = open("xycig_mosaic.txt")
CIG_data_lines = CIG_data_file.readlines()
# Clean CIG_data_lines and convert to tuples
CIG_data_lines = map(lambda x: x.rstrip(), CIG_data_lines)
CIG_data = map(lambda x: tuple(x.split()), CIG_data_lines)

# Get data apart from header
# CIG_header = CIG_data[0][1:] # First split item is # 
CIG_data = CIG_data[1:] # Remove first header line
CIG_field_names_and_formats = [
    ('sex',       str)  , # sextractor file name
    ('imagen',    str)  , # FITS file name
    ('ra',        float), # RA (from NED?)
    ('dec',       float), # Dec (from NED?)
    ('run',       int)  , # SDSS run
    ('rerun',     int)  , # SDSS rerun
    ('camCol',    int)  , # SDSS camcol
    ('field',     int)  , # SDSS field
    ('colc_g',    float), # 
    ('colc_i',    float), # 
    ('colc_r',    float), # 
    ('colc_u',    float), # 
    ('colc_z',    float), # 
    ('rowc_g',    float), # 
    ('rowc_i',    float), # 
    ('rowc_r',    float), # 
    ('rowc_u',    float), # 
    ('rowc_z',    float), # 
    ('CIG',       int)  , # CIG number
    ('RA_AMIGA',  float), # RA from AMIGA database
    ('DEC_AMIGA', float), # Dec from AMIGA database
    ('MB',        float), # Bolometric magnitude
    ('MBcorr',    float), # Corrected bolometric magnitude
    ('side',      float)  # side?
]

field_names   = map(lambda x: x[0], CIG_field_names_and_formats)
field_formats = map(lambda x: x[1], CIG_field_names_and_formats)

# Create a list of dictionaries which allow for more semantic data query:
# CIG_indexed_data[row_number][field_name],
# and the list of values of a field for all rows is:
# map(lambda x: x[field_name], CIG_indexed_data)
CIG_indexed_data = []
for row in CIG_data:
	col = 0
	transformed_row = []
	for field_name, field_format in CIG_field_names_and_formats:
		value = field_format(row[col])
		col += 1
		transformed_row.append( (field_name, value) )
	CIG_indexed_data.append(dict(transformed_row))

#### Create SExtractor files for CIGs