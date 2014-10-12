#!/bin/bash

dir="/home/lourdes/src/Size-of-HCGs-vs-CIGs/test/downloadImage/hcg"

#do not show errors if the folder exists
mkdir -p $dir
cd $dir

if [ ! "$(ls -A $dir)" ]; then 
   curl -e "http://dr10.sdss3.org/mosaics/check" \
       -o Mosaic.tar \
   "http://dr9.sdss3.org/dr9-cgi/getImages/mosaic?onlyprimary=True&pixelscale=0.396&ra=313.0950391&filters=gri&dec=-5.757906&size=0.1"
   tar -xvf Mosaic.tar
   rm Mosaic.tar
else
   echo "$dir is not empty. Nothing was downloaded"
fi

#list one entry per line
ls -d -1 $PWD/**
