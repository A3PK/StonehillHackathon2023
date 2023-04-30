import openai
import json
import pywebio
import PyPDF2
from functools import partial
import os

def main():
    f = pywebio.input.file_upload(label = "Upload your essay here", required=True)
    open(f['filename'], "x")
    open(f['filename'], 'wb').write(f['content']) 
    pdffileobj=open(f["filename"],'rb')
    pdfreader=PyPDF2.PdfFileReader(pdffileobj)
    x=pdfreader.numPages
    text = ''
    for i in range(0,x):
        pageobj=pdfreader.getPage(i)
        text=text+pageobj.extractText()
    pdffileobj.close()
    os.remove(f['filename'])
    openai.api_key = ""
    prompt = ("Give on a 10 point score for each of the criteria: Content, Organization, Style, Grammar, Evidence, Originality, Clarity. Add a suggestion to improve the essay. Essay:" + text)
    completions = openai.Completion.create(
        engine="text-davinci-001",
        prompt=prompt,
        max_tokens=1200,
        n=1,
        stop=None,
        temperature=0.5,
    )
    output = completions.choices[0].text
    pywebio.output.put_text("Your essay score:")
    pywebio.output.put_text(output)


pywebio.start_server(main, port=8000, debug=True)