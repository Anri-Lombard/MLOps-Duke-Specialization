import click
from transformers import pipeline
import urllib.request
from bs4 import BeautifulSoup
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

def extract_from_url(url):
    text = ""
    req = urllib.request.Request(url, data=None, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req)
    parser = BeautifulSoup(html, 'html.parser')
    for paragraph in parser.find_all('p'):
        print(paragraph.text)
        text += paragraph.text
    return text

def process(text):
    summarizer = pipeline("summarization", model="t5-small")
    result = summarizer(text, min_length=30, max_length=100)
    click.echo("Summarization process completed.")
    click.echo("=" * 80)
    return result[0]['summary_text']

@click.command()
@click.option('--url', '-u', help='URL to extract text from')
@click.option('--file', '-f', help='Path to file to summarize')
def main(url, file):
    text = ""
    if url:
        text = extract_from_url(url)
    elif file:
        with open(file, 'r') as f:
            text = f.read()
    if text:
        click.echo(f"Summarized text from -> {url or file}")
        click.echo(process(text))
    else:
        click.echo("No text to summarize.")
