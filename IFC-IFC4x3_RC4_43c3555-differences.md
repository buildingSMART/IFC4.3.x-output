# Express schema differences

6 items


### Missing data

:tada: No issues :tada:


### Type definitions

:tada: No issues :tada:


### Entity definitions

:tada: No issues :tada:


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
