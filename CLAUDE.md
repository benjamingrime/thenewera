## Waterman AI Demo (board presentation)

### Demo structure
- **"Everything is code" reveal**: .docx-to-zip, .xlsx-to-zip, email headers, PDF raw operators
- **Easy tasks** (demo_prompts_easy.md): PDF summary, spreadsheet analysis w/ charts, site visit web app
- **Hard tasks** (demo_prompts_hard.md): IFC/BIM parsing, flood risk GIS mapping
- **METR narrative**: Easy tasks = 2024 models (Claude 3.5 Sonnet v2, o1). Hard tasks = 2025/26 models (Opus 4.5, GPT-5.2). By end of 2026 = 2-3 working weeks of tasks.

### example_data/ files
- `Duplex.ifc` (2.4 MB): Revit 2011 export, IFC2X3, ~39k entities, 1459 property sets. IfcOpenShell can parse.
- `Flood_Zones_2_3_Rivers_and_Sea.json` (496 KB): GeoJSON, 18 features, EPSG:4326, FZ2/FZ3 around Brackley. geopandas+folium.
- `P19-2224_EIAScoping_Report_REVB_201220.pdf` (108 MB): EIA Scoping, 103 pages. PyMuPDF reads it.
- `IC-Sample-Excel-Residential-Construction-Budget-Template-12298.xlsx` (363 KB): Construction budget. openpyxl.

### Next steps (hard mode)
- Dry run IFC task and flood task individually before parallel demo
- Install: ifcopenshell, geopandas, folium (in addition to existing openpyxl, pymupdf)
- ifcopenshell may need special Windows handling

## Project structure
- See CLAUDE.md for running instructions
- venv in `venv/` with numpy, matplotlib, scipy, openpyxl, pymupdf
- metr/ subfolder has METR analysis script and chart