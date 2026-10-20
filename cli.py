#!/usr/bin/env python3
"""
math2pdf - Batch convert LibreOffice Math formula text files to PDF.

Usage:
    python math2pdf.py <input_folder> [-o <output_folder>] [-e .txt,.formula]

Each text file is read as StarMath 5.0 notation, packed into a .odf
formula file, round-tripped through LibreOffice to generate proper
MathML, then exported to PDF.

Requires: libreoffice-math  (apt install libreoffice-math)
"""

import argparse
import os
import subprocess
import sys
import tempfile
import shutil
import zipfile


def build_odf(formula: str, odf_path: str) -> None:
    """Create a minimal .odf Math file with StarMath 5.0 annotation."""
    content_xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<math xmlns="http://www.w3.org/1998/Math/MathML">\n'
        " <semantics>\n"
        '  <annotation encoding="StarMath 5.0">'
        f"{formula}"
        "</annotation>\n"
        " </semantics>\n"
        "</math>"
    )
    manifest_xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<manifest:manifest xmlns:manifest='
        '"urn:oasis:names:tc:opendocument:xmlns:manifest:1.0"'
        ' manifest:version="1.2">\n'
        ' <manifest:file-entry manifest:media-type='
        '"application/vnd.oasis.opendocument.formula"'
        ' manifest:full-path="/"/>\n'
        ' <manifest:file-entry manifest:media-type="text/xml"'
        ' manifest:full-path="content.xml"/>\n'
        "</manifest:manifest>"
    )
    with zipfile.ZipFile(odf_path, "w") as zf:
        zf.writestr(
            "mimetype",
            "application/vnd.oasis.opendocument.formula",
            compress_type=zipfile.ZIP_STORED,
        )
        zf.writestr("content.xml", content_xml)
        zf.writestr("META-INF/manifest.xml", manifest_xml)


def convert_to_pdf(formula: str, pdf_path: str) -> None:
    """StarMath text → ODF → round-trip (generates MathML) → print to PDF.

    Uses --print-to-file instead of --convert-to pdf so the output
    contains only the rendered equation (no title, source code, or border).
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        # 1. Build minimal ODF with just the StarMath annotation
        minimal = os.path.join(tmpdir, "formula.odf")
        build_odf(formula, minimal)

        # 2. Round-trip: LO re-saves ODF with full MathML generated
        rt_dir = os.path.join(tmpdir, "rt")
        os.makedirs(rt_dir)
        r = subprocess.run(
            ["soffice", "--headless", "--convert-to", "odf",
             "--outdir", rt_dir, minimal],
            capture_output=True, text=True,
        )
        complete_odf = os.path.join(rt_dir, "formula.odf")
        if not os.path.exists(complete_odf):
            raise FileNotFoundError("Round-trip failed: " + r.stderr.strip())

        # 3. Print to PDF — equation only, no chrome
        pdf_dir = os.path.join(tmpdir, "pdf")
        os.makedirs(pdf_dir)
        r = subprocess.run(
            ["soffice", "--headless", "--print-to-file",
             "--outdir", pdf_dir, complete_odf],
            capture_output=True, text=True,
        )
        tmp_pdf = os.path.join(pdf_dir, "formula.pdf")
        if not os.path.exists(tmp_pdf):
            raise FileNotFoundError("Print-to-file failed: " + r.stderr.strip())

        os.makedirs(os.path.dirname(pdf_path), exist_ok=True)
        shutil.move(tmp_pdf, pdf_path)


def collect_files(input_folder: str, extensions: tuple):
    """Yield (absolute_path, relative_path) for every matching file."""
    for root, _dirs, files in os.walk(input_folder):
        for fname in sorted(files):
            if fname.lower().endswith(extensions):
                abs_path = os.path.join(root, fname)
                rel_path = os.path.relpath(abs_path, input_folder)
                yield abs_path, rel_path


def main():
    parser = argparse.ArgumentParser(
        description="Batch-convert StarMath 5.0 formula files to PDF.",
    )
    parser.add_argument("input_folder", help="Folder with formula text files")
    parser.add_argument(
        "-o", "--output", default=None,
        help="Output folder (default: <input_folder>_pdf)",
    )
    parser.add_argument(
        "-e", "--ext", default=".txt",
        help="Comma-separated input extensions (default: .txt)",
    )
    args = parser.parse_args()

    input_folder = os.path.abspath(args.input_folder)
    if not os.path.isdir(input_folder):
        print(f"Error: '{input_folder}' is not a directory.", file=sys.stderr)
        sys.exit(1)

    output_folder = (
        os.path.abspath(args.output)
        if args.output
        else input_folder.rstrip(os.sep) + "_pdf"
    )
    os.makedirs(output_folder, exist_ok=True)

    extensions = tuple(
        ext.strip() if ext.strip().startswith(".") else f".{ext.strip()}"
        for ext in args.ext.split(",")
    )

    files = list(collect_files(input_folder, extensions))
    if not files:
        print(f"No {extensions} files found in '{input_folder}'.")
        sys.exit(0)

    print(f"Found {len(files)} file(s). Converting...\n")

    ok, fail = 0, 0
    for abs_path, rel_path in files:
        pdf_rel = os.path.splitext(rel_path)[0] + ".pdf"
        pdf_abs = os.path.join(output_folder, pdf_rel)
        label = rel_path

        try:
            formula = open(abs_path, "r", encoding="utf-8").read().strip()
            if not formula:
                print(f"  SKIP  {label}  (empty file)")
                continue

            convert_to_pdf(formula, pdf_abs)
            print(f"  OK    {label}  →  {pdf_rel}")
            ok += 1
        except Exception as exc:
            print(f"  FAIL  {label}  ({exc})", file=sys.stderr)
            fail += 1

    print(f"\nDone. {ok} converted, {fail} failed.")
    print(f"Output: {output_folder}")


if __name__ == "__main__":
    main()