# IR Portal Tracker

Excel add-in over the IR Portal workbook's **Filtered** tab (headers in row 1, data can start in column C).

- **Dashboard**: totals, controllable items, past due, by description and by location.
- **Worklist**: every row sorted Location → Provider → MRN → Description, with filters and click-to-sort.
- **Signatures**: per-provider "Unsigned Notes" reminder emails (codified patient IDs, HIPAA footer, cc rules).
- **Clinic routing**: per-location emails and printable action lists (clinical documentation and ER/HIM/NB registration items).
- **Settings**: what counts as controllable, where each description routes, contacts, message text. Saved inside the workbook.

- **Reclassify**: open an item and change its Description. Each change (and each undo) adds a row to the **IR Reclassifications** tab; dashboard, worklist, Filtered tabs, pivots and emails use the new category.
- **Carry-over**: every status, note and flag is also saved to the **IR Notes** tab. The EOD email downloads `IR Notes M.D.YY.xlsx` (items still on the report only); **Merge notes file** in the next day's workbook brings them forward by Incident ID, newest save winning, until an item drops off the report. A saved workbook works as the merge file too.

- **Name screen**: after a loading screen, the first open each day asks "Enter your name". The people list is kept in the workbook's add-in settings (`irUsers`), so no tab is added. Today's pick is kept in this browser per workbook, and full screen uses the panel's pick. Notes, reclassifications and reassignments save the picked name in their "Saved by" column. Use **Switch user** next to Location to change it, and Settings › People to remove a name.
- **Dev Update bell**: `dev-updates.js` / `.css` / `.json` (shared with the IVK Tracker) sit at the end of the toolbar and show what changed. Add an entry to the top of `dev-updates.json` with each release. Copies are kept in `src/` and at the root.

Columns are found by header name (case, spacing and punctuation ignored), so column order doesn't matter.

The add-in only reads the workbook. Patient data never leaves it; this site serves the app's code only.

Demo with made-up data: `taskpane.html?demo=1` (`demo.html` redirects there). Install: open `taskpane.html` in a browser and click **Download manifest**, then upload it in Excel (Home → Add-ins → More Add-ins → My Add-ins → Upload My Add-in).

Source is in `src/`. GitHub Pages serves the files at the repo root, which are committed copies of `src/`: `taskpane.html` is `src/taskpane.html` with `src/manifest.xml` pasted in place of `` `__MANIFEST__` ``, and `assets/` mirrors `src/assets/` plus the generated icons. After editing `src/`, run `node build-root.js` from the repo root: it writes `taskpane.html` and `version.json` with a build ID (a hash of the source). Commit both. Open panels check `version.json` every few minutes and when the tab regains focus; a different ID shows an **Update available, Reload now** banner. `python3 build.py` writes the same output, plus icons and the small pages, to `dist/` without touching the root.

SheetJS (`assets/xlsx.full.min.js`, 0.20.3) is self-hosted from cdn.sheetjs.com rather than loaded from a public CDN.
