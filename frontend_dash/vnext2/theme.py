"""Mantine theme configuration for v2 DMC layout."""

# Custom dark palette matching institutional navy design
# Index 0 = lightest, 9 = darkest
# Mantine uses: dark[7] = body bg, dark[6] = card/paper bg, dark[4] = borders
DARK_COLORS = [
    "#E6EDF3",  # 0 - primary text in dark mode
    "#8B949E",  # 1 - secondary text
    "#7D8590",  # 2 - dimmed text / labels
    "#6C7589",  # 3 - placeholder / muted
    "#30363D",  # 4 - borders, dividers
    "#1A2030",  # 5 - hover bg, subtle surfaces
    "#161B22",  # 6 - card / paper background
    "#0D1117",  # 7 - body background
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
