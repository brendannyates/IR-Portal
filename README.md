# IR Portal Tracker

Excel add-in over the IR Portal workbook's **Filtered** tab (headers in row 1, data can start in column C).

- **Dashboard**: totals, controllable items, past due, by description and by location.
- **Worklist**: every row sorted Location → Provider → MRN → Description, with filters and click-to-sort.
- **Signatures**: per-provider "Unsigned Notes" reminder emails (codified patient IDs, HIPAA footer, cc rules).
- **Clinic routing**: per-location emails and printable action lists (clinical documentation and ER/HIM/NB registration items).
- **Settings**: what counts as controllable, where each description routes, contacts, message text. Saved inside the workbook.

The add-in only reads the workbook. Patient data never leaves it; this site serves the app's code only.

Demo with made-up data: `demo.html`. Install: open `taskpane.html` in a browser and click **Download manifest**, then upload it in Excel (Home → Add-ins → More Add-ins → My Add-ins → Upload My Add-in).

Source is in `src/`; `python3 build.py` writes the site files.
