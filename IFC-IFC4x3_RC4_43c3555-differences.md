# Express schema differences

11 items


### Missing data

2 items

| Name          | IFC4x3_RC4_43c3555.exp          | IFC.exp          |
|---------------|---------------------------------|------------------|
| IfcPlant      |                                 | not in 'IFC.exp' |
| IfcVegetation | not in 'IFC4x3_RC4_43c3555.exp' |                  |

### Type definitions

2 items

| Name                           | IFC4x3_RC4_43c3555.exp                                                                                                                                                                           | IFC.exp                                                                                                                                                                                         |
|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IfcPropertySetTemplateTypeEnum | NOTDEFINED, PSET_OCCURRENCEDRIVEN, PSET_PERFORMANCEDRIVEN, PSET_TYPEDRIVENONLY, PSET_TYPEDRIVENOVERRIDE, QTO_OCCURRENCEDRIVEN, QTO_TYPEDRIVENONLY, QTO_TYPEDRIVENOVERRIDE                        | NOTDEFINED                                                                                                                                                                                      |
| IfcRailwayPartTypeEnum         | DILATATIONSUPERSTRUCTURE, LINESIDESTRUCTURE, LINESIDESTRUCTUREPART, NOTDEFINED, PLAINTRACKSUPERSTRUCTURE, SUPERSTRUCTURE, TRACKSTRUCTURE, TRACKSTRUCTUREPART, TURNOUTSUPERSTRUCTURE, USERDEFINED | DILATATIONSUPERSTRUCTURE, LINESIDESTRUCTURE, LINESIDESTRUCTUREPART, NOTDEFINED, PLAINTRACKSUPESTRUCTURE, SUPERSTRUCTURE, TRACKSTRUCTURE, TRACKSTRUCTUREPART, TURNOUTSUPERSTRUCTURE, USERDEFINED |

### Entity definitions

1 items

| Name                   | IFC4x3_RC4_43c3555.exp   | IFC.exp                   |
|------------------------|--------------------------|---------------------------|
| IfcProperty attributes | ['Name', 'Description']  | ['Name', 'Specification'] |

### Constraints

6 items

| Name                            | IFC4x3_RC4_43c3555.exp                                                                                  | IFC.exp                                    |
|---------------------------------|---------------------------------------------------------------------------------------------------------|--------------------------------------------|
| IfcBuildingSystem where rules   | []                                                                                                      | ['CorrectPredefinedType']                  |
| IfcRailway where rules          | ['HasObjectType']                                                                                       | ['HasObjectType', 'CorrectPredefinedType'] |
| IfcRoad where rules             | ['HasObjectType']                                                                                       | ['HasObjectType', 'CorrectPredefinedType'] |
| IfcSectionedSurface where rules | ['DirectrixIs3D', 'AreaProfileTypes', 'SectionsSameType', 'CorrespondingSectionPositions', 'NoOffsets'] | []                                         |
| IfcSurfaceFeature where rules   | ['HasObjectType']                                                                                       | ['HasObjectType', 'CorrectPredefinedType'] |
| IfcVoidingFeature where rules   | ['HasObjectType']                                                                                       | ['HasObjectType', 'CorrectPredefinedType'] |
