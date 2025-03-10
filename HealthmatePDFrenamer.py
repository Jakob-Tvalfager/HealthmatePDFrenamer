import os
import re
from datetime import datetime
import PyPDF2

MONTHS = {
    'jan': 'January', 'feb': 'February', 'mar': 'March', 
    'apr': 'April', 'may': 'May', 'jun': 'June', 'jul': 'July',
    'aug': 'August', 'sep': 'September', 'oct': 'October',
    'nov': 'November', 'dec': 'December',
    'jan.': 'January', 'feb.': 'February', 'mar.': 'March',
    'apr.': 'April', 'may.': 'May', 'jun.': 'June', 'jul.': 'July',
    'aug.': 'August', 'sep.': 'September', 'oct.': 'October',
    'nov.': 'November', 'dec.': 'December',
    'januari': 'January', 'februari': 'February', 'mars': 'March',
    'april': 'April', 'maj': 'May', 'juni': 'June', 'juli': 'July',
    'augusti': 'August', 'september': 'September', 'oktober': 'October',
    'mei': 'May', 'okt': 'October'
}

def get_text(path):
    """Get text from PDF."""
    try:
        with open(path, 'rb') as f:
            text = ""
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                content = page.extract_text()
                if content:
                    text += content
            return text
    except Exception as error:
        raise ValueError(f"Failed to get text: {error}")

def handle_dates(dates, year):
    """Convert date string to start and end dates."""
    dates = dates.strip().replace('.-', '-')
    parts = dates.split('-')

    if len(parts) == 1:
        match = re.match(r'(\d{1,2})\s*([A-Za-z.]+)', parts[0].strip())
        if not match:
            raise ValueError(f"Bad date: {parts[0]}")
        day, month = match.groups()
        month = MONTHS.get(month.lower().replace('.', ''), month)
        date = datetime.strptime(f"{day} {month} {year}", '%d %B %Y')
        return date, date

    if len(parts) == 2:
        start, end = parts
        end_match = re.match(r'(\d{1,2})\s*([A-Za-z.]+)?', end.strip())
        if not end_match:
            raise ValueError(f"Bad end date: {end}")
        end_day, end_month = end_match.groups()
        
        if end_month:
            fixed_month = end_month.lower().replace('.', '')
            end_month = MONTHS.get(fixed_month, fixed_month.capitalize())
        else:
            raise ValueError(f"Missing month: {end}")

        end_date = datetime.strptime(f"{end_day} {end_month} {year}", '%d %B %Y')

        start_match = re.match(r'(\d{1,2})\s*([A-Za-z.]+)?', start.strip())
        if not start_match:
            raise ValueError(f"Bad start date: {start}")
        start_day, start_month = start_match.groups()
        
        start_month = end_month if not start_month else MONTHS.get(
            start_month.lower().replace('.', ''), 
            start_month.capitalize()
        )
        
        start_date = datetime.strptime(f"{start_day} {start_month} {year}", '%d %B %Y')
        return start_date, end_date

    raise ValueError(f"Wrong format: {dates}")

def process_file(file):
    """Rename PDF using date found inside."""
    if re.match(r'\d{4}-\d{2}-\d{2}-to-\d{4}-\d{2}-\d{2} · Overview.pdf', file):
        print(f"Skipping {file}: already correct")
        return

    try:
        text = get_text(file)
        found = re.search(r'Overview\s*·\s*([\d\sA-Za-z.-]+)\s*(\d{4})', text)
        if not found:
            raise ValueError("No dates found")

        date_str, year_str = found.groups()
        start, end = handle_dates(date_str, year_str)
        
        new_name = f"{start.strftime('%Y-%m-%d')}-to-{end.strftime('%Y-%m-%d')} · Overview.pdf"
        os.rename(file, new_name)
        print(f"Changed {file} to {new_name}")
    except Exception as error:
        print(f"Error with {file}: {error}")

# Go through PDF files
for f in os.listdir('.'):
    if f.lower().endswith('.pdf'):
        process_file(f)