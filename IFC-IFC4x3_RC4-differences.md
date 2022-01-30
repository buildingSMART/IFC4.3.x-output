# Express schema differences

67 items


### Missing data

25 items

| Name                                  | IFC4x3_RC4.exp          | IFC.exp          |
|---------------------------------------|-------------------------|------------------|
| IfcBuildingElementProxy               |                         | not in 'IFC.exp' |
| IfcBuildingElementProxyType           |                         | not in 'IFC.exp' |
| IfcBuildingElementProxyTypeEnum       |                         | not in 'IFC.exp' |
| IfcPlant                              |                         | not in 'IFC.exp' |
| IfcPostalAddress                      |                         | not in 'IFC.exp' |
| IfcProxy                              |                         | not in 'IFC.exp' |
| IfcTransportElementFixedTypeEnum      |                         | not in 'IFC.exp' |
| IfcTransportElementNonFixedTypeEnum   |                         | not in 'IFC.exp' |
| IfcAbstractImpactProtectionDevice     | not in 'IFC4x3_RC4.exp' |                  |
| IfcAbstractImpactProtectionDeviceType | not in 'IFC4x3_RC4.exp' |                  |
| IfcBridgePart                         | not in 'IFC4x3_RC4.exp' |                  |
| IfcBuiltElementProxy                  | not in 'IFC4x3_RC4.exp' |                  |
| IfcBuiltElementProxyType              | not in 'IFC4x3_RC4.exp' |                  |
| IfcBuiltElementProxyTypeEnum          | not in 'IFC4x3_RC4.exp' |                  |
| IfcFacilityPartCommon                 | not in 'IFC4x3_RC4.exp' |                  |
| IfcMarinePart                         | not in 'IFC4x3_RC4.exp' |                  |
| IfcRailwayPart                        | not in 'IFC4x3_RC4.exp' |                  |
| IfcRoadPart                           | not in 'IFC4x3_RC4.exp' |                  |
| IfcTransportElementTypeEnum           | not in 'IFC4x3_RC4.exp' |                  |
| IfcTransportationDevice               | not in 'IFC4x3_RC4.exp' |                  |
| IfcVegetation                         | not in 'IFC4x3_RC4.exp' |                  |
| IfcVehicle                            | not in 'IFC4x3_RC4.exp' |                  |
| IfcVehicleType                        | not in 'IFC4x3_RC4.exp' |                  |
| IfcVehicleTypeEnum                    | not in 'IFC4x3_RC4.exp' |                  |
| IfcVirtualElementTypeEnum             | not in 'IFC4x3_RC4.exp' |                  |

### Type definitions

2 items

| Name                           | IFC4x3_RC4.exp                                                                                                                                                            | IFC.exp                                         |
|--------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| IfcTransportElementTypeSelect  | IfcTransportElementFixedTypeEnum, IfcTransportElementNonFixedTypeEnum                                                                                                     | IfcTransportElementTypeEnum, IfcVehicleTypeEnum |
| IfcPropertySetTemplateTypeEnum | NOTDEFINED, PSET_OCCURRENCEDRIVEN, PSET_PERFORMANCEDRIVEN, PSET_TYPEDRIVENONLY, PSET_TYPEDRIVENOVERRIDE, QTO_OCCURRENCEDRIVEN, QTO_TYPEDRIVENONLY, QTO_TYPEDRIVENOVERRIDE | NOTDEFINED                                      |

### Entity definitions

26 items

