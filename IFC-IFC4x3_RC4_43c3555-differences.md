# Express schema differences

12 items


### Missing data

:tada: No issues :tada:


### Type definitions

1 items

| Name                   | IFC4x3_RC4_43c3555.exp                                                                                                                                                                           | IFC.exp                                                                                                                                                                                         |
|------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IfcRailwayPartTypeEnum | DILATATIONSUPERSTRUCTURE, LINESIDESTRUCTURE, LINESIDESTRUCTUREPART, NOTDEFINED, PLAINTRACKSUPERSTRUCTURE, SUPERSTRUCTURE, TRACKSTRUCTURE, TRACKSTRUCTUREPART, TURNOUTSUPERSTRUCTURE, USERDEFINED | DILATATIONSUPERSTRUCTURE, LINESIDESTRUCTURE, LINESIDESTRUCTUREPART, NOTDEFINED, PLAINTRACKSUPESTRUCTURE, SUPERSTRUCTURE, TRACKSTRUCTURE, TRACKSTRUCTUREPART, TURNOUTSUPERSTRUCTURE, USERDEFINED |

### Entity definitions

5 items

| Name                                      | IFC4x3_RC4_43c3555.exp                                                                                          | IFC.exp                                                                      |
|-------------------------------------------|-----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| IfcOpenCrossProfileDef attributes         | ['HorizontalWidths', 'Widths', 'Slopes', 'Tags', 'OffsetPoint']                                                 | ['HorizontalWidths', 'Widths', 'Slopes', 'Tags']                             |
| IfcSectionedSolidHorizontal attributes    | ['CrossSectionPositions']                                                                                       | ['CrossSectionPositions', 'FixedAxisVertical']                               |
| IfcSectionedSurface attributes            | ['Directrix', 'CrossSectionPositions', 'CrossSections']                                                         | ['Directrix', 'CrossSectionPositions', 'CrossSections', 'FixedAxisVertical'] |
| IfcSectionedSurface.CrossSectionPositions | CrossSectionPositions : list[2:?] of IfcAxis2PlacementLinear                                                    | CrossSectionPositions : list[2:?] of IfcPointByDistanceExpression            |
| IfcSpatialElement inverses                | ['ContainsElements', 'ServicedBySystems', 'ReferencesElements', 'IsInterferedByElements', 'InterferesElements'] | ['ContainsElements', 'ServicedBySystems', 'ReferencesElements']              |

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
