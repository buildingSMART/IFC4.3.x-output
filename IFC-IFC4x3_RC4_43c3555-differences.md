# Express schema differences

42 items


### Missing data

15 items

| Name                                | IFC4x3_RC4_43c3555.exp          | IFC.exp          |
|-------------------------------------|---------------------------------|------------------|
| IfcPlant                            |                                 | not in 'IFC.exp' |
| IfcTransportElementNonFixedTypeEnum |                                 | not in 'IFC.exp' |
| IfcBridgePart                       | not in 'IFC4x3_RC4_43c3555.exp' |                  |
| IfcFacilityPartCommon               | not in 'IFC4x3_RC4_43c3555.exp' |                  |
| IfcImpactProtectionDeviceCommon     | not in 'IFC4x3_RC4_43c3555.exp' |                  |
| IfcImpactProtectionDeviceCommonType | not in 'IFC4x3_RC4_43c3555.exp' |                  |
| IfcMarinePart                       | not in 'IFC4x3_RC4_43c3555.exp' |                  |
| IfcRailwayPart                      | not in 'IFC4x3_RC4_43c3555.exp' |                  |
| IfcRoadPart                         | not in 'IFC4x3_RC4_43c3555.exp' |                  |
| IfcTransportElementFixed            | not in 'IFC4x3_RC4_43c3555.exp' |                  |
| IfcTransportElementFixedType        | not in 'IFC4x3_RC4_43c3555.exp' |                  |
| IfcVegetation                       | not in 'IFC4x3_RC4_43c3555.exp' |                  |
| IfcVehicle                          | not in 'IFC4x3_RC4_43c3555.exp' |                  |
| IfcVehicleType                      | not in 'IFC4x3_RC4_43c3555.exp' |                  |
| IfcVehicleTypeEnum                  | not in 'IFC4x3_RC4_43c3555.exp' |                  |

### Type definitions

3 items

| Name                           | IFC4x3_RC4_43c3555.exp                                                                                                                                                                           | IFC.exp                                                                                                                                                                                         |
|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IfcTransportElementTypeSelect  | IfcTransportElementFixedTypeEnum, IfcTransportElementNonFixedTypeEnum                                                                                                                            | IfcTransportElementFixedTypeEnum, IfcVehicleTypeEnum                                                                                                                                            |
| IfcPropertySetTemplateTypeEnum | NOTDEFINED, PSET_OCCURRENCEDRIVEN, PSET_PERFORMANCEDRIVEN, PSET_TYPEDRIVENONLY, PSET_TYPEDRIVENOVERRIDE, QTO_OCCURRENCEDRIVEN, QTO_TYPEDRIVENONLY, QTO_TYPEDRIVENOVERRIDE                        | NOTDEFINED                                                                                                                                                                                      |
| IfcRailwayPartTypeEnum         | DILATATIONSUPERSTRUCTURE, LINESIDESTRUCTURE, LINESIDESTRUCTUREPART, NOTDEFINED, PLAINTRACKSUPERSTRUCTURE, SUPERSTRUCTURE, TRACKSTRUCTURE, TRACKSTRUCTUREPART, TURNOUTSUPERSTRUCTURE, USERDEFINED | DILATATIONSUPERSTRUCTURE, LINESIDESTRUCTURE, LINESIDESTRUCTUREPART, NOTDEFINED, PLAINTRACKSUPESTRUCTURE, SUPERSTRUCTURE, TRACKSTRUCTURE, TRACKSTRUCTUREPART, TURNOUTSUPERSTRUCTURE, USERDEFINED |

### Entity definitions

15 items

| Name                                     | IFC4x3_RC4_43c3555.exp                               | IFC.exp                                     |
|------------------------------------------|------------------------------------------------------|---------------------------------------------|
| IfcFacilityPart                          | not abstract                                         | abstract                                    |
| IfcFacilityPart attributes               | ['PredefinedType', 'UsageType']                      | ['UsageType']                               |
| IfcImpactProtectionDevice                | not abstract                                         | abstract                                    |
| IfcImpactProtectionDevice attributes     | ['PredefinedType']                                   | []                                          |
| IfcImpactProtectionDeviceType            | not abstract                                         | abstract                                    |
| IfcImpactProtectionDeviceType attributes | ['PredefinedType']                                   | []                                          |
| IfcProperty attributes                   | ['Name', 'Description']                              | ['Name', 'Specification']                   |
| IfcTransportElement                      | not abstract                                         | abstract                                    |
| IfcTransportElement attributes           | ['PredefinedType']                                   | []                                          |
| IfcTransportElementType                  | not abstract                                         | abstract                                    |
| IfcTransportElementType attributes       | ['PredefinedType']                                   | []                                          |
| IfcVibrationDamper supertype             | ['IfcElementComponent']                              | ['IfcImpactProtectionDevice']               |
| IfcVibrationDamper.PredefinedType        | PredefinedType : optional IfcVibrationDamperTypeEnum | PredefinedType : IfcDamperTypeEnum          |
| IfcVibrationDamperType supertype         | ['IfcElementComponentType']                          | ['IfcImpactProtectionDeviceType']           |
| IfcVibrationDamperType.PredefinedType    | PredefinedType : optional IfcVibrationDamperTypeEnum | PredefinedType : IfcVibrationDamperTypeEnum |

### Constraints

9 items

| Name                               | IFC4x3_RC4_43c3555.exp                                                                                  | IFC.exp                                                                 |
|------------------------------------|---------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| IfcBuildingSystem where rules      | []                                                                                                      | ['CorrectPredefinedType']                                               |
| IfcRailway where rules             | ['HasObjectType']                                                                                       | ['HasObjectType', 'CorrectPredefinedType']                              |
| IfcRoad where rules                | ['HasObjectType']                                                                                       | ['HasObjectType', 'CorrectPredefinedType']                              |
| IfcSectionedSurface where rules    | ['DirectrixIs3D', 'AreaProfileTypes', 'SectionsSameType', 'CorrespondingSectionPositions', 'NoOffsets'] | []                                                                      |
| IfcSurfaceFeature where rules      | ['HasObjectType']                                                                                       | ['HasObjectType', 'CorrectPredefinedType']                              |
| IfcVibrationDamper where rules     | ['CorrectPredefinedType', 'CorrectTypeAssigned']                                                        | []                                                                      |
| IfcVibrationDamperType where rules | ['CorrectPredefinedType']                                                                               | []                                                                      |
| IfcVibrationIsolator where rules   | ['CorrectPredefinedType', 'CorrectTypeAssigned']                                                        | ['CorrectPredefinedType', 'CorrectTypeAssigned', 'CorrectTypeAssigned'] |
| IfcVoidingFeature where rules      | ['HasObjectType']                                                                                       | ['HasObjectType', 'CorrectPredefinedType']                              |
