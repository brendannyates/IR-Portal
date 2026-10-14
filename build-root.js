// Writes the files GitHub Pages serves, from src/: run `node build-root.js` from the repo root after editing src/.
// taskpane.html = src/taskpane.html with src/manifest.xml pasted in place of `__MANIFEST__` and the build ID in place of
// '__BUILD__'; version.json carries the same ID so open panels can tell a newer version is live.
const fs = require('fs'), crypto = require('crypto');
const lf = s => s.replace(/\r\n/g, '\n'); // LF, as committed
const html = lf(fs.readFileSync('src/taskpane.html', 'utf8')), man = lf(fs.readFileSync('src/manifest.xml', 'utf8'));
if (man.includes('`') || man.includes('${')) throw new Error('manifest can\'t contain backticks or ${');
if (!html.includes("'__BUILD__'")) throw new Error('src/taskpane.html is missing the __BUILD__ marker');
const build = crypto.createHash('sha256').update(html + man).digest('hex').slice(0, 10);
fs.writeFileSync('taskpane.html', html.replace('`__MANIFEST__`', () => '`' + man.replace(/\\/g, '\\\\') + '`').replace("'__BUILD__'", () => `'${build}'`));
fs.writeFileSync('version.json', JSON.stringify({ build }) + '\n');
console.log('built ' + build);
