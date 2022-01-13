# Express schema differences

62 items


### Missing data

24 items

| Name                                | IFC4x3_RC4.exp          | IFC.exp          |
|-------------------------------------|-------------------------|------------------|
| IfcBuildingElementProxy             |                         | not in 'IFC.exp' |
| IfcBuildingElementProxyType         |                         | not in 'IFC.exp' |
| IfcBuildingElementProxyTypeEnum     |                         | not in 'IFC.exp' |
| IfcPlant                            |                         | not in 'IFC.exp' |
| IfcPostalAddress                    |                         | not in 'IFC.exp' |
| IfcProxy                            |                         | not in 'IFC.exp' |
| IfcTransportElementNonFixedTypeEnum |                         | not in 'IFC.exp' |
| IfcBridgePart                       | not in 'IFC4x3_RC4.exp' |                  |
| IfcBuiltElementProxy                | not in 'IFC4x3_RC4.exp' |                  |
| IfcBuiltElementProxyType            | not in 'IFC4x3_RC4.exp' |                  |
| IfcBuiltElementProxyTypeEnum        | not in 'IFC4x3_RC4.exp' |                  |
| IfcFacilityPartCommon               | not in 'IFC4x3_RC4.exp' |                  |
| IfcImpactProtectionDeviceCommon     | not in 'IFC4x3_RC4.exp' |                  |
| IfcImpactProtectionDeviceCommonType | not in 'IFC4x3_RC4.exp' |                  |
| IfcMarinePart                       | not in 'IFC4x3_RC4.exp' |                  |
| IfcRailwayPart                      | not in 'IFC4x3_RC4.exp' |                  |
| IfcRoadPart                         | not in 'IFC4x3_RC4.exp' |                  |
| IfcTransportElementFixed            | not in 'IFC4x3_RC4.exp' |                  |
| IfcTransportElementFixedType        | not in 'IFC4x3_RC4.exp' |                  |
| IfcVegetation                       | not in 'IFC4x3_RC4.exp' |                  |
| IfcVehicle                          | not in 'IFC4x3_RC4.exp' |                  |
| IfcVehicleType                      | not in 'IFC4x3_RC4.exp' |                  |
| IfcVehicleTypeEnum                  | not in 'IFC4x3_RC4.exp' |                  |
| IfcVirtualElementTypeEnum           | not in 'IFC4x3_RC4.exp' |                  |

### Type definitions

2 items

| Name                           | IFC4x3_RC4.exp                                                                                                                                                            | IFC.exp                                              |
|--------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|
| IfcTransportElementTypeSelect  | IfcTransportElementFixedTypeEnum, IfcTransportElementNonFixedTypeEnum                                                                                                     | IfcTransportElementFixedTypeEnum, IfcVehicleTypeEnum |
| IfcPropertySetTemplateTypeEnum | NOTDEFINED, PSET_OCCURRENCEDRIVEN, PSET_PERFORMANCEDRIVEN, PSET_TYPEDRIVENONLY, PSET_TYPEDRIVENOVERRIDE, QTO_OCCURRENCEDRIVEN, QTO_TYPEDRIVENONLY, QTO_TYPEDRIVENOVERRIDE | NOTDEFINED                                           |

### Entity definitions

26 items

