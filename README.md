# IR Portal Tracker

Excel add-in over the IR Portal workbook's **Filtered** tab (headers in row 1, data can start in column C).

- **Dashboard**: totals, controllable items, past due, by description and by location.
- **Worklist**: every row sorted Location → Provider → MRN → Description, with filters and click-to-sort.
- **Signatures**: per-provider "Unsigned Notes" reminder emails (codified patient IDs, HIPAA footer, cc rules).
- **Clinic routing**: per-location emails and printable action lists (clinical documentation and ER/HIM/NB registration items).
- **Settings**: what counts as controllable, where each description routes, contacts, message text. Saved inside the workbook.

- **Reclassify**: open an item and change its Description. Each change (and each undo) adds a row to the **IR Reclassifications** tab; dashboard, worklist, Filtered tabs, pivots and emails use the new category.
- **Carry-over**: every status, note and flag is also saved to the **IR Notes** tab. The EOD email downloads `IR Notes M.D.YY.xlsx` (items still on the report only); **Merge notes file** in the next day's workbook brings them forward by Incident ID, newest save winning, until an item drops off the report. A saved workbook works as the merge file too.

Columns are found by header name (case, spacing and punctuation ignored), so column order doesn't matter.

The add-in only reads the workbook. Patient data never leaves it; this site serves the app's code only.

Demo with made-up data: `taskpane.html?demo=1` (`demo.html` redirects there). Install: open `taskpane.html` in a browser and click **Download manifest**, then upload it in Excel (Home → Add-ins → More Add-ins → My Add-ins → Upload My Add-in).

Source is in `src/`. GitHub Pages serves the files at the repo root, which are committed copies of `src/`: `taskpane.html` is `src/taskpane.html` with `src/manifest.xml` pasted in place of `` `__MANIFEST__` ``, and `assets/` mirrors `src/assets/` plus the generated icons. `python3 build.py` writes the same output to `dist/` (it doesn't touch the root), so after editing `src/`, copy the changes to the root files by hand or from `dist/`.

SheetJS (`assets/xlsx.full.min.js`, 0.20.3) is self-hosted from cdn.sheetjs.com rather than loaded from a public CDN.
