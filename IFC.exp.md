# Express schema differences

13 items

### Entity

8 items

| Name                                     | IFC4x3_RC4.exp                                                                                                                             | IFC.exp                                                                                                                    |
|------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| IfcComplexPropertyTemplate attributes    | ['UsageName', 'TemplateType', 'HasPropertyTemplates']                                                                                      | ['UsageName', 'HasPropertyTemplates']                                                                                      |
| IfcPropertyEnumeration.EnumerationValues | EnumerationValues : list[1:?] of unique IfcValue                                                                                           | EnumerationValues : list[1:?] of IfcValue                                                                                  |
| IfcPropertySetTemplate attributes        | ['TemplateType', 'ApplicableEntity', 'HasPropertyTemplates']                                                                               | ['ApplicableEntity', 'HasPropertyTemplates']                                                                               |
| IfcPropertyTableValue.DefiningValues     | DefiningValues : optional list[1:?] of unique IfcValue                                                                                     | DefiningValues : optional list[1:?] of IfcValue                                                                            |
| IfcRelDefinesByProperties attributes     | ['RelatedObjects', 'RelatingPropertyDefinition']                                                                                           | ['RelatingPropertyDefinition', 'RelatedObjects']                                                                           |
| IfcRelDefinesByProperties.RelatedObjects | RelatedObjects : set[1:?] of IfcObjectDefinition                                                                                           | RelatedObjects : IfcContext                                                                                                |
| IfcSimplePropertyTemplate attributes     | ['TemplateType', 'PrimaryMeasureType', 'SecondaryMeasureType', 'Enumerators', 'PrimaryUnit', 'SecondaryUnit', 'Expression', 'AccessState'] | ['PrimaryMeasureType', 'SecondaryMeasureType', 'Enumerators', 'PrimaryUnit', 'SecondaryUnit', 'Expression', 'AccessState'] |
| IfcSurfaceFeature.AdheresToElement       | AdheresToElement : IfcRelAdheresToElement FOR RelatedSurfaceFeature                                                                        | AdheresToElement : IfcRelAdheresToElement FOR RelatedSurfaceFeatures                                                       |
### Where

5 items

| Name                          | IFC4x3_RC4.exp    | IFC.exp                                    |
|-------------------------------|-------------------|--------------------------------------------|
| IfcBuildingSystem where rules | []                | ['CorrectPredefinedType']                  |
| IfcRailway where rules        | ['HasObjectType'] | ['HasObjectType', 'CorrectPredefinedType'] |
| IfcRoad where rules           | ['HasObjectType'] | ['HasObjectType', 'CorrectPredefinedType'] |
| IfcSurfaceFeature where rules | ['HasObjectType'] | ['HasObjectType', 'CorrectPredefinedType'] |
| IfcVoidingFeature where rules | ['HasObjectType'] | ['HasObjectType', 'CorrectPredefinedType'] |
