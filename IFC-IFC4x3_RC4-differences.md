# Express schema differences

11 items


### Missing data

:tada: No issues :tada:


### Type definitions

1 items

| Name                   | IFC4x3_RC4.exp                                                                                                                                                                                  | IFC.exp                                                                                                                                                                                          |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IfcRailwayPartTypeEnum | DILATATIONSUPERSTRUCTURE, LINESIDESTRUCTURE, LINESIDESTRUCTUREPART, NOTDEFINED, PLAINTRACKSUPESTRUCTURE, SUPERSTRUCTURE, TRACKSTRUCTURE, TRACKSTRUCTUREPART, TURNOUTSUPERSTRUCTURE, USERDEFINED | DILATATIONSUPERSTRUCTURE, LINESIDESTRUCTURE, LINESIDESTRUCTUREPART, NOTDEFINED, PLAINTRACKSUPERSTRUCTURE, SUPERSTRUCTURE, TRACKSTRUCTURE, TRACKSTRUCTUREPART, TURNOUTSUPERSTRUCTURE, USERDEFINED |

### Entity definitions

5 items

| Name                                      | IFC4x3_RC4.exp                                                               | IFC.exp                                                                                                         |
|-------------------------------------------|------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| IfcOpenCrossProfileDef attributes         | ['HorizontalWidths', 'Widths', 'Slopes', 'Tags']                             | ['HorizontalWidths', 'Widths', 'Slopes', 'Tags', 'OffsetPoint']                                                 |
| IfcSectionedSolidHorizontal attributes    | ['CrossSectionPositions', 'FixedAxisVertical']                               | ['CrossSectionPositions']                                                                                       |
| IfcSectionedSurface attributes            | ['Directrix', 'CrossSectionPositions', 'CrossSections', 'FixedAxisVertical'] | ['Directrix', 'CrossSectionPositions', 'CrossSections']                                                         |
| IfcSectionedSurface.CrossSectionPositions | CrossSectionPositions : list[2:?] of IfcPointByDistanceExpression            | CrossSectionPositions : list[2:?] of IfcAxis2PlacementLinear                                                    |
| IfcSpatialElement inverses                | ['ContainsElements', 'ServicedBySystems', 'ReferencesElements']              | ['ContainsElements', 'ServicedBySystems', 'ReferencesElements', 'IsInterferedByElements', 'InterferesElements'] |

### Constraints

5 items

| Name                          | IFC4x3_RC4.exp    | IFC.exp                                    |
|-------------------------------|-------------------|--------------------------------------------|
| IfcBuildingSystem where rules | []                | ['CorrectPredefinedType']                  |
| IfcRailway where rules        | ['HasObjectType'] | ['HasObjectType', 'CorrectPredefinedType'] |
| IfcRoad where rules           | ['HasObjectType'] | ['HasObjectType', 'CorrectPredefinedType'] |
| IfcSurfaceFeature where rules | ['HasObjectType'] | ['HasObjectType', 'CorrectPredefinedType'] |
| IfcVoidingFeature where rules | ['HasObjectType'] | ['HasObjectType', 'CorrectPredefinedType'] |