| Name                                         | IFC4x3_RC4.exp                                                                    | IFC.exp                                                                                                         |
|----------------------------------------------|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| IfcBuilding attributes                       | ['ElevationOfRefHeight', 'ElevationOfTerrain', 'BuildingAddress']                 | ['ElevationOfRefHeight', 'ElevationOfTerrain']                                                                  |
| IfcFacilityPart                              | not abstract                                                                      | abstract                                                                                                        |
| IfcFacilityPart attributes                   | ['PredefinedType', 'UsageType']                                                   | ['UsageType']                                                                                                   |
| IfcImpactProtectionDevice supertype          | ['IfcElementComponent']                                                           | ['IfcAbstractImpactProtectionDevice']                                                                           |
| IfcImpactProtectionDevice.PredefinedType     | PredefinedType : optional IfcImpactProtectionDeviceTypeSelect                     | PredefinedType : optional IfcImpactProtectionDeviceTypeEnum                                                     |
| IfcImpactProtectionDeviceType supertype      | ['IfcElementComponentType']                                                       | ['IfcAbstractImpactProtectionDeviceType']                                                                       |
| IfcImpactProtectionDeviceType.PredefinedType | PredefinedType : IfcImpactProtectionDeviceTypeSelect                              | PredefinedType : IfcImpactProtectionDeviceTypeEnum                                                              |
| IfcObjectPlacement inverses                  | ['PlacesObject']                                                                  | ['PlacesObject', 'ReferencedByPlacements']                                                                      |
| IfcOpenCrossProfileDef attributes            | ['HorizontalWidths', 'Widths', 'Slopes', 'Tags']                                  | ['HorizontalWidths', 'Widths', 'Slopes', 'Tags', 'OffsetPoint']                                                 |
| IfcProperty attributes                       | ['Name', 'Description']                                                           | ['Name', 'Specification']                                                                                       |
| IfcSectionedSolidHorizontal attributes       | ['CrossSectionPositions', 'FixedAxisVertical']                                    | ['CrossSectionPositions']                                                                                       |
| IfcSectionedSurface attributes               | ['Directrix', 'CrossSectionPositions', 'CrossSections', 'FixedAxisVertical']      | ['Directrix', 'CrossSectionPositions', 'CrossSections']                                                         |
| IfcSectionedSurface.CrossSectionPositions    | CrossSectionPositions : list[2:?] of IfcPointByDistanceExpression                 | CrossSectionPositions : list[2:?] of IfcAxis2PlacementLinear                                                    |
| IfcSite attributes                           | ['RefLatitude', 'RefLongitude', 'RefElevation', 'LandTitleNumber', 'SiteAddress'] | ['RefLatitude', 'RefLongitude', 'RefElevation', 'LandTitleNumber']                                              |
| IfcSpatialElement inverses                   | ['ContainsElements', 'ServicedBySystems', 'ReferencesElements']                   | ['ContainsElements', 'ServicedBySystems', 'ReferencesElements', 'IsInterferedByElements', 'InterferesElements'] |
| IfcTransportElement supertype                | ['IfcElement']                                                                    | ['IfcTransportationDevice']                                                                                     |
| IfcTransportElement.PredefinedType           | PredefinedType : optional IfcTransportElementTypeSelect                           | PredefinedType : optional IfcTransportElementTypeEnum                                                           |
| IfcTransportElementType supertype            | ['IfcElementType']                                                                | ['IfcTransportElementType']                                                                                     |
| IfcTransportElementType.PredefinedType       | PredefinedType : IfcTransportElementTypeSelect                                    | PredefinedType : IfcTransportElementTypeEnum                                                                    |
| IfcVibrationDamper supertype                 | ['IfcElementComponent']                                                           | ['IfcAbstractImpactProtectionDevice']                                                                           |
| IfcVibrationDamper.PredefinedType            | PredefinedType : optional IfcVibrationDamperTypeEnum                              | PredefinedType : optional IfcDamperTypeEnum                                                                     |
| IfcVibrationDamperType supertype             | ['IfcElementComponentType']                                                       | ['IfcAbstractImpactProtectionDeviceType']                                                                       |
| IfcVibrationDamperType.PredefinedType        | PredefinedType : optional IfcVibrationDamperTypeEnum                              | PredefinedType : IfcVibrationDamperTypeEnum                                                                     |
| IfcVibrationIsolator supertype               | ['IfcElementComponent']                                                           | ['IfcAbstractImpactProtectionDevice']                                                                           |
| IfcVibrationIsolatorType supertype           | ['IfcElementComponentType']                                                       | ['IfcAbstractImpactProtectionDeviceType']                                                                       |
| IfcVirtualElement attributes                 | []                                                                                | ['PredefinedType']                                                                                              |

### Constraints

14 items

| Name                                      | IFC4x3_RC4.exp                                   | IFC.exp                                    |
|-------------------------------------------|--------------------------------------------------|--------------------------------------------|
| IfcBuildingSystem where rules             | []                                               | ['CorrectPredefinedType']                  |
| IfcImpactProtectionDevice where rules     | ['CorrectPredefinedType', 'CorrectTypeAssigned'] | ['CorrectTypeAssigned']                    |
| IfcImpactProtectionDeviceType where rules | ['CorrectPredefinedType']                        | []                                         |
| IfcRailway where rules                    | ['HasObjectType']                                | ['HasObjectType', 'CorrectPredefinedType'] |
| IfcRoad where rules                       | ['HasObjectType']                                | ['HasObjectType', 'CorrectPredefinedType'] |
| IfcSurfaceFeature where rules             | ['HasObjectType']                                | ['HasObjectType', 'CorrectPredefinedType'] |
| IfcTransportElement where rules           | ['CorrectPredefinedType', 'CorrectTypeAssigned'] | []                                         |
| IfcTransportElementType where rules       | ['CorrectPredefinedType']                        | []                                         |
| IfcVibrationDamper where rules            | ['CorrectPredefinedType', 'CorrectTypeAssigned'] | ['CorrectTypeAssigned']                    |
| IfcVibrationDamperType where rules        | ['CorrectPredefinedType']                        | []                                         |
| IfcVibrationIsolator where rules          | ['CorrectPredefinedType', 'CorrectTypeAssigned'] | ['CorrectTypeAssigned']                    |
| IfcVibrationIsolatorType where rules      | ['CorrectPredefinedType']                        | []                                         |
| IfcVirtualElement where rules             | []                                               | ['CorrectPredefinedType']                  |
| IfcVoidingFeature where rules             | ['HasObjectType']                                | ['HasObjectType', 'CorrectPredefinedType'] |
