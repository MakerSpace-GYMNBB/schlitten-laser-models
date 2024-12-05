import xml.etree.ElementTree as ET
import sys


def edit_svg(input_file, output_file):
    """
    Edits an SVG file to match the desired output with specific attributes and namespaces,
    while preserving the background of the input SVG.

    Parameters:
        input_file (str): Path to the input SVG file.
        output_file (str): Path to save the modified SVG file.
    """
    # Parse the SVG file
    tree = ET.parse(input_file)
    root = tree.getroot()

    # Define namespaces
    namespaces = {
        "inkscape": "http://www.inkscape.org/namespaces/inkscape",
        "sodipodi": "http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd",
        "svg": "http://www.w3.org/2000/svg",
        "shaper": "http://www.shapertools.com/namespaces/shaper",
    }

    # Register namespaces for clean output
    for prefix, uri in namespaces.items():
        ET.register_namespace(prefix, uri)

    # Save the background attributes of the input SVG (if present)
    background_attributes = {
        "width": root.attrib.get("width", "30cm"),
        "height": root.attrib.get("height", "1.5cm"),
        "version": root.attrib.get("version", "1.1"),
        "x": root.attrib.get("x", "0cm"),
        "y": root.attrib.get("y", "0cm"),
        "viewBox": root.attrib.get("viewBox", "0 0 30 1.5"),
        "enable-background": root.attrib.get("enable-background", "new 0 0 30 1.5"),
        "xml:space": root.attrib.get("xml:space", "preserve"),
    }

    # Update root attributes with the preserved background values
    root.attrib.update(background_attributes)

    # Add sodipodi:namedview if not present
    if not root.find("./{http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd}namedview"):
        namedview = ET.Element(
            "{http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd}namedview",
            attrib={
                "id": "namedview1",
                "pagecolor": "#ffffff",
                "bordercolor": "#000000",
                "borderopacity": "0.25",
                "inkscape:showpageshadow": "2",
                "inkscape:pageopacity": "0.0",
                "inkscape:pagecheckerboard": "0",
                "inkscape:deskcolor": "#d1d1d1",
                "inkscape:document-units": "cm",
                "inkscape:zoom": "0.20813889",
                "inkscape:cx": "566.92913",
                "inkscape:cy": "28.826905",
                "inkscape:window-width": "1344",
                "inkscape:window-height": "449",
                "inkscape:window-x": "0",
                "inkscape:window-y": "37",
                "inkscape:window-maximized": "0",
                "inkscape:current-layer": "svg1",
            },
        )
        root.insert(0, namedview)

    # Iterate through all path elements
    for elem in root.findall(".//svg:path", namespaces):
        # Update attributes
        elem.set("fill", "rgb(0,0,0)")
        elem.set("stroke-linecap", "round")
        elem.set("stroke-linejoin", "round")
        elem.set("id", "path1")

        # Update style
        elem.set(
            "style",
            "fill:none;stroke:#ff0000;stroke-opacity:1;stroke-width:0.001;stroke-dasharray:none",
        )

    # Write changes to the output file, preserving the background
    tree.write(output_file, xml_declaration=True, encoding="UTF-8", method="xml")

# Example usage
arguments = sys.argv
print(arguments)
input_svg_path = arguments[1]  # Replace with the path to your input SVG file
output_svg_path = arguments[2] # Replace with the desired output path
edit_svg(input_svg_path, output_svg_path)

