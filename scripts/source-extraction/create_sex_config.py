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

# Esto crea una lista de listas de tuplas pareadas;
# cada sublista representa una línea de CIG_data, y en
# esa lista, el primer elemento de la tupla es el formato del dato, 
# y el segundo elemento es el dato en sí; p.ej:
# [ # lista
#   [  # sublista, primer registro
#      (str, 'CIG0001.fits'), # primer campo
#      (float, 1.002)  # segundo campo
#   ],
#   [  # sublista, segundo registro
#      (str, 'CIG0002.fits'), # primer campo
#      (float, 2.002)  # segundo campo
#   ]
# ]
data_with_formats = map(
	lambda x: zip(field_formats,list(x)), 
	CIG_data
)

# a la lista de sublistas, aplicamos a cada elemento una transformación
# que nos permite generar un diccionario. El resultado final 
data_indexed_list =  map(
    # for each element, we create a dictionary by zipping
    # field names with field values, which are transformed
    # by the innter map 
	lambda x: dict(
		zip(
			field_names,
			# This map applies the first element (conversion function) to
			# the second element, so that data is converted
			map(
				lambda y: y[0](y[1]),
				x)
			)
	),
	data_with_formats # see format above
)

# Without comments:
# data_indexed_list =  map(
# 	lambda x: dict(
# 		zip(
# 			map(lambda x: x[0], CIG_field_names_and_formats),
# 			map(
# 				lambda y: y[0](y[1]),
# 				x)
# 			)
# 	),
# 	map(
# 		lambda x: zip(map(lambda x: x[1], CIG_field_names_and_formats),list(x)), 
# 		CIG_data
# 	)
# )

# Python one-liner:
# data_indexed_list = map( lambda x: dict( zip( map(lambda x: x[0], CIG_field_names_and_formats), map( lambda y: y[0](y[1]), x) ) ), map( lambda x: zip(map(lambda x: x[1], CIG_field_names_and_formats),list(x)), CIG_data ) )


# The iterative way of doing this would be:
data_indexed_list = []
for row in CIG_data:
	col = 0
	transformed_row = []
	for field_name, field_format in CIG_field_names_and_formats:
		value = field_format(row[col])
		col += 1
		transformed_row.append( (field_name, value) )
	data_indexed_list.append(dict(transformed_row))

# After that, each property can be obtained as:
# data_indexed_list[row_number][field_name],
# and the list of values of a field for all rows is:
# map(lambda x: x[field_name], data_indexed_list)