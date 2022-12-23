import requests
from tqdm import tqdm

print('Start processing ...')

input_file = r'D:\Labs\BKC\ATGT\TrafficIncidentRecognitionAndWarningSystem\DoTA\dataset\DoTA_urls.txt'
output_file = r'D:\Labs\BKC\ATGT\TrafficIncidentRecognitionAndWarningSystem\DoTA\dataset\new_DoTA_urls.txt'
invalid_sequence = 'Video này không còn hoạt động'

# Filter valid links
valid_links = []
with open(input_file) as fi:
    links = [line.strip() for line in fi.readlines()]
    
    for link in tqdm(links):
        response = requests.get(link)
        if invalid_sequence not in response.text:
            valid_links.append(link)
            
print('Valid links: {} / {} links'.format(len(valid_links), len(links)))

# Save to file
with open(output_file, 'w') as fo:
    fo.write('\n'.join(valid_links))
    
print('Write valid links to {}'.format(output_file))