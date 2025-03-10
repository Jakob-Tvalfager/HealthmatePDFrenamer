# HealthmatePDFrenamer
Renames Withings PDFs. Finds dates. Changes filenames to dates.

Extracts dates from documents.
Formats as YYYY-MM-DD-to-YYYY-MM-DD · Overview.pdf
Handles English, Dutch, and Swedish months.
Skips good files. Logs errors.

For those who hate renaming files by hand.

Dependency
> pip install PyPDF2
 
Drop in a folder with pdfs. Run it.

# Issues
Make github issue for language update as needed.

# Run & output example
````
python3 ~/Dokument/WithingsReports/HealthmatePDFrenamer.py
````
````
Changed medical_report (1).pdf to 2024-11-14-to-2024-11-29 · Overview.pdf
Changed medical_report (10).pdf to 2025-02-02-to-2025-02-17 · Overview.pdf
Changed medical_report (11).pdf to 2024-11-21-to-2024-11-29 · Overview.pdf
Changed medical_report (12).pdf to 2025-02-02-to-2025-02-17 · Overview.pdf
Changed medical_report (13).pdf to 2025-11-17-to-2025-02-17 · Overview.pdf
Changed medical_report (2).pdf to 2024-10-25-to-2024-11-23 · Overview.pdf
Changed medical_report (3).pdf to 2024-10-17-to-2024-11-23 · Overview.pdf
Changed medical_report (4).pdf to 2024-08-01-to-2024-10-21 · Overview.pdf
Changed medical_report (5).pdf to 2024-07-07-to-2024-10-07 · Overview.pdf
Changed medical_report (6).pdf to 2025-02-03-to-2025-02-09 · Overview.pdf
Changed medical_report (7).pdf to 2025-11-29-to-2025-01-30 · Overview.pdf
Changed medical_report (8).pdf to 2025-02-03-to-2025-02-09 · Overview.pdf
Changed medical_report (9).pdf to 2025-02-01-to-2025-02-17 · Overview.pdf
Changed medical_report.pdf to 2025-12-03-to-2025-03-03 · Overview.pdf
````
