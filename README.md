# calc-problemsets

Calculus derivative problems written in StarMath 5.0 notation, with auto-generated PDF renders.

## Structure

```
problems/          StarMath formula source files (.txt)
solutions-renders/ Rendered PDFs (auto-generated)
cli.py             Batch converter: StarMath → PDF via LibreOffice
hooks/             Git hooks (pre-commit auto-regenerates PDFs)
```

## Usage

```bash
python3 cli.py problems/ -o solutions-renders
```

Requires LibreOffice Math (`apt install libreoffice-math`).

## Setup after cloning

```bash
git config core.hooksPath hooks
```

This activates the pre-commit hook that auto-regenerates PDFs on every commit.
