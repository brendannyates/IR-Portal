# IR Portal Tracker

Excel add-in over the IR Portal workbook's **Filtered** tab (headers in row 1, data can start in column C).

- **Dashboard**: totals, controllable items, past due, by description and by location.
- **Worklist**: every row sorted Location → Provider → MRN → Description, with filters and click-to-sort.
- **Signatures**: per-provider "Unsigned Notes" reminder emails (codified patient IDs, HIPAA footer, cc rules).
- **Clinic routing**: per-location emails and printable action lists (clinical documentation and ER/HIM/NB registration items).
- **Settings**: what counts as controllable, where each description routes, contacts, message text. Saved inside the workbook.

The add-in only reads the workbook. Patient data never leaves it; this site serves the app's code only.

Demo with made-up data: `taskpane.html?demo=1` (`demo.html` redirects there). Install: open `taskpane.html` in a browser and click **Download manifest**, then upload it in Excel (Home → Add-ins → More Add-ins → My Add-ins → Upload My Add-in).

Source is in `src/`. GitHub Pages serves the files at the repo root, which are committed copies of `src/`: `taskpane.html` is `src/taskpane.html` with `src/manifest.xml` pasted in place of `` `__MANIFEST__` ``, and `assets/` mirrors `src/assets/` plus the generated icons. `python3 build.py` writes the same output to `dist/` (it doesn't touch the root), so after editing `src/`, copy the changes to the root files by hand or from `dist/`.

SheetJS (`assets/xlsx.full.min.js`, 0.20.3) is self-hosted from cdn.sheetjs.com rather than loaded from a public CDN.
