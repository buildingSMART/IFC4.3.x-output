# Express schema differences

5 items


### Missing data

:tada: No issues :tada:


### Type definitions

:tada: No issues :tada:


### Entity definitions

:tada: No issues :tada:


### Constraints

5 items

| Name                          | IFC4x3_RC4.exp    | IFC.exp                                    |
|-------------------------------|-------------------|--------------------------------------------|
| IfcBuildingSystem where rules | []                | ['CorrectPredefinedType']                  |
| IfcRailway where rules        | ['HasObjectType'] | ['HasObjectType', 'CorrectPredefinedType'] |
| IfcRoad where rules           | ['HasObjectType'] | ['HasObjectType', 'CorrectPredefinedType'] |
| IfcSurfaceFeature where rules | ['HasObjectType'] | ['HasObjectType', 'CorrectPredefinedType'] |
| IfcVoidingFeature where rules | ['HasObjectType'] | ['HasObjectType', 'CorrectPredefinedType'] |
