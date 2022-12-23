#!/bin/bash
echo "Filtering valid Youtube links ..."
python filter_links.py

echo "Downloading Youtube video ..."
python download_DoTA.py --url_file new_DoTA_urls.txt --download_dir videos --cookiefile cookies.txt

echo "Extracting frames ..."
python video2frames.py -v videos -a annotations -f 10 -o frames

echo "Done!"