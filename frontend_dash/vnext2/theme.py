"""Mantine theme configuration for v2 DMC layout."""

# Custom dark palette matching institutional navy design
# Index 0 = lightest, 9 = darkest
# Mantine uses: dark[7] = body bg, dark[6] = card/paper bg, dark[4] = borders
DARK_COLORS = [
    "#C1C7D6",  # 0 - primary text in dark mode
    "#A8AFBF",  # 1 - secondary text
    "#8E96A8",  # 2 - dimmed text
    "#6C7589",  # 3 - placeholder / muted
    "#1E2433",  # 4 - borders, dividers
    "#1A2030",  # 5 - hover bg, subtle surfaces
    "#141825",  # 6 - card / paper background
    "#0A0E1A",  # 7 - body background
    "#070A14",  # 8
    "#040710",  # 9 - deepest
]

THEME = {
    "primaryColor": "cyan",
    "fontFamily": "'Inter', 'Segoe UI', system-ui, -apple-system, sans-serif",
    "headings": {
        "fontFamily": "'Inter', 'Segoe UI', system-ui, -apple-system, sans-serif",
    },
    "colors": {
        "dark": DARK_COLORS,
    },
    "components": {
        "Card": {
            "defaultProps": {
                "radius": "md",
                "padding": "lg",
            },
        },
        "Button": {
            "defaultProps": {
                "radius": "md",
            },
        },
        "TextInput": {
            "defaultProps": {
                "radius": "md",
            },
        },
        "Select": {
            "defaultProps": {
                "radius": "md",
            },
        },
        "NumberInput": {
            "defaultProps": {
                "radius": "md",
            },
        },
    },
}
