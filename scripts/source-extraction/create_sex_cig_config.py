#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import pi
from pprint import pprint

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

def all_keywords_are_set(dictionary):
    result = True
    for key,value in dictionary.iteritems():
        result = result and (value is not None)
        if not result: break
    return result

#### Create SExtractor files for CIGs
default_param_dict = {
    'CATALOG_NAME':        None,
    'PARAMETERS_NAME':     'CIG0000.param',
    'CATALOG_TYPE':        'ASCII_HEAD', # ASCII with header
    'DETECT_MINAREA':      None,
    'THRESH_TYPE':         'RELATIVE',
    'DETECT_THRESH':       1.5,    # these 2 params are changed for some CIGs
    'ANALYSIS_THRESH':     3.0,    # these 2 params are changed for some CIGs
    'FILTER':              'Y',
    'FILTER_NAME':         'default.conv', # default convolution kernel
    'DEBLEND_NTHRESH':     1,
    'DEBLEND_MINCONT':     0.000005,
    'CLEAN':               'Y',
    'CLEAN_PARAM':         1.0,
    'MAG_ZEROPOINT':       22.5,
    'PHOT_APERTURES':      (0.1, 0.2, 0.4, 0.6, 0.8, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0, 22.0, 23.0, 24.0),
    'PHOT_AUTOPARAMS':     (2.5,1.5),
    'MASK_TYPE':           'CORRECT',
    'DETECT_TYPE':         'CCD',
    'PIXEL_SCALE':         0.396, # default SDSS pixel scale
    'SATUR_LEVEL':         10.,
    'GAIN':                1.0,
    'MAG_GAMMA':           4.0,
    'SEEING_FWHM':         1.0,
    'STARNNW_NAME':        'default.nnw',
    'BACK_SIZE':           64,
    'BACK_FILTERSIZE':     3,
    'BACK_TYPE':           'MANUAL',
    'BACK_VALUE':          (0.0,0.0),
    'BACKPHOTO_TYPE':      'GLOBAL',
    'BACKPHOTO_THICK':     24,
    'CHECKIMAGE_TYPE':     'OBJECTS',
    'CHECKIMAGE_NAME':     None,
    'MEMORY_OBJSTACK':     3000,
    'MEMORY_PIXSTACK':     5000000,
    'MEMORY_BUFSIZE':      1024,
    'VERBOSE_TYPE':        'NORMAL',
    'PHOT_PETROPARAMS':    (2.0,3.5),
    'PHOT_FLUXFRAC':       (0.5,1.0)
}

for cig_record in CIG_indexed_data:
    # get a copy of the default parameters
    # if we did param_dict = default_param_dict instead,
    # we would be changing elements of default_param_dict
    # by changing param_dict
    param_dict = default_param_dict.copy()
    sex_file_name = "CIG%04d_g.sex" % cig_record['CIG']
    cig_number = cig_record['CIG']
    param_dict['CATALOG_NAME'] = cig_record['imagen']+'.cat'
    # object-dependent DETECT_MINAREA
    radius = (cig_record['side']*60./8.)/default_param_dict['PIXEL_SCALE']
    miniarea = (radius * radius * pi) * 0.05
    if cig_number == 2 or cig_number == 566:
        miniarea = miniarea/2.
    param_dict['DETECT_MINAREA'] = miniarea
    # object-dependent threholds for detection/analysis;
    # the default is already set before
    if cig_number in (691, 971):
        param_dict['DETECT_THRESH']   = 0.25
        param_dict['ANALYSIS_THRESH'] = 0.5
    if cig_number in (322, 974):
        param_dict['DETECT_THRESH']   = 3.75
        param_dict['ANALYSIS_THRESH'] = 3.5
    if cig_number in (304, 291, 397, 484, 470, 224):
        param_dict['DETECT_THRESH']   = 5.0
        param_dict['ANALYSIS_THRESH'] = 3.5
    # size-dependent photo-aperture; we apply (map) the same factor to all elements, and then convert to tuple
    param_dict['PHOT_APERTURES'] = tuple(map(
                                    lambda x: x*radius/10.,
                                    default_param_dict['PHOT_APERTURES']
    ))
    param_dict['CHECKIMAGE_NAME'] = cig_record['imagen']+'seg.fits'
    # prepare for writing; file is closed at the end of the with block
    if not all_keywords_are_set(param_dict):
        print "Not all keywords set"
        pprint(param_dict)
        break
    print "Writing %s" % sex_file_name
    with open(sex_file_name,"w") as sex_file:
        for key,value in param_dict.iteritems():
            file_value = str(value)
            if type(value) == type((1,)):
                file_value = str(value)[1:-1] # removing parentheses
            sex_file.write("%-20s%s\n" % (key,file_value))
            print("%-20s%s" % (key,file_value))