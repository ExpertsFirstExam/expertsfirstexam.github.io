"""Build index.html from template.html + data.json + built-in fonts.
Usage: python3 build.py <fonts-dir> <form-url> <out.html>"""
import base64, json, sys, pathlib

here = pathlib.Path(__file__).parent
fonts_dir, form_url, out = pathlib.Path(sys.argv[1]), sys.argv[2], sys.argv[3]

faces = [
    ('Inter', 400, 'fontsource-inter-5.1.0/files/inter-latin-400-normal.woff2'),
    ('Inter', 500, 'fontsource-inter-5.1.0/files/inter-latin-500-normal.woff2'),
    ('Inter', 600, 'fontsource-inter-5.1.0/files/inter-latin-600-normal.woff2'),
    ('Inter', 700, 'fontsource-inter-5.1.0/files/inter-latin-700-normal.woff2'),
    ('JetBrains Mono', 400, 'fontsource-jetbrains-mono-5.1.0/files/jetbrains-mono-latin-400-normal.woff2'),
    ('JetBrains Mono', 500, 'fontsource-jetbrains-mono-5.1.0/files/jetbrains-mono-latin-500-normal.woff2'),
]
css = ''.join(
    f"@font-face{{font-family:'{n}';font-style:normal;font-weight:{w};font-display:swap;"
    f"src:url(data:font/woff2;base64,{base64.b64encode((fonts_dir / p).read_bytes()).decode()}) format('woff2')}}\n"
    for n, w, p in faces)

data = json.loads((here / 'data.json').read_text(encoding='utf8'))
codes = [b['code'] for b in data['benchmarks']]
assert len(codes) == len(set(codes)), 'duplicate codes'
assert {b['area'] for b in data['benchmarks']} <= {a['id'] for a in data['areas']}
html = (here / 'template.html').read_text(encoding='utf8')
html = html.replace('__FONTS__', css).replace("'__FORMURL__'", json.dumps(form_url).replace('"', "'"))
html = html.replace('__DATA__', json.dumps(data, ensure_ascii=False, indent=1).replace('</', '<\\/'))
pathlib.Path(out).write_text(html, encoding='utf8')
print(f'{out}: {len(html)//1024} KB, {len(data["benchmarks"])} benchmarks')
