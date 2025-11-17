# IFC 4.3.x Output Repository

## Übersicht

Dieses Repository enthält die **automatisch generierten Ausgabedateien** für den **IFC 4.3 Standard** (Industry Foundation Classes), basierend auf dem [IFC4.3.x-development Repository](https://github.com/buildingSMART/IFC4.3.x-development) von buildingSMART International.

> **⚠️ Status**: Work in Progress
> Offizielle Veröffentlichungen des IFC-Standards finden Sie auf [standards.buildingsmart.org/IFC](https://standards.buildingsmart.org/IFC/)

**Copyright**: © buildingSMART International Ltd. Alle Rechte vorbehalten bis zur formalen Veröffentlichung.

---

## Was ist IFC?

**IFC (Industry Foundation Classes)** ist ein offener, internationaler Standard für Building Information Modeling (BIM). Er ermöglicht den Datenaustausch zwischen verschiedenen Software-Anwendungen in der Bau- und Facility-Management-Industrie. IFC definiert ein umfassendes Datenmodell für Gebäude, Infrastrukturen und deren Komponenten über den gesamten Lebenszyklus hinweg.

---

## Repository-Struktur

### 📋 Kern-Schema-Dateien

Das IFC-Schema wird in drei verschiedenen Formaten bereitgestellt, die alle das gleiche semantische Modell repräsentieren:

#### 1. **IFC.exp** (13.984 Zeilen)
- **Format**: EXPRESS (ISO 10303-11)
- **Verwendung**: Primäres Schema-Definitionsformat für IFC
- **Schema-Name**: `IFC4X3_DEV_923b0514`
- **Inhalt**:
  - Typ-Definitionen (z.B. `IfcAbsorbedDoseMeasure`, `IfcAngularVelocityMeasure`)
  - Entity-Definitionen (Klassen)
  - Constraints und Regeln (WHERE-Klauseln)
  - Funktionen und Prozeduren

**Begleitdateien**:
- `IFC.exp.cache.dat` (24,9 MB): Cache-Datei für schnellere Verarbeitung
- `IFC.exp.md`: Dokumentation der Schema-Unterschiede (keine Probleme in aktueller Version)

#### 2. **IFC.json** (1.279.591 Zeilen, ~58 MB)
- **Format**: JSON Schema
- **Verwendung**: Für moderne Web- und API-Anwendungen
- **Inhalt**:
  - Hierarchische Klassendefinitionen
  - Property-Mappings zu Property Sets
  - Maschinenlesbare Metadaten
- **Beispiel**: Verknüpfung von Klassen mit Property Sets (z.B. `Pset_ActuatorPHistory` mit Position-, Qualitäts- und Status-Properties)

#### 3. **IFC.xsd** (16.041 Zeilen, ~705 KB)
- **Format**: XML Schema Definition (XSD)
- **Namespace**: `https://standards.buildingsmart.org/IFC/RELEASE/IFC4/3/DEV/923b0514`
- **Verwendung**: Für XML-basierte IFC-Dateien (ifcXML)
- **Inhalt**:
  - XML-Strukturdefinitionen
  - Header-Informationen (name, time_stamp, author, organization, etc.)
  - Element- und Attribut-Deklarationen

**Zusammenhang**: Alle drei Formate beschreiben dieselbe IFC-Ontologie, aber in unterschiedlichen technischen Repräsentationen für verschiedene Anwendungsfälle.

---

### 🎯 Model View Definition

#### **IFC4.3.mvdxml** (2,5 MB)
- **Format**: mvdXML (Model View Definition XML)
- **Schema-Version**: mvdXML 1.1
- **UUID**: `763689e8-383d-5bf7-bfb0-e03021e26f95`
- **Zweck**: Definiert **Konzept-Templates** und **Anwendungsregeln** für IFC-Implementierungen
- **Inhalt**:
  - **Concept Templates**: Wiederverwendbare Muster wie "Object Assignment", "Group Assignment"
  - **Anwendbare Entities**: Z.B. `IfcObjectDefinition`, `IfcGroup`
  - **Semantische Regeln**: Beschreibt Beziehungen zwischen Akteuren, Controls, Produkten, Prozessen und Ressourcen
  - **Validierungsregeln**: Für konforme IFC-Implementierungen

**Verwendung**: Software-Entwickler nutzen MVDs, um zu verstehen, welche IFC-Daten für spezifische Anwendungsfälle (z.B. Architektur, Haustechnik, Infrastruktur) erforderlich sind.

---

### 📦 Property Set Definitionen

Property Sets (Psets) erweitern IFC-Entities mit zusätzlichen Eigenschaften für verschiedene Fachdomänen.

#### **psd/** Verzeichnis (760 XML-Dateien, ~2,4 MB)
Strukturierte Property Set Definitionen, organisiert nach:

**Domänen**:
- **Gebäudetechnik**: `Pset_AirTerminal*`, `Pset_Boiler*`, `Pset_Chiller*`
- **Elektrotechnik**: `Pset_Actuator*`, `Pset_Alarm*`, `Pset_Cable*`
- **HVAC**: `Pset_AirSideSystemInformation`, `Pset_CoilType*`
- **Sanitär**: `Pset_PlumbingFireProtection*`
- **Allgemein**: `Pset_ActorCommon`, `Pset_Address`

**Struktur einer PSD-Datei**:
```xml
<PropertySetDef>
  <Name>Pset_ActuatorTypeCommon</Name>
  <PropertyDefs>
    <PropertyDef>
      <Name>ActuatorApplication</Name>
      <PropertyType>...</PropertyType>
    </PropertyDef>
  </PropertyDefs>
</PropertySetDef>
```

#### **Pset_IFC4X3.ifc** (1,4 MB)
- **Format**: Native IFC-STEP-Datei
- **Inhalt**: Alle Property Sets als IFC-Entities (`IfcPropertySet`, `IfcPropertySingleValue`)
- **Verwendung**: Direkte Verwendung in IFC-Software

**Zusammenhang**:
- Die 760 XML-Dateien in `psd/` sind granulare Einzeldefinitionen
- `Pset_IFC4X3.ifc` ist eine konsolidierte IFC-Repräsentation
- `IFC.json` referenziert diese Property Sets in den Klassendefinitionen

---

### 🌍 Internationalisierung

#### **pot/** Verzeichnis (23 POT-Dateien, ~1,2 MB)
- **Format**: Portable Object Template (Gettext)
- **Zweck**: Übersetzungsvorlagen für die IFC-Dokumentation
- **Organisation nach Modulen**:

| Modul | Datei | Größe | Beschreibung |
|-------|-------|-------|--------------|
| Building Controls | `IfcBuildingControlsDomain.pot` | 112 KB | Sensoren, Aktoren, Alarme |
| Electrical | `IfcElectricalDomain.pot` | 162 KB | Elektrische Systeme |
| HVAC | `IfcHvacDomain.pot` | 251 KB | Heizung, Lüftung, Klimatisierung |
| Shared Building | `IfcSharedBldgElements.pot` | 126 KB | Wände, Decken, Fenster |
| Infrastructure | `IfcSharedInfrastructureElements.pot` | 48 KB | Straßen, Brücken, Schienen |
| Rail | `IfcRailDomain.pot` | 14 KB | Eisenbahninfrastruktur |
| Road | `IfcRoadDomain.pot` | 17 KB | Straßeninfrastruktur |
| Ports & Waterways | `IfcPortsAndWaterwaysDomain.pot` | 74 KB | Hafen- und Wasserstraßeninfrastruktur |
| Structural | `IfcStructuralElementsDomain.pot` | 35 KB | Tragende Bauteile |

**Workflow**: Übersetzer nutzen POT-Dateien als Basis für sprachspezifische PO-Dateien (z.B. de.po, fr.po).

---

### 📊 Qualitätssicherung & Dokumentation

#### **shacl-result.md** (60 KB)
- **Zweck**: Ergebnisse der SHACL-Validierung (Shapes Constraint Language)
- **Kategorien**:
  - **DefinitionForEntity**: Fehlende Entity-Definitionen (z.B. `IfcSurfaceFeature`)
  - **DefinitionForEnumLiteral**: Fehlende Enum-Wert-Dokumentation
  - **DefinitionForProperty**: Fehlende Property-Beschreibungen (z.B. AirFlow-Properties)
  - **LeafEntityHasPredefinedType**: Validierung von PredefinedType-Attributen
- **Status**: Identifiziert ca. 30+ fehlende Definitionen

#### **IFC-psets.md** (213 KB)
Vergleicht Property Sets zwischen verschiedenen IFC-Versionen:

**Fehlend in Output** (13 Psets):
- Entfernte oder nicht mehr unterstützte Property Sets
- Beispiel: `Pset_ThermalLoadAggregate`, `Pset_SpaceThermalRequirements`

**Neu in Output** (zahlreich):
- Infrastruktur: `Pset_RailTypeCheckRail`, `Pset_MechanicalFastenerTypeRailFastening`
- Telekommunikation: `Pset_OpticalSplitter`, `Pset_OpticalPigtail`
- Elektrik: `Pset_SensorTypeRainSensor`, `Pset_ProtectiveDeviceTypeSparkGap`
- Eisenbahn: `Pset_RailwaySignalOccurrence`, `Pset_SignalFrame`

#### **IFC-IFC4x3_RC4-differences.md** (79 KB)
#### **IFC-IFC4x3_RC4_43c3555-differences.md** (78 KB)
Dokumentieren **Schema-Unterschiede** zwischen Release Candidates:

**Constraint-Änderungen** (5 Items):
| Entity | RC4 | Aktuelle Version |
|--------|-----|------------------|
| `IfcBuildingSystem` | - | `CorrectPredefinedType` hinzugefügt |
| `IfcRailway` | `HasObjectType` | + `CorrectPredefinedType` |
| `IfcRoad` | `HasObjectType` | + `CorrectPredefinedType` |
| `IfcSurfaceFeature` | `HasObjectType` | + `CorrectPredefinedType` |
| `IfcVoidingFeature` | `HasObjectType` | + `CorrectPredefinedType` |

**Bedeutung**: Strengere Validierung für Infrastruktur-Entities.

---

### 🔧 Konfigurationsdateien

#### **crowdin.yml** (98 Bytes)
- **Zweck**: Konfiguration für Crowdin (Übersetzungs-Management-Plattform)
- **Verwendung**: Automatisiert die Synchronisation der POT-Dateien mit Übersetzungsprojekten

#### **LICENSE** (229 Bytes)
- Lizenzinformationen von buildingSMART International
- Rechte vorbehalten bis zur offiziellen Veröffentlichung

---

## Zusammenhänge und Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│                    IFC4.3.x-development (Source)                │
│                    github.com/buildingSMART/...                 │
└────────────────────────┬────────────────────────────────────────┘
                         │ Automatische Generierung
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│                   Kern-Schema (Semantisches Modell)             │
├─────────────────────────────────────────────────────────────────┤
│  IFC.exp (EXPRESS) ◄──┬──► IFC.json (JSON) ◄──┬──► IFC.xsd (XML)│
│                       │                        │                 │
│  • Typen              │  • Klassen             │  • XML-Elemente │
│  • Entities           │  • Properties          │  • Attribute    │
│  • Constraints        │  • Referenzen          │  • Header       │
└───────────────────────┴────────────────────────┴─────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│              Property Set Definitionen (Erweiterungen)          │
├─────────────────────────────────────────────────────────────────┤
│  psd/*.xml (760 Dateien) ◄──────► Pset_IFC4X3.ifc              │
│                                                                  │
│  • Fachspezifische Properties                                   │
│  • Domänen: HVAC, Elektro, Infrastruktur, etc.                 │
└──────────────────────────────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│           Anwendungsregeln & Validierung                        │
├─────────────────────────────────────────────────────────────────┤
│  IFC4.3.mvdxml         │  shacl-result.md                       │
│  • Concept Templates   │  • Fehlende Definitionen               │
│  • Verwendungsregeln   │  • Validierungsergebnisse              │
└────────────────────────┴────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────┐
│              Internationalisierung & Dokumentation              │
├─────────────────────────────────────────────────────────────────┤
│  pot/*.pot (23 Module) │  *-differences.md                      │
│  • Übersetzungen       │  • Versionsvergleiche                  │
│  • Domänen-Texte       │  • Changelog                           │
└────────────────────────┴────────────────────────────────────────┘
```

### Datenfluss-Beispiel

1. **Entity-Definition**: `IfcActuator` wird in `IFC.exp` definiert
2. **Schema-Export**: Wird nach `IFC.json` und `IFC.xsd` transformiert
3. **Property-Erweiterung**: `Pset_ActuatorTypeCommon.xml` fügt Properties hinzu (ActuatorApplication, FailPosition, etc.)
4. **JSON-Verknüpfung**: `IFC.json` referenziert diese Properties in der Klassendefinition
5. **MVD-Regel**: `IFC4.3.mvdxml` definiert, wie Aktuatoren in spezifischen Anwendungsfällen verwendet werden
6. **Übersetzung**: `IfcBuildingControlsDomain.pot` enthält Übersetzungsstrings für Aktuator-Beschreibungen
7. **Validierung**: `shacl-result.md` prüft, ob alle erforderlichen Definitionen vorhanden sind

---

## Verwendung

### Für Software-Entwickler

1. **Schema-Implementierung**:
   - Verwenden Sie `IFC.exp` für EXPRESS-basierte Parser
   - Verwenden Sie `IFC.json` für moderne APIs und Web-Anwendungen
   - Verwenden Sie `IFC.xsd` für XML-basierte Workflows

2. **Property Sets integrieren**:
   - Lesen Sie `psd/*.xml` für fachspezifische Property-Definitionen
   - Oder laden Sie `Pset_IFC4X3.ifc` direkt in IFC-Software

3. **MVD-Compliance**:
   - Implementieren Sie Konzepte aus `IFC4.3.mvdxml`
   - Validieren Sie Ihre Implementierung gegen die definierten Templates

### Für Übersetzer

1. Nutzen Sie die POT-Dateien in `pot/` als Übersetzungsvorlagen
2. Erstellen Sie sprachspezifische PO-Dateien
3. Reichen Sie Übersetzungen über Crowdin ein (siehe `crowdin.yml`)

### Für Qualitätssicherung

1. Prüfen Sie `shacl-result.md` auf fehlende Definitionen
2. Vergleichen Sie Versionen mit `IFC-IFC4x3_RC4-differences.md`
3. Validieren Sie Property Sets mit `IFC-psets.md`

---

## Technische Details

### Schema-Version
- **Name**: IFC4X3_DEV
- **Build-ID**: 923b0514
- **Namespace**: `https://standards.buildingsmart.org/IFC/RELEASE/IFC4/3/DEV/923b0514`

### Statistiken
- **EXPRESS-Schema**: 13.984 Zeilen
- **JSON-Schema**: 1.279.591 Zeilen
- **XML-Schema**: 16.041 Zeilen
- **Property Sets**: 760 XML-Dateien
- **Übersetzungsmodule**: 23 POT-Dateien
- **MVD-Größe**: 2,5 MB

### Neuigkeiten in IFC 4.3

**Infrastruktur-Fokus**:
- Erweiterte Unterstützung für Straßen (`IfcRoad`)
- Eisenbahninfrastruktur (`IfcRailway`, `IfcRailType`)
- Brücken (`IfcBridge`)
- Häfen und Wasserstraßen (`IfcPortsAndWaterwaysDomain`)

**Neue Property Sets**:
- Eisenbahn-spezifisch: Signale, Schienen, Befestigungen
- Telekommunikation: Optische Splitter, Pigtails
- Elektrik: Neue Sensor- und Schutzgerät-Typen

**Strengere Validierung**:
- Zusätzliche `CorrectPredefinedType`-Constraints für Infrastruktur-Entities

---

## Bekannte Probleme

### Fehlende Definitionen (aus shacl-result.md)
- **Entities**: `IfcSurfaceFeature`, `Class1`, `Class2`
- **Enum-Werte**: `IfcBridgePartTypeEnum.SURFACESTRUCTURE`, `IfcRailwayPartTypeEnum.DILATIONTRACK`
- **Properties**: Zahlreiche AirFlow-bezogene Properties in HVAC-Psets
- **Quantities**: `Qto_WallBaseQuantities.GrossFootPrintArea/NetFootPrintArea`

### Entfernte Property Sets
13 Property Sets aus älteren Versionen sind nicht mehr enthalten (siehe `IFC-psets.md`).

---

## Beitragen

Dieses Repository enthält **automatisch generierte Dateien**. Änderungen sollten im [IFC4.3.x-development Repository](https://github.com/buildingSMART/IFC4.3.x-development) vorgenommen werden.

Für Fehlerberichte oder Verbesserungsvorschläge:
1. Prüfen Sie zunächst `shacl-result.md` und die Difference-Dateien
2. Melden Sie Probleme im development-Repository
3. Für Übersetzungen: Nutzen Sie Crowdin

---

## Weiterführende Links

- **buildingSMART International**: [buildingsmart.org](https://www.buildingsmart.org)
- **Offizielle IFC-Standards**: [standards.buildingsmart.org/IFC](https://standards.buildingsmart.org/IFC/)
- **Quell-Repository**: [github.com/buildingSMART/IFC4.3.x-development](https://github.com/buildingSMART/IFC4.3.x-development)
- **IFC-Dokumentation**: [standards.buildingsmart.org/IFC/DEV/IFC4_3/](https://standards.buildingsmart.org/IFC/DEV/IFC4_3/)
- **EXPRESS-Spezifikation**: ISO 10303-11
- **mvdXML-Spezifikation**: [buildingsmart-tech.org](http://buildingsmart-tech.org)

---

## Lizenz

© buildingSMART International Ltd.
Alle Rechte vorbehalten bis zur formalen Veröffentlichung des IFC 4.3 Standards.

---

*Dieses Repository ist Teil des offiziellen IFC-Entwicklungsprozesses von buildingSMART International. Stand: November 2024*
