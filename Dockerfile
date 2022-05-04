FROM python:3.8.2
WORKDIR /app

RUN pip install pdfrw
RUN pip install pymupdf
RUN pip install pypdf2
RUN pip install ReportLab

# ...