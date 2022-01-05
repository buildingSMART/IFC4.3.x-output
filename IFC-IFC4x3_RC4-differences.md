# Express schema differences

14 items


### Missing data

2 items

| Name          | IFC4x3_RC4.exp          | IFC.exp          |
|---------------|-------------------------|------------------|
| IfcPlant      |                         | not in 'IFC.exp' |
| IfcVegetation | not in 'IFC4x3_RC4.exp' |                  |

### Type definitions

1 items

| Name                           | IFC4x3_RC4.exp                                                                                                                                                            | IFC.exp    |
|--------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| IfcPropertySetTemplateTypeEnum | NOTDEFINED, PSET_OCCURRENCEDRIVEN, PSET_PERFORMANCEDRIVEN, PSET_TYPEDRIVENONLY, PSET_TYPEDRIVENOVERRIDE, QTO_OCCURRENCEDRIVEN, QTO_TYPEDRIVENONLY, QTO_TYPEDRIVENOVERRIDE | NOTDEFINED |

### Entity definitions

6 items

| Name                                      | IFC4x3_RC4.exp                                                               | IFC.exp                                                                                                         |
|-------------------------------------------|------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| IfcOpenCrossProfileDef attributes         | ['HorizontalWidths', 'Widths', 'Slopes', 'Tags']                             | ['HorizontalWidths', 'Widths', 'Slopes', 'Tags', 'OffsetPoint']                                                 |
| IfcProperty attributes                    | ['Name', 'Description']                                                      | ['Name', 'Specification']                                                                                       |
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
