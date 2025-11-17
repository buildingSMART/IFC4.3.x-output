#!/usr/bin/env python3
"""
Generiert JSON-Dateien pro IFC-Klasse mit allen Property Sets und deren Metadaten.
"""

import xml.etree.ElementTree as ET
import json
from pathlib import Path
from collections import defaultdict
import sys

def parse_property_type(prop_type_elem):
    """Extrahiert Property-Typ und Datentyp aus PropertyType Element."""
    result = {}

    # SingleValue
    single = prop_type_elem.find('.//TypePropertySingleValue')
    if single is not None:
        result['type'] = 'SingleValue'
        datatype = single.find('DataType')
        if datatype is not None:
            result['dataType'] = datatype.get('type')
        return result

    # EnumeratedValue
    enum = prop_type_elem.find('.//TypePropertyEnumeratedValue')
    if enum is not None:
        result['type'] = 'EnumeratedValue'
        enum_list = enum.find('EnumList')
        if enum_list is not None:
            result['enumName'] = enum_list.get('name')
            items = [item.text for item in enum_list.findall('EnumItem')]
            result['enumValues'] = items
        return result

    # BoundedValue
    bounded = prop_type_elem.find('.//TypePropertyBoundedValue')
    if bounded is not None:
        result['type'] = 'BoundedValue'
        datatype = bounded.find('DataType')
        if datatype is not None:
            result['dataType'] = datatype.get('type')
        return result

    # TableValue
    table = prop_type_elem.find('.//TypePropertyTableValue')
    if table is not None:
        result['type'] = 'TableValue'
        defining = table.find('.//DefiningValue/DataType')
        defined = table.find('.//DefinedValue/DataType')
        if defining is not None:
            result['definingValueType'] = defining.get('type')
        if defined is not None:
            result['definedValueType'] = defined.get('type')
        return result

    # ReferenceValue
    reference = prop_type_elem.find('.//TypePropertyReferenceValue')
    if reference is not None:
        result['type'] = 'ReferenceValue'
        result['refType'] = reference.get('reftype')
        return result

    # ListValue
    list_val = prop_type_elem.find('.//TypePropertyListValue')
    if list_val is not None:
        result['type'] = 'ListValue'
        datatype = list_val.find('.//DataType')
        if datatype is not None:
            result['dataType'] = datatype.get('type')
        return result

    return {'type': 'Unknown'}

def parse_psd_file(xml_path):
    """Parsed eine PSD-XML-Datei und extrahiert alle Informationen."""
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()

        pset_data = {
            'name': root.findtext('Name', ''),
            'definition': root.findtext('Definition', ''),
            'templateType': root.get('templatetype', ''),
            'ifcVersion': '',
            'applicableClasses': [],
            'applicableTypeValue': root.findtext('ApplicableTypeValue', ''),
            'properties': []
        }

        # IFC Version
        ifc_version = root.find('IfcVersion')
        if ifc_version is not None:
            pset_data['ifcVersion'] = ifc_version.get('version', '')

        # Applicable Classes
        applicable_classes = root.find('ApplicableClasses')
        if applicable_classes is not None:
            pset_data['applicableClasses'] = [
                cls.text for cls in applicable_classes.findall('ClassName')
                if cls.text
            ]

        # Properties
        property_defs = root.find('PropertyDefs')
        if property_defs is not None:
            for prop_def in property_defs.findall('PropertyDef'):
                prop_data = {
                    'name': prop_def.findtext('Name', ''),
                    'definition': prop_def.findtext('Definition', ''),
                }

                # PropertyType
                prop_type = prop_def.find('PropertyType')
                if prop_type is not None:
                    prop_data.update(parse_property_type(prop_type))

                # NameAliases
                name_aliases = prop_def.find('NameAliases')
                if name_aliases is not None:
                    aliases = {}
                    for alias in name_aliases.findall('NameAlias'):
                        lang = alias.get('lang')
                        if lang and alias.text:
                            aliases[lang] = alias.text
                    if aliases:
                        prop_data['nameAliases'] = aliases

                pset_data['properties'].append(prop_data)

        return pset_data

    except Exception as e:
        print(f"Error parsing {xml_path}: {e}", file=sys.stderr)
        return None

def main():
    psd_dir = Path('psd')
    output_dir = Path('properties_by_class')
    output_dir.mkdir(exist_ok=True)

    # Sammle alle Property Sets nach IFC-Klassen
    class_to_psets = defaultdict(list)

    print("Parsing XML files...")
    xml_files = sorted(psd_dir.glob('*.xml'))

    for i, xml_file in enumerate(xml_files, 1):
        if i % 100 == 0:
            print(f"  Processed {i}/{len(xml_files)} files...")

        pset_data = parse_psd_file(xml_file)
        if pset_data:
            # Füge zu allen anwendbaren Klassen hinzu
            for cls_name in pset_data['applicableClasses']:
                class_to_psets[cls_name].append(pset_data)

    print(f"\nFound {len(class_to_psets)} unique IFC classes")
    print(f"Generating JSON files...")

    # Erstelle JSON-Dateien
    stats = {
        'totalClasses': len(class_to_psets),
        'totalPropertySets': len(xml_files),
        'classes': []
    }

    for i, (cls_name, psets) in enumerate(sorted(class_to_psets.items()), 1):
        if i % 50 == 0:
            print(f"  Generated {i}/{len(class_to_psets)} class files...")

        # Zähle Properties
        total_props = sum(len(pset['properties']) for pset in psets)

        class_data = {
            'ifcClass': cls_name,
            'propertySetsCount': len(psets),
            'totalPropertiesCount': total_props,
            'propertySets': psets
        }

        # Schreibe JSON-Datei (ersetze / durch _ für Dateinamen)
        safe_cls_name = cls_name.replace('/', '_')
        output_file = output_dir / f"{safe_cls_name}.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(class_data, f, indent=2, ensure_ascii=False)

        # Statistik
        stats['classes'].append({
            'name': cls_name,
            'propertySets': len(psets),
            'properties': total_props
        })

    # Erstelle Gesamt-Statistik
    stats_file = output_dir / '_statistics.json'
    with open(stats_file, 'w', encoding='utf-8') as f:
        json.dump(stats, f, indent=2, ensure_ascii=False)

    # Erstelle Index
    index_data = {
        'description': 'IFC 4.3 Property Sets grouped by IFC Class',
        'totalClasses': len(class_to_psets),
        'totalPropertySets': len(xml_files),
        'classes': sorted(class_to_psets.keys())
    }

    index_file = output_dir / '_index.json'
    with open(index_file, 'w', encoding='utf-8') as f:
        json.dump(index_data, f, indent=2, ensure_ascii=False)

    print(f"\n✅ Successfully generated {len(class_to_psets)} JSON files")
    print(f"   Output directory: {output_dir}")
    print(f"   Statistics: {stats_file}")
    print(f"   Index: {index_file}")

    # Top 10 Klassen mit meisten Properties
    print("\n📊 Top 10 classes by property count:")
    top_classes = sorted(stats['classes'], key=lambda x: x['properties'], reverse=True)[:10]
    for cls in top_classes:
        print(f"   {cls['name']:<40} {cls['properties']:>4} properties ({cls['propertySets']} sets)")

if __name__ == '__main__':
    main()
