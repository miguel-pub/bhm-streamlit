import datetime
import os
from pathlib import Path
from PyPDF2 import PdfReader
import openpyxl
import requests
import sys
from bs4 import BeautifulSoup
import subprocess

def get_pdf_url():
    website = "https://service.viona24.com/stpusnl"
    response = requests.get(website)
    soup = BeautifulSoup(response.text, "html.parser")
    thelist = soup.find(id="thelist")
    thelist_items = thelist.find_all("a")
        
        # More efficient dictionary comprehension
    return {
        item.text.strip("\n"): item.get("href").strip("./")
        for item in thelist_items if "US" in item.text
        }

def download_pdf(linksuffix: str, selection: str):
    url = f"https://service.viona24.com/stpusnl/{linksuffix}"
    filename = f"{selection}.pdf"
    response = requests.get(url)
    Path(filename).write_bytes(response.content)
    print(f"Downloaded {filename}")
    return filename

def kalenderwoche():
    today = datetime.datetime.now()
    week = today.strftime("%V")
    year = today.strftime("%Y")
    return week