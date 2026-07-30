

from pathlib import Path
import requests

def main(all_links_address, title1, title2):
    # read links from file all_links.txt
    with open(all_links_address, 'r') as f:
        links = f.readlines()
        links = [x.strip() for x in links]

    # iterate over links
    for link in links:
        if ".pdf" in link:
            # download pdf
            if title1 in link and title2 in link:
                # out_path = link.split("/")[-2] +"_"+ link.split("/")[-1]+"_BY_CHIRAG_SINGHAL_ABES.pdf"
                out_path = link.split("/")[-1] +"_BY_CHIRAG_SINGHAL_AKTU-ONLINE.pdf"
                filename = Path(out_path)
                response = requests.get(link)
                filename.write_bytes(response.content)


                print("Downloaded: ", link)
        else:
            print("Not a pdf: ", link)