| Name                                      | IFC4x3_RC4.exp                                                                    | IFC.exp                                                                                                         |
|-------------------------------------------|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| IfcBuilding attributes                    | ['ElevationOfRefHeight', 'ElevationOfTerrain', 'BuildingAddress']                 | ['ElevationOfRefHeight', 'ElevationOfTerrain']                                                                  |
| IfcFacilityPart                           | not abstract                                                                      | abstract                                                                                                        |
| IfcFacilityPart attributes                | ['PredefinedType', 'UsageType']                                                   | ['UsageType']                                                                                                   |
| IfcImpactProtectionDevice                 | not abstract                                                                      | abstract                                                                                                        |
| IfcImpactProtectionDevice attributes      | ['PredefinedType']                                                                | []                                                                                                              |
| IfcImpactProtectionDeviceType             | not abstract                                                                      | abstract                                                                                                        |
| IfcImpactProtectionDeviceType attributes  | ['PredefinedType']                                                                | []                                                                                                              |
| IfcOpenCrossProfileDef attributes         | ['HorizontalWidths', 'Widths', 'Slopes', 'Tags']                                  | ['HorizontalWidths', 'Widths', 'Slopes', 'Tags', 'OffsetPoint']                                                 |
| IfcProperty attributes                    | ['Name', 'Description']                                                           | ['Name', 'Specification']                                                                                       |
| IfcSectionedSolidHorizontal attributes    | ['CrossSectionPositions', 'FixedAxisVertical']                                    | ['CrossSectionPositions']                                                                                       |
| IfcSectionedSurface attributes            | ['Directrix', 'CrossSectionPositions', 'CrossSections', 'FixedAxisVertical']      | ['Directrix', 'CrossSectionPositions', 'CrossSections']                                                         |
| IfcSectionedSurface.CrossSectionPositions | CrossSectionPositions : list[2:?] of IfcPointByDistanceExpression                 | CrossSectionPositions : list[2:?] of IfcAxis2PlacementLinear                                                    |
| IfcSite attributes                        | ['RefLatitude', 'RefLongitude', 'RefElevation', 'LandTitleNumber', 'SiteAddress'] | ['RefLatitude', 'RefLongitude', 'RefElevation', 'LandTitleNumber']                                              |
| IfcSpatialElement inverses                | ['ContainsElements', 'ServicedBySystems', 'ReferencesElements']                   | ['ContainsElements', 'ServicedBySystems', 'ReferencesElements', 'IsInterferedByElements', 'InterferesElements'] |
| IfcTransportElement                       | not abstract                                                                      | abstract                                                                                                        |
| IfcTransportElement attributes            | ['PredefinedType']                                                                | []                                                                                                              |
| IfcTransportElementType                   | not abstract                                                                      | abstract                                                                                                        |
| IfcTransportElementType attributes        | ['PredefinedType']                                                                | []                                                                                                              |
| IfcVibrationDamper supertype              | ['IfcElementComponent']                                                           | ['IfcImpactProtectionDevice']                                                                                   |
| IfcVibrationDamper.PredefinedType         | PredefinedType : optional IfcVibrationDamperTypeEnum                              | PredefinedType : IfcDamperTypeEnum                                                                              |
| IfcVibrationDamperType supertype          | ['IfcElementComponentType']                                                       | ['IfcImpactProtectionDeviceType']                                                                               |
| IfcVibrationDamperType.PredefinedType     | PredefinedType : optional IfcVibrationDamperTypeEnum                              | PredefinedType : IfcVibrationDamperTypeEnum                                                                     |
| IfcVibrationIsolator supertype            | ['IfcElementComponent']                                                           | ['IfcImpactProtectionDevice']                                                                                   |
| IfcVibrationIsolator.PredefinedType       | PredefinedType : optional IfcVibrationIsolatorTypeEnum                            | PredefinedType : IfcVibrationIsolatorTypeEnum                                                                   |
| IfcVibrationIsolatorType supertype        | ['IfcElementComponentType']                                                       | ['IfcImpactProtectionDeviceType']                                                                               |
| IfcVirtualElement attributes              | []                                                                                | ['PredefinedType']                                                                                              |

### Constraints

10 items

| Name                                 | IFC4x3_RC4.exp                                   | IFC.exp                                    |
|--------------------------------------|--------------------------------------------------|--------------------------------------------|
| IfcBuildingSystem where rules        | []                                               | ['CorrectPredefinedType']                  |
| IfcRailway where rules               | ['HasObjectType']                                | ['HasObjectType', 'CorrectPredefinedType'] |
| IfcRoad where rules                  | ['HasObjectType']                                | ['HasObjectType', 'CorrectPredefinedType'] |
| IfcSurfaceFeature where rules        | ['HasObjectType']                                | ['HasObjectType', 'CorrectPredefinedType'] |
| IfcVibrationDamper where rules       | ['CorrectPredefinedType', 'CorrectTypeAssigned'] | ['CorrectTypeAssigned']                    |
| IfcVibrationDamperType where rules   | ['CorrectPredefinedType']                        | []                                         |
| IfcVibrationIsolator where rules     | ['CorrectPredefinedType', 'CorrectTypeAssigned'] | ['CorrectTypeAssigned']                    |
| IfcVibrationIsolatorType where rules | ['CorrectPredefinedType']                        | []                                         |
| IfcVirtualElement where rules        | []                                               | ['CorrectPredefinedType']                  |
| IfcVoidingFeature where rules        | ['HasObjectType']                                | ['HasObjectType', 'CorrectPredefinedType'] |
