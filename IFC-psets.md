
Missing in output
=================
* Pset_RailwayAlignmentCommon.xml
* Pset_RoadSymbolsCommon.xml
* Pset_TrafficCalmingDeviceCommon.xml
* Pset_SolidStratumCapacity.xml
* Pset_OutletTypeCommunication.xml
* Pset_Stationing.xml
* Pset_LinearReferencingMethod.xml
* Pset_DoorTypeTurnstile.xml
* Pset_RailJoint_Welded.xml
* Pset_PlantCommon.xml
* Pset_SolidStratumComposition.xml
* Pset_GeotechnicalAssemblyCommon.xml
* Pset_RailJoint.xml
* Pset_RoadMarkingCommon.xml
* Pset_MarkingLinesCommon.xml
* Pset_Sleeper.xml
* Pset_WaterStratumCommon.xml
* Pset_SensorTypeIdentifierSensor.xml
* Pset_SpatialZoneCommon.xml
* Pset_RailwaySignGeneral.xml
* Pset_BoreholeCommon.xml
* Pset_BridgeCommon.xml
* Pset_RailwayPowerSupplyFacility.xml
* Pset_RailwayEnergyReservation.xml
* PSet_ElementKinematics.xml
* Pset_MarineFacilityTransportation.xml
* Pset_RoadGuardElement.xml
* Pset_Uncertainty.xml
* Pset_ReferentCommon.xml
* Pset_CivilElementCommon.xml
* Pset_ElementAssemblyCommon.xml
* Pset_PavementCommon.xml
* Pset_SumpBusterCommon.xml
* Pset_RailwaySignalGeneral.xml
* Pset_DiscretizedPointListCommon.xml
* Pset_RailwayReservation.xml
* Pset_VoltageAndCurrentTransformer.xml
* Pset_GeotechnicalStratumCommon.xml
* Pset_MaintenanceStrategy.xml
* Pset_CableConduitGeneral.xml
* Pset_AudioVisualApplianceTypeRailwayCommunicationTerminal.xml
* Pset_TransponderGeneral.xml
* Pset_MechanicalFastener.xml
* Pset_SensorTypeFrostSensor.xml

Missing in reference
=================
* Pset_ElementKinematics.xml

Pset_WindowCommon.xml
=====================

modifications
-------------
* PropertyDefs > PropertyDef [Name="AcousticRating"] > Definition "Acoustic rating for this object.
It is provided according to the national building code. It indicates the sound transmission resistance of this object by an index ratio (instead of providing full sound absorbtion values)."
  ~~Acoustic rating for this object.
It is provided according to the national building code. It indicates the sound transmission resistance of this object by an index ratio (instead of providing full sound absorbtion values).~~ Acoustic rating for this object.\X\0D
It is provided according to the national building code. It indicates the sound transmission resistance of this object by an index ratio (instead of providing full sound absorbtion values).
* PropertyDefs > PropertyDef [Name="FireRating"] > Definition "Fire rating for this object.
It is given according to the national fire safety classification."
  ~~Fire rating for this object.
It is given according to the national fire safety classification.~~ Fire rating for this object.\X\0D
It is given according to the national fire safety classification.
* PropertyDefs > PropertyDef [Name="GlazingAreaFraction"] > Definition "Fraction of the glazing area relative to the total area of the filling element. 
It shall be used, if the glazing area is not given separately for all panels within the filling element."
  ~~Fraction of the glazing area relative to the total area of the filling element. 
It shall be used, if the glazing area is not given separately for all panels within the filling element.~~ Fraction of the glazing area relative to the total area of the filling element. \X\0D
It shall be used, if the glazing area is not given separately for all panels within the filling element.
* PropertyDefs > PropertyDef [Name="MechanicalLoadRating"] > Definition "Mechanical load rating for this object.
It is provided according to the national building code."
  ~~Mechanical load rating for this object.
It is provided according to the national building code.~~ Mechanical load rating for this object.\X\0D
It is provided according to the national building code.
* PropertyDefs > PropertyDef [Name="SecurityRating"] > Definition "Index based rating system indicating security level.
It is giving according to the national building code."
  ~~Index based rating system indicating security level.
It is giving according to the national building code.~~ Index based rating system indicating security level.\X\0D
It is giving according to the national building code.
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="ThermalTransmittance"] > Definition "Thermal transmittance coefficient (U-Value) of a material.
It applies to the total door construction."
  ~~Thermal transmittance coefficient (U-Value) of a material.
It applies to the total door construction.~~ Thermal transmittance coefficient (U-Value) of a material.\X\0D
It applies to the total door construction.
* PropertyDefs > PropertyDef [Name="WaterTightnessRating"] > Definition "Water tightness rating for this object.
It is provided according to the national building code."
  ~~Water tightness rating for this object.
It is provided according to the national building code.~~ Water tightness rating for this object.\X\0D
It is provided according to the national building code.
* PropertyDefs > PropertyDef [Name="WindLoadRating"] > Definition "Wind load resistance rating for this object.
It is provided according to the national building code."
  ~~Wind load resistance rating for this object.
It is provided according to the national building code.~~ Wind load resistance rating for this object.\X\0D
It is provided according to the national building code.
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_LightFixtureTypeCommon.xml
===============================

modifications
-------------
* Definition "Common data for light fixtures.
History: IFC4 - Article number and manufacturer specific information deleted. Use Pset_ManufacturerTypeInformation. ArticleNumber instead.   Load properties moved from Pset_LightFixtureTypeThermal (deleted)."
  ~~Common data for light fixtures.
History: IFC4 - Article number and manufacturer specific information deleted. Use Pset_ManufacturerTypeInformation. ArticleNumber instead.   Load properties moved from Pset_LightFixtureTypeThermal (deleted).~~ Common data for light fixtures.\X\0D
History: IFC4 - Article number and manufacturer specific information deleted. Use Pset_ManufacturerTypeInformation. ArticleNumber instead.   Load properties moved from Pset_LightFixtureTypeThermal (deleted).
* PropertyDefs > PropertyDef [Name="LightFixtureMountingType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="LightFixturePlacingType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="LightFixturePlacingType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="LightFixtureMountingType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Qto_ProtectiveDeviceBaseQuantities.xml
======================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Pset_ControllerTypeTwoPosition.xml
==================================

additions
---------
* ApplicableClasses
* ApplicableClasses
* ApplicableClasses

modifications
-------------
* PropertyDefs
  ~~PropertyDefs~~ ApplicableClasses
* ApplicableClasses
  ~~ApplicableClasses~~ PropertyDefs
* ApplicableClasses > ClassName "IfcController/TWOPOSITION"
  ~~&lt;ClassName&gt;~~ &lt;PropertyDef&gt;


Pset_DistributionPortTypeCable.xml
==================================

additions
---------
* PropertyDefs > PropertyDef [Name="Current"]

modifications
-------------
* PropertyDefs > PropertyDef [Name="ConnectionType"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Voltage"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="ConnectionGender"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Protocols"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="ConductorFunction"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="ConnectionSubtype"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Power"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="Current"]


Pset_ControllerTypeMultiPosition.xml
====================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Labels"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="ControlType"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Range"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Value"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Pset_DiscreteAccessoryWireLoop.xml
==================================

modifications
-------------
* ApplicableClasses > ClassName "IfcDiscreteAccessory/Wire loop"
  ~~IfcDiscreteAccessory/Wire loop~~ IfcDiscreteAccessory
* ApplicableTypeValue "IfcDiscreteAccessory/Wire loop"
  ~~IfcDiscreteAccessory/Wire loop~~ IfcDiscreteAccessory


Pset_CableCarrierFittingTypeCommon.xml
======================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_VesselLineCommon.xml
=========================

modifications
-------------
* ApplicableTypeValue "IfcMechanicalFastener/ROPE,IfcMechanicalFastenerType/ROPE"
  ~~IfcMechanicalFastener/ROPE,IfcMechanicalFastenerType/ROPE~~ IfcMechanicalFastenerType
* ApplicableClasses > ClassName "IfcMechanicalFastenerType/ROPE"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcMechanicalFastener/ROPE"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;


Pset_CommunicationsApplianceTypeCommon.xml
==========================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_HeatExchangerTypeCommon.xml
================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Arrangement"] > Definition "Defines the basic flow arrangements for the heat exchanger:

COUNTERFLOW: Counterflow heat exchanger arrangement. 
CROSSFLOW: Crossflow heat exchanger arrangement. 
PARALLELFLOW: Parallel flow heat exchanger arrangement. 
MULTIPASS: Multipass flow heat exchanger arrangement. 
OTHER: Other type of heat exchanger flow arrangement not defined above."
  ~~Defines the basic flow arrangements for the heat exchanger:

COUNTERFLOW: Counterflow heat exchanger arrangement. 
CROSSFLOW: Crossflow heat exchanger arrangement. 
PARALLELFLOW: Parallel flow heat exchanger arrangement. 
MULTIPASS: Multipass flow heat exchanger arrangement. 
OTHER: Other type of heat exchanger flow arrangement not defined above.~~ Defines the basic flow arrangements for the heat exchanger:\X\0D
\X\0D
COUNTERFLOW: Counterflow heat exchanger arrangement. \X\0D
CROSSFLOW: Crossflow heat exchanger arrangement. \X\0D
PARALLELFLOW: Parallel flow heat exchanger arrangement. \X\0D
MULTIPASS: Multipass flow heat exchanger arrangement. \X\0D
OTHER: Other type of heat exchanger flow arrangement not defined above.
* PropertyDefs > PropertyDef [Name="Arrangement"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Arrangement"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_CableCarrierSegmentTypeCableTrunkingSegment.xml
====================================================

modifications
-------------
* Definition "An enclosed carrier segment with one or more compartments into which cables are placed.
HISTORY: IFC4 - NominalLength deleted. To be handled as a quantity measure"
  ~~An enclosed carrier segment with one or more compartments into which cables are placed.
HISTORY: IFC4 - NominalLength deleted. To be handled as a quantity measure~~ An enclosed carrier segment with one or more compartments into which cables are placed.\X\0D
HISTORY: IFC4 - NominalLength deleted. To be handled as a quantity measure

deletions
---------
* PropertyDefs > PropertyDef [Name="NominalWidth"]




Pset_AirTerminalBoxTypeCommon.xml
=================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="AirflowRateRange"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="AirPressureRange"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="ArrangementType"] > Definition "Terminal box arrangement.
SingleDuct: Terminal box receives warm or cold air from a single air supply duct.
DualDuct: Terminal box receives warm and cold air from separate air supply ducts."
  ~~Terminal box arrangement.
SingleDuct: Terminal box receives warm or cold air from a single air supply duct.
DualDuct: Terminal box receives warm and cold air from separate air supply ducts.~~ Terminal box arrangement.\X\0D
SingleDuct: Terminal box receives warm or cold air from a single air supply duct.\X\0D
DualDuct: Terminal box receives warm and cold air from separate air supply ducts.
* PropertyDefs > PropertyDef [Name="ArrangementType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="OperationTemperatureRange"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="ReheatType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="ReturnAirFractionRange"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="ReheatType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="ArrangementType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_Asset.xml
==============

modifications
-------------
* PropertyDefs > PropertyDef [Name="AssetAccountingType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="AssetInsuranceType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="AssetTaxType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="AssetAccountingType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="AssetInsuranceType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="AssetTaxType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Qto_VibrationIsolatorBaseQuantities.xml
=======================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Pset_ServiceLifeFactors.xml
===========================

modifications
-------------
* 
  ~~PSET_OCCURRENCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="OutdoorEnvironment"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="IndoorEnvironment"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="MaintenanceLevel"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="InUseConditions"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="DesignLevel"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="QualityOfComponents"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="WorkExecutionLevel"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;



Qto_ElectricFlowStorageDeviceBaseQuantities.xml
===============================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Pset_ProtectiveDeviceOccurrence.xml
===================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="LongTimeFunction"] > Definition "Applying long time function
A flag indicating that the long time function (i.e. the thermal tripping) of the device is used. The value should be set to TRUE for all devices except those that allows the Long time function of the device not to be used."
  ~~Applying long time function
A flag indicating that the long time function (i.e. the thermal tripping) of the device is used. The value should be set to TRUE for all devices except those that allows the Long time function of the device not to be used.~~ Applying long time function\X\0D
A flag indicating that the long time function (i.e. the thermal tripping) of the device is used. The value should be set to TRUE for all devices except those that allows the Long time function of the device not to be used.
* PropertyDefs > PropertyDef [Name="PoleUsage"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="ShortTimei2tFunction"] > Definition "Applying short time i2t function. A flag indicating that the I2t short time function of the device is used. The value should be set to TRUE only if the I2t function &#160;is explicitly selected for the device."
  ~~Applying short time i2t function. A flag indicating that the I2t short time function of the device is used. The value should be set to TRUE only if the I2t function &#160;is explicitly selected for the device.~~ Applying short time i2t function. A flag indicating that the I2t short time function of the device is used. The value should be set to TRUE only if the I2t function \S\ is explicitly selected for the device.
* 
  ~~PSET_OCCURRENCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="PoleUsage"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_DistributionChamberElementTypeInspectionChamber.xml
========================================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="AccessCoverMaterial"] > Definition "The material from which the access cover to the chamber is constructed.
NOTE: It is assumed that chamber walls will be constructed of a single material."
  ~~The material from which the access cover to the chamber is constructed.
NOTE: It is assumed that chamber walls will be constructed of a single material.~~ The material from which the access cover to the chamber is constructed.\X\0D
NOTE: It is assumed that chamber walls will be constructed of a single material.
* PropertyDefs > PropertyDef [Name="BaseMaterial"] > Definition "The material from which the base of the chamber is constructed.
NOTE: It is assumed that chamber base will be constructed of a single material."
  ~~The material from which the base of the chamber is constructed.
NOTE: It is assumed that chamber base will be constructed of a single material.~~ The material from which the base of the chamber is constructed.\X\0D
NOTE: It is assumed that chamber base will be constructed of a single material.
* PropertyDefs > PropertyDef [Name="BaseThickness"] > Definition "The thickness of the chamber base construction
NOTE: It is assumed that chamber base will be constructed at a single thickness."
  ~~The thickness of the chamber base construction
NOTE: It is assumed that chamber base will be constructed at a single thickness.~~ The thickness of the chamber base construction\X\0D
NOTE: It is assumed that chamber base will be constructed at a single thickness.
* PropertyDefs > PropertyDef [Name="WallMaterial"] > Definition "The material from which the wall of the chamber is constructed.
NOTE: It is assumed that chamber walls will be constructed of a single material."
  ~~The material from which the wall of the chamber is constructed.
NOTE: It is assumed that chamber walls will be constructed of a single material.~~ The material from which the wall of the chamber is constructed.\X\0D
NOTE: It is assumed that chamber walls will be constructed of a single material.
* PropertyDefs > PropertyDef [Name="WallThickness"] > Definition "The thickness of the chamber wall construction
NOTE: It is assumed that chamber walls will be constructed at a single thickness."
  ~~The thickness of the chamber wall construction
NOTE: It is assumed that chamber walls will be constructed at a single thickness.~~ The thickness of the chamber wall construction\X\0D
NOTE: It is assumed that chamber walls will be constructed at a single thickness.

deletions
---------
* PropertyDefs > PropertyDef [Name="AccessCoverMaterial"] > PropertyType
* PropertyDefs > PropertyDef [Name="BaseMaterial"] > PropertyType
* PropertyDefs > PropertyDef [Name="WallMaterial"] > PropertyType


Pset_BoilerPHistory.xml
=======================

modifications
-------------
* Definition "Boiler performance history common attributes.
WaterQuality attribute deleted in IFC2x2 Pset Addendum: Use IfcWaterProperties instead. CombustionProductsMaximulLoad and CombustionProductsPartialLoad attributes deleted in IFC2x2 Pset Addendum: Use IfcProductsOfCombustionProperties instead."
  ~~Boiler performance history common attributes.
WaterQuality attribute deleted in IFC2x2 Pset Addendum: Use IfcWaterProperties instead. CombustionProductsMaximulLoad and CombustionProductsPartialLoad attributes deleted in IFC2x2 Pset Addendum: Use IfcProductsOfCombustionProperties instead.~~ Boiler performance history common attributes.\X\0D
WaterQuality attribute deleted in IFC2x2 Pset Addendum: Use IfcWaterProperties instead. CombustionProductsMaximulLoad and CombustionProductsPartialLoad attributes deleted in IFC2x2 Pset Addendum: Use IfcProductsOfCombustionProperties instead.
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="AuxiliaryEnergyConsumption"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="WorkingPressure"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="CombustionTemperature"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="PartLoadRatio"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="PrimaryEnergyConsumption"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="OperationalEfficiency"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="CombustionEfficiency"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Load"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="EnergySourceConsumption"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Pset_DuctSegmentTypeCommon.xml
==============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="PressureRange"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Shape"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="TemperatureRange"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Shape"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Qto_AirTerminalBoxTypeBaseQuantities.xml
========================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Pset_CompressorTypeCommon.xml
=============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="PowerSource"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="RefrigerantClass"] > Definition "Refrigerant class used by the compressor.

CFC: Chlorofluorocarbons.
HCFC: Hydrochlorofluorocarbons.
HFC: Hydrofluorocarbons."
  ~~Refrigerant class used by the compressor.

CFC: Chlorofluorocarbons.
HCFC: Hydrochlorofluorocarbons.
HFC: Hydrofluorocarbons.~~ Refrigerant class used by the compressor.\X\0D
\X\0D
CFC: Chlorofluorocarbons.\X\0D
HCFC: Hydrochlorofluorocarbons.\X\0D
HFC: Hydrofluorocarbons.
* PropertyDefs > PropertyDef [Name="RefrigerantClass"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="RefrigerantClass"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="PowerSource"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_BoilerTypeSteam.xml
========================

additions
---------
* ApplicableClasses
* ApplicableClasses

modifications
-------------
* PropertyDefs
  ~~PropertyDefs~~ ApplicableClasses
* ApplicableClasses
  ~~ApplicableClasses~~ PropertyDefs
* ApplicableClasses > ClassName "IfcBoiler/STEAM"
  ~~&lt;ClassName&gt;~~ &lt;PropertyDef&gt;


Pset_DistributionPortTypeDuct.xml
=================================

additions
---------
* PropertyDefs > PropertyDef [Name="ConnectionType"]

modifications
-------------
* PropertyDefs > PropertyDef [Name="NominalThickness"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="WetBulbTemperature"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="DryBulbTemperature"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="VolumetricFlowRate"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="NominalWidth"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="ConnectionType"]
* PropertyDefs > PropertyDef [Name="Velocity"]
* PropertyDefs > PropertyDef [Name="Pressure"]


Pset_SensorTypeLevelSensor.xml
==============================

modifications
-------------
* ApplicableClasses > ClassName "IfcSensor/LEVEL"
  ~~IfcSensor/LEVEL~~ IfcSensor
* ApplicableTypeValue "IfcSensor/LEVEL"
  ~~IfcSensor/LEVEL~~ IfcSensor
* PropertyDefs > PropertyDef [Name="SetPointLevel"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue


Pset_EnvironmentalImpactIndicators.xml
======================================

modifications
-------------
* Definition "Environmental impact indicators are related to a given &#8220;functional unit&#8221; (ISO 14040 concept). An example of functional unit is a "Double glazing window with PVC frame" and the unit to consider is "one square meter of opening elements filled by this product&#8221;.
Indicators values are valid for the whole life cycle or only a specific phase (see LifeCyclePhase property). Values of all the indicators are expressed per year according to the expected service life. The first five properties capture the characteristics of the functional unit. The following properties are related to environmental indicators.
There is a consensus agreement international for the five one. Last ones are not yet fully and formally agreed at the international level."
  ~~Environmental impact indicators are related to a given &#8220;functional unit&#8221; (ISO 14040 concept). An example of functional unit is a "Double glazing window with PVC frame" and the unit to consider is "one square meter of opening elements filled by this product&#8221;.
Indicators values are valid for the whole life cycle or only a specific phase (see LifeCyclePhase property). Values of all the indicators are expressed per year according to the expected service life. The first five properties capture the characteristics of the functional unit. The following properties are related to environmental indicators.
There is a consensus agreement international for the five one. Last ones are not yet fully and formally agreed at the international level.~~ Environmental impact indicators are related to a given \X2\201C\X0\functional unit\X2\201D\X0\ (ISO 14040 concept). An example of functional unit is a "Double glazing window with PVC frame" and the unit to consider is "one square meter of opening elements filled by this product\X2\201D\X0\.\X\0D
Indicators values are valid for the whole life cycle or only a specific phase (see LifeCyclePhase property). Values of all the indicators are expressed per year according to the expected service life. The first five properties capture the characteristics of the functional unit. The following properties are related to environmental indicators.\X\0D
There is a consensus agreement international for the five one. Last ones are not yet fully and formally agreed at the international level.
* PropertyDefs > PropertyDef [Name="LifeCyclePhase"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="LifeCyclePhase"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_DistributionChamberElementTypeValveChamber.xml
===================================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="AccessCoverMaterial"] > Definition "The material from which the access cover to the chamber is constructed.
NOTE: It is assumed that chamber walls will be constructed of a single material."
  ~~The material from which the access cover to the chamber is constructed.
NOTE: It is assumed that chamber walls will be constructed of a single material.~~ The material from which the access cover to the chamber is constructed.\X\0D
NOTE: It is assumed that chamber walls will be constructed of a single material.
* PropertyDefs > PropertyDef [Name="BaseMaterial"] > Definition "The material from which the base of the chamber is constructed.
NOTE: It is assumed that chamber base will be constructed of a single material."
  ~~The material from which the base of the chamber is constructed.
NOTE: It is assumed that chamber base will be constructed of a single material.~~ The material from which the base of the chamber is constructed.\X\0D
NOTE: It is assumed that chamber base will be constructed of a single material.
* PropertyDefs > PropertyDef [Name="BaseThickness"] > Definition "The thickness of the chamber base construction.
NOTE: It is assumed that chamber base will be constructed at a single thickness."
  ~~The thickness of the chamber base construction.
NOTE: It is assumed that chamber base will be constructed at a single thickness.~~ The thickness of the chamber base construction.\X\0D
NOTE: It is assumed that chamber base will be constructed at a single thickness.
* PropertyDefs > PropertyDef [Name="WallMaterial"] > Definition "The material from which the wall of the chamber is constructed.
NOTE: It is assumed that chamber walls will be constructed of a single material."
  ~~The material from which the wall of the chamber is constructed.
NOTE: It is assumed that chamber walls will be constructed of a single material.~~ The material from which the wall of the chamber is constructed.\X\0D
NOTE: It is assumed that chamber walls will be constructed of a single material.
* PropertyDefs > PropertyDef [Name="WallThickness"] > Definition "The thickness of the chamber wall construction.
NOTE: It is assumed that chamber walls will be constructed at a single thickness."
  ~~The thickness of the chamber wall construction.
NOTE: It is assumed that chamber walls will be constructed at a single thickness.~~ The thickness of the chamber wall construction.\X\0D
NOTE: It is assumed that chamber walls will be constructed at a single thickness.

deletions
---------
* PropertyDefs > PropertyDef [Name="AccessCoverMaterial"] > PropertyType
* PropertyDefs > PropertyDef [Name="BaseMaterial"] > PropertyType
* PropertyDefs > PropertyDef [Name="WallMaterial"] > PropertyType


Pset_RailingCommon.xml
======================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Diameter"] > Definition "Diameter of the object. It is the diameter of the handrail of the railing.
The size information is provided in addition to the shape representation and the geometric parameters used within. In cases of inconsistency between the geometric parameters and the size properties, provided in the attached property set, the geometric parameters take precedence.
Here the diameter of the hand or guardrail within the railing."
  ~~Diameter of the object. It is the diameter of the handrail of the railing.
The size information is provided in addition to the shape representation and the geometric parameters used within. In cases of inconsistency between the geometric parameters and the size properties, provided in the attached property set, the geometric parameters take precedence.
Here the diameter of the hand or guardrail within the railing.~~ Diameter of the object. It is the diameter of the handrail of the railing.\X\0D
The size information is provided in addition to the shape representation and the geometric parameters used within. In cases of inconsistency between the geometric parameters and the size properties, provided in the attached property set, the geometric parameters take precedence.\X\0D
Here the diameter of the hand or guardrail within the railing.
* PropertyDefs > PropertyDef [Name="Height"] > Definition "Height of the object. It is the upper hight of the railing above the floor or stair.
The size information is provided in addition to the shape representation and the geometric parameters used within. In cases of inconsistency between the geometric parameters and the size properties, provided in the attached property set, the geometric parameters take precedence."
  ~~Height of the object. It is the upper hight of the railing above the floor or stair.
The size information is provided in addition to the shape representation and the geometric parameters used within. In cases of inconsistency between the geometric parameters and the size properties, provided in the attached property set, the geometric parameters take precedence.~~ Height of the object. It is the upper hight of the railing above the floor or stair.\X\0D
The size information is provided in addition to the shape representation and the geometric parameters used within. In cases of inconsistency between the geometric parameters and the size properties, provided in the attached property set, the geometric parameters take precedence.
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_PrecastConcreteElementGeneral.xml
======================================

modifications
-------------
* ApplicableTypeValue "IfcBeam,IfcBuildingElementProxy,IfcChimney,IfcColumn,IfcFooting,IfcMember,IfcPile,IfcPlate,IfcRamp,IfcRampFlight,IfcRoof,IfcSlab,IfcStair,IfcStairFlight,IfcWall,IfcCivilElement"
  ~~IfcBeam,IfcBuildingElementProxy,IfcChimney,IfcColumn,IfcFooting,IfcMember,IfcPile,IfcPlate,IfcRamp,IfcRampFlight,IfcRoof,IfcSlab,IfcStair,IfcStairFlight,IfcWall,IfcCivilElement~~ IfcCivilElement
* PropertyDefs > PropertyDef [Name="DesignLocationNumber"] > Definition "Defines a unique location within a structure, the &#8216;slot&#8217; for which the piece was designed."
  ~~Defines a unique location within a structure, the &#8216;slot&#8217; for which the piece was designed.~~ Defines a unique location within a structure, the \X2\2018\X0\slot\X2\2019\X0\ for which the piece was designed.
* PropertyDefs > PropertyDef [Name="PieceMark"] > Definition "Defines a unique piece for production purposes. All pieces with the same piece mark value are identical and interchangeable. The piece mark may be composed of sub-parts that have specific locally defined meaning (e.g. B-1A may denote a beam, of generic type &#8216;1&#8217; and specific shape &#8216;A&#8217;)."
  ~~Defines a unique piece for production purposes. All pieces with the same piece mark value are identical and interchangeable. The piece mark may be composed of sub-parts that have specific locally defined meaning (e.g. B-1A may denote a beam, of generic type &#8216;1&#8217; and specific shape &#8216;A&#8217;).~~ Defines a unique piece for production purposes. All pieces with the same piece mark value are identical and interchangeable. The piece mark may be composed of sub-parts that have specific locally defined meaning (e.g. B-1A may denote a beam, of generic type \X2\2018\X0\1\X2\2019\X0\ and specific shape \X2\2018\X0\A\X2\2019\X0\).
* PropertyDefs > PropertyDef [Name="Twisting"] > Definition "The angle, in radians, through which the end face of a precast piece is rotated with respect to its starting face, along its longitudinal axis, as a result of non-aligned supports. This measure is also termed the &#8216;warping&#8217; angle."
  ~~The angle, in radians, through which the end face of a precast piece is rotated with respect to its starting face, along its longitudinal axis, as a result of non-aligned supports. This measure is also termed the &#8216;warping&#8217; angle.~~ The angle, in radians, through which the end face of a precast piece is rotated with respect to its starting face, along its longitudinal axis, as a result of non-aligned supports. This measure is also termed the \X2\2018\X0\warping\X2\2019\X0\ angle.

deletions
---------
* PropertyDefs > PropertyDef [Name="SupportDuringTransportDocReference"] > PropertyType
* PropertyDefs > PropertyDef [Name="TypeDesignation"]


Pset_CooledBeamPHistoryActive.xml
=================================

modifications
-------------
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="Throw"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="AirFlowRate"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="AirPressureDropCurves"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Pset_RevetmentCommon.xml
========================

modifications
-------------
* ApplicableClasses > ClassName "IfcMarineFacility/REVETMENT"
  ~~IfcMarineFacility/REVETMENT~~ IfcMarineFacility
* ApplicableTypeValue "IfcMarineFacility/REVETMENT"
  ~~IfcMarineFacility/REVETMENT~~ IfcMarineFacility


Qto_FilterBaseQuantities.xml
============================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Pset_CableSegmentTypeCableSegment.xml
=====================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="RatedTemperature"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="RatedVoltage"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue


Qto_EarthworksFillBaseQuantities.xml
====================================

additions
---------
* Definition "$"

modifications
-------------
* QtoDefinitionAliases
  ~~QtoDefinitionAliases~~ ApplicableTypeValue
* QtoDefs > QtoDef [Name="Width"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Length"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefs > QtoDef [Name="Depth"]
* QtoDefs > QtoDef [Name="CompactedVolume"]
* QtoDefs > QtoDef [Name="LooseVolume"]


Pset_ProtectiveDeviceTrippingCurve.xml
======================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="TrippingCurve"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="TrippingCurveType"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Pset_SensorTypeIonConcentrationSensor.xml
=========================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="SetPointConcentration"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="SubstanceDetected"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;



Pset_MemberCommon.xml
=====================

modifications
-------------
* PropertyDefs > PropertyDef [Name="FireRating"] > Definition "Fire rating for this object.
It is given according to the national fire safety classification."
  ~~Fire rating for this object.
It is given according to the national fire safety classification.~~ Fire rating for this object.\X\0D
It is given according to the national fire safety classification.
* PropertyDefs > PropertyDef [Name="Roll"] > Definition "Rotation against the longitudinal axis - relative to the global Z direction for all members that are non-vertical in regard to the global coordinate system (Profile direction equals global Z is Roll = 0.)
The shape information is provided in addition to the shape representation and the geometric parameters used within. In cases of inconsistency between the geometric parameters and the shape properties, provided in the attached property, the geometric parameters take precedence.
Note: new property in IFC4."
  ~~Rotation against the longitudinal axis - relative to the global Z direction for all members that are non-vertical in regard to the global coordinate system (Profile direction equals global Z is Roll = 0.)
The shape information is provided in addition to the shape representation and the geometric parameters used within. In cases of inconsistency between the geometric parameters and the shape properties, provided in the attached property, the geometric parameters take precedence.
Note: new property in IFC4.~~ Rotation against the longitudinal axis - relative to the global Z direction for all members that are non-vertical in regard to the global coordinate system (Profile direction equals global Z is Roll = 0.)\X\0D
The shape information is provided in addition to the shape representation and the geometric parameters used within. In cases of inconsistency between the geometric parameters and the shape properties, provided in the attached property, the geometric parameters take precedence.\X\0D
Note: new property in IFC4.
* PropertyDefs > PropertyDef [Name="Slope"] > Definition "Slope angle - relative to horizontal (0.0 degrees).
The shape information is provided in addition to the shape representation and the geometric parameters used within. In cases of inconsistency between the geometric parameters and the shape properties, provided in the attached property, the geometric parameters take precedence."
  ~~Slope angle - relative to horizontal (0.0 degrees).
The shape information is provided in addition to the shape representation and the geometric parameters used within. In cases of inconsistency between the geometric parameters and the shape properties, provided in the attached property, the geometric parameters take precedence.~~ Slope angle - relative to horizontal (0.0 degrees).\X\0D
The shape information is provided in addition to the shape representation and the geometric parameters used within. In cases of inconsistency between the geometric parameters and the shape properties, provided in the attached property, the geometric parameters take precedence.
* PropertyDefs > PropertyDef [Name="Span"] > Definition "Clear span for this object.
The shape information is provided in addition to the shape representation and the geometric parameters used within. In cases of inconsistency between the geometric parameters and the shape properties, provided in the attached property, the geometric parameters take precedence."
  ~~Clear span for this object.
The shape information is provided in addition to the shape representation and the geometric parameters used within. In cases of inconsistency between the geometric parameters and the shape properties, provided in the attached property, the geometric parameters take precedence.~~ Clear span for this object.\X\0D
The shape information is provided in addition to the shape representation and the geometric parameters used within. In cases of inconsistency between the geometric parameters and the shape properties, provided in the attached property, the geometric parameters take precedence.
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="ThermalTransmittance"] > Definition "Thermal transmittance coefficient (U-Value) of a material.
Here the total thermal transmittance coefficient through the member within the direction of the thermal flow (including all materials).
Note: new property in IFC4."
  ~~Thermal transmittance coefficient (U-Value) of a material.
Here the total thermal transmittance coefficient through the member within the direction of the thermal flow (including all materials).
Note: new property in IFC4.~~ Thermal transmittance coefficient (U-Value) of a material.\X\0D
Here the total thermal transmittance coefficient through the member within the direction of the thermal flow (including all materials).\X\0D
Note: new property in IFC4.
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_AudioVisualApplianceTypeReceiver.xml
=========================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="AudioAmplification"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="ReceiverType"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="AudioMode"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;




Qto_JunctionBoxBaseQuantities.xml
=================================

modifications
-------------
* QtoDefs > QtoDef [Name="GrossWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NumberOfGangs"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases


Pset_PumpOccurrence.xml
=======================

modifications
-------------
* PropertyDefs > PropertyDef [Name="BaseType"] > Definition "Defines general types of pump bases.

FRAME: Frame. 
BASE: Base. 
NONE: There is no pump base, such as an inline pump. 
OTHER: Other type of pump base."
  ~~Defines general types of pump bases.

FRAME: Frame. 
BASE: Base. 
NONE: There is no pump base, such as an inline pump. 
OTHER: Other type of pump base.~~ Defines general types of pump bases.\X\0D
\X\0D
FRAME: Frame. \X\0D
BASE: Base. \X\0D
NONE: There is no pump base, such as an inline pump. \X\0D
OTHER: Other type of pump base.
* PropertyDefs > PropertyDef [Name="BaseType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="DriveConnectionType"] > Definition "The way the pump drive mechanism is connected to the pump.

DIRECTDRIVE: Direct drive. 
BELTDRIVE: Belt drive. 
COUPLING: Coupling. 
OTHER: Other type of drive connection."
  ~~The way the pump drive mechanism is connected to the pump.

DIRECTDRIVE: Direct drive. 
BELTDRIVE: Belt drive. 
COUPLING: Coupling. 
OTHER: Other type of drive connection.~~ The way the pump drive mechanism is connected to the pump.\X\0D
\X\0D
DIRECTDRIVE: Direct drive. \X\0D
BELTDRIVE: Belt drive. \X\0D
COUPLING: Coupling. \X\0D
OTHER: Other type of drive connection.
* PropertyDefs > PropertyDef [Name="DriveConnectionType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* 
  ~~PSET_OCCURRENCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="DriveConnectionType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="BaseType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_Superelevation.xml
=======================

modifications
-------------
* ApplicableClasses > ClassName "IfcAnnotation/(.SUPERELEVATIONEVENT.)"
  ~~IfcAnnotation/(.SUPERELEVATIONEVENT.)~~ IfcSpace
* ApplicableTypeValue "IfcAnnotation/(.SUPERELEVATIONEVENT.)"
  ~~IfcAnnotation/(.SUPERELEVATIONEVENT.)~~ IfcSpace
* PropertyDefs > PropertyDef [Name="Side"] > Name "Side"
  ~~&lt;Name&gt;~~ &lt;Name&gt;
* PropertyDefs > PropertyDef [Name="Side"] > PropertyType
  ~~&lt;PropertyType&gt;~~ &lt;PropertyType&gt;
* PropertyDefs > PropertyDef [Name="Side"] > Definition "Specifies if the width is measured to the RIGHT or to the LEFT of the curve referenced by the placement, or if the same value is applied to BOTH sides."
  ~~&lt;Definition&gt;~~ &lt;Definition&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="TransitionSuperelevation"]


Pset_RoadDesignCriteriaCommon.xml
=================================

additions
---------
* ApplicableTypeValue

modifications
-------------
* PropertyDefs > PropertyDef [Name="DesignSpeed"] > Definition "Speed selected in designing a new road or in modernizing, strengthening or rehabilitating an existing road section, to determine the various geometric design features of the carriageway that allow a car to travel safely at that speed, under normal road surface and weather conditions. 

>NOTE&nbsp; Definition according to PIARC. 
>
>NOTE&nbsp; The design speed is not constant, but may vary depending on the conditions of relief (plain, hill, mountain)."
  ~~Speed selected in designing a new road or in modernizing, strengthening or rehabilitating an existing road section, to determine the various geometric design features of the carriageway that allow a car to travel safely at that speed, under normal road surface and weather conditions. 

>NOTE&nbsp; Definition according to PIARC. 
>
>NOTE&nbsp; The design speed is not constant, but may vary depending on the conditions of relief (plain, hill, mountain).~~ Speed selected in designing a new road or in modernizing, strengthening or rehabilitating an existing road section, to determine the various geometric design features of the carriageway that allow a car to travel safely at that speed, under normal road surface and weather conditions. \X\0D
\X\0D
>NOTE&#160; Definition according to PIARC. \X\0D
>\X\0D
>NOTE&#160; The design speed is not constant, but may vary depending on the conditions of relief (plain, hill, mountain).


Pset_DistributionBoardTypeCommon.xml
====================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Qto_FlowInstrumentBaseQuantities.xml
====================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Pset_PavementSurfaceCommon.xml
==============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="PavementTexture"] > Definition "Characterization of pavement texture by mean profile depth

>NOTE&nbsp; Definition according to ISO 13473-1:2019"
  ~~Characterization of pavement texture by mean profile depth

>NOTE&nbsp; Definition according to ISO 13473-1:2019~~ Characterization of pavement texture by mean profile depth\X\0D
\X\0D
>NOTE&#160; Definition according to ISO 13473-1:2019


Pset_MaterialWoodBasedBeam.xml
==============================

modifications
-------------
* Definition "This is a collection of mechanical properties applicable to wood-based materials for beam-like products, especially laminated materials like glulam and LVL.
Anisotropy of such materials is taken into account by different properties according to grain direction and load types.

All values shall be given for a standardized service condition, a standardized load duration and a standardized reference size of the member according to local design codes.

NOTE: In cases where mechanical material properties are graduated for different given reference sizes, separate instances of IfcExtendedMaterialProperties and IfcMaterial have to be used for each required graduation. Mechanically differing versions of a material are treated as different materials.

References to the orientation of grain or lay-up correspond to material orientation given by geometrical or topological representation of element objects or types, especially IfcMemberType and IfcStructuralMember."
  ~~This is a collection of mechanical properties applicable to wood-based materials for beam-like products, especially laminated materials like glulam and LVL.
Anisotropy of such materials is taken into account by different properties according to grain direction and load types.

All values shall be given for a standardized service condition, a standardized load duration and a standardized reference size of the member according to local design codes.

NOTE: In cases where mechanical material properties are graduated for different given reference sizes, separate instances of IfcExtendedMaterialProperties and IfcMaterial have to be used for each required graduation. Mechanically differing versions of a material are treated as different materials.

References to the orientation of grain or lay-up correspond to material orientation given by geometrical or topological representation of element objects or types, especially IfcMemberType and IfcStructuralMember.~~ This is a collection of mechanical properties applicable to wood-based materials for beam-like products, especially laminated materials like glulam and LVL.\X\0D
Anisotropy of such materials is taken into account by different properties according to grain direction and load types.\X\0D
\X\0D
All values shall be given for a standardized service condition, a standardized load duration and a standardized reference size of the member according to local design codes.\X\0D
\X\0D
NOTE: In cases where mechanical material properties are graduated for different given reference sizes, separate instances of IfcExtendedMaterialProperties and IfcMaterial have to be used for each required graduation. Mechanically differing versions of a material are treated as different materials.\X\0D
\X\0D
References to the orientation of grain or lay-up correspond to material orientation given by geometrical or topological representation of element objects or types, especially IfcMemberType and IfcStructuralMember.
* ApplicableClasses > ClassName "IfcMaterial/Wood"
  ~~IfcMaterial/Wood~~ IfcMaterial
* ApplicableTypeValue "IfcMaterial/Wood"
  ~~IfcMaterial/Wood~~ IfcMaterial

deletions
---------
* PropertyDefs > PropertyDef [Name="InPlane"] > PropertyType
* PropertyDefs > PropertyDef [Name="InPlaneNegative"] > PropertyType
* PropertyDefs > PropertyDef [Name="OutOfPlane"] > PropertyType


Qto_LampBaseQuantities.xml
==========================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Pset_ProtectiveDeviceTrippingUnitTypeElectroMagnetic.xml
========================================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="ElectroMagneticTrippingUnitType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="ElectroMagneticTrippingUnitType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_AlignmentVerticalSegmentCommon.xml
=======================================

modifications
-------------
* 
  ~~PSET_OCCURRENCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE


Pset_UnitaryEquipmentTypeAirConditioningUnit.xml
================================================

modifications
-------------
* Definition "Air conditioning unit equipment type attributes.
Note that these attributes were formely Pset_PackagedACUnit prior to IFC2x2.
HeatingEnergySource attribute deleted in IFC2x2 Pset Addendum: Use IfcEnergyProperties, IfcFuelProperties, etc. instead."
  ~~Air conditioning unit equipment type attributes.
Note that these attributes were formely Pset_PackagedACUnit prior to IFC2x2.
HeatingEnergySource attribute deleted in IFC2x2 Pset Addendum: Use IfcEnergyProperties, IfcFuelProperties, etc. instead.~~ Air conditioning unit equipment type attributes.\X\0D
Note that these attributes were formely Pset_PackagedACUnit prior to IFC2x2.\X\0D
HeatingEnergySource attribute deleted in IFC2x2 Pset Addendum: Use IfcEnergyProperties, IfcFuelProperties, etc. instead.


Qto_ActuatorBaseQuantities.xml
==============================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Pset_EngineTypeCommon.xml
=========================

modifications
-------------
* PropertyDefs > PropertyDef [Name="EnergySource"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="EnergySource"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_DuctFittingPHistory.xml
============================

modifications
-------------
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="LossCoefficient"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="AtmosphericPressure"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="AirFlowLeakage"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Pset_TankTypeCommon.xml
=======================

modifications
-------------
* PropertyDefs > PropertyDef [Name="AccessType"] > Definition "Defines the types of access (or cover) to a tank that may be specified.

Note that covers are generally specified for rectangular tanks. For cylindrical tanks, access will normally be via a manhole."
  ~~Defines the types of access (or cover) to a tank that may be specified.

Note that covers are generally specified for rectangular tanks. For cylindrical tanks, access will normally be via a manhole.~~ Defines the types of access (or cover) to a tank that may be specified.\X\0D
\X\0D
Note that covers are generally specified for rectangular tanks. For cylindrical tanks, access will normally be via a manhole.
* PropertyDefs > PropertyDef [Name="AccessType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="EndShapeType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="NominalWidthOrDiameter"] > Definition "The nominal width or, in the case of a horizontal cylindrical tank, the nominal diameter of the tank.

Note: Not required for a vertical cylindrical tank."
  ~~The nominal width or, in the case of a horizontal cylindrical tank, the nominal diameter of the tank.

Note: Not required for a vertical cylindrical tank.~~ The nominal width or, in the case of a horizontal cylindrical tank, the nominal diameter of the tank.\X\0D
\X\0D
Note: Not required for a vertical cylindrical tank.
* PropertyDefs > PropertyDef [Name="NumberOfSections"] > Definition "Number of sections used in the construction of the tank. Default is 1.

Note: All sections assumed to be the same size."
  ~~Number of sections used in the construction of the tank. Default is 1.

Note: All sections assumed to be the same size.~~ Number of sections used in the construction of the tank. Default is 1.\X\0D
\X\0D
Note: All sections assumed to be the same size.
* PropertyDefs > PropertyDef [Name="PatternType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="StorageType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="AccessType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="StorageType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="EndShapeType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="PatternType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_DistributionPortPHistoryDuct.xml
=====================================

modifications
-------------
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="Pressure"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="VolumetricFlowRate"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Velocity"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Temperature"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="MassFlowRate"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="FlowCondition"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="WetBulbTemperature"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Pset_StructuralSurfaceMemberVaryingThickness.xml
================================================

additions
---------
* PropertyDefs > PropertyDef [Name="Location2Local"]

modifications
-------------
* PropertyDefs > PropertyDef [Name="Location3Global"] > PropertyType
  ~~&lt;PropertyType&gt;~~ &lt;PropertyType&gt;
* PropertyDefs > PropertyDef [Name="Location3Global"] > Name "Location3Global"
  ~~&lt;Name&gt;~~ &lt;Name&gt;
* PropertyDefs > PropertyDef [Name="Location1Local"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Location2Local"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Location3Global"] > Definition "Global X,Y,Z coordinates of the point in which Thickness3 is given"
  ~~&lt;Definition&gt;~~ &lt;Definition&gt;
* PropertyDefs > PropertyDef [Name="Location1Global"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Location2Global"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="Location3Local"]


Pset_AudioVisualApplianceTypePlayer.xml
=======================================

additions
---------
* ApplicableClasses
* ApplicableClasses

modifications
-------------
* PropertyDefs
  ~~PropertyDefs~~ ApplicableClasses
* ApplicableClasses
  ~~ApplicableClasses~~ PropertyDefs
* ApplicableClasses > ClassName "IfcAudioVisualAppliance/PLAYER"
  ~~&lt;ClassName&gt;~~ &lt;PropertyDef&gt;


Qto_RampFlightBaseQuantities.xml
================================

modifications
-------------
* QtoDefs > QtoDef [Name="NetVolume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossVolume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Width"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Length"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases


Pset_DamperOccurrence.xml
=========================

modifications
-------------
* PropertyDefs > PropertyDef [Name="SizingMethod"] > Definition "Identifies whether the damper is sized nominally or with exact measurements:

NOMINAL: Nominal sizing method. 
EXACT: Exact sizing method."
  ~~Identifies whether the damper is sized nominally or with exact measurements:

NOMINAL: Nominal sizing method. 
EXACT: Exact sizing method.~~ Identifies whether the damper is sized nominally or with exact measurements:\X\0D
\X\0D
NOMINAL: Nominal sizing method. \X\0D
EXACT: Exact sizing method.
* PropertyDefs > PropertyDef [Name="SizingMethod"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* 
  ~~PSET_OCCURRENCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="SizingMethod"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_KerbStone.xml
==================

modifications
-------------
* PropertyDefs > PropertyDef [Name="StoneFinishes"] > Definition "Eg. 'Polished', 'Bush Hammered', 'Split', 'Sawn', 'Flamed'"
  ~~Eg. 'Polished', 'Bush Hammered', 'Split', 'Sawn', 'Flamed'~~ Eg. 'Polished', 'Bush Hammered', 'Split', 'Sawn', 'Flamed'',

deletions
---------
* PropertyDefs > PropertyDef [Name="NominalLength"]
* PropertyDefs > PropertyDef [Name="NominalWidth"]


Pset_LampTypeCommon.xml
=======================

modifications
-------------
* Definition "A lamp is a component within a light fixture that is designed to emit light. 

History: Name changed from Pset_LampEmitterTypeCommon in IFC 2x3."
  ~~A lamp is a component within a light fixture that is designed to emit light. 

History: Name changed from Pset_LampEmitterTypeCommon in IFC 2x3.~~ A lamp is a component within a light fixture that is designed to emit light. \X\0D
\X\0D
History: Name changed from Pset_LampEmitterTypeCommon in IFC 2x3.
* PropertyDefs > PropertyDef [Name="LampBallastType"] > Definition "The type of ballast used to stabilise gas discharge by limiting the current during operation and to deliver the necessary striking voltage for starting. Ballasts are needed to operate Discharge Lamps such as Fluorescent, Compact Fluorescent, High-pressure Mercury, Metal Halide and High-pressure Sodium Lamps. 
Magnetic ballasts are chokes which limit the current passing through a lamp connected in series on the principle of self-induction. The resultant current and power are decisive for the efficient operation of the lamp. A specially designed ballast is required for every type of lamp to comply with lamp rating in terms of Luminous Flux, Color Appearance and service life. The two types of magnetic ballasts for fluorescent lamps are KVG Conventional   (EC-A series) and VVG Low-loss ballasts (EC-B series). Low-loss ballasts have a higher efficiency, which means reduced ballast losses and a lower thermal load. Electronic ballasts are used to run fluorescent lamps at high frequencies (approx. 35 - 40 kHz)."
  ~~The type of ballast used to stabilise gas discharge by limiting the current during operation and to deliver the necessary striking voltage for starting. Ballasts are needed to operate Discharge Lamps such as Fluorescent, Compact Fluorescent, High-pressure Mercury, Metal Halide and High-pressure Sodium Lamps. 
Magnetic ballasts are chokes which limit the current passing through a lamp connected in series on the principle of self-induction. The resultant current and power are decisive for the efficient operation of the lamp. A specially designed ballast is required for every type of lamp to comply with lamp rating in terms of Luminous Flux, Color Appearance and service life. The two types of magnetic ballasts for fluorescent lamps are KVG Conventional   (EC-A series) and VVG Low-loss ballasts (EC-B series). Low-loss ballasts have a higher efficiency, which means reduced ballast losses and a lower thermal load. Electronic ballasts are used to run fluorescent lamps at high frequencies (approx. 35 - 40 kHz).~~ The type of ballast used to stabilise gas discharge by limiting the current during operation and to deliver the necessary striking voltage for starting. Ballasts are needed to operate Discharge Lamps such as Fluorescent, Compact Fluorescent, High-pressure Mercury, Metal Halide and High-pressure Sodium Lamps. \X\0D
Magnetic ballasts are chokes which limit the current passing through a lamp connected in series on the principle of self-induction. The resultant current and power are decisive for the efficient operation of the lamp. A specially designed ballast is required for every type of lamp to comply with lamp rating in terms of Luminous Flux, Color Appearance and service life. The two types of magnetic ballasts for fluorescent lamps are KVG Conventional   (EC-A series) and VVG Low-loss ballasts (EC-B series). Low-loss ballasts have a higher efficiency, which means reduced ballast losses and a lower thermal load. Electronic ballasts are used to run fluorescent lamps at high frequencies (approx. 35 - 40 kHz).
* PropertyDefs > PropertyDef [Name="LampBallastType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="LampCompensationType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Spectrum"] > PropertyType > TypePropertyTableValue
  ~~TypePropertyTableValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="LampCompensationType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="Spectrum"] > PropertyType > TypePropertyTableValue > Expression
  ~~&lt;Expression&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="LampBallastType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="Spectrum"] > PropertyType > TypePropertyTableValue > DefiningValue
* PropertyDefs > PropertyDef [Name="Spectrum"] > PropertyType > TypePropertyTableValue > DefinedValue


Pset_UtilityConsumptionPHistory.xml
===================================

modifications
-------------
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="Electricity"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Steam"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Water"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Heat"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Fuel"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Qto_CommunicationsApplianceBaseQuantities.xml
=============================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Pset_PlateCommon.xml
====================

modifications
-------------
* PropertyDefs > PropertyDef [Name="AcousticRating"] > Definition "Acoustic rating for this object.
It is provided according to the national building code. It indicates the sound transmission resistance of this object by an index ratio (instead of providing full sound absorbtion values)."
  ~~Acoustic rating for this object.
It is provided according to the national building code. It indicates the sound transmission resistance of this object by an index ratio (instead of providing full sound absorbtion values).~~ Acoustic rating for this object.\X\0D
It is provided according to the national building code. It indicates the sound transmission resistance of this object by an index ratio (instead of providing full sound absorbtion values).
* PropertyDefs > PropertyDef [Name="FireRating"] > Definition "Fire rating for this object.
It is given according to the national fire safety classification."
  ~~Fire rating for this object.
It is given according to the national fire safety classification.~~ Fire rating for this object.\X\0D
It is given according to the national fire safety classification.
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="ThermalTransmittance"] > Definition "Thermal transmittance coefficient (U-Value) of a material.
It applies to the total door construction."
  ~~Thermal transmittance coefficient (U-Value) of a material.
It applies to the total door construction.~~ Thermal transmittance coefficient (U-Value) of a material.\X\0D
It applies to the total door construction.
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_ControllerTypeCommon.xml
=============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_AnnotationLineOfSight.xml
==============================

modifications
-------------
* ApplicableClasses > ClassName "IfcAnnotation/LineOfSight"
  ~~IfcAnnotation/LineOfSight~~ IfcAnnotation
* ApplicableTypeValue "IfcAnnotation/LineOfSight"
  ~~IfcAnnotation/LineOfSight~~ IfcAnnotation


Pset_FireSuppressionTerminalTypeHoseReel.xml
============================================

modifications
-------------
* Definition "A supporting framework on which a hose may be wound (BS6100 155 8201).

Note that the service provided by the hose (water/foam) is determined by the context of the system onto which the hose reel is connected."
  ~~A supporting framework on which a hose may be wound (BS6100 155 8201).

Note that the service provided by the hose (water/foam) is determined by the context of the system onto which the hose reel is connected.~~ A supporting framework on which a hose may be wound (BS6100 155 8201).\X\0D
\X\0D
Note that the service provided by the hose (water/foam) is determined by the context of the system onto which the hose reel is connected.
* PropertyDefs > PropertyDef [Name="HoseNozzleType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="HoseReelMountingType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="HoseReelType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="HoseReelType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="HoseNozzleType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="HoseReelMountingType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;



Pset_CourseCommon.xml
=====================

deletions
---------
* PropertyDefs > PropertyDef [Name="NominalLength"]
* PropertyDefs > PropertyDef [Name="NominalWidth"]


Pset_DamperTypeFireSmokeDamper.xml
==================================

modifications
-------------
* Definition "Combination Fire and Smoke damper type attributes.
New Pset in IFC2x2 Pset Addendum."
  ~~Combination Fire and Smoke damper type attributes.
New Pset in IFC2x2 Pset Addendum.~~ Combination Fire and Smoke damper type attributes.\X\0D
New Pset in IFC2x2 Pset Addendum.
* PropertyDefs > PropertyDef [Name="ActuationType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="ClosureRatingEnum"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="ActuationType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="ClosureRatingEnum"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_FireSuppressionTerminalTypeCommon.xml
==========================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Qto_SlabBaseQuantities.xml
==========================

modifications
-------------
* QtoDefs > QtoDef [Name="GrossArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Length"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetVolume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Width"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossVolume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Perimeter"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Depth"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases


Pset_AirToAirHeatRecoveryTypeCommon.xml
=======================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="HeatTransferTypeEnum"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="OperationalTemperatureRange"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="PrimaryAirflowRateRange"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="SecondaryAirflowRateRange"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="HeatTransferTypeEnum"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_UnitaryControlElementTypeCommon.xml
========================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Mode"] > PropertyType > TypePropertyTableValue
  ~~TypePropertyTableValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Mode"] > PropertyType > TypePropertyTableValue > Expression
  ~~&lt;Expression&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="Mode"] > PropertyType > TypePropertyTableValue > DefiningValue
* PropertyDefs > PropertyDef [Name="Mode"] > PropertyType > TypePropertyTableValue > DefinedValue


Pset_QuayDesignCriteria.xml
===========================

modifications
-------------
* ApplicableClasses > ClassName "IfcMarineFacility/QUAY"
  ~~IfcMarineFacility/QUAY~~ IfcMarineFacility
* ApplicableTypeValue "IfcMarineFacility/QUAY"
  ~~IfcMarineFacility/QUAY~~ IfcMarineFacility


Qto_RoofBaseQuantities.xml
==========================

modifications
-------------
* QtoDefs > QtoDef [Name="NetArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="ProjectedArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases


Pset_FenderCommon.xml
=====================

modifications
-------------
* ApplicableTypeValue "IfcImpactProtectionDevice/IfcImpactProtectionDeviceTypeEnum(.FENDER.),IfcImpactProtectionDeviceType/IfcImpactProtectionDeviceTypeEnum(.FENDER.)"
  ~~IfcImpactProtectionDevice/IfcImpactProtectionDeviceTypeEnum(.FENDER.),IfcImpactProtectionDeviceType/IfcImpactProtectionDeviceTypeEnum(.FENDER.)~~ IfcFastener
* ApplicableClasses > ClassName "IfcImpactProtectionDevice/IfcImpactProtectionDeviceTypeEnum(.FENDER.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* PropertyDefs > PropertyDef [Name="FenderType"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;

deletions
---------
* ApplicableClasses > ClassName "IfcImpactProtectionDeviceType/IfcImpactProtectionDeviceTypeEnum(.FENDER.)"
* PropertyDefs > PropertyDef [Name="CoefficientOfFriction"]
* PropertyDefs > PropertyDef [Name="EnergyAbsorptionTolerance"]
* PropertyDefs > PropertyDef [Name="MaxReactionTolerance"]
* PropertyDefs > PropertyDef [Name="MaximumTemperatureFactor"]
* PropertyDefs > PropertyDef [Name="MinimumTemperatureFactor"]
* PropertyDefs > PropertyDef [Name="VelocityFactorEnergy"]
* PropertyDefs > PropertyDef [Name="VelocityFactorReaction"]
* PropertyDefs > PropertyDef [Name="EnergyAbsorption"]
* PropertyDefs > PropertyDef [Name="MaxReaction"]


Qto_MotorConnectionBaseQuantities.xml
=====================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Pset_ControllerTypeProgrammable.xml
===================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Application"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="ControlType"] > Definition "The type of discrete digital controller: 

PRIMARY: Controller has built-in communication interface for PC connection, may manage secondary controllers.
SECONDARY: Controller communicates with primary controller and its own managed devices."
  ~~The type of discrete digital controller: 

PRIMARY: Controller has built-in communication interface for PC connection, may manage secondary controllers.
SECONDARY: Controller communicates with primary controller and its own managed devices.~~ The type of discrete digital controller: \X\0D
\X\0D
PRIMARY: Controller has built-in communication interface for PC connection, may manage secondary controllers.\X\0D
SECONDARY: Controller communicates with primary controller and its own managed devices.
* PropertyDefs > PropertyDef [Name="ControlType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="ControlType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="Application"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_ManufacturerOccurrence.xml
===============================

modifications
-------------
* Definition "Defines properties of individual instances of manufactured products that may be given by the manufacturer.
HISTORY: IFC 2x4: AssemblyPlace property added. This property does not need to be asserted if Pset_ManufacturerTypeInformation is allocated to the type and the AssemblyPlace property is asserted there."
  ~~Defines properties of individual instances of manufactured products that may be given by the manufacturer.
HISTORY: IFC 2x4: AssemblyPlace property added. This property does not need to be asserted if Pset_ManufacturerTypeInformation is allocated to the type and the AssemblyPlace property is asserted there.~~ Defines properties of individual instances of manufactured products that may be given by the manufacturer.\X\0D
HISTORY: IFC 2x4: AssemblyPlace property added. This property does not need to be asserted if Pset_ManufacturerTypeInformation is allocated to the type and the AssemblyPlace property is asserted there.
* PropertyDefs > PropertyDef [Name="AssemblyPlace"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* 
  ~~PSET_OCCURRENCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="AssemblyPlace"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Qto_BuildingStoreyBaseQuantities.xml
====================================

modifications
-------------
* QtoDefs > QtoDef [Name="GrossHeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossPerimeter"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetHeigtht"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossFloorArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetFloorArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossVolume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetVolume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases


Pset_CommunicationsAppliancePHistory.xml
========================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="PowerState"] > PropertyType > TypePropertyReferenceValue
  ~~TypePropertyReferenceValue~~ TypePropertySingleValue
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE


Pset_WasteTerminalTypeGullyTrap.xml
===================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="BackInletPatternType"] > Definition "Identifies the pattern of inlet connections to a gully trap.

A gulley trap may have 0,1,2,3 or 4 inlet connections and the pattern of their arrangement may vary. The enumeration makes the convention that an outlet is either vertical or is placed at the bottom (south side) of the gully trap (when viewed in plan). Position 1 is to the left (west), position 2 is to the top (north), position 3 is to the right (east) and position 4 is to the bottom (south)."
  ~~Identifies the pattern of inlet connections to a gully trap.

A gulley trap may have 0,1,2,3 or 4 inlet connections and the pattern of their arrangement may vary. The enumeration makes the convention that an outlet is either vertical or is placed at the bottom (south side) of the gully trap (when viewed in plan). Position 1 is to the left (west), position 2 is to the top (north), position 3 is to the right (east) and position 4 is to the bottom (south).~~ Identifies the pattern of inlet connections to a gully trap.\X\0D
\X\0D
A gulley trap may have 0,1,2,3 or 4 inlet connections and the pattern of their arrangement may vary. The enumeration makes the convention that an outlet is either vertical or is placed at the bottom (south side) of the gully trap (when viewed in plan). Position 1 is to the left (west), position 2 is to the top (north), position 3 is to the right (east) and position 4 is to the bottom (south).
* PropertyDefs > PropertyDef [Name="BackInletPatternType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="GullyType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="InletConnectionSize"] > Definition "Size of the inlet connection(s), where used, of the inlet connections.

Note that all inlet connections are assumed to be the same size."
  ~~Size of the inlet connection(s), where used, of the inlet connections.

Note that all inlet connections are assumed to be the same size.~~ Size of the inlet connection(s), where used, of the inlet connections.\X\0D
\X\0D
Note that all inlet connections are assumed to be the same size.
* PropertyDefs > PropertyDef [Name="TrapType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="BackInletPatternType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="GullyType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="TrapType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_ActuatorTypeRotationalActuation.xml
========================================

modifications
-------------
* Definition "Characteristics of rotational actuation of an actuator
History: Replaces Pset_RotationalActuator"
  ~~Characteristics of rotational actuation of an actuator
History: Replaces Pset_RotationalActuator~~ Characteristics of rotational actuation of an actuator\X\0D
History: Replaces Pset_RotationalActuator


Pset_MedicalDeviceTypeCommon.xml
================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_FireSuppressionTerminalTypeFireHydrant.xml
===============================================

modifications
-------------
* Definition "Device, fitted to a pipe, through which a temporary supply of water may be provided (BS6100 330 6107)

For further details on fire hydrants, see www.firehydrant.org"
  ~~Device, fitted to a pipe, through which a temporary supply of water may be provided (BS6100 330 6107)

For further details on fire hydrants, see www.firehydrant.org~~ Device, fitted to a pipe, through which a temporary supply of water may be provided (BS6100 330 6107)\X\0D
\X\0D
For further details on fire hydrants, see www.firehydrant.org
* PropertyDefs > PropertyDef [Name="BodyColor"] > Definition "Color of the body of the hydrant.

Note: Consult local fire regulations for statutory colors that may be required for hydrant bodies in particular circumstances."
  ~~Color of the body of the hydrant.

Note: Consult local fire regulations for statutory colors that may be required for hydrant bodies in particular circumstances.~~ Color of the body of the hydrant.\X\0D
\X\0D
Note: Consult local fire regulations for statutory colors that may be required for hydrant bodies in particular circumstances.
* PropertyDefs > PropertyDef [Name="CapColor"] > Definition "Color of the caps of the hydrant.

Note: Consult local fire regulations for statutory colors that may be required for hydrant caps in particular circumstances."
  ~~Color of the caps of the hydrant.

Note: Consult local fire regulations for statutory colors that may be required for hydrant caps in particular circumstances.~~ Color of the caps of the hydrant.\X\0D
\X\0D
Note: Consult local fire regulations for statutory colors that may be required for hydrant caps in particular circumstances.
* PropertyDefs > PropertyDef [Name="FireHydrantType"] > Definition "Defines the range of hydrant types from which the required type can be selected where.

DryBarrel:	 A hydrant that has isolating valves fitted below ground and that may be used where the possibility of water freezing is a consideration.
WetBarrel:	 A hydrant that has isolating valves fitted above ground and that may be used where there is no possibility of water freezing."
  ~~Defines the range of hydrant types from which the required type can be selected where.

DryBarrel:	 A hydrant that has isolating valves fitted below ground and that may be used where the possibility of water freezing is a consideration.
WetBarrel:	 A hydrant that has isolating valves fitted above ground and that may be used where there is no possibility of water freezing.~~ Defines the range of hydrant types from which the required type can be selected where.\X\0D
\X\0D
DryBarrel:\X\09 A hydrant that has isolating valves fitted below ground and that may be used where the possibility of water freezing is a consideration.\X\0D
WetBarrel:\X\09 A hydrant that has isolating valves fitted above ground and that may be used where there is no possibility of water freezing.
* PropertyDefs > PropertyDef [Name="FireHydrantType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="FireHydrantType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_ProtectiveDeviceBreakerUnitTypeMCB.xml
===========================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="NominalCurrents"] > Definition "A set of nominal currents in [A] for which the data of this instance is valid. At least one value shall be provided. Any value in the set shall not exceed the value of the 
UltimateRatedCurrent associated with the same breaker unit."
  ~~A set of nominal currents in [A] for which the data of this instance is valid. At least one value shall be provided. Any value in the set shall not exceed the value of the 
UltimateRatedCurrent associated with the same breaker unit.~~ A set of nominal currents in [A] for which the data of this instance is valid. At least one value shall be provided. Any value in the set shall not exceed the value of the \X\0D
UltimateRatedCurrent associated with the same breaker unit.
* PropertyDefs > PropertyDef [Name="NominalCurrents"] > PropertyType > TypePropertyListValue
  ~~TypePropertyListValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="NominalCurrents"] > PropertyType > TypePropertyListValue > ListValue
  ~~ListValue~~ DataType
* PropertyDefs > PropertyDef [Name="VoltageLevel"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="VoltageLevel"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_EvaporativeCoolerPHistory.xml
==================================

modifications
-------------
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="LatentHeatTransferRate"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="TotalHeatTransferRate"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="WaterSumpTemperature"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="SensibleHeatTransferRate"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Effectiveness"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Pset_TransportElementCommon.xml
===============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="FireExit"] > Definition "Indication whether this object is designed to serve as an exit in the case of fire (TRUE) or not (FALSE).
Here whether the transport element (in case of e.g., a lift) is designed to serve as a fire exit, e.g., for fire escape purposes."
  ~~Indication whether this object is designed to serve as an exit in the case of fire (TRUE) or not (FALSE).
Here whether the transport element (in case of e.g., a lift) is designed to serve as a fire exit, e.g., for fire escape purposes.~~ Indication whether this object is designed to serve as an exit in the case of fire (TRUE) or not (FALSE).\X\0D
Here whether the transport element (in case of e.g., a lift) is designed to serve as a fire exit, e.g., for fire escape purposes.
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Qto_SignBaseQuantities.xml
==========================

additions
---------
* Definition "$"

modifications
-------------
* QtoDefinitionAliases
  ~~QtoDefinitionAliases~~ ApplicableTypeValue


Pset_MaintenanceTriggerDuration.xml
===================================

modifications
-------------
* ApplicableTypeValue "IfcElement,IfcAsset,IfcSystem"
  ~~IfcElement,IfcAsset,IfcSystem~~ IfcSystem


Pset_HumidifierPHistory.xml
===========================

modifications
-------------
* Definition "Humidifier performance history attributes.
Sound attribute deleted in IFC2x2 Pset Addendum: Use IfcSoundProperties instead."
  ~~Humidifier performance history attributes.
Sound attribute deleted in IFC2x2 Pset Addendum: Use IfcSoundProperties instead.~~ Humidifier performance history attributes.\X\0D
Sound attribute deleted in IFC2x2 Pset Addendum: Use IfcSoundProperties instead.
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="SaturationEfficiency"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="AtmosphericPressure"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Pset_AudioVisualApplianceTypeProjector.xml
==========================================

additions
---------
* PropertyDefs > PropertyDef [Name="VideoScaleMode"]

modifications
-------------
* PropertyDefs > PropertyDef [Name="ProjectorType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="VideoCaptionMode"] > PropertyType > TypePropertyTableValue
  ~~TypePropertyTableValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="VideoResolutionMode"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="ProjectorType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="VideoCaptionMode"] > PropertyType > TypePropertyTableValue > Expression
  ~~&lt;Expression&gt;~~ &lt;DataType&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="VideoCaptionMode"] > PropertyType > TypePropertyTableValue > DefiningValue
* PropertyDefs > PropertyDef [Name="VideoCaptionMode"] > PropertyType > TypePropertyTableValue > DefinedValue
* PropertyDefs > PropertyDef [Name="VideoScaleMode"]


Qto_CoilBaseQuantities.xml
==========================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Qto_DuctSegmentBaseQuantities.xml
=================================

modifications
-------------
* QtoDefs > QtoDef [Name="Length"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetCrossSectionArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossCrossSectionArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="OuterSurfaceArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases


Pset_BuildingStoreyCommon.xml
=============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="SprinklerProtectionAutomatic"] > Definition "Indication whether this object has an automatic sprinkler protection (TRUE) or not (FALSE).
It should only be given, if the property "SprinklerProtection" is set to TRUE."
  ~~Indication whether this object has an automatic sprinkler protection (TRUE) or not (FALSE).
It should only be given, if the property "SprinklerProtection" is set to TRUE.~~ Indication whether this object has an automatic sprinkler protection (TRUE) or not (FALSE).\X\0D
It should only be given, if the property "SprinklerProtection" is set to TRUE.


Pset_DamperTypeSmokeDamper.xml
==============================

modifications
-------------
* Definition "Smoke damper type attributes.
Pset renamed from Pset_DamperTypeSmoke to Pset_DamperTypeSmokeDamper in IFC2x2 Pset Addendum."
  ~~Smoke damper type attributes.
Pset renamed from Pset_DamperTypeSmoke to Pset_DamperTypeSmokeDamper in IFC2x2 Pset Addendum.~~ Smoke damper type attributes.\X\0D
Pset renamed from Pset_DamperTypeSmoke to Pset_DamperTypeSmokeDamper in IFC2x2 Pset Addendum.


Pset_SanitaryTerminalTypeShower.xml
===================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="ShowerType"] > Definition "Selection of the type of shower from the enumerated list of types where:-

Drench:  	Shower that rapidly gives a thorough soaking in an emergency.
Individual: 	Shower unit that is typically enclosed and is for the use of one person at a time.
Tunnel: 	Shower that has a succession of shower heads or spreaders that operate simultaneously along its length."
  ~~Selection of the type of shower from the enumerated list of types where:-

Drench:  	Shower that rapidly gives a thorough soaking in an emergency.
Individual: 	Shower unit that is typically enclosed and is for the use of one person at a time.
Tunnel: 	Shower that has a succession of shower heads or spreaders that operate simultaneously along its length.~~ Selection of the type of shower from the enumerated list of types where:-\X\0D
\X\0D
Drench:  \X\09Shower that rapidly gives a thorough soaking in an emergency.\X\0D
Individual: \X\09Shower unit that is typically enclosed and is for the use of one person at a time.\X\0D
Tunnel: \X\09Shower that has a succession of shower heads or spreaders that operate simultaneously along its length.
* PropertyDefs > PropertyDef [Name="ShowerType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="ShowerType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_ElectricFlowStorageDeviceTypeCommon.xml
============================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="ConnectedConductorFunction"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="NominalSupplyVoltageOffset"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="ConnectedConductorFunction"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_WasteTerminalTypeGullySump.xml
===================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="BackInletPatternType"] > Definition "Identifies the pattern of inlet connections to a gully trap.

A gulley trap may have 0,1,2,3 or 4 inlet connections and the pattern of their arrangement may vary. The enumeration makes the convention that an outlet is either vertical or is placed at the bottom (south side) of the gully trap (when viewed in plan). Position 1 is to the left (west), position 2 is to the top (north), position 3 is to the right (east) and position 4 is to the bottom (south).

               2
               |
   ----------------
   !                       |
1-|                       |-3
   !                       |
   ----------------
               |
              4"
  ~~Identifies the pattern of inlet connections to a gully trap.

A gulley trap may have 0,1,2,3 or 4 inlet connections and the pattern of their arrangement may vary. The enumeration makes the convention that an outlet is either vertical or is placed at the bottom (south side) of the gully trap (when viewed in plan). Position 1 is to the left (west), position 2 is to the top (north), position 3 is to the right (east) and position 4 is to the bottom (south).

               2
               |
   ----------------
   !                       |
1-|                       |-3
   !                       |
   ----------------
               |
              4~~ Identifies the pattern of inlet connections to a gully trap.\X\0D
\X\0D
A gulley trap may have 0,1,2,3 or 4 inlet connections and the pattern of their arrangement may vary. The enumeration makes the convention that an outlet is either vertical or is placed at the bottom (south side) of the gully trap (when viewed in plan). Position 1 is to the left (west), position 2 is to the top (north), position 3 is to the right (east) and position 4 is to the bottom (south).\X\0D
\X\0D
               2\X\0D
               |\X\0D
   ----------------\X\0D
   !                       |\X\0D
1-|                       |-3\X\0D
   !                       |\X\0D
   ----------------\X\0D
               |\X\0D
              4
* PropertyDefs > PropertyDef [Name="BackInletPatternType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="GullyType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="InletConnectionSize"] > Definition "Size of the inlet connection(s), where used, of the inlet connections.

Note that all inlet connections are assumed to be the same size."
  ~~Size of the inlet connection(s), where used, of the inlet connections.

Note that all inlet connections are assumed to be the same size.~~ Size of the inlet connection(s), where used, of the inlet connections.\X\0D
\X\0D
Note that all inlet connections are assumed to be the same size.
* PropertyDefs > PropertyDef [Name="TrapType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="TrapType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="GullyType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="BackInletPatternType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;




Pset_AudioVisualApplianceTypeDisplay.xml
========================================

additions
---------
* PropertyDefs > PropertyDef [Name="VideoCaptionMode"]
* PropertyDefs > PropertyDef [Name="VideoScaleMode"]

modifications
-------------
* PropertyDefs > PropertyDef [Name="AudioMode"] > PropertyType > TypePropertyTableValue
  ~~TypePropertyTableValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="DisplayType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="TouchScreen"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="VideoScaleMode"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="AudioMode"] > PropertyType > TypePropertyTableValue > Expression
  ~~&lt;Expression&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="DisplayType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="TouchScreen"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="AudioMode"] > PropertyType > TypePropertyTableValue > DefiningValue
* PropertyDefs > PropertyDef [Name="AudioMode"] > PropertyType > TypePropertyTableValue > DefinedValue
* PropertyDefs > PropertyDef [Name="VideoResolutionMode"]
* PropertyDefs > PropertyDef [Name="VideoCaptionMode"]


Pset_CoolingTowerPHistory.xml
=============================

modifications
-------------
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="SumpHeaterPower"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="HeatTransferCoefficient"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="UACurve"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Capacity"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Performance"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Pset_CooledBeamTypeActive.xml
=============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="AirFlowConfiguration"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="AirflowRateRange"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="SupplyAirConnectionType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="SupplyAirConnectionType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="AirFlowConfiguration"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_MaintenanceTriggerCondition.xml
====================================

modifications
-------------
* ApplicableTypeValue "IfcElement,IfcAsset,IfcSystem"
  ~~IfcElement,IfcAsset,IfcSystem~~ IfcSystem
* PropertyDefs > PropertyDef [Name="ConditionDisposalLevel"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="ConditionTargetPerformance"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="ConditionMaintenanceLevel"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="ConditionReplacementLevel"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Pset_CompressorPHistory.xml
===========================

modifications
-------------
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="CompressorCapacity"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="ShaftPower"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="InputPower"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="VolumetricEfficiency"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="MechanicalEfficiency"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="LubricantPumpHeatGain"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="FrictionHeatGain"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="CoefficientOfPerformance"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="CompressorTotalHeatGain"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="FullLoadRatio"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="IsentropicEfficiency"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="EnergyEfficiencyRatio"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="CompressionEfficiency"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="CompressorTotalEfficiency"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Qto_EvaporatorBaseQuantities.xml
================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Pset_BerthCommon.xml
====================

modifications
-------------
* ApplicableTypeValue "IfcSpace/BERTH,IfcSpaceType/BERTH"
  ~~IfcSpace/BERTH,IfcSpaceType/BERTH~~ IfcSpaceType
* PropertyDefs > PropertyDef [Name="BerthApproach"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="BerthMode"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* ApplicableClasses > ClassName "IfcSpaceType/BERTH"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* PropertyDefs > PropertyDef [Name="BerthApproach"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="BerthMode"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* ApplicableClasses > ClassName "IfcSpace/BERTH"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;


Pset_AirTerminalBoxPHistory.xml
===============================

modifications
-------------
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="AtmosphericPressure"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Sound"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="AirflowCurve"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="DamperPosition"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Pset_ProtectiveDeviceTypeVaristor.xml
=====================================

modifications
-------------
* PropertyDefs
  ~~PropertyDefs~~ ApplicableClasses
* ApplicableClasses
  ~~ApplicableClasses~~ ApplicableTypeValue
* ApplicableTypeValue "IfcProtectiveDevice/VARISTOR"
  ~~ApplicableTypeValue~~ PropertyDefs



Pset_SensorTypeLightSensor.xml
==============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="SetPointIlluminance"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue


Pset_ChillerPHistory.xml
========================

modifications
-------------
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="CoefficientOfPerformance"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Capacity"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="EnergyEfficiencyRatio"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;



Pset_CableSegmentTypeCoreSegment.xml
====================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="RatedTemperature"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="RatedVoltage"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="SheathColors"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="SheathColors"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_ElectricMotorTypeCommon.xml
================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="MotorEnclosureType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="MotorEnclosureType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_JettyCommon.xml
====================

modifications
-------------
* ApplicableClasses > ClassName "IfcMarineFacility/JETTY"
  ~~IfcMarineFacility/JETTY~~ IfcMarineFacility
* ApplicableTypeValue "IfcMarineFacility/JETTY"
  ~~IfcMarineFacility/JETTY~~ IfcMarineFacility
* PropertyDefs > PropertyDef [Name="PierSectionType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="PierSectionType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_EvaporatorTypeCommon.xml
=============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="EvaporatorCoolant"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="EvaporatorMediumType"] > Definition "ColdLiquid: Evaporator is using liquid type of fluid to exchange heat with refrigerant.
ColdAir: Evaporator is using air to exchange heat with refrigerant."
  ~~ColdLiquid: Evaporator is using liquid type of fluid to exchange heat with refrigerant.
ColdAir: Evaporator is using air to exchange heat with refrigerant.~~ ColdLiquid: Evaporator is using liquid type of fluid to exchange heat with refrigerant.\X\0D
ColdAir: Evaporator is using air to exchange heat with refrigerant.
* PropertyDefs > PropertyDef [Name="EvaporatorMediumType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="RefrigerantClass"] > Definition "Refrigerant class used by the compressor.
CFC: Chlorofluorocarbons.
HCFC: Hydrochlorofluorocarbons.
HFC: Hydrofluorocarbons."
  ~~Refrigerant class used by the compressor.
CFC: Chlorofluorocarbons.
HCFC: Hydrochlorofluorocarbons.
HFC: Hydrofluorocarbons.~~ Refrigerant class used by the compressor.\X\0D
CFC: Chlorofluorocarbons.\X\0D
HCFC: Hydrochlorofluorocarbons.\X\0D
HFC: Hydrofluorocarbons.
* PropertyDefs > PropertyDef [Name="RefrigerantClass"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="EvaporatorMediumType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="EvaporatorCoolant"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="RefrigerantClass"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_DiscreteAccessoryDiagonalTrussConnector.xml
================================================

modifications
-------------
* ApplicableClasses > ClassName "IfcDiscreteAccessory/Diagonal truss connector"
  ~~IfcDiscreteAccessory/Diagonal truss connector~~ IfcDiscreteAccessory
* ApplicableTypeValue "IfcDiscreteAccessory/Diagonal truss connector"
  ~~IfcDiscreteAccessory/Diagonal truss connector~~ IfcDiscreteAccessory


Pset_ElectricApplianceTypeElectricCooker.xml
============================================

modifications
-------------
* PropertyDefs
  ~~PropertyDefs~~ ApplicableClasses
* ApplicableClasses
  ~~ApplicableClasses~~ ApplicableTypeValue
* ApplicableTypeValue "IfcElectricAppliance/ELECTRICCOOKER"
  ~~ApplicableTypeValue~~ PropertyDefs


Pset_CableSegmentTypeCommon.xml
===============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;




Qto_ReinforcedSoilBaseQuantities.xml
====================================

additions
---------
* Definition "$"

modifications
-------------
* QtoDefinitionAliases
  ~~QtoDefinitionAliases~~ ApplicableTypeValue


Pset_PipeSegmentTypeCommon.xml
==============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="PressureRange"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="TemperatureRange"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_VibrationIsolatorTypeCommon.xml
====================================

additions
---------
* PropertyDefs > PropertyDef [Name="IsolatorStaticDeflection"] > Definition "Static deflection of the vibration isolator."

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_CableCarrierSegmentTypeCableTraySegment.xml
================================================

modifications
-------------
* Definition "An (typically) open carrier segment onto which cables are laid. 
HISTORY: IFC4 - NominalLength deleted. To be handled as a quantity measure"
  ~~An (typically) open carrier segment onto which cables are laid. 
HISTORY: IFC4 - NominalLength deleted. To be handled as a quantity measure~~ An (typically) open carrier segment onto which cables are laid. \X\0D
HISTORY: IFC4 - NominalLength deleted. To be handled as a quantity measure

deletions
---------
* PropertyDefs > PropertyDef [Name="NominalWidth"]


Pset_CooledBeamPHistory.xml
===========================

modifications
-------------
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="CoolingWaterFlowRate"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="TotalHeatingCapacity"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="WaterPressureDropCurves"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="BeamCoolingCapacity"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="TotalCoolingCapacity"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="ReturnWaterTemperatureHeating"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="HeatingWaterFlowRate"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="ReturnWaterTemperatureCooling"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="SupplyWaterTemperatureHeating"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="CorrectionFactorForHeating"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="BeamHeatingCapacity"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="SupplyWaterTemperatureCooling"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="CorrectionFactorForCooling"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Qto_ElectricMotorBaseQuantities.xml
===================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Pset_LightFixtureTypeSecurityLighting.xml
=========================================

additions
---------
* PropertyDefs > PropertyDef [Name="BackupSupplySystem"]

modifications
-------------
* PropertyDefs > PropertyDef [Name="PictogramEscapeDirection"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="BackupSupplySystem"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="SecurityLightingType"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Addressablility"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="SelfTestFunction"]


Pset_AirTerminalTypeCommon.xml
==============================

modifications
-------------
* Definition "Air terminal type common attributes.
SoundLevel attribute deleted in IFC2x2 Pset Addendum: Use IfcSoundProperties instead."
  ~~Air terminal type common attributes.
SoundLevel attribute deleted in IFC2x2 Pset Addendum: Use IfcSoundProperties instead.~~ Air terminal type common attributes.\X\0D
SoundLevel attribute deleted in IFC2x2 Pset Addendum: Use IfcSoundProperties instead.
* PropertyDefs > PropertyDef [Name="AirFlowrateRange"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="AirFlowrateVersusFlowControlElement"] > PropertyType > TypePropertyTableValue
  ~~TypePropertyTableValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="CoreType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="DischargeDirection"] > Definition "Discharge direction of the air terminal.

Parallel: discharges parallel to mounting surface designed so that flow attaches to the surface.
Perpendicular:  discharges away from mounting surface.
Adjustable: both parallel and perpendicular discharge."
  ~~Discharge direction of the air terminal.

Parallel: discharges parallel to mounting surface designed so that flow attaches to the surface.
Perpendicular:  discharges away from mounting surface.
Adjustable: both parallel and perpendicular discharge.~~ Discharge direction of the air terminal.\X\0D
\X\0D
Parallel: discharges parallel to mounting surface designed so that flow attaches to the surface.\X\0D
Perpendicular:  discharges away from mounting surface.\X\0D
Adjustable: both parallel and perpendicular discharge.
* PropertyDefs > PropertyDef [Name="DischargeDirection"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="FaceType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="FinishType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="FlowControlType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="FlowPattern"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="MountingType"] > Definition "The way the air terminal is mounted to the ceiling, wall, etc.

Surface: mounted to the surface of something (e.g., wall, duct, etc.).
Flat flush: mounted flat and flush with a surface.
Lay-in: mounted in a lay-in type ceiling (e.g., a dropped ceiling grid)."
  ~~The way the air terminal is mounted to the ceiling, wall, etc.

Surface: mounted to the surface of something (e.g., wall, duct, etc.).
Flat flush: mounted flat and flush with a surface.
Lay-in: mounted in a lay-in type ceiling (e.g., a dropped ceiling grid).~~ The way the air terminal is mounted to the ceiling, wall, etc.\X\0D
\X\0D
Surface: mounted to the surface of something (e.g., wall, duct, etc.).\X\0D
Flat flush: mounted flat and flush with a surface.\X\0D
Lay-in: mounted in a lay-in type ceiling (e.g., a dropped ceiling grid).
* PropertyDefs > PropertyDef [Name="MountingType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Shape"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="TemperatureRange"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="FlowPattern"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="AirFlowrateVersusFlowControlElement"] > PropertyType > TypePropertyTableValue > Expression
  ~~&lt;Expression&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="FaceType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="FinishType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="CoreType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="MountingType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="Shape"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="FlowControlType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="DischargeDirection"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="AirFlowrateVersusFlowControlElement"] > PropertyType > TypePropertyTableValue > DefiningValue
* PropertyDefs > PropertyDef [Name="AirFlowrateVersusFlowControlElement"] > PropertyType > TypePropertyTableValue > DefinedValue


Qto_CompressorBaseQuantities.xml
================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Pset_ActuatorTypeCommon.xml
===========================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Application"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="FailPosition"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Application"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="FailPosition"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_TransportElementElevator.xml
=================================

modifications
-------------
* ApplicableClasses > ClassName "IfcTransportElement/ELEVATOR"
  ~~IfcTransportElement/ELEVATOR~~ IfcTransportElement
* ApplicableTypeValue "IfcTransportElement/ELEVATOR"
  ~~IfcTransportElement/ELEVATOR~~ IfcTransportElement
* PropertyDefs > PropertyDef [Name="ClearDepth"] > Definition "Clear depth of the object (elevator). It indicates the distance from the inner surface of the elevator door to the opposite surface of the elevator car. 
The shape information is provided in addition to the shape representation and the geometric parameters used within. In cases of inconsistency between the geometric parameters and the shape properties, provided in the attached property, the geometric parameters take precedence."
  ~~Clear depth of the object (elevator). It indicates the distance from the inner surface of the elevator door to the opposite surface of the elevator car. 
The shape information is provided in addition to the shape representation and the geometric parameters used within. In cases of inconsistency between the geometric parameters and the shape properties, provided in the attached property, the geometric parameters take precedence.~~ Clear depth of the object (elevator). It indicates the distance from the inner surface of the elevator door to the opposite surface of the elevator car. \X\0D
The shape information is provided in addition to the shape representation and the geometric parameters used within. In cases of inconsistency between the geometric parameters and the shape properties, provided in the attached property, the geometric parameters take precedence.
* PropertyDefs > PropertyDef [Name="ClearHeight"] > Definition "Clear height of the object (elevator).  
The shape information is provided in addition to the shape representation and the geometric parameters used within. In cases of inconsistency between the geometric parameters and the shape properties, provided in the attached property, the geometric parameters take precedence."
  ~~Clear height of the object (elevator).  
The shape information is provided in addition to the shape representation and the geometric parameters used within. In cases of inconsistency between the geometric parameters and the shape properties, provided in the attached property, the geometric parameters take precedence.~~ Clear height of the object (elevator).  \X\0D
The shape information is provided in addition to the shape representation and the geometric parameters used within. In cases of inconsistency between the geometric parameters and the shape properties, provided in the attached property, the geometric parameters take precedence.
* PropertyDefs > PropertyDef [Name="ClearWidth"] > Definition "Clear width of the object (elevator). It indicates the distance from the inner surfaces of the elevator car left and right from the elevator door. 
The shape information is provided in addition to the shape representation and the geometric parameters used within. In cases of inconsistency between the geometric parameters and the shape properties, provided in the attached property, the geometric parameters take precedence."
  ~~Clear width of the object (elevator). It indicates the distance from the inner surfaces of the elevator car left and right from the elevator door. 
The shape information is provided in addition to the shape representation and the geometric parameters used within. In cases of inconsistency between the geometric parameters and the shape properties, provided in the attached property, the geometric parameters take precedence.~~ Clear width of the object (elevator). It indicates the distance from the inner surfaces of the elevator car left and right from the elevator door. \X\0D
The shape information is provided in addition to the shape representation and the geometric parameters used within. In cases of inconsistency between the geometric parameters and the shape properties, provided in the attached property, the geometric parameters take precedence.


Pset_BeamCommon.xml
===================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Roll"] > Definition "Rotation against the longitudinal axis - relative to the global Z direction for all beams that are non-vertical in regard to the global coordinate system (Profile direction equals global Z is Roll = 0.)

The shape information is provided in addition to the shape representation and the geometric parameters used within. In cases of inconsistency between the geometric parameters and the shape properties, provided in the attached property, the geometric parameters take precedence.  For geometry editing applications, like CAD: this value should be write-only.

Note: new property in IFC4"
  ~~Rotation against the longitudinal axis - relative to the global Z direction for all beams that are non-vertical in regard to the global coordinate system (Profile direction equals global Z is Roll = 0.)

The shape information is provided in addition to the shape representation and the geometric parameters used within. In cases of inconsistency between the geometric parameters and the shape properties, provided in the attached property, the geometric parameters take precedence.  For geometry editing applications, like CAD: this value should be write-only.

Note: new property in IFC4~~ Rotation against the longitudinal axis - relative to the global Z direction for all beams that are non-vertical in regard to the global coordinate system (Profile direction equals global Z is Roll = 0.)\X\0D
\X\0D
The shape information is provided in addition to the shape representation and the geometric parameters used within. In cases of inconsistency between the geometric parameters and the shape properties, provided in the attached property, the geometric parameters take precedence.  For geometry editing applications, like CAD: this value should be write-only.\X\0D
\X\0D
Note: new property in IFC4
* PropertyDefs > PropertyDef [Name="Slope"] > Definition "Slope angle - relative to horizontal (0.0 degrees).

The shape information is provided in addition to the shape representation and the geometric parameters used within. In cases of inconsistency between the geometric parameters and the shape properties, provided in the attached property, the geometric parameters take precedence.  For geometry editing applications, like CAD: this value should be write-only."
  ~~Slope angle - relative to horizontal (0.0 degrees).

The shape information is provided in addition to the shape representation and the geometric parameters used within. In cases of inconsistency between the geometric parameters and the shape properties, provided in the attached property, the geometric parameters take precedence.  For geometry editing applications, like CAD: this value should be write-only.~~ Slope angle - relative to horizontal (0.0 degrees).\X\0D
\X\0D
The shape information is provided in addition to the shape representation and the geometric parameters used within. In cases of inconsistency between the geometric parameters and the shape properties, provided in the attached property, the geometric parameters take precedence.  For geometry editing applications, like CAD: this value should be write-only.
* PropertyDefs > PropertyDef [Name="Span"] > Definition "Clear span for this object.

The shape information is provided in addition to the shape representation and the geometric parameters used within. In cases of inconsistency between the geometric parameters and the shape properties, provided in the attached property, the geometric parameters take precedence. For geometry editing applications, like CAD: this value should be write-only."
  ~~Clear span for this object.

The shape information is provided in addition to the shape representation and the geometric parameters used within. In cases of inconsistency between the geometric parameters and the shape properties, provided in the attached property, the geometric parameters take precedence. For geometry editing applications, like CAD: this value should be write-only.~~ Clear span for this object.\X\0D
\X\0D
The shape information is provided in addition to the shape representation and the geometric parameters used within. In cases of inconsistency between the geometric parameters and the shape properties, provided in the attached property, the geometric parameters take precedence. For geometry editing applications, like CAD: this value should be write-only.
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="ThermalTransmittance"] > Definition "Thermal transmittance coefficient (U-Value) of the element. Here the total thermal transmittance coefficient through the beam within the direction of the thermal flow (including all materials).

Note: new property in IFC4"
  ~~Thermal transmittance coefficient (U-Value) of the element. Here the total thermal transmittance coefficient through the beam within the direction of the thermal flow (including all materials).

Note: new property in IFC4~~ Thermal transmittance coefficient (U-Value) of the element. Here the total thermal transmittance coefficient through the beam within the direction of the thermal flow (including all materials).\X\0D
\X\0D
Note: new property in IFC4
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_ValveTypeCommon.xml
========================

additions
---------
* PropertyDefs > PropertyDef [Name="FlowCoefficient"] > Definition "Flow coefficient (the quantity of fluid that passes through a fully open valve at unit pressure drop), typically expressed as the Kv or Cv value for the valve."

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="ValveMechanism"] > Definition "The mechanism by which the valve function is achieved where:

BALL: Valve that has a ported ball that can be turned relative to the body seat ports.
BUTTERFLY: Valve in which a streamlined disc pivots about a diametric axis.
CONFIGUREDGATE: Screwdown valve in which the closing gate is shaped in a configured manner to have a more precise control of pressure and flow change across the valve.
GLAND: Valve with a tapered seating, in which a rotatable plug is retained by means of a gland and gland packing.
GLOBE: Screwdown valve that has a spherical body.
LUBRICATEDPLUG: Plug valve in which a lubricant is injected under pressure between the plug face and the body.
NEEDLE: Valve for regulating the flow in or from a pipe, in which a slender cone moves along the axis of flow to close against a fixed conical seat.
PARALLELSLIDE: Screwdown valve that has a machined plate that slides in formed grooves to form a seal.
PLUG: Valve that has a ported plug that can be turned relative to the body seat ports.
WEDGEGATE: Screwdown valve that has a wedge shaped plate fitting into tapered guides to form a seal."
  ~~The mechanism by which the valve function is achieved where:

BALL: Valve that has a ported ball that can be turned relative to the body seat ports.
BUTTERFLY: Valve in which a streamlined disc pivots about a diametric axis.
CONFIGUREDGATE: Screwdown valve in which the closing gate is shaped in a configured manner to have a more precise control of pressure and flow change across the valve.
GLAND: Valve with a tapered seating, in which a rotatable plug is retained by means of a gland and gland packing.
GLOBE: Screwdown valve that has a spherical body.
LUBRICATEDPLUG: Plug valve in which a lubricant is injected under pressure between the plug face and the body.
NEEDLE: Valve for regulating the flow in or from a pipe, in which a slender cone moves along the axis of flow to close against a fixed conical seat.
PARALLELSLIDE: Screwdown valve that has a machined plate that slides in formed grooves to form a seal.
PLUG: Valve that has a ported plug that can be turned relative to the body seat ports.
WEDGEGATE: Screwdown valve that has a wedge shaped plate fitting into tapered guides to form a seal.~~ The mechanism by which the valve function is achieved where:\X\0D
\X\0D
BALL: Valve that has a ported ball that can be turned relative to the body seat ports.\X\0D
BUTTERFLY: Valve in which a streamlined disc pivots about a diametric axis.\X\0D
CONFIGUREDGATE: Screwdown valve in which the closing gate is shaped in a configured manner to have a more precise control of pressure and flow change across the valve.\X\0D
GLAND: Valve with a tapered seating, in which a rotatable plug is retained by means of a gland and gland packing.\X\0D
GLOBE: Screwdown valve that has a spherical body.\X\0D
LUBRICATEDPLUG: Plug valve in which a lubricant is injected under pressure between the plug face and the body.\X\0D
NEEDLE: Valve for regulating the flow in or from a pipe, in which a slender cone moves along the axis of flow to close against a fixed conical seat.\X\0D
PARALLELSLIDE: Screwdown valve that has a machined plate that slides in formed grooves to form a seal.\X\0D
PLUG: Valve that has a ported plug that can be turned relative to the body seat ports.\X\0D
WEDGEGATE: Screwdown valve that has a wedge shaped plate fitting into tapered guides to form a seal.
* PropertyDefs > PropertyDef [Name="ValveMechanism"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="ValveOperation"] > Definition "The method of valve operation where:

DROPWEIGHT: A valve that is closed by the action of a weighted lever being released, the weight normally being prevented from dropping by being held by a wire, the closure normally being made by the action of heat on a fusible link in the wire
FLOAT: A valve that is opened and closed by the action of a float that rises and falls with water level. The float may be a ball attached to a lever or other mechanism
HYDRAULIC: A valve that is opened and closed by hydraulic actuation
LEVER: A valve that is opened and closed by the action of a lever rotating the gate within the valve.
LOCKSHIELD: A valve that requires the use of a special lockshield key for opening and closing, the operating mechanism being protected by a shroud during normal operation.
MOTORIZED: A valve that is opened and closed by the action of an electric motor on an actuator
PNEUMATIC: A valve that is opened and closed by pneumatic actuation
SOLENOID: A valve that is normally held open by a magnetic field in a coil acting on the gate but that is closed immediately if the electrical current generating the magnetic field is removed. 
SPRING: A valve that is normally held in position by the pressure of a spring on a plate but that may be caused to open if the pressure of the fluid is sufficient to overcome the spring pressure. 
THERMOSTATIC: A valve in which the ports are opened or closed to maintain a required predetermined temperature.
WHEEL: A valve that is opened and closed by the action of a wheel moving the gate within the valve."
  ~~The method of valve operation where:

DROPWEIGHT: A valve that is closed by the action of a weighted lever being released, the weight normally being prevented from dropping by being held by a wire, the closure normally being made by the action of heat on a fusible link in the wire
FLOAT: A valve that is opened and closed by the action of a float that rises and falls with water level. The float may be a ball attached to a lever or other mechanism
HYDRAULIC: A valve that is opened and closed by hydraulic actuation
LEVER: A valve that is opened and closed by the action of a lever rotating the gate within the valve.
LOCKSHIELD: A valve that requires the use of a special lockshield key for opening and closing, the operating mechanism being protected by a shroud during normal operation.
MOTORIZED: A valve that is opened and closed by the action of an electric motor on an actuator
PNEUMATIC: A valve that is opened and closed by pneumatic actuation
SOLENOID: A valve that is normally held open by a magnetic field in a coil acting on the gate but that is closed immediately if the electrical current generating the magnetic field is removed. 
SPRING: A valve that is normally held in position by the pressure of a spring on a plate but that may be caused to open if the pressure of the fluid is sufficient to overcome the spring pressure. 
THERMOSTATIC: A valve in which the ports are opened or closed to maintain a required predetermined temperature.
WHEEL: A valve that is opened and closed by the action of a wheel moving the gate within the valve.~~ The method of valve operation where:\X\0D
\X\0D
DROPWEIGHT: A valve that is closed by the action of a weighted lever being released, the weight normally being prevented from dropping by being held by a wire, the closure normally being made by the action of heat on a fusible link in the wire\X\0D
FLOAT: A valve that is opened and closed by the action of a float that rises and falls with water level. The float may be a ball attached to a lever or other mechanism\X\0D
HYDRAULIC: A valve that is opened and closed by hydraulic actuation\X\0D
LEVER: A valve that is opened and closed by the action of a lever rotating the gate within the valve.\X\0D
LOCKSHIELD: A valve that requires the use of a special lockshield key for opening and closing, the operating mechanism being protected by a shroud during normal operation.\X\0D
MOTORIZED: A valve that is opened and closed by the action of an electric motor on an actuator\X\0D
PNEUMATIC: A valve that is opened and closed by pneumatic actuation\X\0D
SOLENOID: A valve that is normally held open by a magnetic field in a coil acting on the gate but that is closed immediately if the electrical current generating the magnetic field is removed. \X\0D
SPRING: A valve that is normally held in position by the pressure of a spring on a plate but that may be caused to open if the pressure of the fluid is sufficient to overcome the spring pressure. \X\0D
THERMOSTATIC: A valve in which the ports are opened or closed to maintain a required predetermined temperature.\X\0D
WHEEL: A valve that is opened and closed by the action of a wheel moving the gate within the valve.
* PropertyDefs > PropertyDef [Name="ValveOperation"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="ValvePattern"] > Definition "The configuration of the ports of a valve according to either the linear route taken by a fluid flowing through the valve or by the number of ports where:

SINGLEPORT: Valve that has a single entry port from the system that it serves, the exit port being to the surrounding environment.
ANGLED_2_PORT: Valve in which the direction of flow is changed through 90 degrees.
STRAIGHT_2_PORT: Valve in which the flow is straight through.
STRAIGHT_3_PORT: Valve with three separate ports.
CROSSOVER_4_PORT: Valve with 4 separate ports."
  ~~The configuration of the ports of a valve according to either the linear route taken by a fluid flowing through the valve or by the number of ports where:

SINGLEPORT: Valve that has a single entry port from the system that it serves, the exit port being to the surrounding environment.
ANGLED_2_PORT: Valve in which the direction of flow is changed through 90 degrees.
STRAIGHT_2_PORT: Valve in which the flow is straight through.
STRAIGHT_3_PORT: Valve with three separate ports.
CROSSOVER_4_PORT: Valve with 4 separate ports.~~ The configuration of the ports of a valve according to either the linear route taken by a fluid flowing through the valve or by the number of ports where:\X\0D
\X\0D
SINGLEPORT: Valve that has a single entry port from the system that it serves, the exit port being to the surrounding environment.\X\0D
ANGLED_2_PORT: Valve in which the direction of flow is changed through 90 degrees.\X\0D
STRAIGHT_2_PORT: Valve in which the flow is straight through.\X\0D
STRAIGHT_3_PORT: Valve with three separate ports.\X\0D
CROSSOVER_4_PORT: Valve with 4 separate ports.
* PropertyDefs > PropertyDef [Name="ValvePattern"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="ValveMechanism"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="ValveOperation"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="ValvePattern"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_ProtectiveDeviceTrippingUnitTimeAdjustment.xml
===================================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="AdjustmentRange"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="AdjustmentValues"] > PropertyType > TypePropertyListValue
  ~~TypePropertyListValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="AdjustmentValues"] > PropertyType > TypePropertyListValue > ListValue
  ~~ListValue~~ DataType
* PropertyDefs > PropertyDef [Name="AdjustmentValueType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="I2TApplicability"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="AdjustmentValueType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="I2TApplicability"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_SwitchingDeviceTypeDimmerSwitch.xml
========================================

modifications
-------------
* PropertyDefs
  ~~PropertyDefs~~ ApplicableClasses
* ApplicableClasses
  ~~ApplicableClasses~~ ApplicableTypeValue
* ApplicableTypeValue "IfcSwitchingDevice/DIMMERSWITCH"
  ~~ApplicableTypeValue~~ PropertyDefs



Pset_ProtectiveDeviceTypeFuseDisconnector.xml
=============================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="FuseDisconnectorType"] > Definition "A list of the available types of fuse disconnector from which that required may be selected where:

EngineProtectionDevice: A fuse whose characteristic is specifically designed for the protection of a motor or generator.
FuseSwitchDisconnector: A switch disconnector in which a fuse link or a fuse carrier with fuse link forms the moving contact,
HRC: A standard fuse (High Rupturing Capacity)
OverloadProtectionDevice: A device that disconnects the supply when the operating conditions in an electrically undamaged circuit causes an overcurrent,
SemiconductorFuse: A fuse whose characteristic is specifically designed for the protection of sem-conductor devices.
SwitchDisconnectorFuse: A switch disconnector in which one or more poles have a fuse in series in a composite unit."
  ~~A list of the available types of fuse disconnector from which that required may be selected where:

EngineProtectionDevice: A fuse whose characteristic is specifically designed for the protection of a motor or generator.
FuseSwitchDisconnector: A switch disconnector in which a fuse link or a fuse carrier with fuse link forms the moving contact,
HRC: A standard fuse (High Rupturing Capacity)
OverloadProtectionDevice: A device that disconnects the supply when the operating conditions in an electrically undamaged circuit causes an overcurrent,
SemiconductorFuse: A fuse whose characteristic is specifically designed for the protection of sem-conductor devices.
SwitchDisconnectorFuse: A switch disconnector in which one or more poles have a fuse in series in a composite unit.~~ A list of the available types of fuse disconnector from which that required may be selected where:\X\0D
\X\0D
EngineProtectionDevice: A fuse whose characteristic is specifically designed for the protection of a motor or generator.\X\0D
FuseSwitchDisconnector: A switch disconnector in which a fuse link or a fuse carrier with fuse link forms the moving contact,\X\0D
HRC: A standard fuse (High Rupturing Capacity)\X\0D
OverloadProtectionDevice: A device that disconnects the supply when the operating conditions in an electrically undamaged circuit causes an overcurrent,\X\0D
SemiconductorFuse: A fuse whose characteristic is specifically designed for the protection of sem-conductor devices.\X\0D
SwitchDisconnectorFuse: A switch disconnector in which one or more poles have a fuse in series in a composite unit.
* PropertyDefs > PropertyDef [Name="FuseDisconnectorType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="VoltageLevel"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="FuseDisconnectorType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="VoltageLevel"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_WasteTerminalTypeCommon.xml
================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_AirToAirHeatRecoveryPHistory.xml
=====================================

modifications
-------------
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="SensibleEffectivenessTable"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="SensibleEffectiveness"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="AirPressureDropCurves"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="TemperatureEffectiveness"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="HumidityEffectiveness"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="SensibleHeatTransferRate"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="TotalHeatTransferRate"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="DefrostTemperatureEffectiveness"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="LatentHeatTransferRate"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="TotalEffectivenessTable"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="TotalEffectiveness"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;



Pset_FanTypeCommon.xml
======================

additions
---------
* PropertyDefs > PropertyDef [Name="PressureCurve"]

modifications
-------------
* PropertyDefs > PropertyDef [Name="CapacityControlType"] > Definition "InletVane: Control by adjusting inlet vane.
VariableSpeedDrive: Control by variable speed drive. 
BladePitchAngle: Control by adjusting blade pitch angle.
TwoSpeed: Control by switch between high and low speed.
DischargeDamper: Control by modulating discharge damper."
  ~~InletVane: Control by adjusting inlet vane.
VariableSpeedDrive: Control by variable speed drive. 
BladePitchAngle: Control by adjusting blade pitch angle.
TwoSpeed: Control by switch between high and low speed.
DischargeDamper: Control by modulating discharge damper.~~ InletVane: Control by adjusting inlet vane.\X\0D
VariableSpeedDrive: Control by variable speed drive. \X\0D
BladePitchAngle: Control by adjusting blade pitch angle.\X\0D
TwoSpeed: Control by switch between high and low speed.\X\0D
DischargeDamper: Control by modulating discharge damper.
* PropertyDefs > PropertyDef [Name="CapacityControlType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="EfficiencyCurve"] > PropertyType > TypePropertyTableValue
  ~~TypePropertyTableValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="MotorDriveType"] > Definition "Motor drive type:
DIRECTDRIVE: Direct drive. 
BELTDRIVE: Belt drive. 
COUPLING: Coupling. 
OTHER: Other type of motor drive. 
UNKNOWN: Unknown motor drive type."
  ~~Motor drive type:
DIRECTDRIVE: Direct drive. 
BELTDRIVE: Belt drive. 
COUPLING: Coupling. 
OTHER: Other type of motor drive. 
UNKNOWN: Unknown motor drive type.~~ Motor drive type:\X\0D
DIRECTDRIVE: Direct drive. \X\0D
BELTDRIVE: Belt drive. \X\0D
COUPLING: Coupling. \X\0D
OTHER: Other type of motor drive. \X\0D
UNKNOWN: Unknown motor drive type.
* PropertyDefs > PropertyDef [Name="MotorDriveType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="OperationTemperatureRange"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="MotorDriveType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="EfficiencyCurve"] > PropertyType > TypePropertyTableValue > Expression
  ~~&lt;Expression&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="CapacityControlType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="EfficiencyCurve"] > PropertyType > TypePropertyTableValue > DefiningValue
* PropertyDefs > PropertyDef [Name="EfficiencyCurve"] > PropertyType > TypePropertyTableValue > DefinedValue
* PropertyDefs > PropertyDef [Name="PressureCurve"]


Pset_TransformerTypeCommon.xml
==============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="ImaginaryImpedanceRatio"] > Definition "The ratio between the imaginary part of the zero sequence impedance and the imaginary part of the positive impedance (i.e. imaginary part of the short-circuit voltage) of the transformer.
Used for three-phase transformer which includes a N-conductor."
  ~~The ratio between the imaginary part of the zero sequence impedance and the imaginary part of the positive impedance (i.e. imaginary part of the short-circuit voltage) of the transformer.
Used for three-phase transformer which includes a N-conductor.~~ The ratio between the imaginary part of the zero sequence impedance and the imaginary part of the positive impedance (i.e. imaginary part of the short-circuit voltage) of the transformer.\X\0D
Used for three-phase transformer which includes a N-conductor.
* PropertyDefs > PropertyDef [Name="RealImpedanceRatio"] > Definition "The ratio between the real part of the zero sequence impedance and the real part of the positive impedance (i.e. real part of the short-circuit voltage) of the transformer.
Used for three-phase transformer which includes a N-conductor."
  ~~The ratio between the real part of the zero sequence impedance and the real part of the positive impedance (i.e. real part of the short-circuit voltage) of the transformer.
Used for three-phase transformer which includes a N-conductor.~~ The ratio between the real part of the zero sequence impedance and the real part of the positive impedance (i.e. real part of the short-circuit voltage) of the transformer.\X\0D
Used for three-phase transformer which includes a N-conductor.
* PropertyDefs > PropertyDef [Name="SecondaryCurrentType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="TransformerVectorGroup"] > Definition "List of the possible vector groups for the transformer from which that required may be set. Values in the enumeration list follow a standard international code where the first letter  describes how the primary windings are connected,
the second letter describes how the secondary windings are connected, and the numbers describe the rotation of voltages and currents from the primary to the secondary side in multiples of 30 degrees.

D: means that the windings are delta-connected.
Y: means that the windings are star-connected. 
Z: means that the windings are zig-zag connected (a special start-connected providing low reactance of the transformer); 
The connectivity is only relevant for three-phase transformers."
  ~~List of the possible vector groups for the transformer from which that required may be set. Values in the enumeration list follow a standard international code where the first letter  describes how the primary windings are connected,
the second letter describes how the secondary windings are connected, and the numbers describe the rotation of voltages and currents from the primary to the secondary side in multiples of 30 degrees.

D: means that the windings are delta-connected.
Y: means that the windings are star-connected. 
Z: means that the windings are zig-zag connected (a special start-connected providing low reactance of the transformer); 
The connectivity is only relevant for three-phase transformers.~~ List of the possible vector groups for the transformer from which that required may be set. Values in the enumeration list follow a standard international code where the first letter  describes how the primary windings are connected,\X\0D
the second letter describes how the secondary windings are connected, and the numbers describe the rotation of voltages and currents from the primary to the secondary side in multiples of 30 degrees.\X\0D
\X\0D
D: means that the windings are delta-connected.\X\0D
Y: means that the windings are star-connected. \X\0D
Z: means that the windings are zig-zag connected (a special start-connected providing low reactance of the transformer); \X\0D
The connectivity is only relevant for three-phase transformers.
* PropertyDefs > PropertyDef [Name="TransformerVectorGroup"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="TransformerVectorGroup"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="SecondaryCurrentType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;



Pset_FlowInstrumentTypeThermometer.xml
======================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="ThermometerType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="ThermometerType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_CoveringCeiling.xml
========================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Permeability"] > Definition "Ratio of the permeability of the ceiling.
The ration can be used to indicate an open ceiling (that enables identification of whether ceiling construction should be considered as impeding distribution of sprinkler water, light etc. from installations within the ceiling area)."
  ~~Ratio of the permeability of the ceiling.
The ration can be used to indicate an open ceiling (that enables identification of whether ceiling construction should be considered as impeding distribution of sprinkler water, light etc. from installations within the ceiling area).~~ Ratio of the permeability of the ceiling.\X\0D
The ration can be used to indicate an open ceiling (that enables identification of whether ceiling construction should be considered as impeding distribution of sprinkler water, light etc. from installations within the ceiling area).


Pset_SpaceLightingRequirements.xml
==================================

modifications
-------------
* ApplicableTypeValue "IfcSpace, IfcSpatialZone, IfcZone"
  ~~IfcSpace, IfcSpatialZone, IfcZone~~ IfcZone



Pset_ProtectiveDeviceBreakerUnitI2TFuseCurve.xml
================================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="VoltageLevel"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="BreakerUnitFuseBreakingingCurve"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="BreakerUnitFuseMeltingCurve"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Pset_ShipyardCommon.xml
=======================

modifications
-------------
* ApplicableClasses > ClassName "IfcMarineFacility/SHIPYARD"
  ~~IfcMarineFacility/SHIPYARD~~ IfcMarineFacility
* ApplicableTypeValue "IfcMarineFacility/SHIPYARD"
  ~~IfcMarineFacility/SHIPYARD~~ IfcMarineFacility


Pset_ProjectCommon.xml
======================

modifications
-------------
* PropertyDefs > PropertyDef [Name="ProjectType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* 
  ~~PSET_OCCURRENCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="ProjectType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="NetEarnedValue"] > PropertyType
* PropertyDefs > PropertyDef [Name="ProjectInvestmentEstimate"] > PropertyType


Pset_PileCommon.xml
===================

additions
---------
* PropertyDefs > PropertyDef [Name="Status"] > Definition "Status of the element, predominately used in renovation or retrofitting projects. The status can be assigned to as "New" - element designed as new addition, "Existing" - element exists and remains, "Demolish" - element existed but is to be demolished,  "Temporary" - element will exists only temporary (like a temporary support structure)."

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;



Pset_SystemFurnitureElementTypeWorkSurface.xml
==============================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="SupportType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="SupportType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="NominalThickness"]


Pset_DistributionPortPHistoryPipe.xml
=====================================

modifications
-------------
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="Temperature"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Pressure"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Flowrate"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Qto_RailingBaseQuantities.xml
=============================

deletions
---------
* QtoDefs > QtoDef [Name="Length"] > NameAliases
* QtoDefs > QtoDef [Name="Length"] > DefinitionAliases
* QtoDefinitionAliases


Pset_DuctSilencerPHistory.xml
=============================

modifications
-------------
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="AirFlowRate"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="AirPressureDropCurve"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Pset_VehicleAvailability.xml
============================

modifications
-------------
* ApplicableTypeValue "IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLE.),IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLETRACKED.),IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.),IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLEAIR.),IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.ROLLINGSTOCK.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLE.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLETRACKED.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLEAIR.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.ROLLINGSTOCK.)"
  ~~IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLE.),IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLETRACKED.),IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.),IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLEAIR.),IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.ROLLINGSTOCK.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLE.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLETRACKED.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLEAIR.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.ROLLINGSTOCK.)~~ IfcValve
* ApplicableClasses > ClassName "IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLE.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;

deletions
---------
* ApplicableClasses > ClassName "IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLETRACKED.)"
* ApplicableClasses > ClassName "IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.)"
* ApplicableClasses > ClassName "IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLEAIR.)"
* ApplicableClasses > ClassName "IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.ROLLINGSTOCK.)"
* ApplicableClasses > ClassName "IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLE.)"
* ApplicableClasses > ClassName "IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLETRACKED.)"
* ApplicableClasses > ClassName "IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.)"
* ApplicableClasses > ClassName "IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLEAIR.)"
* ApplicableClasses > ClassName "IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.ROLLINGSTOCK.)"


Pset_RampCommon.xml
===================

modifications
-------------
* PropertyDefs > PropertyDef [Name="FireExit"] > Definition "Indication whether this object is designed to serve as an exit in the case of fire (TRUE) or not (FALSE).
Here it defines an exit ramp in accordance to the national building code."
  ~~Indication whether this object is designed to serve as an exit in the case of fire (TRUE) or not (FALSE).
Here it defines an exit ramp in accordance to the national building code.~~ Indication whether this object is designed to serve as an exit in the case of fire (TRUE) or not (FALSE).\X\0D
Here it defines an exit ramp in accordance to the national building code.
* PropertyDefs > PropertyDef [Name="FireRating"] > Definition "Fire rating for this object.
It is given according to the national fire safety classification."
  ~~Fire rating for this object.
It is given according to the national fire safety classification.~~ Fire rating for this object.\X\0D
It is given according to the national fire safety classification.
* PropertyDefs > PropertyDef [Name="HandicapAccessible"] > Definition "Indication that this object is designed to be accessible by the handicapped. 
Set to (TRUE) if this ramp is rated as handicap accessible  according the local building codes, otherwise (FALSE)."
  ~~Indication that this object is designed to be accessible by the handicapped. 
Set to (TRUE) if this ramp is rated as handicap accessible  according the local building codes, otherwise (FALSE).~~ Indication that this object is designed to be accessible by the handicapped. \X\0D
Set to (TRUE) if this ramp is rated as handicap accessible  according the local building codes, otherwise (FALSE).
* PropertyDefs > PropertyDef [Name="LoadBearing"] > PropertyType
  ~~PropertyType~~ Definition
* PropertyDefs > PropertyDef [Name="RequiredSlope"] > Definition "Required sloping angle of the object  - relative to horizontal (0.0 degrees).
Required maximum slope for the passageway according to the applicable building code or additional requirements."
  ~~Required sloping angle of the object  - relative to horizontal (0.0 degrees).
Required maximum slope for the passageway according to the applicable building code or additional requirements.~~ Required sloping angle of the object  - relative to horizontal (0.0 degrees).\X\0D
Required maximum slope for the passageway according to the applicable building code or additional requirements.
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="ThermalTransmittance"] > PropertyType
  ~~PropertyType~~ Definition
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Qto_BuildingElementProxyQuantities.xml
======================================

modifications
-------------
* QtoDefinitionAliases
  ~~QtoDefinitionAliases~~ Definition
* QtoDefs > QtoDef [Name="NetSurfaceArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetVolume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;


Qto_BuildingBaseQuantities.xml
==============================

modifications
-------------
* QtoDefs > QtoDef [Name="GrossFloorArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="EavesHeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Height"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossVolume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="FootprintArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetVolume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetFloorArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases


Pset_DuctFittingOccurrence.xml
==============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Color"] > Definition "The color of the duct segment.

Note: This is typically used for any duct segments with a painted surface which is not otherwise specified as a covering."
  ~~The color of the duct segment.

Note: This is typically used for any duct segments with a painted surface which is not otherwise specified as a covering.~~ The color of the duct segment.\X\0D
\X\0D
Note: This is typically used for any duct segments with a painted surface which is not otherwise specified as a covering.
* 
  ~~PSET_OCCURRENCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE


Qto_ProjectionElementBaseQuantities.xml
=======================================

modifications
-------------
* QtoDefs > QtoDef [Name="Area"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Volume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases


Pset_SpaceThermalPHistory.xml
=============================

modifications
-------------
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="SpaceTemperature"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="HeatingAirFlowRate"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="SpaceRelativeHumidity"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="CoolingAirFlowRate"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="ExhaustAirFlowRate"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="VentilationAirFlowRate"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Pset_AudioVisualApplianceTypeTuner.xml
======================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="TunerFrequency"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="TunerType"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="TunerChannel"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="TunerMode"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Pset_BoilerTypeCommon.xml
=========================

modifications
-------------
* Definition "Boiler type common attributes.
SoundLevel attribute deleted in IFC2x2 Pset Addendum: Use IfcSoundProperties instead. PrimaryEnergySource and AuxiliaryEnergySource attributes deleted in IFC2x2 Pset Addendum: Use IfcEnergyProperties, IfcFuelProperties, etc. instead."
  ~~Boiler type common attributes.
SoundLevel attribute deleted in IFC2x2 Pset Addendum: Use IfcSoundProperties instead. PrimaryEnergySource and AuxiliaryEnergySource attributes deleted in IFC2x2 Pset Addendum: Use IfcEnergyProperties, IfcFuelProperties, etc. instead.~~ Boiler type common attributes.\X\0D
SoundLevel attribute deleted in IFC2x2 Pset Addendum: Use IfcSoundProperties instead. PrimaryEnergySource and AuxiliaryEnergySource attributes deleted in IFC2x2 Pset Addendum: Use IfcEnergyProperties, IfcFuelProperties, etc. instead.
* PropertyDefs > PropertyDef [Name="EnergySource"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="NominalPartLoadRatio"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="OperatingMode"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="OutletTemperatureRange"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="PartialLoadEfficiencyCurves"] > PropertyType > TypePropertyTableValue
  ~~TypePropertyTableValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="WaterInletTemperatureRange"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="OperatingMode"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="PartialLoadEfficiencyCurves"] > PropertyType > TypePropertyTableValue > Expression
  ~~&lt;Expression&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="EnergySource"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="PartialLoadEfficiencyCurves"] > PropertyType > TypePropertyTableValue > DefiningValue
* PropertyDefs > PropertyDef [Name="PartialLoadEfficiencyCurves"] > PropertyType > TypePropertyTableValue > DefinedValue


Pset_SanitaryTerminalTypeToiletPan.xml
======================================

additions
---------
* ApplicableClasses
* ApplicableClasses
* ApplicableClasses

modifications
-------------
* PropertyDefs
  ~~PropertyDefs~~ ApplicableClasses
* ApplicableClasses
  ~~ApplicableClasses~~ PropertyDefs
* ApplicableClasses > ClassName "IfcSanitaryTerminal/TOILETPAN"
  ~~&lt;ClassName&gt;~~ &lt;PropertyDef&gt;


Pset_PipeFittingTypeJunction.xml
================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="JunctionType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="JunctionType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Qto_ConstructionEquipmentResourceBaseQuantities.xml
===================================================

modifications
-------------
* QtoDefs > QtoDef [Name="UsageTime"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="OperatingTime"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases


Qto_CoveringBaseQuantities.xml
==============================

modifications
-------------
* QtoDefs > QtoDef [Name="Width"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases


Pset_ProfileArbitraryHollowCore.xml
===================================

modifications
-------------
* Definition "This is a collection of geometric properties of hollow core section profiles of precast concrete elements, to be used in conjunction with IfcArbitraryProfileDefWithVoids when profile designation alone does not fulfill the information requirements.  

In all cases, the cores are symmetrically distributed on either side of the plank center line, irrespective of whether the number of cores is odd or even. For planks with a center core with different geometry to that of the other cores, provide the property CenterCoreSpacing. When the number of cores is even, no Center Core properties shall be asserted.

Key chamfers and draft chamfer are all 45 degree chamfers.

The CoreTopRadius and CoreBaseRadius parameters can be derived and are therefore not listed in the property set. They are shown to define that the curves are arcs. The parameters for the center core are the same as above, but with the prefix "Center"."
  ~~This is a collection of geometric properties of hollow core section profiles of precast concrete elements, to be used in conjunction with IfcArbitraryProfileDefWithVoids when profile designation alone does not fulfill the information requirements.  

In all cases, the cores are symmetrically distributed on either side of the plank center line, irrespective of whether the number of cores is odd or even. For planks with a center core with different geometry to that of the other cores, provide the property CenterCoreSpacing. When the number of cores is even, no Center Core properties shall be asserted.

Key chamfers and draft chamfer are all 45 degree chamfers.

The CoreTopRadius and CoreBaseRadius parameters can be derived and are therefore not listed in the property set. They are shown to define that the curves are arcs. The parameters for the center core are the same as above, but with the prefix "Center".~~ This is a collection of geometric properties of hollow core section profiles of precast concrete elements, to be used in conjunction with IfcArbitraryProfileDefWithVoids when profile designation alone does not fulfill the information requirements.  \X\0D
\X\0D
In all cases, the cores are symmetrically distributed on either side of the plank center line, irrespective of whether the number of cores is odd or even. For planks with a center core with different geometry to that of the other cores, provide the property CenterCoreSpacing. When the number of cores is even, no Center Core properties shall be asserted.\X\0D
\X\0D
Key chamfers and draft chamfer are all 45 degree chamfers.\X\0D
\X\0D
The CoreTopRadius and CoreBaseRadius parameters can be derived and are therefore not listed in the property set. They are shown to define that the curves are arcs. The parameters for the center core are the same as above, but with the prefix "Center".


Pset_MarineVehicleCommon.xml
============================

modifications
-------------
* 
  ~~PropertySetDef~~ QtoSetDef
* ApplicableTypeValue "IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.)"
  ~~IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.)~~ IfcLightFixture
* PropertyDefs
  ~~PropertyDefs~~ QtoDefs
* 
  ~~QTO_TYPEDRIVENOVERRIDE~~ PSET_TYPEDRIVENOVERRIDE
* 
  ~~http://buildingSMART-tech.org/xml/psd/PSD_IFC4.xsd~~ http://buildingSMART-tech.org/xml/psd/QTO_IFC4.xsd
* PropertyDefs > PropertyDef [Name="AboveDeckProjectedWindSide"]
  ~~&lt;PropertyDef&gt;~~ &lt;QtoDef&gt;
* PropertyDefs > PropertyDef [Name="VesselDepth"]
  ~~&lt;PropertyDef&gt;~~ &lt;QtoDef&gt;
* PropertyDefs > PropertyDef [Name="CargoDeadWeight"]
  ~~&lt;PropertyDef&gt;~~ &lt;QtoDef&gt;
* PropertyDefs > PropertyDef [Name="LengthBetweenPerpendiculars"]
  ~~&lt;PropertyDef&gt;~~ &lt;QtoDef&gt;
* ApplicableClasses > ClassName "IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* PropertyDefs > PropertyDef [Name="VesselDraft"]
  ~~&lt;PropertyDef&gt;~~ &lt;QtoDef&gt;
* PropertyDefs > PropertyDef [Name="AboveDeckProjectedWindEnd"]
  ~~&lt;PropertyDef&gt;~~ &lt;QtoDef&gt;
* PropertyDefs > PropertyDef [Name="Displacement"]
  ~~&lt;PropertyDef&gt;~~ &lt;QtoDef&gt;
* PropertyDefs > PropertyDef [Name="LaneMeters"]
  ~~&lt;PropertyDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* ApplicableClasses > ClassName "IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.)"


Pset_SanitaryTerminalTypeSink.xml
=================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Mounting"] > Definition "Selection of the form of mounting of the sink from the enumerated list of mountings where:-

BackToWall: A pedestal mounted sanitary terminal that fits flush to the wall at the rear to cover its service connections.
Pedestal: 	A floor mounted sanitary terminal that has an integral base.
CounterTop: 	A sanitary terminal that is installed into a horizontal surface that is installed into a horizontal surface. Note: When applied to a wash hand basin, the term more normally used is &#8216;vanity&#8217;. See also Wash Hand Basin Type specification.
WallHung: 	A sanitary terminal cantilevered clear of the floor."
  ~~Selection of the form of mounting of the sink from the enumerated list of mountings where:-

BackToWall: A pedestal mounted sanitary terminal that fits flush to the wall at the rear to cover its service connections.
Pedestal: 	A floor mounted sanitary terminal that has an integral base.
CounterTop: 	A sanitary terminal that is installed into a horizontal surface that is installed into a horizontal surface. Note: When applied to a wash hand basin, the term more normally used is &#8216;vanity&#8217;. See also Wash Hand Basin Type specification.
WallHung: 	A sanitary terminal cantilevered clear of the floor.~~ Selection of the form of mounting of the sink from the enumerated list of mountings where:-\X\0D
\X\0D
BackToWall: A pedestal mounted sanitary terminal that fits flush to the wall at the rear to cover its service connections.\X\0D
Pedestal: \X\09A floor mounted sanitary terminal that has an integral base.\X\0D
CounterTop: \X\09A sanitary terminal that is installed into a horizontal surface that is installed into a horizontal surface. Note: When applied to a wash hand basin, the term more normally used is \X2\2018\X0\vanity\X2\2019\X0\. See also Wash Hand Basin Type specification.\X\0D
WallHung: \X\09A sanitary terminal cantilevered clear of the floor.
* PropertyDefs > PropertyDef [Name="Mounting"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="SinkType"] > Definition "Selection of the type of sink from the enumerated list of types where:-

Belfast: 	Deep sink that has a plain edge and a weir overflow
.
Bucket: 	Sink at low level, with protected front edge, that facilitates filling and emptying buckets, usually with a hinged grid on which to stand them.
Cleaners:	 Sink, usually fixed at normal height (900mm), with protected front edge.
Combination_Left:	 Sink with integral drainer on left hand side
.
Combination_Right: Sink with integral drainer on right hand side
.
Combination_Double: 	Sink with integral drainer on both sides
.
Drip: Small sink that catches drips or flow from a faucet
.
Laboratory: Sink, of acid resisting material, with a top edge shaped to facilitate fixing to the underside of a desktop
.
London: Deep sink that has a plain edge and no overflow
.
Plaster: Sink with sediment receiver to prevent waste plaster passing into drains
.
Pot: Large metal sink, with a standing waste, for washing cooking utensils
.
Rinsing: Metal sink in which water can be heated and culinary utensils and tableware immersed at high temperature that destroys most harmful bacteria and allows subsequent self drying.
.
Shelf: Ceramic sink with an integral back shelf through which water fittings are mounted
.
VegetablePreparation: 	Large metal sink, with a standing waste, for washing and preparing vegetables
."
  ~~Selection of the type of sink from the enumerated list of types where:-

Belfast: 	Deep sink that has a plain edge and a weir overflow
.
Bucket: 	Sink at low level, with protected front edge, that facilitates filling and emptying buckets, usually with a hinged grid on which to stand them.
Cleaners:	 Sink, usually fixed at normal height (900mm), with protected front edge.
Combination_Left:	 Sink with integral drainer on left hand side
.
Combination_Right: Sink with integral drainer on right hand side
.
Combination_Double: 	Sink with integral drainer on both sides
.
Drip: Small sink that catches drips or flow from a faucet
.
Laboratory: Sink, of acid resisting material, with a top edge shaped to facilitate fixing to the underside of a desktop
.
London: Deep sink that has a plain edge and no overflow
.
Plaster: Sink with sediment receiver to prevent waste plaster passing into drains
.
Pot: Large metal sink, with a standing waste, for washing cooking utensils
.
Rinsing: Metal sink in which water can be heated and culinary utensils and tableware immersed at high temperature that destroys most harmful bacteria and allows subsequent self drying.
.
Shelf: Ceramic sink with an integral back shelf through which water fittings are mounted
.
VegetablePreparation: 	Large metal sink, with a standing waste, for washing and preparing vegetables
.~~ Selection of the type of sink from the enumerated list of types where:-\X\0D
\X\0D
Belfast: \X\09Deep sink that has a plain edge and a weir overflow\X\0D
.\X\0D
Bucket: \X\09Sink at low level, with protected front edge, that facilitates filling and emptying buckets, usually with a hinged grid on which to stand them.\X\0D
Cleaners:\X\09 Sink, usually fixed at normal height (900mm), with protected front edge.\X\0D
Combination_Left:\X\09 Sink with integral drainer on left hand side\X\0D
.\X\0D
Combination_Right: Sink with integral drainer on right hand side\X\0D
.\X\0D
Combination_Double: \X\09Sink with integral drainer on both sides\X\0D
.\X\0D
Drip: Small sink that catches drips or flow from a faucet\X\0D
.\X\0D
Laboratory: Sink, of acid resisting material, with a top edge shaped to facilitate fixing to the underside of a desktop\X\0D
.\X\0D
London: Deep sink that has a plain edge and no overflow\X\0D
.\X\0D
Plaster: Sink with sediment receiver to prevent waste plaster passing into drains\X\0D
.\X\0D
Pot: Large metal sink, with a standing waste, for washing cooking utensils\X\0D
.\X\0D
Rinsing: Metal sink in which water can be heated and culinary utensils and tableware immersed at high temperature that destroys most harmful bacteria and allows subsequent self drying.\X\0D
.\X\0D
Shelf: Ceramic sink with an integral back shelf through which water fittings are mounted\X\0D
.\X\0D
VegetablePreparation: \X\09Large metal sink, with a standing waste, for washing and preparing vegetables\X\0D
.
* PropertyDefs > PropertyDef [Name="SinkType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="SinkType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="Mounting"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Qto_CurtainWallQuantities.xml
=============================

modifications
-------------
* QtoDefs > QtoDef [Name="Length"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossSideArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Width"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Height"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetSideArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases



Qto_ReinforcingElementBaseQuantities.xml
========================================

modifications
-------------
* QtoDefs > QtoDef [Name="Length"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Count"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefs > QtoDef [Name="Weight"]
* QtoDefinitionAliases


Pset_ServiceLife.xml
====================

modifications
-------------
* PropertyDefs > PropertyDef [Name="ServiceLifeDuration"] > Definition "The length or duration of a service life.  

The lower bound indicates pessimistic service life, the upper bound indicates optimistic service life, and the setpoint indicates the typical service life."
  ~~The length or duration of a service life.  

The lower bound indicates pessimistic service life, the upper bound indicates optimistic service life, and the setpoint indicates the typical service life.~~ The length or duration of a service life.  \X\0D
\X\0D
The lower bound indicates pessimistic service life, the upper bound indicates optimistic service life, and the setpoint indicates the typical service life.
* PropertyDefs > PropertyDef [Name="ServiceLifeDuration"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue


Pset_TankOccurrence.xml
=======================

modifications
-------------
* PropertyDefs > PropertyDef [Name="HasLadder"] > Definition "Indication of whether the tank is provided with a ladder (set TRUE) for access to the top. If no ladder is provided then value is set FALSE.

Note: No indication is given of the type of ladder (gooseneck etc.)"
  ~~Indication of whether the tank is provided with a ladder (set TRUE) for access to the top. If no ladder is provided then value is set FALSE.

Note: No indication is given of the type of ladder (gooseneck etc.)~~ Indication of whether the tank is provided with a ladder (set TRUE) for access to the top. If no ladder is provided then value is set FALSE.\X\0D
\X\0D
Note: No indication is given of the type of ladder (gooseneck etc.)
* PropertyDefs > PropertyDef [Name="TankComposition"] > Definition "Defines the level of element composition where.

COMPLEX: A set of elementary units aggregated together to fulfill the overall  required purpose.
ELEMENT: A single elementary unit that may exist of itself or as an aggregation of partial units..
PARTIAL: A partial elementary unit."
  ~~Defines the level of element composition where.

COMPLEX: A set of elementary units aggregated together to fulfill the overall  required purpose.
ELEMENT: A single elementary unit that may exist of itself or as an aggregation of partial units..
PARTIAL: A partial elementary unit.~~ Defines the level of element composition where.\X\0D
\X\0D
COMPLEX: A set of elementary units aggregated together to fulfill the overall  required purpose.\X\0D
ELEMENT: A single elementary unit that may exist of itself or as an aggregation of partial units..\X\0D
PARTIAL: A partial elementary unit.
* PropertyDefs > PropertyDef [Name="TankComposition"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* 
  ~~PSET_OCCURRENCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="TankComposition"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_SpaceThermalLoad.xml
=========================

modifications
-------------
* PropertyDefs > PropertyDef [Name="RecirculatedAir"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="People"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Lighting"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="EquipmentSensible"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="AirExchangeRate"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="InfiltrationSensible"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="TotalRadiantLoad"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="VentilationOutdoorAir"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="ExhaustAir"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="TotalLatentLoad"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="RelativeHumidity"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="DryBulbTemperature"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="TotalSensibleLoad"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="VentilationIndoorAir"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;



Pset_PipeSegmentOccurrence.xml
==============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Color"] > Definition "The color of the pipe segment.

Note: This is typically used only for plastic pipe segments. However, it may be used for any pipe segments with a painted surface which is not otherwise specified as a covering."
  ~~The color of the pipe segment.

Note: This is typically used only for plastic pipe segments. However, it may be used for any pipe segments with a painted surface which is not otherwise specified as a covering.~~ The color of the pipe segment.\X\0D
\X\0D
Note: This is typically used only for plastic pipe segments. However, it may be used for any pipe segments with a painted surface which is not otherwise specified as a covering.
* 
  ~~PSET_OCCURRENCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE


Pset_FilterTypeCommon.xml
=========================

modifications
-------------
* PropertyDefs > PropertyDef [Name="FlowRateRange"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="OperationTemperatureRange"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Qto_FootingBaseQuantities.xml
=============================

modifications
-------------
* QtoDefs > QtoDef [Name="Height"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="CrossSectionArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Length"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossSurfaceArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetVolume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Width"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="OuterSurfaceArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossVolume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases


Qto_UnitaryControlElementBaseQuantities.xml
===========================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases



Pset_ProtectiveDeviceTrippingUnitTypeElectronic.xml
===================================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="ElectronicTrippingUnitType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="NominalCurrents"] > Definition "A set of values providing information on available modules (chips) for setting the nominal current of the protective device. If
the set is empty, no nominal current modules are available for the tripping unit."
  ~~A set of values providing information on available modules (chips) for setting the nominal current of the protective device. If
the set is empty, no nominal current modules are available for the tripping unit.~~ A set of values providing information on available modules (chips) for setting the nominal current of the protective device. If\X\0D
the set is empty, no nominal current modules are available for the tripping unit.
* PropertyDefs > PropertyDef [Name="NominalCurrents"] > PropertyType > TypePropertyListValue
  ~~TypePropertyListValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="NominalCurrents"] > PropertyType > TypePropertyListValue > ListValue
  ~~ListValue~~ DataType
* PropertyDefs > PropertyDef [Name="ElectronicTrippingUnitType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_CoolingTowerTypeCommon.xml
===============================

modifications
-------------
* Definition "Cooling tower type common attributes.
WaterRequirement attribute unit type modified in IFC2x2 Pset Addendum."
  ~~Cooling tower type common attributes.
WaterRequirement attribute unit type modified in IFC2x2 Pset Addendum.~~ Cooling tower type common attributes.\X\0D
WaterRequirement attribute unit type modified in IFC2x2 Pset Addendum.
* PropertyDefs > PropertyDef [Name="CapacityControl"] > Definition "FanCycling: Fan is cycled on and off to control duty.
TwoSpeedFan: Fan is switched between low and high speed to control duty.
VariableSpeedFan: Fan speed is varied to control duty.
DampersControl: Dampers modulate the air flow to control duty.
BypassValveControl: Bypass valve modulates the water flow to control duty.
MultipleSeriesPumps: Turn on/off multiple series pump to control duty.
TwoSpeedPump: Switch between high/low pump speed to control duty.
VariableSpeedPump: vary pump speed to control duty."
  ~~FanCycling: Fan is cycled on and off to control duty.
TwoSpeedFan: Fan is switched between low and high speed to control duty.
VariableSpeedFan: Fan speed is varied to control duty.
DampersControl: Dampers modulate the air flow to control duty.
BypassValveControl: Bypass valve modulates the water flow to control duty.
MultipleSeriesPumps: Turn on/off multiple series pump to control duty.
TwoSpeedPump: Switch between high/low pump speed to control duty.
VariableSpeedPump: vary pump speed to control duty.~~ FanCycling: Fan is cycled on and off to control duty.\X\0D
TwoSpeedFan: Fan is switched between low and high speed to control duty.\X\0D
VariableSpeedFan: Fan speed is varied to control duty.\X\0D
DampersControl: Dampers modulate the air flow to control duty.\X\0D
BypassValveControl: Bypass valve modulates the water flow to control duty.\X\0D
MultipleSeriesPumps: Turn on/off multiple series pump to control duty.\X\0D
TwoSpeedPump: Switch between high/low pump speed to control duty.\X\0D
VariableSpeedPump: vary pump speed to control duty.
* PropertyDefs > PropertyDef [Name="CapacityControl"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="CircuitType"] > Definition "OpenCircuit: Exposes water directly to the cooling atmosphere.
CloseCircuit: The fluid is separated from the atmosphere by a heat exchanger.
Wet: The air stream or the heat exchange surface is evaporatively cooled.
Dry: No evaporation into the air stream.
DryWet: A combination of a dry tower and a wet tower."
  ~~OpenCircuit: Exposes water directly to the cooling atmosphere.
CloseCircuit: The fluid is separated from the atmosphere by a heat exchanger.
Wet: The air stream or the heat exchange surface is evaporatively cooled.
Dry: No evaporation into the air stream.
DryWet: A combination of a dry tower and a wet tower.~~ OpenCircuit: Exposes water directly to the cooling atmosphere.\X\0D
CloseCircuit: The fluid is separated from the atmosphere by a heat exchanger.\X\0D
Wet: The air stream or the heat exchange surface is evaporatively cooled.\X\0D
Dry: No evaporation into the air stream.\X\0D
DryWet: A combination of a dry tower and a wet tower.
* PropertyDefs > PropertyDef [Name="CircuitType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="ControlStrategy"] > Definition "FixedExitingWaterTemp: The capacity is controlled to maintain a fixed exiting water temperature.
WetBulbTempReset: The set-point is reset based on the wet-bulb temperature."
  ~~FixedExitingWaterTemp: The capacity is controlled to maintain a fixed exiting water temperature.
WetBulbTempReset: The set-point is reset based on the wet-bulb temperature.~~ FixedExitingWaterTemp: The capacity is controlled to maintain a fixed exiting water temperature.\X\0D
WetBulbTempReset: The set-point is reset based on the wet-bulb temperature.
* PropertyDefs > PropertyDef [Name="ControlStrategy"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="FlowArrangement"] > Definition "CounterFlow: Air and water flow enter in different directions.
CrossFlow: Air and water flow are perpendicular.
ParallelFlow: air and water flow enter in same directions."
  ~~CounterFlow: Air and water flow enter in different directions.
CrossFlow: Air and water flow are perpendicular.
ParallelFlow: air and water flow enter in same directions.~~ CounterFlow: Air and water flow enter in different directions.\X\0D
CrossFlow: Air and water flow are perpendicular.\X\0D
ParallelFlow: air and water flow enter in same directions.
* PropertyDefs > PropertyDef [Name="FlowArrangement"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="SprayType"] > Definition "SprayFilled: Water is sprayed into airflow.
SplashTypeFill: water cascades over successive rows of splash bars.
FilmTypeFill: water flows in a thin layer over closely spaced sheets."
  ~~SprayFilled: Water is sprayed into airflow.
SplashTypeFill: water cascades over successive rows of splash bars.
FilmTypeFill: water flows in a thin layer over closely spaced sheets.~~ SprayFilled: Water is sprayed into airflow.\X\0D
SplashTypeFill: water cascades over successive rows of splash bars.\X\0D
FilmTypeFill: water flows in a thin layer over closely spaced sheets.
* PropertyDefs > PropertyDef [Name="SprayType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="ControlStrategy"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="SprayType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="CapacityControl"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="CircuitType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="FlowArrangement"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;



Pset_ElectricApplianceTypeDishwasher.xml
========================================

modifications
-------------
* PropertyDefs
  ~~PropertyDefs~~ ApplicableClasses
* ApplicableClasses
  ~~ApplicableClasses~~ ApplicableTypeValue
* ApplicableTypeValue "IfcElectricAppliance/DISHWASHER"
  ~~ApplicableTypeValue~~ PropertyDefs


Qto_CableCarrierSegmentBaseQuantities.xml
=========================================

modifications
-------------
* QtoDefs > QtoDef [Name="CrossSectionArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="OuterSurfaceArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Length"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases


Pset_ValveTypeFlushing.xml
==========================

modifications
-------------
* Definition "Valve that flushes a predetermined quantity of water to cleanse a WC, urinal or slop hopper.
Note that a flushing valve is constrained to have a 2 port  pattern."
  ~~Valve that flushes a predetermined quantity of water to cleanse a WC, urinal or slop hopper.
Note that a flushing valve is constrained to have a 2 port  pattern.~~ Valve that flushes a predetermined quantity of water to cleanse a WC, urinal or slop hopper.\X\0D
Note that a flushing valve is constrained to have a 2 port  pattern.


Qto_CableFittingBaseQuantities.xml
==================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Qto_SignalBaseQuantities.xml
============================

additions
---------
* Definition "$"

modifications
-------------
* QtoDefinitionAliases
  ~~QtoDefinitionAliases~~ ApplicableTypeValue


Pset_ProtectiveDeviceTrippingFunctionLCurve.xml
===============================================

modifications
-------------
* Definition "Tripping functions are applied to electronic tripping units (i.e. tripping units having type property sets for electronic tripping defined). They are not applied to thermal, thermal magnetic or RCD tripping units.
This property set represent the long time protection (L-curve) of an electronic protection device"
  ~~Tripping functions are applied to electronic tripping units (i.e. tripping units having type property sets for electronic tripping defined). They are not applied to thermal, thermal magnetic or RCD tripping units.
This property set represent the long time protection (L-curve) of an electronic protection device~~ Tripping functions are applied to electronic tripping units (i.e. tripping units having type property sets for electronic tripping defined). They are not applied to thermal, thermal magnetic or RCD tripping units.\X\0D
This property set represent the long time protection (L-curve) of an electronic protection device


Pset_SwitchingDeviceTypeStarter.xml
===================================

modifications
-------------
* PropertyDefs
  ~~PropertyDefs~~ ApplicableClasses
* ApplicableClasses
  ~~ApplicableClasses~~ ApplicableTypeValue
* ApplicableTypeValue "IfcSwitchingDevice/STARTER"
  ~~ApplicableTypeValue~~ PropertyDefs


Pset_HumidifierTypeCommon.xml
=============================

additions
---------
* PropertyDefs > PropertyDef [Name="SaturationEfficiencyCurve"]

modifications
-------------
* Definition "Humidifier type common attributes.
WaterProperties attribute renamed to WaterRequirement and unit type modified in IFC2x2 Pset Addendum."
  ~~Humidifier type common attributes.
WaterProperties attribute renamed to WaterRequirement and unit type modified in IFC2x2 Pset Addendum.~~ Humidifier type common attributes.\X\0D
WaterProperties attribute renamed to WaterRequirement and unit type modified in IFC2x2 Pset Addendum.
* PropertyDefs > PropertyDef [Name="AirPressureDropCurve"] > PropertyType > TypePropertyTableValue
  ~~TypePropertyTableValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Application"] > Definition "Humidifier application.

Fixed: Humidifier installed in a ducted flow distribution system.
Portable: Humidifier is not installed in a ducted flow distribution system."
  ~~Humidifier application.

Fixed: Humidifier installed in a ducted flow distribution system.
Portable: Humidifier is not installed in a ducted flow distribution system.~~ Humidifier application.\X\0D
\X\0D
Fixed: Humidifier installed in a ducted flow distribution system.\X\0D
Portable: Humidifier is not installed in a ducted flow distribution system.
* PropertyDefs > PropertyDef [Name="Application"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="InternalControl"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="InternalControl"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="AirPressureDropCurve"] > PropertyType > TypePropertyTableValue > Expression
  ~~&lt;Expression&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="Application"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="AirPressureDropCurve"] > PropertyType > TypePropertyTableValue > DefiningValue
* PropertyDefs > PropertyDef [Name="AirPressureDropCurve"] > PropertyType > TypePropertyTableValue > DefinedValue
* PropertyDefs > PropertyDef [Name="SaturationEfficiencyCurve"]



Pset_SoundGeneration.xml
========================

modifications
-------------
* PropertyDefs > PropertyDef [Name="SoundCurve"] > PropertyType
  ~~PropertyType~~ Definition
* PropertyDefs > PropertyDef [Name="SoundCurve"] > Definition "Table of sound frequencies and sound power measured in decibels at a reference power of 1 picowatt(10\^(-12) watt) for the referenced octave band frequency."
  ~~Definition~~ PropertyType


Pset_ProtectiveDeviceTrippingFunctionSCurve.xml
===============================================

modifications
-------------
* Definition "Tripping functions are applied to electronic tripping units (i.e. tripping units having type property sets for electronic tripping defined). They are not applied to thermal, thermal magnetic or RCD tripping units.
This property set represent the short time protection (S-curve) of an electronic protection device."
  ~~Tripping functions are applied to electronic tripping units (i.e. tripping units having type property sets for electronic tripping defined). They are not applied to thermal, thermal magnetic or RCD tripping units.
This property set represent the short time protection (S-curve) of an electronic protection device.~~ Tripping functions are applied to electronic tripping units (i.e. tripping units having type property sets for electronic tripping defined). They are not applied to thermal, thermal magnetic or RCD tripping units.\X\0D
This property set represent the short time protection (S-curve) of an electronic protection device.


Pset_CondenserPHistory.xml
==========================

modifications
-------------
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="CompressorCondenserHeatGain"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="InteriorHeatTransferCoefficient"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="ExteriorHeatTransferCoefficient"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="UAcurves"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="CompressorCondenserPressureDrop"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="HeatRejectionRate"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="CondenserMeanVoidFraction"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="RefrigerantFoulingResistance"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="CondensingTemperature"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="LogarithmicMeanTemperatureDifference"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="WaterFoulingResistance"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Pset_PavementMillingCommon.xml
==============================

modifications
-------------
* ApplicableClasses > ClassName "IfcEarthworksCut/(.PAVEMENTMILLING.)"
  ~~IfcEarthworksCut/(.PAVEMENTMILLING.)~~ IfcTask
* ApplicableTypeValue "IfcEarthworksCut/(.PAVEMENTMILLING.)"
  ~~IfcEarthworksCut/(.PAVEMENTMILLING.)~~ IfcTask


Pset_ProtectiveDeviceTypeCircuitBreaker.xml
===========================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="PerformanceClasses"] > Definition "A set of designations of performance classes for the breaker unit for which the data of this instance is valid. A breaker unit being a circuit breaker may be
constructed for different levels of breaking capacities. A maximum of 7 different
performance classes may be provided. Examples of performance classes that may be specified include B, C, N, S, H, L, V."
  ~~A set of designations of performance classes for the breaker unit for which the data of this instance is valid. A breaker unit being a circuit breaker may be
constructed for different levels of breaking capacities. A maximum of 7 different
performance classes may be provided. Examples of performance classes that may be specified include B, C, N, S, H, L, V.~~ A set of designations of performance classes for the breaker unit for which the data of this instance is valid. A breaker unit being a circuit breaker may be\X\0D
constructed for different levels of breaking capacities. A maximum of 7 different\X\0D
performance classes may be provided. Examples of performance classes that may be specified include B, C, N, S, H, L, V.
* PropertyDefs > PropertyDef [Name="PerformanceClasses"] > PropertyType > TypePropertyListValue
  ~~TypePropertyListValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="PerformanceClasses"] > PropertyType > TypePropertyListValue > ListValue
  ~~ListValue~~ DataType
* PropertyDefs > PropertyDef [Name="VoltageLevel"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="VoltageLevel"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_StackTerminalTypeCommon.xml
================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_SwitchingDeviceTypeToggleSwitch.xml
========================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="SwitchActivation"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="SwitchUsage"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="ToggleSwitchType"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Pset_SystemFurnitureElementTypePanel.xml
========================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="FurniturePanelType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="FurniturePanelType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="NominalThickness"]


Pset_AlarmTypeCommon.xml
========================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Condition"] > PropertyType > TypePropertyTableValue
  ~~TypePropertyTableValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Condition"] > PropertyType > TypePropertyTableValue > Expression
  ~~&lt;Expression&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="Condition"] > PropertyType > TypePropertyTableValue > DefiningValue
* PropertyDefs > PropertyDef [Name="Condition"] > PropertyType > TypePropertyTableValue > DefinedValue



Pset_StairCommon.xml
====================

modifications
-------------
* PropertyDefs > PropertyDef [Name="FireExit"] > Definition "Indication whether this object is designed to serve as an exit in the case of fire (TRUE) or not (FALSE).
Here it defines an exit stair in accordance to the national building code."
  ~~Indication whether this object is designed to serve as an exit in the case of fire (TRUE) or not (FALSE).
Here it defines an exit stair in accordance to the national building code.~~ Indication whether this object is designed to serve as an exit in the case of fire (TRUE) or not (FALSE).\X\0D
Here it defines an exit stair in accordance to the national building code.
* PropertyDefs > PropertyDef [Name="FireRating"] > Definition "Fire rating for this object.
It is given according to the national fire safety classification."
  ~~Fire rating for this object.
It is given according to the national fire safety classification.~~ Fire rating for this object.\X\0D
It is given according to the national fire safety classification.
* PropertyDefs > PropertyDef [Name="HandicapAccessible"] > Definition "Indication that this object is designed to be accessible by the handicapped. 
Set to (TRUE) if this stair is rated as handicap accessible  according the local building codes, otherwise (FALSE). Accessibility maybe provided by additional means."
  ~~Indication that this object is designed to be accessible by the handicapped. 
Set to (TRUE) if this stair is rated as handicap accessible  according the local building codes, otherwise (FALSE). Accessibility maybe provided by additional means.~~ Indication that this object is designed to be accessible by the handicapped. \X\0D
Set to (TRUE) if this stair is rated as handicap accessible  according the local building codes, otherwise (FALSE). Accessibility maybe provided by additional means.
* PropertyDefs > PropertyDef [Name="LoadBearing"] > PropertyType
  ~~PropertyType~~ Definition
* PropertyDefs > PropertyDef [Name="RiserHeight"] > Definition "Vertical distance from tread to tread. 
The riser height is supposed to be equal for all steps of a stair or stair flight."
  ~~Vertical distance from tread to tread. 
The riser height is supposed to be equal for all steps of a stair or stair flight.~~ Vertical distance from tread to tread. \X\0D
The riser height is supposed to be equal for all steps of a stair or stair flight.
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="ThermalTransmittance"] > PropertyType
  ~~PropertyType~~ Definition
* PropertyDefs > PropertyDef [Name="TreadLength"] > Definition "Horizontal distance from the front of the thread to the front of the next tread. 
The tread length is supposed to be equal for all steps of the stair or stair flight at the walking line."
  ~~Horizontal distance from the front of the thread to the front of the next tread. 
The tread length is supposed to be equal for all steps of the stair or stair flight at the walking line.~~ Horizontal distance from the front of the thread to the front of the next tread. \X\0D
The tread length is supposed to be equal for all steps of the stair or stair flight at the walking line.
* PropertyDefs > PropertyDef [Name="TreadLengthAtInnerSide"] > Definition "Minimum length of treads at the inner side of the winder. 
Only relevant in case of winding flights, for straight flights it is identical with IfcStairFlight.TreadLength. It is a pre-calculated value, in case of inconsistencies, the value derived from the shape representation shall take precedence."
  ~~Minimum length of treads at the inner side of the winder. 
Only relevant in case of winding flights, for straight flights it is identical with IfcStairFlight.TreadLength. It is a pre-calculated value, in case of inconsistencies, the value derived from the shape representation shall take precedence.~~ Minimum length of treads at the inner side of the winder. \X\0D
Only relevant in case of winding flights, for straight flights it is identical with IfcStairFlight.TreadLength. It is a pre-calculated value, in case of inconsistencies, the value derived from the shape representation shall take precedence.
* PropertyDefs > PropertyDef [Name="TreadLengthAtOffset"] > Definition "Length of treads at a given offset.
Walking line position is given by the 'WalkingLineOffset'. The resulting value should normally be identical with TreadLength, it may be given in addition, if the walking line offset for building code calculations is different from that used in design."
  ~~Length of treads at a given offset.
Walking line position is given by the 'WalkingLineOffset'. The resulting value should normally be identical with TreadLength, it may be given in addition, if the walking line offset for building code calculations is different from that used in design.~~ Length of treads at a given offset.\X\0D
Walking line position is given by the 'WalkingLineOffset'. The resulting value should normally be identical with TreadLength, it may be given in addition, if the walking line offset for building code calculations is different from that used in design.
* PropertyDefs > PropertyDef [Name="WalkingLineOffset"] > Definition "Offset of the walking line from the inner side of the flight. 
Note: the walking line may have a own shape representation (in case of inconsistencies, the value derived from the shape representation shall take precedence)."
  ~~Offset of the walking line from the inner side of the flight. 
Note: the walking line may have a own shape representation (in case of inconsistencies, the value derived from the shape representation shall take precedence).~~ Offset of the walking line from the inner side of the flight. \X\0D
Note: the walking line may have a own shape representation (in case of inconsistencies, the value derived from the shape representation shall take precedence).
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;



Pset_DiscreteAccessoryFixingSocket.xml
======================================

modifications
-------------
* ApplicableClasses > ClassName "IfcDiscreteAccessory/Fixing socket"
  ~~IfcDiscreteAccessory/Fixing socket~~ IfcDiscreteAccessory
* ApplicableTypeValue "IfcDiscreteAccessory/Fixing socket"
  ~~IfcDiscreteAccessory/Fixing socket~~ IfcDiscreteAccessory

deletions
---------
* PropertyDefs > PropertyDef [Name="FixingSocketTypeReference"] > PropertyType


Qto_AirToAirHeatRecoveryBaseQuantities.xml
==========================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Pset_UnitaryEquipmentTypeCommon.xml
===================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_ActuatorTypeElectricActuator.xml
=====================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="ElectricActuatorType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="ElectricActuatorType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_FanCentrifugal.xml
=======================

modifications
-------------
* ApplicableClasses > ClassName "IfcFan/CENTRIFUGAL"
  ~~IfcFan/CENTRIFUGAL~~ IfcFan
* ApplicableTypeValue "IfcFan/CENTRIFUGAL"
  ~~IfcFan/CENTRIFUGAL~~ IfcFan
* PropertyDefs > PropertyDef [Name="DirectionOfRotation"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Arrangement"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="DischargePosition"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Pset_AlignmentCantSegmentCommon.xml
===================================

modifications
-------------
* 
  ~~PSET_OCCURRENCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE


Qto_UnitaryEquipmentBaseQuantities.xml
======================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases



Qto_WasteTerminalBaseQuantities.xml
===================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Pset_BoilerTypeWater.xml
========================

modifications
-------------
* PropertyDefs > PropertyDef [Name="HeatOutput"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="NominalEfficiency"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Qto_ValveBaseQuantities.xml
===========================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Pset_SanitaryTerminalTypeBath.xml
=================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="BathType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="BathType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Qto_AirTerminalBaseQuantities.xml
=================================

modifications
-------------
* QtoDefs > QtoDef [Name="GrossWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="TotalSurfaceArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Perimeter"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases




Pset_DistributionChamberElementCommon.xml
=========================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_SensorPHistory.xml
=======================

modifications
-------------
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="Status"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Quality"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Value"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Direction"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Pset_WasteTerminalTypeFloorTrap.xml
===================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="InletConnectionSize"] > Definition "Size of the inlet connection(s), where used, of the inlet connections.

Note that all inlet connections are assumed to be the same size."
  ~~Size of the inlet connection(s), where used, of the inlet connections.

Note that all inlet connections are assumed to be the same size.~~ Size of the inlet connection(s), where used, of the inlet connections.\X\0D
\X\0D
Note that all inlet connections are assumed to be the same size.
* PropertyDefs > PropertyDef [Name="InletPatternType"] > Definition "Identifies the pattern of inlet connections to a trap.

A trap may have 0,1,2,3 or 4 inlet connections and the pattern of their arrangement may vary. The enumeration makes the convention that an outlet is either vertical or is placed at the bottom (south side) of the trap (when viewed in plan). Position 1 is to the left (west), position 2 is to the top (north), position 3 is to the right (east) and position 4 is to the bottom (south)."
  ~~Identifies the pattern of inlet connections to a trap.

A trap may have 0,1,2,3 or 4 inlet connections and the pattern of their arrangement may vary. The enumeration makes the convention that an outlet is either vertical or is placed at the bottom (south side) of the trap (when viewed in plan). Position 1 is to the left (west), position 2 is to the top (north), position 3 is to the right (east) and position 4 is to the bottom (south).~~ Identifies the pattern of inlet connections to a trap.\X\0D
\X\0D
A trap may have 0,1,2,3 or 4 inlet connections and the pattern of their arrangement may vary. The enumeration makes the convention that an outlet is either vertical or is placed at the bottom (south side) of the trap (when viewed in plan). Position 1 is to the left (west), position 2 is to the top (north), position 3 is to the right (east) and position 4 is to the bottom (south).
* PropertyDefs > PropertyDef [Name="InletPatternType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="TrapType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="InletPatternType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="TrapType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="CoverMaterial"] > PropertyType


Pset_SwitchingDeviceTypeContactor.xml
=====================================

modifications
-------------
* PropertyDefs
  ~~PropertyDefs~~ ApplicableClasses
* ApplicableClasses
  ~~ApplicableClasses~~ ApplicableTypeValue
* ApplicableTypeValue "IfcSwitchingDevice/CONTACTOR"
  ~~ApplicableTypeValue~~ PropertyDefs


Qto_DamperBaseQuantities.xml
============================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Qto_SanitaryTerminalBaseQuantities.xml
======================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases



Qto_EarthworksCutBaseQuantities.xml
===================================

additions
---------
* Definition "$"

modifications
-------------
* QtoDefinitionAliases
  ~~QtoDefinitionAliases~~ ApplicableTypeValue
* QtoDefs > QtoDef [Name="Length"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Width"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefs > QtoDef [Name="Depth"]
* QtoDefs > QtoDef [Name="UndisturbedVolume"]
* QtoDefs > QtoDef [Name="LooseVolume"]
* QtoDefs > QtoDef [Name="Weight"]


Pset_UnitaryEquipmentTypeAirHandler.xml
=======================================

modifications
-------------
* Definition "Air handler unitary equipment type attributes.
Note that these attributes were formerly Pset_AirHandler prior to IFC2x2."
  ~~Air handler unitary equipment type attributes.
Note that these attributes were formerly Pset_AirHandler prior to IFC2x2.~~ Air handler unitary equipment type attributes.\X\0D
Note that these attributes were formerly Pset_AirHandler prior to IFC2x2.
* PropertyDefs > PropertyDef [Name="AirHandlerConstruction"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="AirHandlerFanCoilArrangement"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="AirHandlerConstruction"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="AirHandlerFanCoilArrangement"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_ActuatorTypeLinearActuation.xml
====================================

modifications
-------------
* Definition "Characteristics of linear actuation of an actuator
History: Replaces Pset_LinearActuator"
  ~~Characteristics of linear actuation of an actuator
History: Replaces Pset_LinearActuator~~ Characteristics of linear actuation of an actuator\X\0D
History: Replaces Pset_LinearActuator


Pset_SpaceHeaterTypeConvector.xml
=================================

modifications
-------------
* PropertyDefs
  ~~PropertyDefs~~ ApplicableClasses
* ApplicableClasses
  ~~ApplicableClasses~~ ApplicableTypeValue
* ApplicableTypeValue "IfcSpaceHeater/CONVECTOR"
  ~~ApplicableTypeValue~~ PropertyDefs


Pset_OpeningElementCommon.xml
=============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="FireExit"] > Definition "Indication whether this object is designed to serve as an exit in the case of fire (TRUE) or not (FALSE).
Here whether the space (in case of e.g., a corridor) is designed to serve as an exit space, e.g., for fire escape purposes."
  ~~Indication whether this object is designed to serve as an exit in the case of fire (TRUE) or not (FALSE).
Here whether the space (in case of e.g., a corridor) is designed to serve as an exit space, e.g., for fire escape purposes.~~ Indication whether this object is designed to serve as an exit in the case of fire (TRUE) or not (FALSE).\X\0D
Here whether the space (in case of e.g., a corridor) is designed to serve as an exit space, e.g., for fire escape purposes.
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;




Pset_DistributionBoardOccurrence.xml
====================================

modifications
-------------
* 
  ~~PSET_OCCURRENCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE


Pset_TrenchExcavationCommon.xml
===============================

modifications
-------------
* ApplicableClasses > ClassName "IfcEarthworksCut/(.TRENCH.)"
  ~~IfcEarthworksCut/(.TRENCH.)~~ IfcTransportElement
* ApplicableTypeValue "IfcEarthworksCut/(.TRENCH.)"
  ~~IfcEarthworksCut/(.TRENCH.)~~ IfcTransportElement


Pset_FanPHistory.xml
====================

modifications
-------------
* Definition "Fan performance history attributes.
Sound attribute deleted in IFC2x2 Pset Addendum: Use IfcSoundProperties instead."
  ~~Fan performance history attributes.
Sound attribute deleted in IFC2x2 Pset Addendum: Use IfcSoundProperties instead.~~ Fan performance history attributes.\X\0D
Sound attribute deleted in IFC2x2 Pset Addendum: Use IfcSoundProperties instead.
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="DischargePressureLoss"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="FanPowerRate"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="FanEfficiency"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="FanRotationSpeed"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="OverallEfficiency"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="DrivePowerLoss"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="WheelTipSpeed"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="DischargeVelocity"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="ShaftPowerRate"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Qto_OpeningElementBaseQuantities.xml
====================================

modifications
-------------
* QtoDefs > QtoDef [Name="Width"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Volume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Depth"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Area"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Height"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases


Pset_DuctFittingTypeCommon.xml
==============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="PressureRange"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="TemperatureRange"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_SensorTypeMoistureSensor.xml
=================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="SetPointMoisture"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue


Pset_FireSuppressionTerminalTypeBreechingInlet.xml
==================================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="BreechingInletType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="CouplingType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="CouplingType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="BreechingInletType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;



Qto_SensorBaseQuantities.xml
============================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Pset_AirTerminalOccurrence.xml
==============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Location"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* 
  ~~PSET_OCCURRENCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="Location"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="AirflowType"] > PropertyType


Pset_RoofCommon.xml
===================

modifications
-------------
* PropertyDefs > PropertyDef [Name="AcousticRating"] > Definition "Acoustic rating for this object.
It is provided according to the national building code. It indicates the sound transmission resistance of this object by an index ratio (instead of providing full sound absorbtion values)."
  ~~Acoustic rating for this object.
It is provided according to the national building code. It indicates the sound transmission resistance of this object by an index ratio (instead of providing full sound absorbtion values).~~ Acoustic rating for this object.\X\0D
It is provided according to the national building code. It indicates the sound transmission resistance of this object by an index ratio (instead of providing full sound absorbtion values).
* PropertyDefs > PropertyDef [Name="LoadBearing"] > PropertyType
  ~~PropertyType~~ Definition
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="ThermalTransmittance"] > Definition "Thermal transmittance coefficient (U-Value) of a material.
Here the total thermal transmittance coefficient through the roof surface (including all materials)."
  ~~Thermal transmittance coefficient (U-Value) of a material.
Here the total thermal transmittance coefficient through the roof surface (including all materials).~~ Thermal transmittance coefficient (U-Value) of a material.\X\0D
Here the total thermal transmittance coefficient through the roof surface (including all materials).
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_ValveTypeIsolating.xml
===========================

modifications
-------------
* Definition "Valve that is used to isolate system components.
Note that an isolating valve is constrained to have a 2 port  pattern."
  ~~Valve that is used to isolate system components.
Note that an isolating valve is constrained to have a 2 port  pattern.~~ Valve that is used to isolate system components.\X\0D
Note that an isolating valve is constrained to have a 2 port  pattern.
* PropertyDefs > PropertyDef [Name="IsolatingPurpose"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="IsolatingPurpose"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_FlowMeterOccurrence.xml
============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Purpose"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* 
  ~~PSET_OCCURRENCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="Purpose"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_FlowInstrumentTypeCommon.xml
=================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_Tolerance.xml
==================

modifications
-------------
* ApplicableTypeValue "IfcProduct,IfcTypeProduct"
  ~~IfcProduct,IfcTypeProduct~~ IfcTypeProduct
* PropertyDefs > PropertyDef [Name="ToleranceBasis"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="ToleranceBasis"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_FilterPHistory.xml
=======================

modifications
-------------
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="ParticleMassHolding"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="WeightedEfficiency"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="CountedEfficiency"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Pset_ProtectiveDeviceTrippingFunctionICurve.xml
===============================================

modifications
-------------
* Definition "Tripping functions are applied to electronic tripping units (i.e. tripping units having type property sets for electronic tripping defined). They are not applied to thermal, thermal magnetic or RCD tripping units.
This property set represent the instantaneous time protection (I-curve) of an electronic protection device."
  ~~Tripping functions are applied to electronic tripping units (i.e. tripping units having type property sets for electronic tripping defined). They are not applied to thermal, thermal magnetic or RCD tripping units.
This property set represent the instantaneous time protection (I-curve) of an electronic protection device.~~ Tripping functions are applied to electronic tripping units (i.e. tripping units having type property sets for electronic tripping defined). They are not applied to thermal, thermal magnetic or RCD tripping units.\X\0D
This property set represent the instantaneous time protection (I-curve) of an electronic protection device.
* PropertyDefs > PropertyDef [Name="MaxAdjustmentX_ICS"] > Definition "Provides the maximum setting value for the available current adjustment in relation to the
Ics breaking capacity of the protection device of which the actual tripping unit is a part of. The value is not asserted unless the instantaneous time protection is."
  ~~Provides the maximum setting value for the available current adjustment in relation to the
Ics breaking capacity of the protection device of which the actual tripping unit is a part of. The value is not asserted unless the instantaneous time protection is.~~ Provides the maximum setting value for the available current adjustment in relation to the\X\0D
Ics breaking capacity of the protection device of which the actual tripping unit is a part of. The value is not asserted unless the instantaneous time protection is.


Pset_ProtectiveDeviceTrippingUnitTypeCommon.xml
===============================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Standard"] > Definition "The designation of the standard applicable for the definition of the characteristics of the
tripping_unit."
  ~~The designation of the standard applicable for the definition of the characteristics of the
tripping_unit.~~ The designation of the standard applicable for the definition of the characteristics of the\X\0D
tripping_unit.
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="UseInDiscrimination"] > Definition "An indication whether the time/current tripping information can be applied in a discrimination
analysis or not."
  ~~An indication whether the time/current tripping information can be applied in a discrimination
analysis or not.~~ An indication whether the time/current tripping information can be applied in a discrimination\X\0D
analysis or not.
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_EnvironmentalImpactValues.xml
==================================

modifications
-------------
* Definition "The following properties capture environmental impact values of an element. They correspond to the indicators defined into Pset_EnvironmentalImpactIndicators. 
Environmental impact values are obtained multiplying indicator value per unit by the relevant quantity of the element."
  ~~The following properties capture environmental impact values of an element. They correspond to the indicators defined into Pset_EnvironmentalImpactIndicators. 
Environmental impact values are obtained multiplying indicator value per unit by the relevant quantity of the element.~~ The following properties capture environmental impact values of an element. They correspond to the indicators defined into Pset_EnvironmentalImpactIndicators. \X\0D
Environmental impact values are obtained multiplying indicator value per unit by the relevant quantity of the element.


Qto_TankBaseQuantities.xml
==========================

modifications
-------------
* QtoDefs > QtoDef [Name="NetWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="TotalSurfaceArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases


Pset_ShiplockDesignCriteria.xml
===============================

modifications
-------------
* ApplicableClasses > ClassName "IfcMarineFacility/SHIPLOCK"
  ~~IfcMarineFacility/SHIPLOCK~~ IfcMarineFacility
* ApplicableTypeValue "IfcMarineFacility/SHIPLOCK"
  ~~IfcMarineFacility/SHIPLOCK~~ IfcMarineFacility


Pset_DiscreteAccessoryCornerFixingPlate.xml
===========================================

modifications
-------------
* ApplicableClasses > ClassName "IfcDiscreteAccessory/Corner fixing plate"
  ~~IfcDiscreteAccessory/Corner fixing plate~~ IfcDiscreteAccessory
* ApplicableTypeValue "IfcDiscreteAccessory/Corner fixing plate"
  ~~IfcDiscreteAccessory/Corner fixing plate~~ IfcDiscreteAccessory


Pset_BuildingElementProxyCommon.xml
===================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="FireRating"] > Definition "Fire rating for the element.
It is given according to the national fire safety classification."
  ~~Fire rating for the element.
It is given according to the national fire safety classification.~~ Fire rating for the element.\X\0D
It is given according to the national fire safety classification.
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="ThermalTransmittance"] > Definition "Thermal transmittance coefficient (U-Value) of the element. It is the total thermal transmittance coefficient through the building element proxy within the direction of the thermal flow (including all materials).

Note: new property in IFC4"
  ~~Thermal transmittance coefficient (U-Value) of the element. It is the total thermal transmittance coefficient through the building element proxy within the direction of the thermal flow (including all materials).

Note: new property in IFC4~~ Thermal transmittance coefficient (U-Value) of the element. It is the total thermal transmittance coefficient through the building element proxy within the direction of the thermal flow (including all materials).\X\0D
\X\0D
Note: new property in IFC4
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_FilterTypeAirParticleFilter.xml
====================================

additions
---------
* PropertyDefs > PropertyDef [Name="WeightedEfficiencyCurve"]

modifications
-------------
* PropertyDefs > PropertyDef [Name="AirParticleFilterType"] > Definition "A panel dry type extended surface filter is a dry-type air filter with random fiber mats or blankets in the forms of pockets, V-shaped or radial pleats, and include the following:

CoarseFilter: Filter with a efficiency lower than 30% for atmosphere dust-spot.
CoarseMetalScreen: Filter made of metal screen.
CoarseCellFoams: Filter made of cell foams.
CoarseSpunGlass: Filter made of spun glass.
MediumFilter: Filter with an efficiency between 30-98% for atmosphere dust-spot.
MediumElectretFilter: Filter with fine electret synthetic fibers.
MediumNaturalFiberFilter: Filter with natural fibers.
HEPAFilter: High efficiency particulate air filter.
ULPAFilter: Ultra low penetration air filter.
MembraneFilters: Filter made of membrane for certain pore diameters in flat sheet and pleated form.
A renewable media with a moving curtain viscous filter are random-fiber media coated with viscous substance in roll form or curtain where fresh media is fed across the face of the filter and the dirty media is rewound onto a roll at the bottom or to into a reservoir:
RollForm: Viscous filter used in roll form.
AdhesiveReservoir: Viscous filter used in moving curtain form.
A renewable moving curtain dry media filter is a random-fiber dry media of relatively high porosity used in moving-curtain(roll) filters.
An electrical filter uses electrostatic precipitation to remove and collect particulate contaminants."
  ~~A panel dry type extended surface filter is a dry-type air filter with random fiber mats or blankets in the forms of pockets, V-shaped or radial pleats, and include the following:

CoarseFilter: Filter with a efficiency lower than 30% for atmosphere dust-spot.
CoarseMetalScreen: Filter made of metal screen.
CoarseCellFoams: Filter made of cell foams.
CoarseSpunGlass: Filter made of spun glass.
MediumFilter: Filter with an efficiency between 30-98% for atmosphere dust-spot.
MediumElectretFilter: Filter with fine electret synthetic fibers.
MediumNaturalFiberFilter: Filter with natural fibers.
HEPAFilter: High efficiency particulate air filter.
ULPAFilter: Ultra low penetration air filter.
MembraneFilters: Filter made of membrane for certain pore diameters in flat sheet and pleated form.
A renewable media with a moving curtain viscous filter are random-fiber media coated with viscous substance in roll form or curtain where fresh media is fed across the face of the filter and the dirty media is rewound onto a roll at the bottom or to into a reservoir:
RollForm: Viscous filter used in roll form.
AdhesiveReservoir: Viscous filter used in moving curtain form.
A renewable moving curtain dry media filter is a random-fiber dry media of relatively high porosity used in moving-curtain(roll) filters.
An electrical filter uses electrostatic precipitation to remove and collect particulate contaminants.~~ A panel dry type extended surface filter is a dry-type air filter with random fiber mats or blankets in the forms of pockets, V-shaped or radial pleats, and include the following:\X\0D
\X\0D
CoarseFilter: Filter with a efficiency lower than 30% for atmosphere dust-spot.\X\0D
CoarseMetalScreen: Filter made of metal screen.\X\0D
CoarseCellFoams: Filter made of cell foams.\X\0D
CoarseSpunGlass: Filter made of spun glass.\X\0D
MediumFilter: Filter with an efficiency between 30-98% for atmosphere dust-spot.\X\0D
MediumElectretFilter: Filter with fine electret synthetic fibers.\X\0D
MediumNaturalFiberFilter: Filter with natural fibers.\X\0D
HEPAFilter: High efficiency particulate air filter.\X\0D
ULPAFilter: Ultra low penetration air filter.\X\0D
MembraneFilters: Filter made of membrane for certain pore diameters in flat sheet and pleated form.\X\0D
A renewable media with a moving curtain viscous filter are random-fiber media coated with viscous substance in roll form or curtain where fresh media is fed across the face of the filter and the dirty media is rewound onto a roll at the bottom or to into a reservoir:\X\0D
RollForm: Viscous filter used in roll form.\X\0D
AdhesiveReservoir: Viscous filter used in moving curtain form.\X\0D
A renewable moving curtain dry media filter is a random-fiber dry media of relatively high porosity used in moving-curtain(roll) filters.\X\0D
An electrical filter uses electrostatic precipitation to remove and collect particulate contaminants.
* PropertyDefs > PropertyDef [Name="AirParticleFilterType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="SeparationType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="WeightedEfficiencyCurve"] > Definition "Weighted efficiency curve as a function of dust holding weight, efficiency = f (dust holding weight)."
  ~~&lt;Definition&gt;~~ &lt;Definition&gt;
* PropertyDefs > PropertyDef [Name="AirParticleFilterType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="WeightedEfficiencyCurve"] > PropertyType
  ~~&lt;PropertyType&gt;~~ &lt;PropertyType&gt;
* PropertyDefs > PropertyDef [Name="SeparationType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="PressureDropCurve"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="WeightedEfficiencyCurve"] > Name "WeightedEfficiencyCurve"
  ~~&lt;Name&gt;~~ &lt;Name&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="FrameMaterial"] > PropertyType
* PropertyDefs > PropertyDef [Name="CountedEfficiencyCurve"]


Pset_DiscreteAccessoryEdgeFixingPlate.xml
=========================================

modifications
-------------
* ApplicableClasses > ClassName "IfcDiscreteAccessory/Edge fixing plate"
  ~~IfcDiscreteAccessory/Edge fixing plate~~ IfcDiscreteAccessory
* ApplicableTypeValue "IfcDiscreteAccessory/Edge fixing plate"
  ~~IfcDiscreteAccessory/Edge fixing plate~~ IfcDiscreteAccessory


Pset_ProtectiveDeviceBreakerUnitTypeMotorProtection.xml
=======================================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="PerformanceClasses"] > Definition "A set of designations of performance classes for the breaker unit for which the data of this instance is valid. A breaker unit being a motor protection device may be
constructed for different levels of breaking capacities. A maximum of 7 different
performance classes may be provided. Examples of performance classes that may be specified include B, C, N, S, H, L, V."
  ~~A set of designations of performance classes for the breaker unit for which the data of this instance is valid. A breaker unit being a motor protection device may be
constructed for different levels of breaking capacities. A maximum of 7 different
performance classes may be provided. Examples of performance classes that may be specified include B, C, N, S, H, L, V.~~ A set of designations of performance classes for the breaker unit for which the data of this instance is valid. A breaker unit being a motor protection device may be\X\0D
constructed for different levels of breaking capacities. A maximum of 7 different\X\0D
performance classes may be provided. Examples of performance classes that may be specified include B, C, N, S, H, L, V.
* PropertyDefs > PropertyDef [Name="PerformanceClasses"] > PropertyType > TypePropertyListValue
  ~~TypePropertyListValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="PerformanceClasses"] > PropertyType > TypePropertyListValue > ListValue
  ~~ListValue~~ DataType
* PropertyDefs > PropertyDef [Name="VoltageLevel"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="VoltageLevel"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_AirTerminalPHistory.xml
============================

modifications
-------------
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="PressureDrop"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="NeckAirVelocity"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="AirFlowRate"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="SupplyAirTemperatureHeating"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="SupplyAirTemperatureCooling"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="CenterlineAirVelocity"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="InductionRatio"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Pset_FurnitureTypeCommon.xml
============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="NominalDepth"] > Definition "Nominal Depth of the object"
  ~~&lt;Definition&gt;~~ &lt;Definition&gt;
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType
  ~~&lt;PropertyType&gt;~~ &lt;Definition&gt;
* PropertyDefs > PropertyDef [Name="NominalDepth"] > Name "NominalDepth"
  ~~&lt;Name&gt;~~ &lt;Name&gt;
* PropertyDefs > PropertyDef [Name="Status"] > Name "Status"
  ~~&lt;Name&gt;~~ &lt;Name&gt;
* PropertyDefs > PropertyDef [Name="NominalDepth"] > PropertyType
  ~~&lt;PropertyType&gt;~~ &lt;PropertyType&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="Reference"]
* PropertyDefs > PropertyDef [Name="NominalLength"]


Pset_DistributionChamberElementTypeFormedDuct.xml
=================================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="BaseThickness"] > Definition "The thickness of the duct base construction
NOTE: It is assumed that duct base will be constructed at a single thickness."
  ~~The thickness of the duct base construction
NOTE: It is assumed that duct base will be constructed at a single thickness.~~ The thickness of the duct base construction\X\0D
NOTE: It is assumed that duct base will be constructed at a single thickness.
* PropertyDefs > PropertyDef [Name="WallThickness"] > Definition "The thickness of the duct wall construction
NOTE: It is assumed that chamber walls will be constructed at a single thickness."
  ~~The thickness of the duct wall construction
NOTE: It is assumed that chamber walls will be constructed at a single thickness.~~ The thickness of the duct wall construction\X\0D
NOTE: It is assumed that chamber walls will be constructed at a single thickness.


Pset_SensorTypePHSensor.xml
===========================

modifications
-------------
* PropertyDefs > PropertyDef [Name="SetPointPH"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue


Pset_ValveTypePressureReducing.xml
==================================

modifications
-------------
* Definition "Valve that reduces the pressure of a fluid immediately downstream of its position in a pipeline to a preselected value or by a predetermined ratio.
Note that a pressure reducing valve is constrained to have a 2 port  pattern."
  ~~Valve that reduces the pressure of a fluid immediately downstream of its position in a pipeline to a preselected value or by a predetermined ratio.
Note that a pressure reducing valve is constrained to have a 2 port  pattern.~~ Valve that reduces the pressure of a fluid immediately downstream of its position in a pipeline to a preselected value or by a predetermined ratio.\X\0D
Note that a pressure reducing valve is constrained to have a 2 port  pattern.



Pset_ControllerPHistory.xml
===========================

modifications
-------------
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="Quality"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Status"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Value"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;



Qto_PileBaseQuantities.xml
==========================

modifications
-------------
* QtoDefs > QtoDef [Name="Length"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetVolume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossVolume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="OuterSurfaceArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="CrossSectionArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossSurfaceArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases


Pset_PrecastConcreteElementFabrication.xml
==========================================

modifications
-------------
* ApplicableTypeValue "IfcBeam,IfcBuildingElementProxy,IfcChimney,IfcColumn,IfcFooting,IfcMember,IfcPile,IfcPlate,IfcRamp,IfcRampFlight,IfcRoof,IfcSlab,IfcStair,IfcStairFlight,IfcWall,IfcCivilElement"
  ~~IfcBeam,IfcBuildingElementProxy,IfcChimney,IfcColumn,IfcFooting,IfcMember,IfcPile,IfcPlate,IfcRamp,IfcRampFlight,IfcRoof,IfcSlab,IfcStair,IfcStairFlight,IfcWall,IfcCivilElement~~ IfcCivilElement
* PropertyDefs > PropertyDef [Name="AsBuiltLocationNumber"] > Definition "Defines a unique location within a structure, the &#8216;slot&#8217; into which the piece was installed. Where pieces share the same piece mark, they can be interchanged. The value is only known after erection."
  ~~Defines a unique location within a structure, the &#8216;slot&#8217; into which the piece was installed. Where pieces share the same piece mark, they can be interchanged. The value is only known after erection.~~ Defines a unique location within a structure, the \X2\2018\X0\slot\X2\2019\X0\ into which the piece was installed. Where pieces share the same piece mark, they can be interchanged. The value is only known after erection.
* PropertyDefs > PropertyDef [Name="PieceMark"] > Definition "Defines a unique piece for production purposes. All pieces with the same piece mark value are identical and interchangeable. The piece mark may be composed of sub-parts that have specific locally defined meaning (e.g. B-1A may denote a beam, of generic type &#8216;1&#8217; and specific shape &#8216;A&#8217;)."
  ~~Defines a unique piece for production purposes. All pieces with the same piece mark value are identical and interchangeable. The piece mark may be composed of sub-parts that have specific locally defined meaning (e.g. B-1A may denote a beam, of generic type &#8216;1&#8217; and specific shape &#8216;A&#8217;).~~ Defines a unique piece for production purposes. All pieces with the same piece mark value are identical and interchangeable. The piece mark may be composed of sub-parts that have specific locally defined meaning (e.g. B-1A may denote a beam, of generic type \X2\2018\X0\1\X2\2019\X0\ and specific shape \X2\2018\X0\A\X2\2019\X0\).

deletions
---------
* PropertyDefs > PropertyDef [Name="TypeDesignation"]


Pset_ManufacturerTypeInformation.xml
====================================

modifications
-------------
* Definition "Defines characteristics of types (ranges) of manufactured products that may be given by the manufacturer. Note that the term 'manufactured' may also be used to refer to products that are supplied and identified by the supplier or that are assembled off site by a third party provider. 
HISTORY: This property set replaces the entity IfcManufacturerInformation from previous IFC releases. IFC 2x4: AssemblyPlace property added."
  ~~Defines characteristics of types (ranges) of manufactured products that may be given by the manufacturer. Note that the term 'manufactured' may also be used to refer to products that are supplied and identified by the supplier or that are assembled off site by a third party provider. 
HISTORY: This property set replaces the entity IfcManufacturerInformation from previous IFC releases. IFC 2x4: AssemblyPlace property added.~~ Defines characteristics of types (ranges) of manufactured products that may be given by the manufacturer. Note that the term 'manufactured' may also be used to refer to products that are supplied and identified by the supplier or that are assembled off site by a third party provider. \X\0D
HISTORY: This property set replaces the entity IfcManufacturerInformation from previous IFC releases. IFC 2x4: AssemblyPlace property added.
* PropertyDefs > PropertyDef [Name="AssemblyPlace"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="AssemblyPlace"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="OperationalDocument"] > PropertyType
* PropertyDefs > PropertyDef [Name="PerformanceCertificate"] > PropertyType
* PropertyDefs > PropertyDef [Name="SafetyDocument"] > PropertyType


Pset_DiscreteAccessoryStandardFixingPlate.xml
=============================================

modifications
-------------
* ApplicableClasses > ClassName "IfcDiscreteAccessory/Standard fixing plate"
  ~~IfcDiscreteAccessory/Standard fixing plate~~ IfcDiscreteAccessory
* ApplicableTypeValue "IfcDiscreteAccessory/Standard fixing plate"
  ~~IfcDiscreteAccessory/Standard fixing plate~~ IfcDiscreteAccessory


Pset_SpaceThermalLoadPHistory.xml
=================================

modifications
-------------
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="Lighting"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="VentilationIndoorAir"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="InfiltrationSensible"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="VentilationOutdoorAir"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="TotalRadiantLoad"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="EquipmentSensible"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="AirExchangeRate"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="RelativeHumidity"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="People"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="RecirculatedAir"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="TotalSensibleLoad"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="DryBulbTemperature"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="ExhaustAir"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="TotalLatentLoad"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;



Qto_DuctFittingBaseQuantities.xml
=================================

modifications
-------------
* QtoDefs > QtoDef [Name="Length"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossCrossSectionArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="OuterSurfaceArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetCrossSectionArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases


Pset_CableCarrierSegmentTypeConduitSegment.xml
==============================================

modifications
-------------
* Definition "An enclosed tubular carrier segment through which cables are pulled.
HISTORY: IFC4 - NominalLength deleted. To be handled as a quantity measure."
  ~~An enclosed tubular carrier segment through which cables are pulled.
HISTORY: IFC4 - NominalLength deleted. To be handled as a quantity measure.~~ An enclosed tubular carrier segment through which cables are pulled.\X\0D
HISTORY: IFC4 - NominalLength deleted. To be handled as a quantity measure.
* PropertyDefs > PropertyDef [Name="ConduitShapeType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="ConduitShapeType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_JettyDesignCriteria.xml
============================

modifications
-------------
* ApplicableClasses > ClassName "IfcMarineFacility/JETTY"
  ~~IfcMarineFacility/JETTY~~ IfcMarineFacility
* ApplicableTypeValue "IfcMarineFacility/JETTY"
  ~~IfcMarineFacility/JETTY~~ IfcMarineFacility


Pset_SolarDeviceTypeCommon.xml
==============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;



Pset_SwitchingDeviceTypeMomentarySwitch.xml
===========================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="MomentaryType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="MomentaryType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_SensorTypeConductanceSensor.xml
====================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="SetPointConductance"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue


Qto_TransformerBaseQuantities.xml
=================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases



Qto_ElectricGeneratorBaseQuantities.xml
=======================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Pset_EvaporatorPHistory.xml
===========================

modifications
-------------
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="CompressorEvaporatorHeatGain"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="EvaporatingTemperature"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="ExteriorHeatTransferCoefficient"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="EvaporatorMeanVoidFraction"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="InteriorHeatTransferCoefficient"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="LogarithmicMeanTemperatureDifference"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="UAcurves"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="CompressorEvaporatorPressureDrop"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="WaterFoulingResistance"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="HeatRejectionRate"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="RefrigerantFoulingResistance"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Pset_SensorTypeSoundSensor.xml
==============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="SetPointSound"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue


Pset_ColumnCommon.xml
=====================

modifications
-------------
* PropertyDefs > PropertyDef [Name="FireRating"] > Definition "Fire rating for the element.
It is given according to the national fire safety classification."
  ~~Fire rating for the element.
It is given according to the national fire safety classification.~~ Fire rating for the element.\X\0D
It is given according to the national fire safety classification.
* PropertyDefs > PropertyDef [Name="Roll"] > Definition "Rotation against the longitudinal axis - relative to the global  X direction for all columns that are vertical in regard to the global coordinate system (Profile direction equals global X is Roll = 0.). For all non-vertical columns the following applies:  Roll is relative to the global Z direction f(Profile direction of non-vertical columns that equals global Z is Roll = 0.)

The shape information is provided in addition to the shape representation and the geometric parameters used within. In cases of inconsistency between the geometric parameters and the shape properties, provided in the attached property, the geometric parameters take precedence.  For geometry editing applications, like CAD: this value should be write-only.

Note: new property in IFC4"
  ~~Rotation against the longitudinal axis - relative to the global  X direction for all columns that are vertical in regard to the global coordinate system (Profile direction equals global X is Roll = 0.). For all non-vertical columns the following applies:  Roll is relative to the global Z direction f(Profile direction of non-vertical columns that equals global Z is Roll = 0.)

The shape information is provided in addition to the shape representation and the geometric parameters used within. In cases of inconsistency between the geometric parameters and the shape properties, provided in the attached property, the geometric parameters take precedence.  For geometry editing applications, like CAD: this value should be write-only.

Note: new property in IFC4~~ Rotation against the longitudinal axis - relative to the global  X direction for all columns that are vertical in regard to the global coordinate system (Profile direction equals global X is Roll = 0.). For all non-vertical columns the following applies:  Roll is relative to the global Z direction f(Profile direction of non-vertical columns that equals global Z is Roll = 0.)\X\0D
\X\0D
The shape information is provided in addition to the shape representation and the geometric parameters used within. In cases of inconsistency between the geometric parameters and the shape properties, provided in the attached property, the geometric parameters take precedence.  For geometry editing applications, like CAD: this value should be write-only.\X\0D
\X\0D
Note: new property in IFC4
* PropertyDefs > PropertyDef [Name="Slope"] > Definition "Slope angle - relative to horizontal (0.0 degrees).

The shape information is provided in addition to the shape representation and the geometric parameters used within. In cases of inconsistency between the geometric parameters and the shape properties, provided in the attached property, the geometric parameters take precedence.   For geometry editing applications, like CAD: this value should be write-only."
  ~~Slope angle - relative to horizontal (0.0 degrees).

The shape information is provided in addition to the shape representation and the geometric parameters used within. In cases of inconsistency between the geometric parameters and the shape properties, provided in the attached property, the geometric parameters take precedence.   For geometry editing applications, like CAD: this value should be write-only.~~ Slope angle - relative to horizontal (0.0 degrees).\X\0D
\X\0D
The shape information is provided in addition to the shape representation and the geometric parameters used within. In cases of inconsistency between the geometric parameters and the shape properties, provided in the attached property, the geometric parameters take precedence.   For geometry editing applications, like CAD: this value should be write-only.
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="ThermalTransmittance"] > Definition "Thermal transmittance coefficient (U-Value) of the element. Here the total thermal transmittance coefficient through the column within the direction of the thermal flow (including all materials).

Nore: new property in IFC4"
  ~~Thermal transmittance coefficient (U-Value) of the element. Here the total thermal transmittance coefficient through the column within the direction of the thermal flow (including all materials).

Nore: new property in IFC4~~ Thermal transmittance coefficient (U-Value) of the element. Here the total thermal transmittance coefficient through the column within the direction of the thermal flow (including all materials).\X\0D
\X\0D
Nore: new property in IFC4
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_SpaceOccupancyRequirements.xml
===================================

modifications
-------------
* ApplicableTypeValue "IfcSpace, IfcSpatialZone, IfcZone"
  ~~IfcSpace, IfcSpatialZone, IfcZone~~ IfcZone


Pset_SanitaryTerminalTypeWashHandBasin.xml
==========================================

additions
---------
* ApplicableClasses
* ApplicableClasses
* ApplicableClasses

modifications
-------------
* PropertyDefs
  ~~PropertyDefs~~ ApplicableClasses
* ApplicableClasses
  ~~ApplicableClasses~~ PropertyDefs
* ApplicableClasses > ClassName "IfcSanitaryTerminal/WASHHANDBASIN"
  ~~&lt;ClassName&gt;~~ &lt;PropertyDef&gt;


Qto_SpaceBaseQuantities.xml
===========================

modifications
-------------
* QtoDefs > QtoDef [Name="GrossVolume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="FinishCeilingHeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossPerimeter"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossCeilingArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetFloorArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="FinishFloorHeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetCeilingArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Height"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetPerimeter"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetWallArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossWallArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetVolume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossFloorArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases


Pset_DamperTypeFireDamper.xml
=============================

modifications
-------------
* Definition "Fire damper type attributes.
Pset renamed from Pset_DamperTypeFire to Pset_DamperTypeFireDamper in IFC2x2 Pset Addendum."
  ~~Fire damper type attributes.
Pset renamed from Pset_DamperTypeFire to Pset_DamperTypeFireDamper in IFC2x2 Pset Addendum.~~ Fire damper type attributes.\X\0D
Pset renamed from Pset_DamperTypeFire to Pset_DamperTypeFireDamper in IFC2x2 Pset Addendum.
* PropertyDefs > PropertyDef [Name="ActuationType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="ClosureRatingEnum"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="ActuationType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="ClosureRatingEnum"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_FlowInstrumentPHistory.xml
===============================

modifications
-------------
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="Value"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Status"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Quality"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Qto_MemberBaseQuantities.xml
============================

modifications
-------------
* QtoDefs > QtoDef [Name="GrossVolume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="OuterSurfaceArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="CrossSectionArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetVolume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Length"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossSurfaceArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetSurfaceArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases


Pset_CableSegmentOccurrence.xml
===============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="DesignAmbientTemperature"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="InstallationMethodFlagEnum"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="MountingMethod"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* 
  ~~PSET_OCCURRENCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="InstallationMethodFlagEnum"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="MountingMethod"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_RadiiKerbStone.xml
=======================

modifications
-------------
* PropertyDefs > PropertyDef [Name="CurveShape"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="CurveShape"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Qto_PlateBaseQuantities.xml
===========================

modifications
-------------
* QtoDefs > QtoDef [Name="GrossWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetVolume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Perimeter"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Width"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossVolume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases


Pset_ConstructionResource.xml
=============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="ScheduleCompletion"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="ActualCost"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="RemainingCost"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="ScheduleCost"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="ScheduleWork"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="ActualWork"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="RemainingWork"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="ActualCompletion"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Pset_MotorConnectionTypeCommon.xml
==================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_SensorTypeMovementSensor.xml
=================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="SetPointMovement"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="MovementSensingType"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Pset_ReinforcementBarPitchOfWall.xml
====================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="BarAllocationType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="BarAllocationType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_RampFlightCommon.xml
=========================

additions
---------
* PropertyDefs > PropertyDef [Name="ClearWidth"]

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Slope"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Headroom"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="CounterSlope"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="ClearWidth"]


Pset_ElectricApplianceTypeCommon.xml
====================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_QuayCommon.xml
===================

modifications
-------------
* ApplicableClasses > ClassName "IfcMarineFacility/QUAY"
  ~~IfcMarineFacility/QUAY~~ IfcMarineFacility
* ApplicableTypeValue "IfcMarineFacility/QUAY"
  ~~IfcMarineFacility/QUAY~~ IfcMarineFacility
* PropertyDefs > PropertyDef [Name="StructuralType"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="BentSpacing"]
* PropertyDefs > PropertyDef [Name="QuaySectionType"]
* PropertyDefs > PropertyDef [Name="Elevation"]


Qto_ColumnBaseQuantities.xml
============================

modifications
-------------
* QtoDefs > QtoDef [Name="GrossSurfaceArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetSurfaceArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetVolume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Length"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="CrossSectionArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossVolume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="OuterSurfaceArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases


Pset_CableFittingTypeCommon.xml
===============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Qto_CooledBeamBaseQuantities.xml
================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Qto_PipeSegmentBaseQuantities.xml
=================================

modifications
-------------
* QtoDefs > QtoDef [Name="Length"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="OuterSurfaceArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossCrossSectionArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetCrossSectionArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases



Pset_ProtectiveDeviceTrippingFunctionGCurve.xml
===============================================

modifications
-------------
* Definition "Tripping functions are applied to electronic tripping units (i.e. tripping units having type property sets for electronic tripping defined). They are not applied to thermal, thermal magnetic or RCD tripping units.
This property set represent the ground fault protection (G-curve) of an electronic protection device"
  ~~Tripping functions are applied to electronic tripping units (i.e. tripping units having type property sets for electronic tripping defined). They are not applied to thermal, thermal magnetic or RCD tripping units.
This property set represent the ground fault protection (G-curve) of an electronic protection device~~ Tripping functions are applied to electronic tripping units (i.e. tripping units having type property sets for electronic tripping defined). They are not applied to thermal, thermal magnetic or RCD tripping units.\X\0D
This property set represent the ground fault protection (G-curve) of an electronic protection device


Pset_WasteTerminalTypeWasteTrap.xml
===================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="InletConnectionSize"] > Definition "Size of the inlet connection(s), where used, of the inlet connections.

Note that all inlet connections are assumed to be the same size."
  ~~Size of the inlet connection(s), where used, of the inlet connections.

Note that all inlet connections are assumed to be the same size.~~ Size of the inlet connection(s), where used, of the inlet connections.\X\0D
\X\0D
Note that all inlet connections are assumed to be the same size.
* PropertyDefs > PropertyDef [Name="WasteTrapType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="WasteTrapType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;



Qto_DistributionBoardBaseQuantities.xml
=======================================

modifications
-------------
* QtoDefs > QtoDef [Name="GrossWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NumberOfCircuits"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases


Pset_DoorCommon.xml
===================

modifications
-------------
* PropertyDefs > PropertyDef [Name="AcousticRating"] > Definition "Acoustic rating for this object.
It is provided according to the national building code. It indicates the sound transmission resistance of this object by an index ratio (instead of providing full sound absorbtion values)."
  ~~Acoustic rating for this object.
It is provided according to the national building code. It indicates the sound transmission resistance of this object by an index ratio (instead of providing full sound absorbtion values).~~ Acoustic rating for this object.\X\0D
It is provided according to the national building code. It indicates the sound transmission resistance of this object by an index ratio (instead of providing full sound absorbtion values).
* PropertyDefs > PropertyDef [Name="FireExit"] > Definition "Indication whether this object is designed to serve as an exit in the case of fire (TRUE) or not (FALSE).
Here it defines an exit door in accordance to the national building code."
  ~~Indication whether this object is designed to serve as an exit in the case of fire (TRUE) or not (FALSE).
Here it defines an exit door in accordance to the national building code.~~ Indication whether this object is designed to serve as an exit in the case of fire (TRUE) or not (FALSE).\X\0D
Here it defines an exit door in accordance to the national building code.
* PropertyDefs > PropertyDef [Name="GlazingAreaFraction"] > Definition "Fraction of the glazing area relative to the total area of the filling element. 
It shall be used, if the glazing area is not given separately for all panels within the filling element."
  ~~Fraction of the glazing area relative to the total area of the filling element. 
It shall be used, if the glazing area is not given separately for all panels within the filling element.~~ Fraction of the glazing area relative to the total area of the filling element. \X\0D
It shall be used, if the glazing area is not given separately for all panels within the filling element.
* PropertyDefs > PropertyDef [Name="HandicapAccessible"] > Definition "Indication that this object is designed to be accessible by the handicapped. 
It is giving according to the requirements of the national building code."
  ~~Indication that this object is designed to be accessible by the handicapped. 
It is giving according to the requirements of the national building code.~~ Indication that this object is designed to be accessible by the handicapped. \X\0D
It is giving according to the requirements of the national building code.
* PropertyDefs > PropertyDef [Name="MechanicalLoadRating"] > Definition "Mechanical load rating for this object.
It is provided according to the national building code."
  ~~Mechanical load rating for this object.
It is provided according to the national building code.~~ Mechanical load rating for this object.\X\0D
It is provided according to the national building code.
* PropertyDefs > PropertyDef [Name="SecurityRating"] > Definition "Index based rating system indicating security level.
It is giving according to the national building code."
  ~~Index based rating system indicating security level.
It is giving according to the national building code.~~ Index based rating system indicating security level.\X\0D
It is giving according to the national building code.
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="ThermalTransmittance"] > Definition "Thermal transmittance coefficient (U-Value) of a material.
It applies to the total door construction."
  ~~Thermal transmittance coefficient (U-Value) of a material.
It applies to the total door construction.~~ Thermal transmittance coefficient (U-Value) of a material.\X\0D
It applies to the total door construction.
* PropertyDefs > PropertyDef [Name="WaterTightnessRating"] > Definition "Water tightness rating for this object.
It is provided according to the national building code."
  ~~Water tightness rating for this object.
It is provided according to the national building code.~~ Water tightness rating for this object.\X\0D
It is provided according to the national building code.
* PropertyDefs > PropertyDef [Name="WindLoadRating"] > Definition "Wind load resistance rating for this object.
It is provided according to the national building code."
  ~~Wind load resistance rating for this object.
It is provided according to the national building code.~~ Wind load resistance rating for this object.\X\0D
It is provided according to the national building code.
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;



Pset_CoilTypeHydronic.xml
=========================

modifications
-------------
* PropertyDefs > PropertyDef [Name="CoilConnectionDirection"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="CoilCoolant"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="CoilFluidArrangement"] > Definition "Fluid flow arrangement of the coil.

CrossCounterFlow: Air and water flow enter in different directions.
CrossFlow: Air and water flow are perpendicular.
CrossParallelFlow: Air and water flow enter in same directions."
  ~~Fluid flow arrangement of the coil.

CrossCounterFlow: Air and water flow enter in different directions.
CrossFlow: Air and water flow are perpendicular.
CrossParallelFlow: Air and water flow enter in same directions.~~ Fluid flow arrangement of the coil.\X\0D
\X\0D
CrossCounterFlow: Air and water flow enter in different directions.\X\0D
CrossFlow: Air and water flow are perpendicular.\X\0D
CrossParallelFlow: Air and water flow enter in same directions.
* PropertyDefs > PropertyDef [Name="CoilFluidArrangement"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="FluidPressureRange"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="WaterPressureDropCurve"] > Name "WaterPressureDropCurve"
  ~~&lt;Name&gt;~~ &lt;Name&gt;
* PropertyDefs > PropertyDef [Name="TotalUACurves"] > PropertyType
  ~~&lt;PropertyType&gt;~~ &lt;PropertyType&gt;
* PropertyDefs > PropertyDef [Name="CoilFluidArrangement"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="CoilCoolant"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="WaterPressureDropCurve"] > PropertyType
  ~~&lt;PropertyType&gt;~~ &lt;PropertyType&gt;
* PropertyDefs > PropertyDef [Name="CoilConnectionDirection"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="WaterPressureDropCurve"] > Definition "Water pressure drop curve, pressure drop &#8211; flow rate curve, WaterPressureDrop = f(WaterflowRate)."
  ~~&lt;Definition&gt;~~ &lt;Definition&gt;
* PropertyDefs > PropertyDef [Name="TotalUACurves"] > Definition "Total UA curves, UA - air and water velocities, UA = [(C1 \* AirFlowRate\^0.8)\^-1 + (C2 \* WaterFlowRate\^0.8)\^-1]\^-1.  Note: as two variables are used, DefiningValues and DefinedValues are null, and values are stored in IfcTable in the following order: AirFlowRate,WaterFlowRate,UA.  The IfcTable is related to IfcPropertyTableValue using IfcMetric and IfcPropertyConstraintRelationship."
  ~~&lt;Definition&gt;~~ &lt;Definition&gt;
* PropertyDefs > PropertyDef [Name="TotalUACurves"] > Name "TotalUACurves"
  ~~&lt;Name&gt;~~ &lt;Name&gt;


Pset_InterceptorTypeCommon.xml
==============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;



Pset_DuctSegmentPHistory.xml
============================

modifications
-------------
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="AtmosphericPressure"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="LossCoefficient"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="FluidFlowLeakage"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="LeakageCurve"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Qto_FlowMeterBaseQuantities.xml
===============================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Pset_ProcessCapacity.xml
========================

modifications
-------------
* PropertyDefs
  ~~PropertyDefs~~ ApplicableTypeValue
* ApplicableTypeValue "IfcSpatialElement,IfcSpatialElementType,IfcTransportElement,IfcTransportElementType"
  ~~ApplicableTypeValue~~ PropertyDefs



Pset_ElectricalDeviceCommon.xml
===============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="ConductorFunction"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="IK_Code"] > Definition "IK Code according to IEC 62262 (2002) is a numeric classification for the degree of protection provided by enclosures for electrical equipment against external mechanical impacts.
> NOTE&nbsp; In earlier labeling, the third numeral (1..) had been occasionally added to the closely related IP Code on ingress protection, to indicate the level of impact protection."
  ~~IK Code according to IEC 62262 (2002) is a numeric classification for the degree of protection provided by enclosures for electrical equipment against external mechanical impacts.
> NOTE&nbsp; In earlier labeling, the third numeral (1..) had been occasionally added to the closely related IP Code on ingress protection, to indicate the level of impact protection.~~ IK Code according to IEC 62262 (2002) is a numeric classification for the degree of protection provided by enclosures for electrical equipment against external mechanical impacts.\X\0D
> NOTE&#160; In earlier labeling, the third numeral (1..) had been occasionally added to the closely related IP Code on ingress protection, to indicate the level of impact protection.
* PropertyDefs > PropertyDef [Name="InsulationStandardClass"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="NominalFrequencyRange"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="RatedCurrent"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="RatedVoltage"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="ConductorFunction"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="InsulationStandardClass"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="IK_Code"] > PropertyType


Pset_AudioVisualAppliancePHistory.xml
=====================================

modifications
-------------
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="PowerState"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="MediaContent"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="AudioVolume"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="MediaSource"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Qto_PavementBaseQuantities.xml
==============================

additions
---------
* Definition "$"

modifications
-------------
* QtoDefinitionAliases
  ~~QtoDefinitionAliases~~ ApplicableTypeValue


Pset_SwitchingDeviceTypeSwitchDisconnector.xml
==============================================

modifications
-------------
* Definition "A switch disconnector is a switch which in the open position satisfies the isolating requirements specified for a disconnector.

History: Property 'HasVisualIndication' changed to 'IsIlluminated' to conform with property name for toggle switch"
  ~~A switch disconnector is a switch which in the open position satisfies the isolating requirements specified for a disconnector.

History: Property 'HasVisualIndication' changed to 'IsIlluminated' to conform with property name for toggle switch~~ A switch disconnector is a switch which in the open position satisfies the isolating requirements specified for a disconnector.\X\0D
\X\0D
History: Property 'HasVisualIndication' changed to 'IsIlluminated' to conform with property name for toggle switch
* PropertyDefs > PropertyDef [Name="LoadDisconnectionType"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="SwitchDisconnectorType"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;



Pset_ShadingDeviceCommon.xml
============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="ShadingDeviceType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="SolarReflectance"] > Definition "(Rsol): The ratio of incident solar radiation that is reflected by a shading system (also named &#961;e). Note the following equation Asol + Rsol + Tsol = 1"
  ~~(Rsol): The ratio of incident solar radiation that is reflected by a shading system (also named &#961;e). Note the following equation Asol + Rsol + Tsol = 1~~ (Rsol): The ratio of incident solar radiation that is reflected by a shading system (also named \X2\03C1\X0\e). Note the following equation Asol + Rsol + Tsol = 1
* PropertyDefs > PropertyDef [Name="SolarTransmittance"] > Definition "(Tsol): The ratio of incident solar radiation that directly passes through a shading system (also named &#964;e). Note the following equation Asol + Rsol + Tsol = 1"
  ~~(Tsol): The ratio of incident solar radiation that directly passes through a shading system (also named &#964;e). Note the following equation Asol + Rsol + Tsol = 1~~ (Tsol): The ratio of incident solar radiation that directly passes through a shading system (also named \X2\03C4\X0\e). Note the following equation Asol + Rsol + Tsol = 1
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="ShadingDeviceType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_SensorTypePressureSensor.xml
=================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="SetPointPressure"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue


Pset_SanitaryTerminalTypeSanitaryFountain.xml
=============================================

additions
---------
* ApplicableClasses
* ApplicableClasses

modifications
-------------
* PropertyDefs
  ~~PropertyDefs~~ ApplicableClasses
* ApplicableClasses
  ~~ApplicableClasses~~ PropertyDefs
* ApplicableClasses > ClassName "IfcSanitaryTerminal/SANITARYFOUNTAIN"
  ~~&lt;ClassName&gt;~~ &lt;PropertyDef&gt;


Pset_BreakwaterCommon.xml
=========================

modifications
-------------
* ApplicableClasses > ClassName "IfcMarineFacility/BREAKWATER"
  ~~IfcMarineFacility/BREAKWATER~~ IfcMarineFacility
* ApplicableTypeValue "IfcMarineFacility/BREAKWATER"
  ~~IfcMarineFacility/BREAKWATER~~ IfcMarineFacility

deletions
---------
* PropertyDefs > PropertyDef [Name="Elevation"]


Pset_SensorTypeRadioactivitySensor.xml
======================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="SetPointRadioactivity"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue


Pset_TankTypePreformed.xml
==========================

modifications
-------------
* Definition "Fixed vessel manufactured as a single unit with one or more compartments for storing a liquid.

Pset renamed from Pset_TankTypePreformedTank to Pset_TankTypePreformed in IFC2x2 Pset Addendum."
  ~~Fixed vessel manufactured as a single unit with one or more compartments for storing a liquid.

Pset renamed from Pset_TankTypePreformedTank to Pset_TankTypePreformed in IFC2x2 Pset Addendum.~~ Fixed vessel manufactured as a single unit with one or more compartments for storing a liquid.\X\0D
\X\0D
Pset renamed from Pset_TankTypePreformedTank to Pset_TankTypePreformed in IFC2x2 Pset Addendum.
* ApplicableClasses > ClassName "IfcTank/PREFORMED"
  ~~IfcTank/PREFORMED~~ IfcTank
* ApplicableTypeValue "IfcTank/PREFORMED"
  ~~IfcTank/PREFORMED~~ IfcTank
* PropertyDefs > PropertyDef [Name="EndShapeType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="PatternType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="EndShapeType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="PatternType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Qto_StairFlightBaseQuantities.xml
=================================

modifications
-------------
* QtoDefs > QtoDef [Name="GrossVolume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Length"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetVolume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases


Pset_AnnotationSurveyArea.xml
=============================

modifications
-------------
* ApplicableClasses > ClassName "IfcAnnotation/SurveyArea"
  ~~IfcAnnotation/SurveyArea~~ IfcAnnotation
* ApplicableTypeValue "IfcAnnotation/SurveyArea"
  ~~IfcAnnotation/SurveyArea~~ IfcAnnotation
* PropertyDefs > PropertyDef [Name="AcquisitionMethod"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="AcquisitionMethod"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Qto_SolarDeviceBaseQuantities.xml
=================================

modifications
-------------
* QtoDefs > QtoDef [Name="GrossWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases


Pset_SanitaryTerminalTypeCistern.xml
====================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="CisternHeight"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="FlushRate"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="FlushType"] > Definition "The property enumeration Pset_FlushTypeEnum defines the types of flushing mechanism that may be specified for cisterns and sanitary terminals where:-

Lever: 	Flushing is achieved by twisting a lever that causes a predetermined flow of water to be passed from a cistern to the sanitary terminal.
Pull: 	Flushing is achieved by pulling a handle or knob vertically upwards that causes a predetermined flow of water to be passed from a cistern to the sanitary terminal.
Push: 	Flushing is achieved by pushing a button or plate that causes a predetermined flow of water to be passed from a cistern to the sanitary terminal.
Sensor: Flush is activated through an automatic sensing mechanism."
  ~~The property enumeration Pset_FlushTypeEnum defines the types of flushing mechanism that may be specified for cisterns and sanitary terminals where:-

Lever: 	Flushing is achieved by twisting a lever that causes a predetermined flow of water to be passed from a cistern to the sanitary terminal.
Pull: 	Flushing is achieved by pulling a handle or knob vertically upwards that causes a predetermined flow of water to be passed from a cistern to the sanitary terminal.
Push: 	Flushing is achieved by pushing a button or plate that causes a predetermined flow of water to be passed from a cistern to the sanitary terminal.
Sensor: Flush is activated through an automatic sensing mechanism.~~ The property enumeration Pset_FlushTypeEnum defines the types of flushing mechanism that may be specified for cisterns and sanitary terminals where:-\X\0D
\X\0D
Lever: \X\09Flushing is achieved by twisting a lever that causes a predetermined flow of water to be passed from a cistern to the sanitary terminal.\X\0D
Pull: \X\09Flushing is achieved by pulling a handle or knob vertically upwards that causes a predetermined flow of water to be passed from a cistern to the sanitary terminal.\X\0D
Push: \X\09Flushing is achieved by pushing a button or plate that causes a predetermined flow of water to be passed from a cistern to the sanitary terminal.\X\0D
Sensor: Flush is activated through an automatic sensing mechanism.
* PropertyDefs > PropertyDef [Name="FlushType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="CisternHeight"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="FlushType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_MaterialConcrete.xml
=========================

modifications
-------------
* ApplicableClasses > ClassName "IfcMaterial/Concrete"
  ~~IfcMaterial/Concrete~~ IfcMaterial
* ApplicableTypeValue "IfcMaterial/Concrete"
  ~~IfcMaterial/Concrete~~ IfcMaterial


Pset_SensorTypeWindSensor.xml
=============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="WindSensorType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="WindSensorType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_ValveTypeFaucet.xml
========================

additions
---------
* ApplicableClasses
* ApplicableClasses
* ApplicableClasses
* ApplicableClasses

modifications
-------------
* PropertyDefs
  ~~PropertyDefs~~ ApplicableClasses
* ApplicableClasses
  ~~ApplicableClasses~~ PropertyDefs
* ApplicableClasses > ClassName "IfcValve/FAUCET"
  ~~&lt;ClassName&gt;~~ &lt;PropertyDef&gt;


Qto_DoorBaseQuantities.xml
==========================

modifications
-------------
* QtoDefs > QtoDef [Name="Perimeter"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Width"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Height"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Area"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases


Pset_CableCarrierSegmentTypeCommon.xml
======================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_Width.xml
==============

modifications
-------------
* ApplicableClasses > ClassName "IfcAnnotation/(.WIDTHEVENT.)"
  ~~IfcAnnotation/(.WIDTHEVENT.)~~ IfcWasteTerminal
* ApplicableTypeValue "IfcAnnotation/(.WIDTHEVENT.)"
  ~~IfcAnnotation/(.WIDTHEVENT.)~~ IfcWasteTerminal
* PropertyDefs > PropertyDef [Name="TransitionWidth"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Side"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="NominalWidth"]


Pset_EvaporativeCoolerTypeCommon.xml
====================================

additions
---------
* PropertyDefs > PropertyDef [Name="EffectivenessTable"]

modifications
-------------
* Definition "Evaporative cooler type common attributes.
Sound attribute deleted in IFC2x2 Pset Addendum: Use IfcSoundProperties instead. WaterRequirement attribute unit type modified in IFC2x2 Pset Addendum."
  ~~Evaporative cooler type common attributes.
Sound attribute deleted in IFC2x2 Pset Addendum: Use IfcSoundProperties instead. WaterRequirement attribute unit type modified in IFC2x2 Pset Addendum.~~ Evaporative cooler type common attributes.\X\0D
Sound attribute deleted in IFC2x2 Pset Addendum: Use IfcSoundProperties instead. WaterRequirement attribute unit type modified in IFC2x2 Pset Addendum.
* PropertyDefs > PropertyDef [Name="FlowArrangement"] > Definition "CounterFlow: Air and water flow enter in different directions.

CrossFlow: Air and water flow are perpendicular.
ParallelFlow: Air and water flow enter in same directions."
  ~~CounterFlow: Air and water flow enter in different directions.

CrossFlow: Air and water flow are perpendicular.
ParallelFlow: Air and water flow enter in same directions.~~ CounterFlow: Air and water flow enter in different directions.\X\0D
\X\0D
CrossFlow: Air and water flow are perpendicular.\X\0D
ParallelFlow: Air and water flow enter in same directions.
* PropertyDefs > PropertyDef [Name="FlowArrangement"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="OperationTemperatureRange"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="WaterPressDropCurve"] > Definition "Water pressure drop as function of water flow rate."
  ~~&lt;Definition&gt;~~ &lt;Definition&gt;
* PropertyDefs > PropertyDef [Name="FlowArrangement"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="WaterPressDropCurve"] > Name "WaterPressDropCurve"
  ~~&lt;Name&gt;~~ &lt;Name&gt;
* PropertyDefs > PropertyDef [Name="AirPressureDropCurve"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="WaterPressDropCurve"] > PropertyType
  ~~&lt;PropertyType&gt;~~ &lt;PropertyType&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="EffectivenessTable"]


Pset_PackingInstructions.xml
============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="PackingCareType"] > Definition "Identifies the predefined types of care that may be required when handling the artefact during a move where:

Fragile: artefact may be broken during a move through careless handling.
HandleWithCare: artefact may be damaged during a move through careless handling."
  ~~Identifies the predefined types of care that may be required when handling the artefact during a move where:

Fragile: artefact may be broken during a move through careless handling.
HandleWithCare: artefact may be damaged during a move through careless handling.~~ Identifies the predefined types of care that may be required when handling the artefact during a move where:\X\0D
\X\0D
Fragile: artefact may be broken during a move through careless handling.\X\0D
HandleWithCare: artefact may be damaged during a move through careless handling.
* PropertyDefs > PropertyDef [Name="PackingCareType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="PackingCareType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="ContainerMaterial"] > PropertyType
* PropertyDefs > PropertyDef [Name="WrappingMaterial"] > PropertyType


Pset_PipeSegmentPHistory.xml
============================

modifications
-------------
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="FluidFlowLeakage"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="LeakageCurve"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Qto_LinearStratumBaseQuantities.xml
===================================

modifications
-------------
* QtoDefs > QtoDef [Name="Diameter"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Length"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases


Qto_ChillerBaseQuantities.xml
=============================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Pset_ElectricTimeControlTypeCommon.xml
======================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_Permit.xml
===============

modifications
-------------
* Definition "A permit is a document that allows permission to gain access to an area or carry out work in a situation where security or other access restrictions apply.
HISTORY: IFC4 EndDate added. PermitType, PermitDuration, StartTime and EndTime are deleted."
  ~~A permit is a document that allows permission to gain access to an area or carry out work in a situation where security or other access restrictions apply.
HISTORY: IFC4 EndDate added. PermitType, PermitDuration, StartTime and EndTime are deleted.~~ A permit is a document that allows permission to gain access to an area or carry out work in a situation where security or other access restrictions apply.\X\0D
HISTORY: IFC4 EndDate added. PermitType, PermitDuration, StartTime and EndTime are deleted.
* PropertyDefs > PropertyDef [Name="EscortRequirement"] > Definition "Indicates whether or not an escort is required to accompany persons carrying out a work order at or to/from the place of work (= TRUE) or not (= FALSE).

NOTE - There are many instances where escorting is required, particularly in a facility that has a high security rating. Escorting may require that persons are escorted to and from the place of work. Alternatively, it may involve the escort remaining at the place of work at all times."
  ~~Indicates whether or not an escort is required to accompany persons carrying out a work order at or to/from the place of work (= TRUE) or not (= FALSE).

NOTE - There are many instances where escorting is required, particularly in a facility that has a high security rating. Escorting may require that persons are escorted to and from the place of work. Alternatively, it may involve the escort remaining at the place of work at all times.~~ Indicates whether or not an escort is required to accompany persons carrying out a work order at or to/from the place of work (= TRUE) or not (= FALSE).\X\0D
\X\0D
NOTE - There are many instances where escorting is required, particularly in a facility that has a high security rating. Escorting may require that persons are escorted to and from the place of work. Alternatively, it may involve the escort remaining at the place of work at all times.
* PropertyDefs > PropertyDef [Name="SpecialRequirements"] > Definition "Any additional special requirements that need to be included in the permit to work.

NOTE - Additional permit requirements may be imposed according to the nature of the facility at which the work is carried out. For instance, in clean areas, special clothing may be required whilst in corrective institutions, it may be necessary to check in and check out tools that will be used for work as a safety precaution."
  ~~Any additional special requirements that need to be included in the permit to work.

NOTE - Additional permit requirements may be imposed according to the nature of the facility at which the work is carried out. For instance, in clean areas, special clothing may be required whilst in corrective institutions, it may be necessary to check in and check out tools that will be used for work as a safety precaution.~~ Any additional special requirements that need to be included in the permit to work.\X\0D
\X\0D
NOTE - Additional permit requirements may be imposed according to the nature of the facility at which the work is carried out. For instance, in clean areas, special clothing may be required whilst in corrective institutions, it may be necessary to check in and check out tools that will be used for work as a safety precaution.


Pset_ActionRequest.xml
======================

deletions
---------
* PropertyDefs > PropertyDef [Name="RequestSourceName"] > PropertyType




Pset_ProjectOrderMaintenanceWorkOrder.xml
=========================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="FaultPriorityType"] > Definition "Identifies the predefined types of priority that can be assigned from which the type may be set where:

High: action is required urgently.
Medium: action can occur within a reasonable period of time.
Low: action can occur when convenient."
  ~~Identifies the predefined types of priority that can be assigned from which the type may be set where:

High: action is required urgently.
Medium: action can occur within a reasonable period of time.
Low: action can occur when convenient.~~ Identifies the predefined types of priority that can be assigned from which the type may be set where:\X\0D
\X\0D
High: action is required urgently.\X\0D
Medium: action can occur within a reasonable period of time.\X\0D
Low: action can occur when convenient.
* PropertyDefs > PropertyDef [Name="FaultPriorityType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="LocationPriorityType"] > Definition "Identifies the predefined types of priority that can be assigned from which the type may be set where:

High: action is required urgently.
Medium: action can occur within a reasonable period of time.
Low: action can occur when convenient."
  ~~Identifies the predefined types of priority that can be assigned from which the type may be set where:

High: action is required urgently.
Medium: action can occur within a reasonable period of time.
Low: action can occur when convenient.~~ Identifies the predefined types of priority that can be assigned from which the type may be set where:\X\0D
\X\0D
High: action is required urgently.\X\0D
Medium: action can occur within a reasonable period of time.\X\0D
Low: action can occur when convenient.
* PropertyDefs > PropertyDef [Name="LocationPriorityType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="MaintenaceType"] > Definition "Identifies the predefined types of maintenance that can be done from which the type that generates the maintenance work order may be set where:

ConditionBased: generated as a result of the condition of an asset or artefact being less than a determined value.
Corrective: generated as a result of an immediate and urgent need for maintenance action.
PlannedCorrective: generated as a result of immediate corrective action being needed but with sufficient time available for the work order to be included in maintenance planning.
Scheduled: generated as a result of a fixed, periodic maintenance requirement."
  ~~Identifies the predefined types of maintenance that can be done from which the type that generates the maintenance work order may be set where:

ConditionBased: generated as a result of the condition of an asset or artefact being less than a determined value.
Corrective: generated as a result of an immediate and urgent need for maintenance action.
PlannedCorrective: generated as a result of immediate corrective action being needed but with sufficient time available for the work order to be included in maintenance planning.
Scheduled: generated as a result of a fixed, periodic maintenance requirement.~~ Identifies the predefined types of maintenance that can be done from which the type that generates the maintenance work order may be set where:\X\0D
\X\0D
ConditionBased: generated as a result of the condition of an asset or artefact being less than a determined value.\X\0D
Corrective: generated as a result of an immediate and urgent need for maintenance action.\X\0D
PlannedCorrective: generated as a result of immediate corrective action being needed but with sufficient time available for the work order to be included in maintenance planning.\X\0D
Scheduled: generated as a result of a fixed, periodic maintenance requirement.
* PropertyDefs > PropertyDef [Name="MaintenaceType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="LocationPriorityType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="MaintenaceType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="FaultPriorityType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_CooledBeamTypeCommon.xml
=============================

modifications
-------------
* Definition "Cooled beam common attributes.
SoundLevel and SoundAttenuation attributes deleted in IFC2x2 Pset Addendum: Use IfcSoundProperties instead."
  ~~Cooled beam common attributes.
SoundLevel and SoundAttenuation attributes deleted in IFC2x2 Pset Addendum: Use IfcSoundProperties instead.~~ Cooled beam common attributes.\X\0D
SoundLevel and SoundAttenuation attributes deleted in IFC2x2 Pset Addendum: Use IfcSoundProperties instead.
* PropertyDefs > PropertyDef [Name="IntegratedLightingType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="PipeConnection"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="WaterFlowControlSystemType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="WaterPressureRange"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="PipeConnection"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="WaterFlowControlSystemType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="IntegratedLightingType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Qto_VolumetricStratumBaseQuantities.xml
=======================================

modifications
-------------
* QtoDefs > QtoDef [Name="Mass"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Volume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Area"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="PlanArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases


Pset_SensorTypeFlowSensor.xml
=============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="SetPointFlow"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue


Pset_BuildingCommon.xml
=======================

modifications
-------------
* PropertyDefs > PropertyDef [Name="NumberOfStoreys"] > Definition "The number of storeys within a building.
Captured for those cases where the IfcBuildingStorey entity is not used. Note that if IfcBuilingStorey is asserted and the number of storeys in a building can be determined from it, then this approach should be used in preference to setting a property for the number of storeys."
  ~~The number of storeys within a building.
Captured for those cases where the IfcBuildingStorey entity is not used. Note that if IfcBuilingStorey is asserted and the number of storeys in a building can be determined from it, then this approach should be used in preference to setting a property for the number of storeys.~~ The number of storeys within a building.\X\0D
Captured for those cases where the IfcBuildingStorey entity is not used. Note that if IfcBuilingStorey is asserted and the number of storeys in a building can be determined from it, then this approach should be used in preference to setting a property for the number of storeys.
* PropertyDefs > PropertyDef [Name="OccupancyType"] > Definition "Occupancy type for this object.
It is defined according to the presiding national building code."
  ~~Occupancy type for this object.
It is defined according to the presiding national building code.~~ Occupancy type for this object.\X\0D
It is defined according to the presiding national building code.


Pset_JunctionBoxTypeCommon.xml
==============================

modifications
-------------
* Definition "A junction box is an enclosure within which cables are connected.

History: New in IFC4"
  ~~A junction box is an enclosure within which cables are connected.

History: New in IFC4~~ A junction box is an enclosure within which cables are connected.\X\0D
\X\0D
History: New in IFC4
* PropertyDefs > PropertyDef [Name="MountingType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="PlacingType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="ShapeType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="PlacingType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="ShapeType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="MountingType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_DistributionSystemTypeVentilation.xml
==========================================

modifications
-------------
* Definition "This property set is used to define the general characteristics of the duct design parameters within a system.
HISTORY: New property set in IFC Release 2.0.  Renamed from Pset_DuctDesignCriteria in IFC4."
  ~~This property set is used to define the general characteristics of the duct design parameters within a system.
HISTORY: New property set in IFC Release 2.0.  Renamed from Pset_DuctDesignCriteria in IFC4.~~ This property set is used to define the general characteristics of the duct design parameters within a system.\X\0D
HISTORY: New property set in IFC Release 2.0.  Renamed from Pset_DuctDesignCriteria in IFC4.
* ApplicableClasses > ClassName "IfcDistributionSystem/VENTILATION"
  ~~IfcDistributionSystem/VENTILATION~~ IfcDistributionSystem
* ApplicableTypeValue "IfcDistributionSystem/VENTILATION"
  ~~IfcDistributionSystem/VENTILATION~~ IfcDistributionSystem
* PropertyDefs > PropertyDef [Name="DuctSizingMethod"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="DuctSizingMethod"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="DuctSealant"] > PropertyType


Pset_FlowInstrumentTypePressureGauge.xml
========================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="PressureGaugeType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="PressureGaugeType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_SanitaryTerminalTypeBidet.xml
==================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Mounting"] > Definition "The property enumeration Pset_SanitaryMountingEnum defines the forms of mounting or fixing of the sanitary terminal that may be specified within property sets used to define sanitary terminals (WC&#8217;s, basins, sinks, etc.) where:-

BackToWall: 	A pedestal mounted sanitary terminal that fits flush to the wall at the rear to cover its service connections
.
Pedestal: 	A floor mounted sanitary terminal that has an integral base
.
CounterTop: 	A sanitary terminal that is installed into a horizontal surface that is installed into a horizontal surface. Note: When applied to a wash hand basin, the term more normally used is &#8216;vanity&#8217;. See also Wash Hand Basin Type specification.
WallHung: 	A sanitary terminal cantilevered clear of the floor.

Note that BackToWall, Pedestal and WallHung are allowable values for a bidet."
  ~~The property enumeration Pset_SanitaryMountingEnum defines the forms of mounting or fixing of the sanitary terminal that may be specified within property sets used to define sanitary terminals (WC&#8217;s, basins, sinks, etc.) where:-

BackToWall: 	A pedestal mounted sanitary terminal that fits flush to the wall at the rear to cover its service connections
.
Pedestal: 	A floor mounted sanitary terminal that has an integral base
.
CounterTop: 	A sanitary terminal that is installed into a horizontal surface that is installed into a horizontal surface. Note: When applied to a wash hand basin, the term more normally used is &#8216;vanity&#8217;. See also Wash Hand Basin Type specification.
WallHung: 	A sanitary terminal cantilevered clear of the floor.

Note that BackToWall, Pedestal and WallHung are allowable values for a bidet.~~ The property enumeration Pset_SanitaryMountingEnum defines the forms of mounting or fixing of the sanitary terminal that may be specified within property sets used to define sanitary terminals (WC\X2\2019\X0\s, basins, sinks, etc.) where:-\X\0D
\X\0D
BackToWall: \X\09A pedestal mounted sanitary terminal that fits flush to the wall at the rear to cover its service connections\X\0D
.\X\0D
Pedestal: \X\09A floor mounted sanitary terminal that has an integral base\X\0D
.\X\0D
CounterTop: \X\09A sanitary terminal that is installed into a horizontal surface that is installed into a horizontal surface. Note: When applied to a wash hand basin, the term more normally used is \X2\2018\X0\vanity\X2\2019\X0\. See also Wash Hand Basin Type specification.\X\0D
WallHung: \X\09A sanitary terminal cantilevered clear of the floor.\X\0D
\X\0D
Note that BackToWall, Pedestal and WallHung are allowable values for a bidet.
* PropertyDefs > PropertyDef [Name="Mounting"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Mounting"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_SpaceCoveringRequirements.xml
==================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="CeilingCovering"] > Definition "Label to indicate the material or finish of the space flooring. The label is used for room book information and often displayed in room stamp.

The material information is provided in absence of an IfcCovering (type=CEILING) object with own shape representation and material assignment. In case of inconsistency the material assigned to IfcCovering elements takes precedence."
  ~~Label to indicate the material or finish of the space flooring. The label is used for room book information and often displayed in room stamp.

The material information is provided in absence of an IfcCovering (type=CEILING) object with own shape representation and material assignment. In case of inconsistency the material assigned to IfcCovering elements takes precedence.~~ Label to indicate the material or finish of the space flooring. The label is used for room book information and often displayed in room stamp.\X\0D
\X\0D
The material information is provided in absence of an IfcCovering (type=CEILING) object with own shape representation and material assignment. In case of inconsistency the material assigned to IfcCovering elements takes precedence.
* PropertyDefs > PropertyDef [Name="CeilingCoveringThickness"] > Definition "Thickness of the material layer(s) for the space ceiling.  

The thickness information is provided in absence of an IfcCovering (type=CEILING) object with own shape representation. In cases of inconsistency between the geometric parameters of an assigned IfcCovering and this attached property, the geometric parameters take precedence."
  ~~Thickness of the material layer(s) for the space ceiling.  

The thickness information is provided in absence of an IfcCovering (type=CEILING) object with own shape representation. In cases of inconsistency between the geometric parameters of an assigned IfcCovering and this attached property, the geometric parameters take precedence.~~ Thickness of the material layer(s) for the space ceiling.  \X\0D
\X\0D
The thickness information is provided in absence of an IfcCovering (type=CEILING) object with own shape representation. In cases of inconsistency between the geometric parameters of an assigned IfcCovering and this attached property, the geometric parameters take precedence.
* PropertyDefs > PropertyDef [Name="FloorCovering"] > Definition "Label to indicate the material or finish of the space flooring. The label is used for room book information and often displayed in room stamp.

The material information is provided in absence of an IfcCovering (type=FLOORING) object with own shape representation and material assignment. In case of inconsistency the material assigned to IfcCovering elements takes precedence."
  ~~Label to indicate the material or finish of the space flooring. The label is used for room book information and often displayed in room stamp.

The material information is provided in absence of an IfcCovering (type=FLOORING) object with own shape representation and material assignment. In case of inconsistency the material assigned to IfcCovering elements takes precedence.~~ Label to indicate the material or finish of the space flooring. The label is used for room book information and often displayed in room stamp.\X\0D
\X\0D
The material information is provided in absence of an IfcCovering (type=FLOORING) object with own shape representation and material assignment. In case of inconsistency the material assigned to IfcCovering elements takes precedence.
* PropertyDefs > PropertyDef [Name="FloorCoveringThickness"] > Definition "Thickness of the material layer(s) for the space flooring.  

The thickness information is provided in absence of an IfcCovering (type=FLOORING) object with own shape representation. In cases of inconsistency between the geometric parameters of an assigned IfcCovering and this attached property, the geometric parameters take precedence."
  ~~Thickness of the material layer(s) for the space flooring.  

The thickness information is provided in absence of an IfcCovering (type=FLOORING) object with own shape representation. In cases of inconsistency between the geometric parameters of an assigned IfcCovering and this attached property, the geometric parameters take precedence.~~ Thickness of the material layer(s) for the space flooring.  \X\0D
\X\0D
The thickness information is provided in absence of an IfcCovering (type=FLOORING) object with own shape representation. In cases of inconsistency between the geometric parameters of an assigned IfcCovering and this attached property, the geometric parameters take precedence.
* PropertyDefs > PropertyDef [Name="Molding"] > Definition "Label to indicate the material or construction of the molding around the space ceiling. The label is used for room book information.

The material information is provided in absence of an IfcCovering (type=MOLDING) object with own shape representation and material assignment. In case of inconsistency the material assigned to IfcCovering elements takes precedence."
  ~~Label to indicate the material or construction of the molding around the space ceiling. The label is used for room book information.

The material information is provided in absence of an IfcCovering (type=MOLDING) object with own shape representation and material assignment. In case of inconsistency the material assigned to IfcCovering elements takes precedence.~~ Label to indicate the material or construction of the molding around the space ceiling. The label is used for room book information.\X\0D
\X\0D
The material information is provided in absence of an IfcCovering (type=MOLDING) object with own shape representation and material assignment. In case of inconsistency the material assigned to IfcCovering elements takes precedence.
* PropertyDefs > PropertyDef [Name="MoldingHeight"] > Definition "Height of the molding.

The height information is provided in absence of an IfcCovering (type=MOLDING) object with own shape representation and material assignment. In case of inconsistency the height assigned to IfcCovering elements takes precedence."
  ~~Height of the molding.

The height information is provided in absence of an IfcCovering (type=MOLDING) object with own shape representation and material assignment. In case of inconsistency the height assigned to IfcCovering elements takes precedence.~~ Height of the molding.\X\0D
\X\0D
The height information is provided in absence of an IfcCovering (type=MOLDING) object with own shape representation and material assignment. In case of inconsistency the height assigned to IfcCovering elements takes precedence.
* PropertyDefs > PropertyDef [Name="SkirtingBoard"] > Definition "Label to indicate the material or construction of the skirting board around the space flooring. The label is used for room book information.

The material information is provided in absence of an IfcCovering (type=SKIRTINGBOARD) object with own shape representation and material assignment. In case of inconsistency the material assigned to IfcCovering elements takes precedence."
  ~~Label to indicate the material or construction of the skirting board around the space flooring. The label is used for room book information.

The material information is provided in absence of an IfcCovering (type=SKIRTINGBOARD) object with own shape representation and material assignment. In case of inconsistency the material assigned to IfcCovering elements takes precedence.~~ Label to indicate the material or construction of the skirting board around the space flooring. The label is used for room book information.\X\0D
\X\0D
The material information is provided in absence of an IfcCovering (type=SKIRTINGBOARD) object with own shape representation and material assignment. In case of inconsistency the material assigned to IfcCovering elements takes precedence.
* PropertyDefs > PropertyDef [Name="SkirtingBoardHeight"] > Definition "Height of the skirting board.

The height information is provided in absence of an IfcCovering (type=SKIRTINGBOARD) object with own shape representation and material assignment. In case of inconsistency the height assigned to IfcCovering elements takes precedence."
  ~~Height of the skirting board.

The height information is provided in absence of an IfcCovering (type=SKIRTINGBOARD) object with own shape representation and material assignment. In case of inconsistency the height assigned to IfcCovering elements takes precedence.~~ Height of the skirting board.\X\0D
\X\0D
The height information is provided in absence of an IfcCovering (type=SKIRTINGBOARD) object with own shape representation and material assignment. In case of inconsistency the height assigned to IfcCovering elements takes precedence.
* PropertyDefs > PropertyDef [Name="WallCovering"] > Definition "Label to indicate the material or finish of the space flooring. The label is used for room book information and often displayed in room stamp.

The material information is provided in absence of an IfcCovering (type=CLADDING) object with own shape representation and material assignment. In case of inconsistency the material assigned to IfcCovering elements takes precedence."
  ~~Label to indicate the material or finish of the space flooring. The label is used for room book information and often displayed in room stamp.

The material information is provided in absence of an IfcCovering (type=CLADDING) object with own shape representation and material assignment. In case of inconsistency the material assigned to IfcCovering elements takes precedence.~~ Label to indicate the material or finish of the space flooring. The label is used for room book information and often displayed in room stamp.\X\0D
\X\0D
The material information is provided in absence of an IfcCovering (type=CLADDING) object with own shape representation and material assignment. In case of inconsistency the material assigned to IfcCovering elements takes precedence.
* PropertyDefs > PropertyDef [Name="WallCoveringThickness"] > Definition "Thickness of the material layer(s) for the space cladding.  

The thickness information is provided in absence of an IfcCovering (type=CLADDING) object with own shape representation. In cases of inconsistency between the geometric parameters of an assigned IfcCovering and this attached property, the geometric parameters take precedence."
  ~~Thickness of the material layer(s) for the space cladding.  

The thickness information is provided in absence of an IfcCovering (type=CLADDING) object with own shape representation. In cases of inconsistency between the geometric parameters of an assigned IfcCovering and this attached property, the geometric parameters take precedence.~~ Thickness of the material layer(s) for the space cladding.  \X\0D
\X\0D
The thickness information is provided in absence of an IfcCovering (type=CLADDING) object with own shape representation. In cases of inconsistency between the geometric parameters of an assigned IfcCovering and this attached property, the geometric parameters take precedence.


Pset_SystemFurnitureElementTypeCommon.xml
=========================================

deletions
---------
* PropertyDefs > PropertyDef [Name="NominalWidth"]


Pset_MooringDeviceCommon.xml
============================

modifications
-------------
* ApplicableTypeValue "IfcMooringDevice,IfcMooringDeviceType"
  ~~IfcMooringDevice,IfcMooringDeviceType~~ IfcMooringDeviceType
* PropertyDefs > PropertyDef [Name="AnchorageType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="DeviceType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="AnchorageType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="DeviceType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_ValveTypeMixing.xml
========================

modifications
-------------
* PropertyDefs > PropertyDef [Name="MixerControl"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="MixerControl"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_SensorTypeCO2Sensor.xml
============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="SetPointConcentration"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue


Pset_Risk.xml
=============

modifications
-------------
* Definition "An indication of exposure to mischance, peril, menace, hazard or loss. Documentation of a potential hazard, likilihood and consequence aligned with AS/NZS 4360 and BS PAS 1192-6:2017, which can be assigned to or associated with a product, activity and/or location. Alternatively it may be assigned to an ISO 3864 annotation symbol.

HISTORY: Extended in IFC2x3, Revised IFC4x3 

There are various types of risk that may be encountered and there may be several instances of Pset_Risk associated to an instance or type."
  ~~An indication of exposure to mischance, peril, menace, hazard or loss. Documentation of a potential hazard, likilihood and consequence aligned with AS/NZS 4360 and BS PAS 1192-6:2017, which can be assigned to or associated with a product, activity and/or location. Alternatively it may be assigned to an ISO 3864 annotation symbol.

HISTORY: Extended in IFC2x3, Revised IFC4x3 

There are various types of risk that may be encountered and there may be several instances of Pset_Risk associated to an instance or type.~~ An indication of exposure to mischance, peril, menace, hazard or loss. Documentation of a potential hazard, likilihood and consequence aligned with AS/NZS 4360 and BS PAS 1192-6:2017, which can be assigned to or associated with a product, activity and/or location. Alternatively it may be assigned to an ISO 3864 annotation symbol.\X\0D
\X\0D
HISTORY: Extended in IFC2x3, Revised IFC4x3 \X\0D
\X\0D
There are various types of risk that may be encountered and there may be several instances of Pset_Risk associated to an instance or type.
* ApplicableTypeValue "IfcProcess,IfcTypeProcess,IfcProduct,IfcTypeProduct,IfcGroup"
  ~~IfcProcess,IfcTypeProcess,IfcProduct,IfcTypeProduct,IfcGroup~~ IfcGroup
* PropertyDefs > PropertyDef [Name="MitigatedRiskConsequence"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="MitigatedRiskLikelihood"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="MitigatedRiskSignificance"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="RiskType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="UnmitigatedRiskConsequence"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="UnmitigatedRiskLikelihood"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="UnmitigatedRiskSignificance"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="UnmitigatedRiskSignificance"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="UnmitigatedRiskConsequence"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="RiskType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="MitigatedRiskLikelihood"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="MitigatedRiskSignificance"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="MitigatedRiskConsequence"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="UnmitigatedRiskLikelihood"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;



Pset_FootingCommon.xml
======================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_CurtainWallCommon.xml
==========================

modifications
-------------
* PropertyDefs > PropertyDef [Name="AcousticRating"] > Definition "Acoustic rating for this object.
It is provided according to the national building code. It indicates the sound transmission resistance of this object by an index ratio (instead of providing full sound absorbtion values)."
  ~~Acoustic rating for this object.
It is provided according to the national building code. It indicates the sound transmission resistance of this object by an index ratio (instead of providing full sound absorbtion values).~~ Acoustic rating for this object.\X\0D
It is provided according to the national building code. It indicates the sound transmission resistance of this object by an index ratio (instead of providing full sound absorbtion values).
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="SurfaceSpreadOfFlame"] > Definition "Indication on how the flames spread around the surface,
It is given according to the national building code that governs the fire behaviour for materials."
  ~~Indication on how the flames spread around the surface,
It is given according to the national building code that governs the fire behaviour for materials.~~ Indication on how the flames spread around the surface,\X\0D
It is given according to the national building code that governs the fire behaviour for materials.
* PropertyDefs > PropertyDef [Name="ThermalTransmittance"] > Definition "Thermal transmittance coefficient (U-Value) of a material.
Here the total thermal transmittance coefficient through the wall (including all materials)."
  ~~Thermal transmittance coefficient (U-Value) of a material.
Here the total thermal transmittance coefficient through the wall (including all materials).~~ Thermal transmittance coefficient (U-Value) of a material.\X\0D
Here the total thermal transmittance coefficient through the wall (including all materials).
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Qto_VehicleBaseQuantities.xml
=============================

modifications
-------------
* QtoDefinitionAliases
  ~~QtoDefinitionAliases~~ ApplicableClasses

deletions
---------
* ApplicableClasses


Pset_BearingCommon.xml
======================

additions
---------
* Definition "$"

modifications
-------------
* PropertyDefs > PropertyDef [Name="RotationAccomodated"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="DisplacementAccomodated"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Pset_DistributionPortTypePipe.xml
=================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="ConnectionType"] > Definition "The end-style treatment of the pipe port:

BRAZED: Brazed. 
COMPRESSION: Compression. 
FLANGED: Flanged. 
GROOVED: Grooved. 
OUTSIDESLEEVE: Outside Sleeve. 
SOLDERED: Soldered. 
SWEDGE: Swedge. 
THREADED: Threaded. 
WELDED: Welded. 
OTHER: Another type of end-style has been applied.
NONE: No end-style has been applied.
USERDEFINED: User-defined port connection type. 
NOTDEFINED: Undefined port connection type."
  ~~The end-style treatment of the pipe port:

BRAZED: Brazed. 
COMPRESSION: Compression. 
FLANGED: Flanged. 
GROOVED: Grooved. 
OUTSIDESLEEVE: Outside Sleeve. 
SOLDERED: Soldered. 
SWEDGE: Swedge. 
THREADED: Threaded. 
WELDED: Welded. 
OTHER: Another type of end-style has been applied.
NONE: No end-style has been applied.
USERDEFINED: User-defined port connection type. 
NOTDEFINED: Undefined port connection type.~~ The end-style treatment of the pipe port:\X\0D
\X\0D
BRAZED: Brazed. \X\0D
COMPRESSION: Compression. \X\0D
FLANGED: Flanged. \X\0D
GROOVED: Grooved. \X\0D
OUTSIDESLEEVE: Outside Sleeve. \X\0D
SOLDERED: Soldered. \X\0D
SWEDGE: Swedge. \X\0D
THREADED: Threaded. \X\0D
WELDED: Welded. \X\0D
OTHER: Another type of end-style has been applied.\X\0D
NONE: No end-style has been applied.\X\0D
USERDEFINED: User-defined port connection type. \X\0D
NOTDEFINED: Undefined port connection type.
* PropertyDefs > PropertyDef [Name="ConnectionType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="FlowCondition"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="MassFlowRate"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Pressure"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Temperature"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Velocity"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="VolumetricFlowRate"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="ConnectionType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;



Pset_ProfileMechanical.xml
==========================

modifications
-------------
* PropertyDefs > PropertyDef [Name="MaximumSectionModulusY"] > Definition "Bending resistance about the ys axis at the point with maximum zs ordinate. For example measured in mm&#179;."
  ~~Bending resistance about the ys axis at the point with maximum zs ordinate. For example measured in mm&#179;.~~ Bending resistance about the ys axis at the point with maximum zs ordinate. For example measured in mm\S\3.
* PropertyDefs > PropertyDef [Name="MaximumSectionModulusZ"] > Definition "Bending resistance about the zs axis at the point with maximum ys ordinate. For example measured in mm&#179;."
  ~~Bending resistance about the zs axis at the point with maximum ys ordinate. For example measured in mm&#179;.~~ Bending resistance about the zs axis at the point with maximum ys ordinate. For example measured in mm\S\3.
* PropertyDefs > PropertyDef [Name="MinimumSectionModulusY"] > Definition "Bending resistance about the ys axis at the point with minimum zs ordinate. For example measured in mm&#179;."
  ~~Bending resistance about the ys axis at the point with minimum zs ordinate. For example measured in mm&#179;.~~ Bending resistance about the ys axis at the point with minimum zs ordinate. For example measured in mm\S\3.
* PropertyDefs > PropertyDef [Name="MinimumSectionModulusZ"] > Definition "Bending resistance about the zs axis at the point with minimum ys ordinate. For example measured in mm&#179;."
  ~~Bending resistance about the zs axis at the point with minimum ys ordinate. For example measured in mm&#179;.~~ Bending resistance about the zs axis at the point with minimum ys ordinate. For example measured in mm\S\3.
* PropertyDefs > PropertyDef [Name="ShearAreaY"] > Definition "Area of the profile for calculating the shear stress due to shear force parallel to the section analysis axis ys. For example measured in mm&#178;. If given, the shear area ys shall be non-negative."
  ~~Area of the profile for calculating the shear stress due to shear force parallel to the section analysis axis ys. For example measured in mm&#178;. If given, the shear area ys shall be non-negative.~~ Area of the profile for calculating the shear stress due to shear force parallel to the section analysis axis ys. For example measured in mm\S\2. If given, the shear area ys shall be non-negative.
* PropertyDefs > PropertyDef [Name="ShearAreaZ"] > Definition "Area of the profile for calculating the shear stress due to shear force parallel to the section analysis axis zs. For example measured in mm&#178;. If given, the shear area zs shall be non-negative."
  ~~Area of the profile for calculating the shear stress due to shear force parallel to the section analysis axis zs. For example measured in mm&#178;. If given, the shear area zs shall be non-negative.~~ Area of the profile for calculating the shear stress due to shear force parallel to the section analysis axis zs. For example measured in mm\S\2. If given, the shear area zs shall be non-negative.
* PropertyDefs > PropertyDef [Name="ShearDeformationAreaY"] > Definition "Area of the profile for calculating the shear deformation due to a shear force parallel to ys. For example measured in mm&#178;. If given, the shear deformation area ys shall be non-negative."
  ~~Area of the profile for calculating the shear deformation due to a shear force parallel to ys. For example measured in mm&#178;. If given, the shear deformation area ys shall be non-negative.~~ Area of the profile for calculating the shear deformation due to a shear force parallel to ys. For example measured in mm\S\2. If given, the shear deformation area ys shall be non-negative.
* PropertyDefs > PropertyDef [Name="ShearDeformationAreaZ"] > Definition "Area of the profile for calculating the shear deformation due to a shear force parallel to zs. For example measured in mm&#178;. If given, the shear deformation area zs shall be non-negative."
  ~~Area of the profile for calculating the shear deformation due to a shear force parallel to zs. For example measured in mm&#178;. If given, the shear deformation area zs shall be non-negative.~~ Area of the profile for calculating the shear deformation due to a shear force parallel to zs. For example measured in mm\S\2. If given, the shear deformation area zs shall be non-negative.
* PropertyDefs > PropertyDef [Name="TorsionalSectionModulus"] > Definition "Torsional resistance (about xs). For example measured in mm&#179;."
  ~~Torsional resistance (about xs). For example measured in mm&#179;.~~ Torsional resistance (about xs). For example measured in mm\S\3.


Qto_ControllerBaseQuantities.xml
================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Pset_ShiplockComplex.xml
========================

modifications
-------------
* ApplicableClasses > ClassName "IfcMarineFacility/SHIPLOCK"
  ~~IfcMarineFacility/SHIPLOCK~~ IfcMarineFacility
* ApplicableTypeValue "IfcMarineFacility/SHIPLOCK"
  ~~IfcMarineFacility/SHIPLOCK~~ IfcMarineFacility


Pset_DamperTypeControlDamper.xml
================================

modifications
-------------
* Definition "Control damper type attributes.
Pset renamed from Pset_DamperTypeControl to Pset_DamperTypeControlDamper in IFC2x2 Pset Addendum."
  ~~Control damper type attributes.
Pset renamed from Pset_DamperTypeControl to Pset_DamperTypeControlDamper in IFC2x2 Pset Addendum.~~ Control damper type attributes.\X\0D
Pset renamed from Pset_DamperTypeControl to Pset_DamperTypeControlDamper in IFC2x2 Pset Addendum.
* PropertyDefs > PropertyDef [Name="TorqueRange"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="ControlDamperOperation"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Qto_PumpBaseQuantities.xml
==========================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Pset_SensorTypeHeatSensor.xml
=============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="SetPointTemperature"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue


Qto_DuctSilencerBaseQuantities.xml
==================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases



Qto_PictorialSignQuantities.xml
===============================

additions
---------
* Definition "$"

modifications
-------------
* QtoDefinitionAliases
  ~~QtoDefinitionAliases~~ ApplicableTypeValue
* QtoDefs > QtoDef [Name="Area"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefs > QtoDef [Name="SignArea"]


Pset_SoundAttenuation.xml
=========================

modifications
-------------
* ApplicableClasses > ClassName "IfcAnnotation/SOUND"
  ~~IfcAnnotation/SOUND~~ IfcAnnotation
* ApplicableTypeValue "IfcAnnotation/SOUND"
  ~~IfcAnnotation/SOUND~~ IfcAnnotation
* PropertyDefs > PropertyDef [Name="SoundFrequency"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="SoundScale"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="SoundPressure"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Pset_SensorTypeRadiationSensor.xml
==================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="SetPointRadiation"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue


Qto_DistributionChamberElementBaseQuantities.xml
================================================

modifications
-------------
* QtoDefs > QtoDef [Name="GrossSurfaceArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetSurfaceArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetVolume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossVolume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases



Pset_OutletTypeCommon.xml
=========================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_FlowMeterTypeCommon.xml
============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="ReadOutType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="ReadOutType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_DistributionChamberElementTypeManhole.xml
==============================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="AccessCoverMaterial"] > Definition "The material from which the access cover to the chamber is constructed.
NOTE: It is assumed that chamber walls will be constructed of a single material."
  ~~The material from which the access cover to the chamber is constructed.
NOTE: It is assumed that chamber walls will be constructed of a single material.~~ The material from which the access cover to the chamber is constructed.\X\0D
NOTE: It is assumed that chamber walls will be constructed of a single material.
* PropertyDefs > PropertyDef [Name="BaseMaterial"] > Definition "The material from which the base of the chamber is constructed.
NOTE: It is assumed that chamber base will be constructed of a single material."
  ~~The material from which the base of the chamber is constructed.
NOTE: It is assumed that chamber base will be constructed of a single material.~~ The material from which the base of the chamber is constructed.\X\0D
NOTE: It is assumed that chamber base will be constructed of a single material.
* PropertyDefs > PropertyDef [Name="BaseThickness"] > Definition "The thickness of the chamber base construction
NOTE: It is assumed that chamber base will be constructed at a single thickness."
  ~~The thickness of the chamber base construction
NOTE: It is assumed that chamber base will be constructed at a single thickness.~~ The thickness of the chamber base construction\X\0D
NOTE: It is assumed that chamber base will be constructed at a single thickness.
* PropertyDefs > PropertyDef [Name="WallMaterial"] > Definition "The material from which the wall of the chamber is constructed.
NOTE: It is assumed that chamber walls will be constructed of a single material."
  ~~The material from which the wall of the chamber is constructed.
NOTE: It is assumed that chamber walls will be constructed of a single material.~~ The material from which the wall of the chamber is constructed.\X\0D
NOTE: It is assumed that chamber walls will be constructed of a single material.
* PropertyDefs > PropertyDef [Name="WallThickness"] > Definition "The thickness of the chamber wall construction
NOTE: It is assumed that chamber walls will be constructed at a single thickness."
  ~~The thickness of the chamber wall construction
NOTE: It is assumed that chamber walls will be constructed at a single thickness.~~ The thickness of the chamber wall construction\X\0D
NOTE: It is assumed that chamber walls will be constructed at a single thickness.

deletions
---------
* PropertyDefs > PropertyDef [Name="AccessCoverMaterial"] > PropertyType
* PropertyDefs > PropertyDef [Name="BaseMaterial"] > PropertyType
* PropertyDefs > PropertyDef [Name="WallMaterial"] > PropertyType


Qto_EvaporativeCoolerBaseQuantities.xml
=======================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Pset_CableCarrierSegmentTypeCableLadderSegment.xml
==================================================

modifications
-------------
* Definition "An open carrier segment on which cables are carried on a ladder structure.
HISTORY: IFC4 - NominalLength deleted. To be handled as a quantity measure."
  ~~An open carrier segment on which cables are carried on a ladder structure.
HISTORY: IFC4 - NominalLength deleted. To be handled as a quantity measure.~~ An open carrier segment on which cables are carried on a ladder structure.\X\0D
HISTORY: IFC4 - NominalLength deleted. To be handled as a quantity measure.

deletions
---------
* PropertyDefs > PropertyDef [Name="NominalWidth"]


Pset_ConcreteElementGeneral.xml
===============================

modifications
-------------
* ApplicableTypeValue "IfcBeam,IfcBuildingElementProxy,IfcChimney,IfcColumn,IfcFooting,IfcMember,IfcPile,IfcPlate,IfcRailing,IfcRamp,IfcRampFlight,IfcRoof,IfcSlab,IfcStair,IfcStairFlight,IfcWall,IfcCivilElement"
  ~~IfcBeam,IfcBuildingElementProxy,IfcChimney,IfcColumn,IfcFooting,IfcMember,IfcPile,IfcPlate,IfcRailing,IfcRamp,IfcRampFlight,IfcRoof,IfcSlab,IfcStair,IfcStairFlight,IfcWall,IfcCivilElement~~ IfcCivilElement


Pset_SanitaryTerminalTypeCommon.xml
===================================

additions
---------
* PropertyDefs > PropertyDef [Name="NominalLength"] > Definition "Nominal length of the object"

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="NominalWidth"]
* PropertyDefs > PropertyDef [Name="NominalDepth"]


Pset_ShadingDevicePHistory.xml
==============================

modifications
-------------
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="TiltAngle"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Azimuth"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Pset_CoilPHistory.xml
=====================

modifications
-------------
* Definition "Coil performance history common attributes.
Sound attribute deleted in IFC2x2 Pset Addendum: Use IfcSoundProperties instead."
  ~~Coil performance history common attributes.
Sound attribute deleted in IFC2x2 Pset Addendum: Use IfcSoundProperties instead.~~ Coil performance history common attributes.\X\0D
Sound attribute deleted in IFC2x2 Pset Addendum: Use IfcSoundProperties instead.
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="AtmosphericPressure"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="SoundCurve"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="AirPressureDropCurve"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="FaceVelocity"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Pset_TubeBundleTypeFinned.xml
=============================

modifications
-------------
* Definition "Finned tube bundle type attributes.
Contains the attributes related to the fins attached to a tube in a finned tube bundle such as is commonly found in coils."
  ~~Finned tube bundle type attributes.
Contains the attributes related to the fins attached to a tube in a finned tube bundle such as is commonly found in coils.~~ Finned tube bundle type attributes.\X\0D
Contains the attributes related to the fins attached to a tube in a finned tube bundle such as is commonly found in coils.


Pset_SanitaryTerminalTypeUrinal.xml
===================================

additions
---------
* ApplicableClasses
* ApplicableClasses

modifications
-------------
* PropertyDefs
  ~~PropertyDefs~~ ApplicableClasses
* ApplicableClasses
  ~~ApplicableClasses~~ PropertyDefs
* ApplicableClasses > ClassName "IfcSanitaryTerminal/URINAL"
  ~~&lt;ClassName&gt;~~ &lt;PropertyDef&gt;


Pset_ValvePHistory.xml
======================

modifications
-------------
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="PercentageOpen"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="MeasuredFlowRate"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="MeasuredPressureDrop"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Qto_ConstructionMaterialResourceBaseQuantities.xml
==================================================

modifications
-------------
* QtoDefs > QtoDef [Name="GrossWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossVolume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetVolume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases


Pset_AudioVisualApplianceTypeCamera.xml
=======================================

additions
---------
* PropertyDefs > PropertyDef [Name="PanHorizontal"]
* PropertyDefs > PropertyDef [Name="PanTiltZoomPreset"]

modifications
-------------
* PropertyDefs > PropertyDef [Name="VideoResolutionMode"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="TiltHorizontal"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="CameraType"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Zoom"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="VideoCaptureInterval"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="PanHorizontal"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="PanTiltZoomPreset"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="PanVertical"]
* PropertyDefs > PropertyDef [Name="TiltVertical"]



Pset_PumpTypeCommon.xml
=======================

modifications
-------------
* PropertyDefs > PropertyDef [Name="FlowRateRange"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="FlowResistanceRange"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="TemperatureRange"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_ControllerTypeFloating.xml
===============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="ControlType"] > Definition "The type of signal modification effected and applicable ports: 

CONSTANT: No inputs; SignalOffset is written to the output value.
MODIFIER: Single analog input is read, added to SignalOffset, multiplied by SignalFactor, and written to the output value.
ABSOLUTE: Single analog input is read and absolute value is written to the output value.
INVERSE: Single analog input is read, 1.0 is divided by the input value and written to the output value.
HYSTERISIS: Single analog input is read, delayed according to SignalTime, and written to the output value.
RUNNINGAVERAGE: Single analog input is read, averaged over SignalTime, and written to the output value.
DERIVATIVE: Single analog input is read and the rate of change during the SignalTime is written to the output value.
INTEGRAL: Single analog input is read and the average value during the SignalTime is written to the output value.
BINARY: Single binary input is read and SignalOffset is written to the output value if True.
ACCUMULATOR: Single binary input is read, and for each pulse the SignalOffset is added to the accumulator, and while the accumulator is greater than the SignalFactor, the accumulator is decremented by SignalFactor and the integer result is incremented by one.
PULSECONVERTER: Single integer input is read, and for each increment the SignalMultiplier is added and written to the output value.
SUM: Two analog inputs are read, added, and written to the output value.
SUBTRACT: Two analog inputs are read, subtracted, and written to the output value.
PRODUCT: Two analog inputs are read, multiplied, and written to the output value.
DIVIDE: Two analog inputs are read, divided, and written to the output value.
AVERAGE: Two analog inputs are read and the average is written to the output value.
MAXIMUM: Two analog inputs are read and the maximum is written to the output value.
MINIMUM: Two analog inputs are read and the minimum is written to the output value..
INPUT: Controller element is a dedicated input.
OUTPUT: Controller element is a dedicated output.
VARIABLE: Controller element is an in-memory variable."
  ~~The type of signal modification effected and applicable ports: 

CONSTANT: No inputs; SignalOffset is written to the output value.
MODIFIER: Single analog input is read, added to SignalOffset, multiplied by SignalFactor, and written to the output value.
ABSOLUTE: Single analog input is read and absolute value is written to the output value.
INVERSE: Single analog input is read, 1.0 is divided by the input value and written to the output value.
HYSTERISIS: Single analog input is read, delayed according to SignalTime, and written to the output value.
RUNNINGAVERAGE: Single analog input is read, averaged over SignalTime, and written to the output value.
DERIVATIVE: Single analog input is read and the rate of change during the SignalTime is written to the output value.
INTEGRAL: Single analog input is read and the average value during the SignalTime is written to the output value.
BINARY: Single binary input is read and SignalOffset is written to the output value if True.
ACCUMULATOR: Single binary input is read, and for each pulse the SignalOffset is added to the accumulator, and while the accumulator is greater than the SignalFactor, the accumulator is decremented by SignalFactor and the integer result is incremented by one.
PULSECONVERTER: Single integer input is read, and for each increment the SignalMultiplier is added and written to the output value.
SUM: Two analog inputs are read, added, and written to the output value.
SUBTRACT: Two analog inputs are read, subtracted, and written to the output value.
PRODUCT: Two analog inputs are read, multiplied, and written to the output value.
DIVIDE: Two analog inputs are read, divided, and written to the output value.
AVERAGE: Two analog inputs are read and the average is written to the output value.
MAXIMUM: Two analog inputs are read and the maximum is written to the output value.
MINIMUM: Two analog inputs are read and the minimum is written to the output value..
INPUT: Controller element is a dedicated input.
OUTPUT: Controller element is a dedicated output.
VARIABLE: Controller element is an in-memory variable.~~ The type of signal modification effected and applicable ports: \X\0D
\X\0D
CONSTANT: No inputs; SignalOffset is written to the output value.\X\0D
MODIFIER: Single analog input is read, added to SignalOffset, multiplied by SignalFactor, and written to the output value.\X\0D
ABSOLUTE: Single analog input is read and absolute value is written to the output value.\X\0D
INVERSE: Single analog input is read, 1.0 is divided by the input value and written to the output value.\X\0D
HYSTERISIS: Single analog input is read, delayed according to SignalTime, and written to the output value.\X\0D
RUNNINGAVERAGE: Single analog input is read, averaged over SignalTime, and written to the output value.\X\0D
DERIVATIVE: Single analog input is read and the rate of change during the SignalTime is written to the output value.\X\0D
INTEGRAL: Single analog input is read and the average value during the SignalTime is written to the output value.\X\0D
BINARY: Single binary input is read and SignalOffset is written to the output value if True.\X\0D
ACCUMULATOR: Single binary input is read, and for each pulse the SignalOffset is added to the accumulator, and while the accumulator is greater than the SignalFactor, the accumulator is decremented by SignalFactor and the integer result is incremented by one.\X\0D
PULSECONVERTER: Single integer input is read, and for each increment the SignalMultiplier is added and written to the output value.\X\0D
SUM: Two analog inputs are read, added, and written to the output value.\X\0D
SUBTRACT: Two analog inputs are read, subtracted, and written to the output value.\X\0D
PRODUCT: Two analog inputs are read, multiplied, and written to the output value.\X\0D
DIVIDE: Two analog inputs are read, divided, and written to the output value.\X\0D
AVERAGE: Two analog inputs are read and the average is written to the output value.\X\0D
MAXIMUM: Two analog inputs are read and the maximum is written to the output value.\X\0D
MINIMUM: Two analog inputs are read and the minimum is written to the output value..\X\0D
INPUT: Controller element is a dedicated input.\X\0D
OUTPUT: Controller element is a dedicated output.\X\0D
VARIABLE: Controller element is an in-memory variable.
* PropertyDefs > PropertyDef [Name="ControlType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Labels"] > PropertyType > TypePropertyTableValue
  ~~TypePropertyTableValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Range"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Value"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Labels"] > PropertyType > TypePropertyTableValue > Expression
  ~~&lt;Expression&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="ControlType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="Labels"] > PropertyType > TypePropertyTableValue > DefiningValue
* PropertyDefs > PropertyDef [Name="Labels"] > PropertyType > TypePropertyTableValue > DefinedValue


Qto_CourseBaseQuantities.xml
============================

additions
---------
* Definition "$"

modifications
-------------
* QtoDefinitionAliases
  ~~QtoDefinitionAliases~~ ApplicableTypeValue
* QtoDefs > QtoDef [Name="Length"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefs > QtoDef [Name="Width"]
* QtoDefs > QtoDef [Name="Thickness"]
* QtoDefs > QtoDef [Name="Volume"]
* QtoDefs > QtoDef [Name="GrossVolume"]
* QtoDefs > QtoDef [Name="Weight"]


Qto_CoolingTowerBaseQuantities.xml
==================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Qto_WindowBaseQuantities.xml
============================

modifications
-------------
* QtoDefs > QtoDef [Name="Perimeter"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Area"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Height"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Width"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases


Pset_ValveTypePressureRelief.xml
================================

modifications
-------------
* Definition "Spring or weight loaded valve that automatically discharges to a safe place fluid that has built up to excessive pressure in pipes or fittings.
Note that a pressure relief valve is constrained to have a single port pattern."
  ~~Spring or weight loaded valve that automatically discharges to a safe place fluid that has built up to excessive pressure in pipes or fittings.
Note that a pressure relief valve is constrained to have a single port pattern.~~ Spring or weight loaded valve that automatically discharges to a safe place fluid that has built up to excessive pressure in pipes or fittings.\X\0D
Note that a pressure relief valve is constrained to have a single port pattern.


Pset_DuctSilencerTypeCommon.xml
===============================

modifications
-------------
* Definition "Duct silencer type common attributes.
InsertionLoss and RegeneratedSound attributes deleted in IFC2x2 Pset Addendum: Use IfcSoundProperties instead."
  ~~Duct silencer type common attributes.
InsertionLoss and RegeneratedSound attributes deleted in IFC2x2 Pset Addendum: Use IfcSoundProperties instead.~~ Duct silencer type common attributes.\X\0D
InsertionLoss and RegeneratedSound attributes deleted in IFC2x2 Pset Addendum: Use IfcSoundProperties instead.
* PropertyDefs > PropertyDef [Name="AirFlowrateRange"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="TemperatureRange"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="WorkingPressureRange"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_SensorTypeTemperatureSensor.xml
====================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="TemperatureSensorType"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="SetPointTemperature"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Pset_FanOccurrence.xml
======================

modifications
-------------
* PropertyDefs > PropertyDef [Name="ApplicationOfFan"] > Definition "The functional application of the fan.

SupplyAir: Supply air fan. 
ReturnAir: Return air fan. 
ExhaustAir: Exhaust air fan. 
Other: Other type of application not defined above."
  ~~The functional application of the fan.

SupplyAir: Supply air fan. 
ReturnAir: Return air fan. 
ExhaustAir: Exhaust air fan. 
Other: Other type of application not defined above.~~ The functional application of the fan.\X\0D
\X\0D
SupplyAir: Supply air fan. \X\0D
ReturnAir: Return air fan. \X\0D
ExhaustAir: Exhaust air fan. \X\0D
Other: Other type of application not defined above.
* PropertyDefs > PropertyDef [Name="ApplicationOfFan"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="CoilPosition"] > Definition "Defines the relationship between a fan and a coil.

DrawThrough: Fan located downstream of the coil.
BlowThrough: Fan located upstream of the coil."
  ~~Defines the relationship between a fan and a coil.

DrawThrough: Fan located downstream of the coil.
BlowThrough: Fan located upstream of the coil.~~ Defines the relationship between a fan and a coil.\X\0D
\X\0D
DrawThrough: Fan located downstream of the coil.\X\0D
BlowThrough: Fan located upstream of the coil.
* PropertyDefs > PropertyDef [Name="CoilPosition"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="DischargeType"] > Definition "Defines the type of connection at the fan discharge.

Duct: Discharge into ductwork.
Screen: Discharge into screen outlet.
Louver: Discharge into a louver.
Damper: Discharge into a damper."
  ~~Defines the type of connection at the fan discharge.

Duct: Discharge into ductwork.
Screen: Discharge into screen outlet.
Louver: Discharge into a louver.
Damper: Discharge into a damper.~~ Defines the type of connection at the fan discharge.\X\0D
\X\0D
Duct: Discharge into ductwork.\X\0D
Screen: Discharge into screen outlet.\X\0D
Louver: Discharge into a louver.\X\0D
Damper: Discharge into a damper.
* PropertyDefs > PropertyDef [Name="DischargeType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="FanMountingType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="MotorPosition"] > Definition "Defines the location of the motor relative to the air stream.

InAirStream: Fan motor is in the air stream.
OutOfAirStream: Fan motor is out of the air stream."
  ~~Defines the location of the motor relative to the air stream.

InAirStream: Fan motor is in the air stream.
OutOfAirStream: Fan motor is out of the air stream.~~ Defines the location of the motor relative to the air stream.\X\0D
\X\0D
InAirStream: Fan motor is in the air stream.\X\0D
OutOfAirStream: Fan motor is out of the air stream.
* PropertyDefs > PropertyDef [Name="MotorPosition"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* 
  ~~PSET_OCCURRENCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="MotorPosition"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="FanMountingType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="ApplicationOfFan"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="CoilPosition"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="DischargeType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_SwitchingDeviceTypeSelectorSwitch.xml
==========================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="SelectorType"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="SwitchActivation"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="SwitchUsage"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Pset_DoorWindowGlazingType.xml
==============================

modifications
-------------
* ApplicableTypeValue "IfcDoor, IfcWindow"
  ~~IfcDoor, IfcWindow~~ IfcWindow
* PropertyDefs > PropertyDef [Name="SolarHeatGainTransmittance"] > Definition "(SHGC): The ratio of incident solar radiation that contributes to the heat gain of the interior, it is the solar radiation that directly passes (Tsol or &#964;e) plus the part of the absorbed radiation that is distributed to the interior (qi). The SHGC is refered to also as g-value (g = &#964;e + qi)."
  ~~(SHGC): The ratio of incident solar radiation that contributes to the heat gain of the interior, it is the solar radiation that directly passes (Tsol or &#964;e) plus the part of the absorbed radiation that is distributed to the interior (qi). The SHGC is refered to also as g-value (g = &#964;e + qi).~~ (SHGC): The ratio of incident solar radiation that contributes to the heat gain of the interior, it is the solar radiation that directly passes (Tsol or \X2\03C4\X0\e) plus the part of the absorbed radiation that is distributed to the interior (qi). The SHGC is refered to also as g-value (g = \X2\03C4\X0\e + qi).
* PropertyDefs > PropertyDef [Name="SolarReflectance"] > Definition "(Rsol): The ratio of incident solar radiation that is reflected by a glazing system (also named &#961;e). Note the following equation Asol + Rsol + Tsol = 1"
  ~~(Rsol): The ratio of incident solar radiation that is reflected by a glazing system (also named &#961;e). Note the following equation Asol + Rsol + Tsol = 1~~ (Rsol): The ratio of incident solar radiation that is reflected by a glazing system (also named \X2\03C1\X0\e). Note the following equation Asol + Rsol + Tsol = 1
* PropertyDefs > PropertyDef [Name="SolarTransmittance"] > Definition "(Tsol): The ratio of incident solar radiation that directly passes through a glazing system (also named &#964;e). Note the following equation Asol + Rsol + Tsol = 1"
  ~~(Tsol): The ratio of incident solar radiation that directly passes through a glazing system (also named &#964;e). Note the following equation Asol + Rsol + Tsol = 1~~ (Tsol): The ratio of incident solar radiation that directly passes through a glazing system (also named \X2\03C4\X0\e). Note the following equation Asol + Rsol + Tsol = 1
* PropertyDefs > PropertyDef [Name="ThermalTransmittanceSummer"] > Definition "Thermal transmittance coefficient (U-Value) of a material.
Summer thermal transmittance coefficient of the glazing only, often referred to as (U-value)."
  ~~Thermal transmittance coefficient (U-Value) of a material.
Summer thermal transmittance coefficient of the glazing only, often referred to as (U-value).~~ Thermal transmittance coefficient (U-Value) of a material.\X\0D
Summer thermal transmittance coefficient of the glazing only, often referred to as (U-value).
* PropertyDefs > PropertyDef [Name="ThermalTransmittanceWinter"] > Definition "Thermal transmittance coefficient (U-Value) of a material.
Winter thermal transmittance coefficient of the glazing only, often referred to as (U-value)."
  ~~Thermal transmittance coefficient (U-Value) of a material.
Winter thermal transmittance coefficient of the glazing only, often referred to as (U-value).~~ Thermal transmittance coefficient (U-Value) of a material.\X\0D
Winter thermal transmittance coefficient of the glazing only, often referred to as (U-value).



Qto_CondenserBaseQuantities.xml
===============================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Pset_DuctSegmentOccurrence.xml
==============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Color"] > Definition "The color of the duct segment.

Note: This is typically used for any duct segments with a painted surface which is not otherwise specified as a covering."
  ~~The color of the duct segment.

Note: This is typically used for any duct segments with a painted surface which is not otherwise specified as a covering.~~ The color of the duct segment.\X\0D
\X\0D
Note: This is typically used for any duct segments with a painted surface which is not otherwise specified as a covering.
* 
  ~~PSET_OCCURRENCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE


Pset_PipeFittingTypeCommon.xml
==============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="PressureRange"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="TemperatureRange"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;



Pset_SpaceFireSafetyRequirements.xml
====================================

modifications
-------------
* ApplicableTypeValue "IfcSpace, IfcSpatialZone, IfcZone"
  ~~IfcSpace, IfcSpatialZone, IfcZone~~ IfcZone
* PropertyDefs > PropertyDef [Name="FireExit"] > Definition "Indication whether this object is designed to serve as an exit in the case of fire (TRUE) or not (FALSE).
Here whether the space (in case of e.g., a corridor) is designed to serve as an exit space, e.g., for fire escape purposes."
  ~~Indication whether this object is designed to serve as an exit in the case of fire (TRUE) or not (FALSE).
Here whether the space (in case of e.g., a corridor) is designed to serve as an exit space, e.g., for fire escape purposes.~~ Indication whether this object is designed to serve as an exit in the case of fire (TRUE) or not (FALSE).\X\0D
Here whether the space (in case of e.g., a corridor) is designed to serve as an exit space, e.g., for fire escape purposes.
* PropertyDefs > PropertyDef [Name="SprinklerProtectionAutomatic"] > Definition "Indication whether the space has an automatic sprinkler protection (TRUE) or not (FALSE).
It should only be given, if the property "SprinklerProtection" is set to TRUE."
  ~~Indication whether the space has an automatic sprinkler protection (TRUE) or not (FALSE).
It should only be given, if the property "SprinklerProtection" is set to TRUE.~~ Indication whether the space has an automatic sprinkler protection (TRUE) or not (FALSE).\X\0D
It should only be given, if the property "SprinklerProtection" is set to TRUE.


Qto_KerbBaseQuantities.xml
==========================

additions
---------
* Definition "$"

modifications
-------------
* QtoDefinitionAliases
  ~~QtoDefinitionAliases~~ ApplicableTypeValue


Qto_SpaceHeaterBaseQuantities.xml
=================================

modifications
-------------
* QtoDefs > QtoDef [Name="Length"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases



Qto_CableSegmentBaseQuantities.xml
==================================

modifications
-------------
* QtoDefs > QtoDef [Name="Length"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="OuterSurfaceArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="CrossSectionArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases



Pset_SpaceHeaterTypeRadiator.xml
================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="RadiatorType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="RadiatorType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_UnitaryControlElementTypeThermostat.xml
============================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="TemperatureSetPoint"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue


Qto_HumidifierBaseQuantities.xml
================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Pset_AnnotationContourLine.xml
==============================

modifications
-------------
* ApplicableClasses > ClassName "IfcAnnotation/ContourLine"
  ~~IfcAnnotation/ContourLine~~ IfcAnnotation
* ApplicableTypeValue "IfcAnnotation/ContourLine"
  ~~IfcAnnotation/ContourLine~~ IfcAnnotation


Pset_ProtectiveDeviceTrippingUnitTypeThermal.xml
================================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="ThermalTrippingUnitType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="ThermalTrippingUnitType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_PipeFittingPHistory.xml
============================

modifications
-------------
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="LossCoefficient"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="FlowrateLeakage"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Pset_ElectricGeneratorTypeCommon.xml
====================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_EnergyRequirements.xml
===========================

modifications
-------------
* ApplicableTypeValue "IfcDistributionElement,IfcDistributionElementType,IfcTransportElement,IfcTransportElementType"
  ~~IfcDistributionElement,IfcDistributionElementType,IfcTransportElement,IfcTransportElementType~~ IfcTransportElementType


Qto_OutletBaseQuantities.xml
============================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases



Pset_FlowMeterTypeWaterMeter.xml
================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="BackflowPreventerType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Type"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="BackflowPreventerType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="Type"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_ChillerTypeCommon.xml
==========================

additions
---------
* PropertyDefs > PropertyDef [Name="FullLoadRatioCurve"]

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="CapacityCurve"] > PropertyType
  ~~&lt;PropertyType&gt;~~ &lt;PropertyType&gt;
* PropertyDefs > PropertyDef [Name="FullLoadRatioCurve"] > Name "FullLoadRatioCurve"
  ~~&lt;Name&gt;~~ &lt;Name&gt;
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="CapacityCurve"] > Name "CapacityCurve"
  ~~&lt;Name&gt;~~ &lt;Name&gt;
* PropertyDefs > PropertyDef [Name="FullLoadRatioCurve"] > Definition "Ratio of actual power to full load power as a quadratic function of part load, at certain condensing and evaporating temperature, FracFullLoadPower = f ( PartLoadRatio)."
  ~~&lt;Definition&gt;~~ &lt;Definition&gt;
* PropertyDefs > PropertyDef [Name="FullLoadRatioCurve"] > PropertyType
  ~~&lt;PropertyType&gt;~~ &lt;PropertyType&gt;
* PropertyDefs > PropertyDef [Name="CapacityCurve"] > Definition "Chiller cooling capacity is a function of condensing temperature and evaporating temperature, data is in table form, Capacity = f (TempCon, TempEvp), capacity = a1+b1\*Tei+c1\*Tei\^2+d1\*Tci+e1\*Tci\^2+f1\*Tei\*Tci. 
This table uses multiple input variables; to represent, both DefiningValues and DefinedValues lists are null and IfcTable is attached using IfcPropertyConstraintRelationship and IfcMetric.  Columns are specified in the following order: 
1.IfcPowerMeasure:Capacity
2.IfcThermodynamicTemperatureMeasure:CondensingTemperature
3.IfcThermodynamicTemperatureMeasure:EvaporatingTemperature"
  ~~&lt;Definition&gt;~~ &lt;Definition&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="CoefficientOfPerformanceCurve"]


Pset_DiscreteAccessoryLadderTrussConnector.xml
==============================================

modifications
-------------
* ApplicableClasses > ClassName "IfcDiscreteAccessory/Ladder truss connector"
  ~~IfcDiscreteAccessory/Ladder truss connector~~ IfcDiscreteAccessory
* ApplicableTypeValue "IfcDiscreteAccessory/Ladder truss connector"
  ~~IfcDiscreteAccessory/Ladder truss connector~~ IfcDiscreteAccessory



Pset_EnvironmentalEmissions.xml
===============================

modifications
-------------
* ApplicableTypeValue "IfcDistributionElement,IfcDistributionElementType,IfcTransportElement,IfcTransportElementType"
  ~~IfcDistributionElement,IfcDistributionElementType,IfcTransportElement,IfcTransportElementType~~ IfcTransportElementType


Pset_Condition.xml
==================

modifications
-------------
* ApplicableTypeValue "IfcElement,IfcSystem,IfcAsset"
  ~~IfcElement,IfcSystem,IfcAsset~~ IfcAsset

deletions
---------
* PropertyDefs > PropertyDef [Name="AssessmentMethod"] > PropertyType



Pset_ProtectiveDeviceTypeEarthLeakageCircuitBreaker.xml
=======================================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="EarthFailureDeviceType"] > Definition "A list of the available types of circuit breaker from which that required may be selected where:

Standard: Device that operates without a time delay.
TimeDelayed: Device that operates after a time delay."
  ~~A list of the available types of circuit breaker from which that required may be selected where:

Standard: Device that operates without a time delay.
TimeDelayed: Device that operates after a time delay.~~ A list of the available types of circuit breaker from which that required may be selected where:\X\0D
\X\0D
Standard: Device that operates without a time delay.\X\0D
TimeDelayed: Device that operates after a time delay.
* PropertyDefs > PropertyDef [Name="EarthFailureDeviceType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="EarthFailureDeviceType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;



Qto_FanBaseQuantities.xml
=========================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Pset_ProtectiveDeviceTrippingUnitCurrentAdjustment.xml
======================================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="AdjustmentRange"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="AdjustmentValues"] > PropertyType > TypePropertyListValue
  ~~TypePropertyListValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="AdjustmentValues"] > PropertyType > TypePropertyListValue > ListValue
  ~~ListValue~~ DataType
* PropertyDefs > PropertyDef [Name="AdjustmentValueType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="AdjustmentValueType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Qto_ProtectiveDeviceTrippingUnitBaseQuantities.xml
==================================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Qto_MarineFacilityBaseQuantities.xml
====================================

deletions
---------
* QtoDefinitionAliases


Pset_DistributionSystemTypeElectrical.xml
=========================================

modifications
-------------
* ApplicableClasses > ClassName "IfcDistributionSystem/ELECTRICAL"
  ~~IfcDistributionSystem/ELECTRICAL~~ IfcDistributionSystem
* ApplicableTypeValue "IfcDistributionSystem/ELECTRICAL"
  ~~IfcDistributionSystem/ELECTRICAL~~ IfcDistributionSystem
* PropertyDefs > PropertyDef [Name="Diversity"] > Definition "The ratio, expressed as a numerical
value or as a percentage, of the
simultaneous maximum demand of
a group of electrical appliances or
consumers within a specified period,
to the sum of their individual maximum
demands within the same
period. The group of electrical appliances is in this case connected to this circuit. Defenition from IEC 60050, IEV 691-10-04 
NOTE1: It is often not desirable to size each conductor in a distribution system to support the total connected load at that point in the network. Diversity is applied on the basis of the anticipated loadings that are likely to result from all loads not being connected at the same time.
NOTE2: Diversity is applied to final circuits only, not to sub-main circuits supplying other DBs."
  ~~The ratio, expressed as a numerical
value or as a percentage, of the
simultaneous maximum demand of
a group of electrical appliances or
consumers within a specified period,
to the sum of their individual maximum
demands within the same
period. The group of electrical appliances is in this case connected to this circuit. Defenition from IEC 60050, IEV 691-10-04 
NOTE1: It is often not desirable to size each conductor in a distribution system to support the total connected load at that point in the network. Diversity is applied on the basis of the anticipated loadings that are likely to result from all loads not being connected at the same time.
NOTE2: Diversity is applied to final circuits only, not to sub-main circuits supplying other DBs.~~ The ratio, expressed as a numerical\X\0D
value or as a percentage, of the\X\0D
simultaneous maximum demand of\X\0D
a group of electrical appliances or\X\0D
consumers within a specified period,\X\0D
to the sum of their individual maximum\X\0D
demands within the same\X\0D
period. The group of electrical appliances is in this case connected to this circuit. Defenition from IEC 60050, IEV 691-10-04 \X\0D
NOTE1: It is often not desirable to size each conductor in a distribution system to support the total connected load at that point in the network. Diversity is applied on the basis of the anticipated loadings that are likely to result from all loads not being connected at the same time.\X\0D
NOTE2: Diversity is applied to final circuits only, not to sub-main circuits supplying other DBs.
* PropertyDefs > PropertyDef [Name="ElectricalSystemCategory"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="ElectricalSystemType"] > Definition "For certain purposes of electrical regulations, IEC 60364 defines types of system using type identifiers. Assignment of identifiers depends upon the relationship of the source, and of exposed conductive parts of the installation, to Ground (Earth).   Identifiers that may be assigned through IEC 60364 are: 

&#8226;TN type system, a system having one or more points of the source of energy directly earthed, the exposed conductive parts of the installation being connected to that point by protective conductors, 
&#8226;TN C type system, a TN type system in which neutral and protective functions are combined in a single conductor throughout the system, 
&#8226;TN S type system, a TN type system having separate neutral and protective conductors throughout the system, 
&#8226;TN C S type system, a TN type system in which neutral and protective functions are combined in a single conductor in part of the system, 
&#8226;TT type system, a system having one point of the source of energy directly earthed, the exposed conductive parts of the installation being connected to earth electrodes electrically independent of the earth electrodes of the source, 
&#8226;IT type system, a system having no direct connection between live parts and Earth, the exposed conductive parts of the electrical installation being earthed."
  ~~For certain purposes of electrical regulations, IEC 60364 defines types of system using type identifiers. Assignment of identifiers depends upon the relationship of the source, and of exposed conductive parts of the installation, to Ground (Earth).   Identifiers that may be assigned through IEC 60364 are: 

&#8226;TN type system, a system having one or more points of the source of energy directly earthed, the exposed conductive parts of the installation being connected to that point by protective conductors, 
&#8226;TN C type system, a TN type system in which neutral and protective functions are combined in a single conductor throughout the system, 
&#8226;TN S type system, a TN type system having separate neutral and protective conductors throughout the system, 
&#8226;TN C S type system, a TN type system in which neutral and protective functions are combined in a single conductor in part of the system, 
&#8226;TT type system, a system having one point of the source of energy directly earthed, the exposed conductive parts of the installation being connected to earth electrodes electrically independent of the earth electrodes of the source, 
&#8226;IT type system, a system having no direct connection between live parts and Earth, the exposed conductive parts of the electrical installation being earthed.~~ For certain purposes of electrical regulations, IEC 60364 defines types of system using type identifiers. Assignment of identifiers depends upon the relationship of the source, and of exposed conductive parts of the installation, to Ground (Earth).   Identifiers that may be assigned through IEC 60364 are: \X\0D
\X\0D
\X2\2022\X0\TN type system, a system having one or more points of the source of energy directly earthed, the exposed conductive parts of the installation being connected to that point by protective conductors, \X\0D
\X2\2022\X0\TN C type system, a TN type system in which neutral and protective functions are combined in a single conductor throughout the system, \X\0D
\X2\2022\X0\TN S type system, a TN type system having separate neutral and protective conductors throughout the system, \X\0D
\X2\2022\X0\TN C S type system, a TN type system in which neutral and protective functions are combined in a single conductor in part of the system, \X\0D
\X2\2022\X0\TT type system, a system having one point of the source of energy directly earthed, the exposed conductive parts of the installation being connected to earth electrodes electrically independent of the earth electrodes of the source, \X\0D
\X2\2022\X0\IT type system, a system having no direct connection between live parts and Earth, the exposed conductive parts of the electrical installation being earthed.
* PropertyDefs > PropertyDef [Name="ElectricalSystemType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="MaximumAllowedVoltageDrop"] > Definition "The maximum voltage drop across the circuit that must not be exceeded. 
There are two  voltage drop limit settings that may be applied; one for sub-main circuits, and one in each Distribution Board or Consumer Unit for final circuits connected to that board. The settings should limit the overall voltage drop to the required level. Default settings of 1.5% for sub-main circuits and 2.5% for final circuits, giving an overall limit of 4% may be applied.
NOTE: This value may also be specified as a constraint within an IFC model if required but is included within the property set at this stage pending implementation of the required capabilities within software applications."
  ~~The maximum voltage drop across the circuit that must not be exceeded. 
There are two  voltage drop limit settings that may be applied; one for sub-main circuits, and one in each Distribution Board or Consumer Unit for final circuits connected to that board. The settings should limit the overall voltage drop to the required level. Default settings of 1.5% for sub-main circuits and 2.5% for final circuits, giving an overall limit of 4% may be applied.
NOTE: This value may also be specified as a constraint within an IFC model if required but is included within the property set at this stage pending implementation of the required capabilities within software applications.~~ The maximum voltage drop across the circuit that must not be exceeded. \X\0D
There are two  voltage drop limit settings that may be applied; one for sub-main circuits, and one in each Distribution Board or Consumer Unit for final circuits connected to that board. The settings should limit the overall voltage drop to the required level. Default settings of 1.5% for sub-main circuits and 2.5% for final circuits, giving an overall limit of 4% may be applied.\X\0D
NOTE: This value may also be specified as a constraint within an IFC model if required but is included within the property set at this stage pending implementation of the required capabilities within software applications.
* PropertyDefs > PropertyDef [Name="ElectricalSystemType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="ElectricalSystemCategory"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_PrecastSlab.xml
====================

modifications
-------------
* PropertyDefs > PropertyDef [Name="AngleToFirstAxis"] > Definition "The angle of rotation of the axis of the first component relative to the &#8216;West&#8217; edge of the slab."
  ~~The angle of rotation of the axis of the first component relative to the &#8216;West&#8217; edge of the slab.~~ The angle of rotation of the axis of the first component relative to the \X2\2018\X0\West\X2\2019\X0\ edge of the slab.
* PropertyDefs > PropertyDef [Name="DistanceBetweenComponentAxes"] > Definition "The distance between the axes of the components, measured along the &#8216;South&#8217; edge of the slab."
  ~~The distance between the axes of the components, measured along the &#8216;South&#8217; edge of the slab.~~ The distance between the axes of the components, measured along the \X2\2018\X0\South\X2\2019\X0\ edge of the slab.
* PropertyDefs > PropertyDef [Name="EdgeDistanceToFirstAxis"] > Definition "The distance from the left (&#8216;West&#8217;) edge of the slab (in the direction of span of the components) to the axis of the first component."
  ~~The distance from the left (&#8216;West&#8217;) edge of the slab (in the direction of span of the components) to the axis of the first component.~~ The distance from the left (\X2\2018\X0\West\X2\2019\X0\) edge of the slab (in the direction of span of the components) to the axis of the first component.
* PropertyDefs > PropertyDef [Name="ToppingType"] > Definition "Defines if a topping is applied and what kind. Values are &#8220;Full topping&#8221;, &#8220;Perimeter Wash&#8221;, &#8220;None&#8221;"
  ~~Defines if a topping is applied and what kind. Values are &#8220;Full topping&#8221;, &#8220;Perimeter Wash&#8221;, &#8220;None&#8221;~~ Defines if a topping is applied and what kind. Values are \X2\201C\X0\Full topping\X2\201D\X0\, \X2\201C\X0\Perimeter Wash\X2\201D\X0\, \X2\201C\X0\None\X2\201D\X0\

deletions
---------
* PropertyDefs > PropertyDef [Name="TypeDesignation"]
* PropertyDefs > PropertyDef [Name="NominalThickness"]


Qto_FacilityPartBaseQuantities.xml
==================================

modifications
-------------
* QtoDefs > QtoDef [Name="Length"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Height"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Area"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Width"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Volume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases


Qto_ArealStratumBaseQuantities.xml
==================================

modifications
-------------
* QtoDefs > QtoDef [Name="PlanLength"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Area"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Length"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases


Pset_ReinforcementBarPitchOfColumn.xml
======================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="ReinforcementBarType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="ReinforcementBarType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;



Pset_BurnerTypeCommon.xml
=========================

modifications
-------------
* PropertyDefs > PropertyDef [Name="EnergySource"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="EnergySource"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_FenderDesignCriteria.xml
=============================

modifications
-------------
* ApplicableClasses > ClassName "IfcSpace/BERTH"
  ~~IfcSpace/BERTH~~ IfcSpace
* ApplicableTypeValue "IfcSpace/BERTH"
  ~~IfcSpace/BERTH~~ IfcSpace
* PropertyDefs > PropertyDef [Name="AddedMassCoefficientMethod"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="AddedMassCoefficientMethod"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_DamperTypeCommon.xml
=========================

additions
---------
* PropertyDefs > PropertyDef [Name="LossCoefficentCurve"]
* PropertyDefs > PropertyDef [Name="RegeneratedSoundCurve"]

modifications
-------------
* PropertyDefs > PropertyDef [Name="BladeAction"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="BladeEdge"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="BladeShape"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Operation"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Orientation"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="TemperatureRange"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="BladeEdge"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="Orientation"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="BladeAction"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="RegeneratedSoundCurve"] > PropertyType
  ~~&lt;PropertyType&gt;~~ &lt;PropertyType&gt;
* PropertyDefs > PropertyDef [Name="RegeneratedSoundCurve"] > Definition "Regenerated sound versus air flow rate."
  ~~&lt;Definition&gt;~~ &lt;Definition&gt;
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="BladeShape"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="RegeneratedSoundCurve"] > Name "RegeneratedSoundCurve"
  ~~&lt;Name&gt;~~ &lt;Name&gt;
* PropertyDefs > PropertyDef [Name="Operation"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="LossCoefficentCurve"]
* PropertyDefs > PropertyDef [Name="LeakageCurve"]


Pset_SensorTypeGasSensor.xml
============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="SetPointConcentration"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue


Qto_WallBaseQuantities.xml
==========================

modifications
-------------
* QtoDefs > QtoDef [Name="NetSideArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossSideArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossFootprintArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Length"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Height"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetFootprintArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetVolume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Width"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossVolume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases


Pset_ControllerTypeProportional.xml
===================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="ControlType"] > Definition "The type of signal modification.
PROPORTIONAL: Output is proportional to the control error. The gain of a proportional control (Kp) will have the effect of reducing the rise time and reducing , but never eliminating, the steady-state error of the variable controlled. 
PROPORTIONALINTEGRAL: Part of the output is proportional to the control error and part is proportional to the time integral of the control error. Adding the gain of an integral control (Ki) will have the effect of eliminating the steady-state error of the variable controlled, but it may make the transient response worse. 
PROPORTIONALINTEGRALDERIVATIVE: Part of the output is proportional to the control error, part is proportional to the time integral of the control error and part is proportional to the time derivative of the control error. Adding the gain of a derivative control (Kd) will have the effect of increasing the stability of the system, reducing the overshoot, and improving the transient response of the variable controlled."
  ~~The type of signal modification.
PROPORTIONAL: Output is proportional to the control error. The gain of a proportional control (Kp) will have the effect of reducing the rise time and reducing , but never eliminating, the steady-state error of the variable controlled. 
PROPORTIONALINTEGRAL: Part of the output is proportional to the control error and part is proportional to the time integral of the control error. Adding the gain of an integral control (Ki) will have the effect of eliminating the steady-state error of the variable controlled, but it may make the transient response worse. 
PROPORTIONALINTEGRALDERIVATIVE: Part of the output is proportional to the control error, part is proportional to the time integral of the control error and part is proportional to the time derivative of the control error. Adding the gain of a derivative control (Kd) will have the effect of increasing the stability of the system, reducing the overshoot, and improving the transient response of the variable controlled.~~ The type of signal modification.\X\0D
PROPORTIONAL: Output is proportional to the control error. The gain of a proportional control (Kp) will have the effect of reducing the rise time and reducing , but never eliminating, the steady-state error of the variable controlled. \X\0D
PROPORTIONALINTEGRAL: Part of the output is proportional to the control error and part is proportional to the time integral of the control error. Adding the gain of an integral control (Ki) will have the effect of eliminating the steady-state error of the variable controlled, but it may make the transient response worse. \X\0D
PROPORTIONALINTEGRALDERIVATIVE: Part of the output is proportional to the control error, part is proportional to the time integral of the control error and part is proportional to the time derivative of the control error. Adding the gain of a derivative control (Kd) will have the effect of increasing the stability of the system, reducing the overshoot, and improving the transient response of the variable controlled.
* PropertyDefs > PropertyDef [Name="ControlType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Labels"] > PropertyType > TypePropertyTableValue
  ~~TypePropertyTableValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Range"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Value"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="ControlType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="Labels"] > PropertyType > TypePropertyTableValue > Expression
  ~~&lt;Expression&gt;~~ &lt;DataType&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="Labels"] > PropertyType > TypePropertyTableValue > DefiningValue
* PropertyDefs > PropertyDef [Name="Labels"] > PropertyType > TypePropertyTableValue > DefinedValue


Pset_FilterTypeWaterFilter.xml
==============================

modifications
-------------
* PropertyDefs
  ~~PropertyDefs~~ ApplicableClasses
* ApplicableClasses
  ~~ApplicableClasses~~ ApplicableTypeValue
* ApplicableTypeValue "IfcFilter/WATERFILTER"
  ~~ApplicableTypeValue~~ PropertyDefs


Pset_DamperPHistory.xml
=======================

modifications
-------------
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="BladePositionAngle"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="PressureDrop"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="DamperPosition"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Leakage"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="PressureLossCoefficient"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="AirFlowRate"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Pset_ValveTypeAirRelease.xml
============================

modifications
-------------
* Definition "Valve used to release air from a pipe or fitting. 
Note that an air release valve is constrained to have a single port pattern"
  ~~Valve used to release air from a pipe or fitting. 
Note that an air release valve is constrained to have a single port pattern~~ Valve used to release air from a pipe or fitting. \X\0D
Note that an air release valve is constrained to have a single port pattern


Pset_CondenserTypeCommon.xml
============================

additions
---------
* PropertyDefs > PropertyDef [Name="InternalRefrigerantVolume"] > Definition "Internal volume of condenser (refrigerant side)."

modifications
-------------
* PropertyDefs > PropertyDef [Name="RefrigerantClass"] > Definition "Refrigerant class used by the condenser.

CFC: Chlorofluorocarbons.
HCFC: Hydrochlorofluorocarbons.
HFC: Hydrofluorocarbons."
  ~~Refrigerant class used by the condenser.

CFC: Chlorofluorocarbons.
HCFC: Hydrochlorofluorocarbons.
HFC: Hydrofluorocarbons.~~ Refrigerant class used by the condenser.\X\0D
\X\0D
CFC: Chlorofluorocarbons.\X\0D
HCFC: Hydrochlorofluorocarbons.\X\0D
HFC: Hydrofluorocarbons.
* PropertyDefs > PropertyDef [Name="RefrigerantClass"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="RefrigerantClass"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_ElementComponentCommon.xml
===============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="CorrosionTreatment"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="DeliveryType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="CorrosionTreatment"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="DeliveryType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_SpaceThermalRequirements.xml
=================================

modifications
-------------
* ApplicableTypeValue "IfcSpace, IfcSpatialZone, IfcZone"
  ~~IfcSpace, IfcSpatialZone, IfcZone~~ IfcZone
* PropertyDefs > PropertyDef [Name="AirConditioningCentral"] > Definition "Indication whether the space  requires a central air conditioning provided (TRUE) or not (FALSE).
It should only be given, if the property "AirConditioning" is set to TRUE."
  ~~Indication whether the space  requires a central air conditioning provided (TRUE) or not (FALSE).
It should only be given, if the property "AirConditioning" is set to TRUE.~~ Indication whether the space  requires a central air conditioning provided (TRUE) or not (FALSE).\X\0D
It should only be given, if the property "AirConditioning" is set to TRUE.


Qto_CableCarrierFittingBaseQuantities.xml
=========================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Qto_InterceptorBaseQuantities.xml
=================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Pset_PumpPHistory.xml
=====================

modifications
-------------
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="OverallEfficiency"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="RotationSpeed"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Flowrate"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Power"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="PressureRise"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="MechanicalEfficiency"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Pset_MechanicalFastenerBolt.xml
===============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="HeadShape"] > Definition "Shape of the bolt's head, e.g. 'Hexagon', 'Countersunk', 'Cheese'"
  ~~Shape of the bolt's head, e.g. 'Hexagon', 'Countersunk', 'Cheese'~~ Shape of the bolt's head, e.g. 'Hexagon', 'Countersunk', 'Cheese'',
* PropertyDefs > PropertyDef [Name="KeyShape"] > Definition "If applicable, shape of the head's slot, e.g. 'Slot', 'Allen'"
  ~~If applicable, shape of the head's slot, e.g. 'Slot', 'Allen'~~ If applicable, shape of the head's slot, e.g. 'Slot', 'Allen'',
* PropertyDefs > PropertyDef [Name="NutShape"] > Definition "Shape of the nut, e.g. 'Hexagon', 'Cap', 'Castle', 'Wing'"
  ~~Shape of the nut, e.g. 'Hexagon', 'Cap', 'Castle', 'Wing'~~ Shape of the nut, e.g. 'Hexagon', 'Cap', 'Castle', 'Wing'',
* PropertyDefs > PropertyDef [Name="WasherShape"] > Definition "Shape of the washers, e.g. 'Standard', 'Square'"
  ~~Shape of the washers, e.g. 'Standard', 'Square'~~ Shape of the washers, e.g. 'Standard', 'Square'',


Pset_AlarmPHistory.xml
======================

modifications
-------------
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="Acknowledge"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Condition"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="User"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Severity"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Enabled"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;



Pset_FilterTypeCompressedAirFilter.xml
======================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="CompressedAirFilterType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="ParticleAbsorptionCurve"] > PropertyType > TypePropertyTableValue
  ~~TypePropertyTableValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="ParticleAbsorptionCurve"] > PropertyType > TypePropertyTableValue > Expression
  ~~&lt;Expression&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="CompressedAirFilterType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="ParticleAbsorptionCurve"] > PropertyType > TypePropertyTableValue > DefiningValue
* PropertyDefs > PropertyDef [Name="ParticleAbsorptionCurve"] > PropertyType > TypePropertyTableValue > DefinedValue


Qto_FireSuppressionTerminalBaseQuantities.xml
=============================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Pset_SensorTypeContactSensor.xml
================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="SetPointContact"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue



Qto_SiteBaseQuantities.xml
==========================

modifications
-------------
* QtoDefs > QtoDef [Name="GrossPerimeter"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases


Pset_UnitaryControlElementTypeIndicatorPanel.xml
================================================

modifications
-------------
* PropertyDefs
  ~~PropertyDefs~~ ApplicableClasses
* ApplicableClasses
  ~~ApplicableClasses~~ ApplicableTypeValue
* ApplicableTypeValue "IfcUnitaryControlElement/INDICATORPANEL"
  ~~ApplicableTypeValue~~ PropertyDefs


Pset_AudioVisualApplianceTypeSpeaker.xml
========================================

additions
---------
* PropertyDefs > PropertyDef [Name="SpeakerType"]

modifications
-------------
* PropertyDefs > PropertyDef [Name="SpeakerType"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="SpeakerDriverSize"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="FrequencyResponse"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="SpeakerMounting"]


Pset_SwitchingDeviceTypeKeypad.xml
==================================

modifications
-------------
* PropertyDefs
  ~~PropertyDefs~~ ApplicableClasses
* ApplicableClasses
  ~~ApplicableClasses~~ ApplicableTypeValue
* ApplicableTypeValue "IfcSwitchingDevice/KEYPAD"
  ~~ApplicableTypeValue~~ PropertyDefs


Qto_SwitchingDeviceBaseQuantities.xml
=====================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Pset_MaterialWoodBasedPanel.xml
===============================

modifications
-------------
* ApplicableClasses > ClassName "IfcMaterial/Wood"
  ~~IfcMaterial/Wood~~ IfcMaterial
* ApplicableTypeValue "IfcMaterial/Wood"
  ~~IfcMaterial/Wood~~ IfcMaterial

deletions
---------
* PropertyDefs > PropertyDef [Name="InPlane"] > PropertyType
* PropertyDefs > PropertyDef [Name="OutOfPlane"] > PropertyType
* PropertyDefs > PropertyDef [Name="OutOfPlaneNegative"] > PropertyType


Qto_AlarmBaseQuantities.xml
===========================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases



Qto_ChimneyBaseQuantities.xml
=============================

deletions
---------
* QtoDefs > QtoDef [Name="Length"] > NameAliases
* QtoDefs > QtoDef [Name="Length"] > DefinitionAliases
* QtoDefinitionAliases


Pset_ShipLockCommon.xml
=======================

modifications
-------------
* ApplicableClasses > ClassName "IfcMarineFacility/SHIPLOCK"
  ~~IfcMarineFacility/SHIPLOCK~~ IfcMarineFacility
* ApplicableTypeValue "IfcMarineFacility/SHIPLOCK"
  ~~IfcMarineFacility/SHIPLOCK~~ IfcMarineFacility



Pset_SensorTypeCommon.xml
=========================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_ProtectiveDeviceBreakerUnitI2TCurve.xml
============================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="VoltageLevel"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="NominalCurrent"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="BreakerUnitCurve"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;



Pset_SensorTypeSmokeSensor.xml
==============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="SetPointConcentration"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue



Pset_WasteTerminalTypeWasteDisposalUnit.xml
===========================================

deletions
---------
* PropertyDefs > PropertyDef [Name="NominalDepth"]


Pset_MarineVehicleDesignCriteria.xml
====================================

modifications
-------------
* ApplicableTypeValue "IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.)"
  ~~IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.)~~ IfcLightFixture
* ApplicableClasses > ClassName "IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;

deletions
---------
* ApplicableClasses > ClassName "IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.)"


Qto_HeatExchangerBaseQuantities.xml
===================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Pset_TankTypeSectional.xml
==========================

modifications
-------------
* Definition "Fixed vessel constructed from sectional parts with one or more compartments for storing a liquid.

Note (1): All sectional construction tanks are considered to be rectangular by default.
Note (2): Generally, it is not expected that sectional construction tanks will be used for the purposes of gas storage.

Pset renamed from Pset_TankTypeSectionalTank to Pset_TankTypeSectional in IFC2x2 Pset Addendum."
  ~~Fixed vessel constructed from sectional parts with one or more compartments for storing a liquid.

Note (1): All sectional construction tanks are considered to be rectangular by default.
Note (2): Generally, it is not expected that sectional construction tanks will be used for the purposes of gas storage.

Pset renamed from Pset_TankTypeSectionalTank to Pset_TankTypeSectional in IFC2x2 Pset Addendum.~~ Fixed vessel constructed from sectional parts with one or more compartments for storing a liquid.\X\0D
\X\0D
Note (1): All sectional construction tanks are considered to be rectangular by default.\X\0D
Note (2): Generally, it is not expected that sectional construction tanks will be used for the purposes of gas storage.\X\0D
\X\0D
Pset renamed from Pset_TankTypeSectionalTank to Pset_TankTypeSectional in IFC2x2 Pset Addendum.
* ApplicableClasses > ClassName "IfcTank/SECTIONAL"
  ~~IfcTank/SECTIONAL~~ IfcTank
* ApplicableTypeValue "IfcTank/SECTIONAL"
  ~~IfcTank/SECTIONAL~~ IfcTank
* PropertyDefs > PropertyDef [Name="NumberOfSections"] > Definition "Number of sections used in the construction of the tank

Note: All sections assumed to be the same size."
  ~~Number of sections used in the construction of the tank

Note: All sections assumed to be the same size.~~ Number of sections used in the construction of the tank\X\0D
\X\0D
Note: All sections assumed to be the same size.


Pset_TransitionSectionCommon.xml
================================

modifications
-------------
* ApplicableClasses > ClassName "IfcEarthworksFill/(.TRANSITIONSECTION.)"
  ~~IfcEarthworksFill/(.TRANSITIONSECTION.)~~ IfcTank
* ApplicableTypeValue "IfcEarthworksFill/(.TRANSITIONSECTION.)"
  ~~IfcEarthworksFill/(.TRANSITIONSECTION.)~~ IfcTank


Pset_GateHeadCommon.xml
=======================

modifications
-------------
* ApplicableClasses > ClassName "IfcFacilityPart/IfcMarinePartTypeEnum(.GATEHEAD.)"
  ~~IfcFacilityPart/IfcMarinePartTypeEnum(.GATEHEAD.)~~ IfcFurniture
* ApplicableTypeValue "IfcFacilityPart/IfcMarinePartTypeEnum(.GATEHEAD.)"
  ~~IfcFacilityPart/IfcMarinePartTypeEnum(.GATEHEAD.)~~ IfcFurniture


Qto_StackTerminalBaseQuantities.xml
===================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Qto_LaborResourceBaseQuantities.xml
===================================

modifications
-------------
* QtoDefs > QtoDef [Name="StandardWork"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="OvertimeWork"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases


Pset_DistributionPortPHistoryCable.xml
======================================

modifications
-------------
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="Voltage"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Current"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="PowerFactor"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="RealPower"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="DataReceived"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="DataTransmitted"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="ReactivePower"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="ApparentPower"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Qto_ElectricApplianceBaseQuantities.xml
=======================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Pset_SwitchingDeviceTypePHistory.xml
====================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="SetPoint"] > PropertyType > TypePropertyReferenceValue
  ~~TypePropertyReferenceValue~~ TypePropertySingleValue
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE


Pset_CargoCommon.xml
====================

modifications
-------------
* ApplicableTypeValue "IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.CARGO.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.CARGO.)"
  ~~IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.CARGO.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.CARGO.)~~ IfcCableSegment
* PropertyDefs > PropertyDef [Name="ProcessItem"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="AdditionalProcessing"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* ApplicableClasses > ClassName "IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.CARGO.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* PropertyDefs > PropertyDef [Name="ProcessDirection"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;

deletions
---------
* ApplicableClasses > ClassName "IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.CARGO.)"


Pset_FireSuppressionTerminalTypeSprinkler.xml
=============================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Activation"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="BulbLiquidColor"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Response"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="SprinklerType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Response"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="Activation"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="BulbLiquidColor"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="SprinklerType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_SwitchingDeviceTypeCommon.xml
==================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="SetPoint"] > PropertyType
  ~~PropertyType~~ Definition
* PropertyDefs > PropertyDef [Name="SetPoint"] > Definition "Indicates the setpoint and label.  For toggle switches, there are two positions, 0 for off and 1 for on.  For dimmer switches, the values may indicate the fully-off and full-on positions, where missing integer values in between are interpolated.   For selector switches, the range indicates the available positions.  
An IfcTable may be attached (using IfcMetric and IfcPropertyConstraintRelationship) containing columns of the specified header names and types:
'Position' (IfcInteger): The discrete setpoint level.
'Sink' (IfcLabel): The Name of the switched input port (IfcDistributionPort with FlowDirection=SINK).
'Source' (IfcLabel): The Name of the switched output port (IfcDistributionPort with FlowDirection=SOURCE).
'Ratio' (IfcNormalizedRatioMeasure): The ratio of power at the setpoint where 0.0 is off and 1.0 is fully on."
  ~~Definition~~ PropertyType
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="SwitchFunction"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="SwitchFunction"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;



Pset_SlabCommon.xml
===================

modifications
-------------
* PropertyDefs > PropertyDef [Name="AcousticRating"] > Definition "Acoustic rating for this object.
It is provided according to the national building code. It indicates the sound transmission resistance of this object by an index ratio (instead of providing full sound absorbtion values)."
  ~~Acoustic rating for this object.
It is provided according to the national building code. It indicates the sound transmission resistance of this object by an index ratio (instead of providing full sound absorbtion values).~~ Acoustic rating for this object.\X\0D
It is provided according to the national building code. It indicates the sound transmission resistance of this object by an index ratio (instead of providing full sound absorbtion values).
* PropertyDefs > PropertyDef [Name="PitchAngle"] > Definition "Angle of the slab to the horizontal when used as a component for the roof (specified as 0 degrees or not asserted for cases where the slab is not used as a roof component).      

The shape information is provided in addition to the shape representation and the geometric parameters used within. In cases of inconsistency between the geometric parameters and the shape properties, provided in the attached property, the geometric parameters take precedence.  For geometry editing applications, like CAD: this value should be write-only."
  ~~Angle of the slab to the horizontal when used as a component for the roof (specified as 0 degrees or not asserted for cases where the slab is not used as a roof component).      

The shape information is provided in addition to the shape representation and the geometric parameters used within. In cases of inconsistency between the geometric parameters and the shape properties, provided in the attached property, the geometric parameters take precedence.  For geometry editing applications, like CAD: this value should be write-only.~~ Angle of the slab to the horizontal when used as a component for the roof (specified as 0 degrees or not asserted for cases where the slab is not used as a roof component).      \X\0D
\X\0D
The shape information is provided in addition to the shape representation and the geometric parameters used within. In cases of inconsistency between the geometric parameters and the shape properties, provided in the attached property, the geometric parameters take precedence.  For geometry editing applications, like CAD: this value should be write-only.

deletions
---------
* PropertyDefs > PropertyDef [Name="Status"]


Pset_MaintenanceTriggerPerformance.xml
======================================

modifications
-------------
* ApplicableTypeValue "IfcElement,IfcAsset,IfcSystem"
  ~~IfcElement,IfcAsset,IfcSystem~~ IfcSystem


Pset_ChamberCommon.xml
======================

modifications
-------------
* ApplicableClasses > ClassName "IfcFacilityPart/IfcMarinePartTypeEnum(.CHAMBER.)"
  ~~IfcFacilityPart/IfcMarinePartTypeEnum(.CHAMBER.)~~ IfcCableSegment
* ApplicableTypeValue "IfcFacilityPart/IfcMarinePartTypeEnum(.CHAMBER.)"
  ~~IfcFacilityPart/IfcMarinePartTypeEnum(.CHAMBER.)~~ IfcCableSegment

deletions
---------
* PropertyDefs > PropertyDef [Name="StructuralType"]


Qto_TubeBundleBaseQuantities.xml
================================

modifications
-------------
* QtoDefs > QtoDef [Name="NetWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases


Pset_DistributionChamberElementTypeMeterChamber.xml
===================================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="AccessCoverMaterial"] > Definition "The material from which the access cover to the chamber is constructed.
NOTE: It is assumed that chamber walls will be constructed of a single material."
  ~~The material from which the access cover to the chamber is constructed.
NOTE: It is assumed that chamber walls will be constructed of a single material.~~ The material from which the access cover to the chamber is constructed.\X\0D
NOTE: It is assumed that chamber walls will be constructed of a single material.
* PropertyDefs > PropertyDef [Name="BaseMaterial"] > Definition "The material from which the base of the chamber is constructed.
NOTE: It is assumed that chamber base will be constructed of a single material."
  ~~The material from which the base of the chamber is constructed.
NOTE: It is assumed that chamber base will be constructed of a single material.~~ The material from which the base of the chamber is constructed.\X\0D
NOTE: It is assumed that chamber base will be constructed of a single material.
* PropertyDefs > PropertyDef [Name="BaseThickness"] > Definition "The thickness of the chamber base construction.
NOTE: It is assumed that chamber base will be constructed at a single thickness."
  ~~The thickness of the chamber base construction.
NOTE: It is assumed that chamber base will be constructed at a single thickness.~~ The thickness of the chamber base construction.\X\0D
NOTE: It is assumed that chamber base will be constructed at a single thickness.
* PropertyDefs > PropertyDef [Name="WallMaterial"] > Definition "The material from which the wall of the chamber is constructed.
NOTE: It is assumed that chamber walls will be constructed of a single material."
  ~~The material from which the wall of the chamber is constructed.
NOTE: It is assumed that chamber walls will be constructed of a single material.~~ The material from which the wall of the chamber is constructed.\X\0D
NOTE: It is assumed that chamber walls will be constructed of a single material.
* PropertyDefs > PropertyDef [Name="WallThickness"] > Definition "The thickness of the chamber wall construction
.
NOTE: It is assumed that chamber walls will be constructed at a single thickness."
  ~~The thickness of the chamber wall construction
.
NOTE: It is assumed that chamber walls will be constructed at a single thickness.~~ The thickness of the chamber wall construction\X\0D
.\X\0D
NOTE: It is assumed that chamber walls will be constructed at a single thickness.

deletions
---------
* PropertyDefs > PropertyDef [Name="AccessCoverMaterial"] > PropertyType
* PropertyDefs > PropertyDef [Name="BaseMaterial"] > PropertyType
* PropertyDefs > PropertyDef [Name="WallMaterial"] > PropertyType


Qto_BoilerBaseQuantities.xml
============================

modifications
-------------
* QtoDefs > QtoDef [Name="GrossWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="TotalSurfaceArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases


Pset_AudioVisualApplianceTypeCommon.xml
=======================================

additions
---------
* PropertyDefs > PropertyDef [Name="MediaSource"]

modifications
-------------
* PropertyDefs > PropertyDef [Name="AudioVolume"] > PropertyType > TypePropertyTableValue
  ~~TypePropertyTableValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="AudioVolume"] > PropertyType > TypePropertyTableValue > Expression
  ~~&lt;Expression&gt;~~ &lt;DataType&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="AudioVolume"] > PropertyType > TypePropertyTableValue > DefiningValue
* PropertyDefs > PropertyDef [Name="AudioVolume"] > PropertyType > TypePropertyTableValue > DefinedValue
* PropertyDefs > PropertyDef [Name="MediaSource"]


Pset_AudioVisualApplianceTypeAmplifier.xml
==========================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="AudioMode"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="AudioAmplification"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="AmplifierType"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Pset_AirSideSystemInformation.xml
=================================

modifications
-------------
* ApplicableTypeValue "IfcSpace,IfcZone,IfcSpatialZone"
  ~~IfcSpace,IfcZone,IfcSpatialZone~~ IfcSpatialZone
* PropertyDefs > PropertyDef [Name="AirSideSystemDistributionType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="AirSideSystemType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="AirSideSystemType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="AirSideSystemDistributionType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;



Pset_UnitaryControlElementPHistory.xml
======================================

modifications
-------------
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="Fan"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Temperature"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Mode"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="SetPoint"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Pset_CoilTypeCommon.xml
=======================

modifications
-------------
* PropertyDefs > PropertyDef [Name="AirflowRateRange"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="OperationalTemperatureRange"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="PlacementType"] > Definition "Indicates the placement of the coil.  
FLOOR indicates an under floor heater (if coil type is WATERHEATINGCOIL or ELECTRICHEATINGCOIL); 
CEILING indicates a cooling ceiling (if coil type is WATERCOOLINGCOIL);
UNIT indicates that the coil is part of a cooling or heating unit, like cooled beam, etc."
  ~~Indicates the placement of the coil.  
FLOOR indicates an under floor heater (if coil type is WATERHEATINGCOIL or ELECTRICHEATINGCOIL); 
CEILING indicates a cooling ceiling (if coil type is WATERCOOLINGCOIL);
UNIT indicates that the coil is part of a cooling or heating unit, like cooled beam, etc.~~ Indicates the placement of the coil.  \X\0D
FLOOR indicates an under floor heater (if coil type is WATERHEATINGCOIL or ELECTRICHEATINGCOIL); \X\0D
CEILING indicates a cooling ceiling (if coil type is WATERCOOLINGCOIL);\X\0D
UNIT indicates that the coil is part of a cooling or heating unit, like cooled beam, etc.
* PropertyDefs > PropertyDef [Name="PlacementType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="PlacementType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_CoilOccurrence.xml
=======================

modifications
-------------
* 
  ~~PSET_OCCURRENCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE



Pset_SpaceHeaterPHistory.xml
============================

modifications
-------------
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="HeatOutputRate"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="UACurve"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="FractionConvectiveHeatTransfer"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="OutputCapacityCurve"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="SurfaceTemperature"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="SpaceMeanRadiantTemperature"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="SpaceAirTemperature"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="FractionRadiantHeatTransfer"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Effectiveness"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="AuxiliaryEnergySourceConsumption"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="AirResistanceCurve"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Exponent"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Pset_CoveringCommon.xml
=======================

modifications
-------------
* PropertyDefs > PropertyDef [Name="AcousticRating"] > Definition "Acoustic rating for this object.
It is giving according to the national building code. It indicates the sound transmission resistance of this object by an index ration (instead of providing full sound absorbtion values)."
  ~~Acoustic rating for this object.
It is giving according to the national building code. It indicates the sound transmission resistance of this object by an index ration (instead of providing full sound absorbtion values).~~ Acoustic rating for this object.\X\0D
It is giving according to the national building code. It indicates the sound transmission resistance of this object by an index ration (instead of providing full sound absorbtion values).
* PropertyDefs > PropertyDef [Name="Finish"] > Definition "Finish selection for this object.
Here specification of the surface finish for informational purposes."
  ~~Finish selection for this object.
Here specification of the surface finish for informational purposes.~~ Finish selection for this object.\X\0D
Here specification of the surface finish for informational purposes.
* PropertyDefs > PropertyDef [Name="FireRating"] > Definition "Fire rating for this object.
It is given according to the national fire safety classification."
  ~~Fire rating for this object.
It is given according to the national fire safety classification.~~ Fire rating for this object.\X\0D
It is given according to the national fire safety classification.
* PropertyDefs > PropertyDef [Name="FlammabilityRating"] > Definition "Flammability Rating for this object.
It is given according to the national building code that governs the rating of flammability for materials."
  ~~Flammability Rating for this object.
It is given according to the national building code that governs the rating of flammability for materials.~~ Flammability Rating for this object.\X\0D
It is given according to the national building code that governs the rating of flammability for materials.
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="SurfaceSpreadOfFlame"] > Definition "Indication on how the flames spread around the surface,
It is given according to the national building code that governs the fire behaviour for materials."
  ~~Indication on how the flames spread around the surface,
It is given according to the national building code that governs the fire behaviour for materials.~~ Indication on how the flames spread around the surface,\X\0D
It is given according to the national building code that governs the fire behaviour for materials.
* PropertyDefs > PropertyDef [Name="ThermalTransmittance"] > Definition "Thermal transmittance coefficient (U-Value) of an element. 
Here the total thermal transmittance coefficient through the covering (including all materials)."
  ~~Thermal transmittance coefficient (U-Value) of an element. 
Here the total thermal transmittance coefficient through the covering (including all materials).~~ Thermal transmittance coefficient (U-Value) of an element. \X\0D
Here the total thermal transmittance coefficient through the covering (including all materials).
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_StairFlightCommon.xml
==========================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Headroom"] > Definition "Actual headroom clearance for the passageway according to the current design. 
The shape information is provided in addition to the shape representation and the geometric parameters used within. In cases of inconsistency between the geometric parameters and the shape properties, provided in the attached property, the geometric parameters take precedence."
  ~~Actual headroom clearance for the passageway according to the current design. 
The shape information is provided in addition to the shape representation and the geometric parameters used within. In cases of inconsistency between the geometric parameters and the shape properties, provided in the attached property, the geometric parameters take precedence.~~ Actual headroom clearance for the passageway according to the current design. \X\0D
The shape information is provided in addition to the shape representation and the geometric parameters used within. In cases of inconsistency between the geometric parameters and the shape properties, provided in the attached property, the geometric parameters take precedence.
* PropertyDefs > PropertyDef [Name="RiserHeight"] > Definition "Vertical distance from tread to tread. 
The riser height is supposed to be equal for all steps of a stair or stair flight."
  ~~Vertical distance from tread to tread. 
The riser height is supposed to be equal for all steps of a stair or stair flight.~~ Vertical distance from tread to tread. \X\0D
The riser height is supposed to be equal for all steps of a stair or stair flight.
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="TreadLength"] > Definition "Horizontal distance from the front of the thread to the front of the next tread. 
The tread length is supposed to be equal for all steps of the stair or stair flight at the walking line."
  ~~Horizontal distance from the front of the thread to the front of the next tread. 
The tread length is supposed to be equal for all steps of the stair or stair flight at the walking line.~~ Horizontal distance from the front of the thread to the front of the next tread. \X\0D
The tread length is supposed to be equal for all steps of the stair or stair flight at the walking line.
* PropertyDefs > PropertyDef [Name="TreadLengthAtInnerSide"] > Definition "Minimum length of treads at the inner side of the winder. 
Only relevant in case of winding flights, for straight flights it is identical with IfcStairFlight.TreadLength. It is a pre-calculated value, in case of inconsistencies, the value derived from the shape representation shall take precedence."
  ~~Minimum length of treads at the inner side of the winder. 
Only relevant in case of winding flights, for straight flights it is identical with IfcStairFlight.TreadLength. It is a pre-calculated value, in case of inconsistencies, the value derived from the shape representation shall take precedence.~~ Minimum length of treads at the inner side of the winder. \X\0D
Only relevant in case of winding flights, for straight flights it is identical with IfcStairFlight.TreadLength. It is a pre-calculated value, in case of inconsistencies, the value derived from the shape representation shall take precedence.
* PropertyDefs > PropertyDef [Name="TreadLengthAtOffset"] > Definition "Length of treads at a given offset.
Walking line position is given by the 'WalkingLineOffset'. The resulting value should normally be identical with TreadLength, it may be given in addition, if the walking line offset for building code calculations is different from that used in design."
  ~~Length of treads at a given offset.
Walking line position is given by the 'WalkingLineOffset'. The resulting value should normally be identical with TreadLength, it may be given in addition, if the walking line offset for building code calculations is different from that used in design.~~ Length of treads at a given offset.\X\0D
Walking line position is given by the 'WalkingLineOffset'. The resulting value should normally be identical with TreadLength, it may be given in addition, if the walking line offset for building code calculations is different from that used in design.
* PropertyDefs > PropertyDef [Name="WalkingLineOffset"] > Definition "Offset of the walking line from the inner side of the flight. 
Note: the walking line may have a own shape representation (in case of inconsistencies, the value derived from the shape representation shall take precedence)."
  ~~Offset of the walking line from the inner side of the flight. 
Note: the walking line may have a own shape representation (in case of inconsistencies, the value derived from the shape representation shall take precedence).~~ Offset of the walking line from the inner side of the flight. \X\0D
Note: the walking line may have a own shape representation (in case of inconsistencies, the value derived from the shape representation shall take precedence).
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_ElectricAppliancePHistory.xml
==================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="PowerState"] > PropertyType > TypePropertyReferenceValue
  ~~TypePropertyReferenceValue~~ TypePropertySingleValue
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE


Qto_AudioVisualApplianceBaseQuantities.xml
==========================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Pset_BuildingUse.xml
====================

additions
---------
* PropertyDefs > PropertyDef [Name="MarketSubCategoriesAvailableNow"]
* PropertyDefs > PropertyDef [Name="TenureModesAvailableFuture"]

modifications
-------------
* PropertyDefs > PropertyDef [Name="MarketSubCategoriesAvailableFuture"] > PropertyType > TypePropertyListValue
  ~~TypePropertyListValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="MarketSubCategoriesAvailableFuture"] > PropertyType > TypePropertyListValue > ListValue
  ~~ListValue~~ DataType
* PropertyDefs > PropertyDef [Name="RentalRatesInCategoryFuture"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="RentalRatesInCategoryNow"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="TenureModesAvailableFuture"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="TenureModesAvailableNow"]
* PropertyDefs > PropertyDef [Name="MarketSubCategoriesAvailableNow"]


Pset_SensorTypeHumiditySensor.xml
=================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="SetPointHumidity"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue


Pset_ProtectiveDeviceBreakerUnitIPICurve.xml
============================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="NominalCurrent"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="VoltageLevel"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="BreakerUnitIPICurve"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Pset_CableSegmentTypeConductorSegment.xml
=========================================

additions
---------
* PropertyDefs > PropertyDef [Name="Construction"]

modifications
-------------
* PropertyDefs > PropertyDef [Name="Construction"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Shape"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Material"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="Function"]


Qto_SurfaceFeatureBaseQuantities.xml
====================================

additions
---------
* Definition "$"

modifications
-------------
* QtoDefinitionAliases
  ~~QtoDefinitionAliases~~ ApplicableTypeValue



Pset_WallCommon.xml
===================

modifications
-------------
* PropertyDefs > PropertyDef [Name="AcousticRating"] > Definition "Acoustic rating for this object.
It is provided according to the national building code. It indicates the sound transmission resistance of this object by an index ratio (instead of providing full sound absorbtion values)."
  ~~Acoustic rating for this object.
It is provided according to the national building code. It indicates the sound transmission resistance of this object by an index ratio (instead of providing full sound absorbtion values).~~ Acoustic rating for this object.\X\0D
It is provided according to the national building code. It indicates the sound transmission resistance of this object by an index ratio (instead of providing full sound absorbtion values).
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="SurfaceSpreadOfFlame"] > Definition "Indication on how the flames spread around the surface,
It is given according to the national building code that governs the fire behaviour for materials."
  ~~Indication on how the flames spread around the surface,
It is given according to the national building code that governs the fire behaviour for materials.~~ Indication on how the flames spread around the surface,\X\0D
It is given according to the national building code that governs the fire behaviour for materials.
* PropertyDefs > PropertyDef [Name="ThermalTransmittance"] > Definition "Thermal transmittance coefficient (U-Value) of a material.
Here the total thermal transmittance coefficient through the wall (including all materials)."
  ~~Thermal transmittance coefficient (U-Value) of a material.
Here the total thermal transmittance coefficient through the wall (including all materials).~~ Thermal transmittance coefficient (U-Value) of a material.\X\0D
Here the total thermal transmittance coefficient through the wall (including all materials).
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_FlowMeterTypeGasMeter.xml
==============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="GasType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="GasType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;



Pset_SpaceHeaterTypeCommon.xml
==============================

modifications
-------------
* Definition "Space heater type common attributes.
SoundLevel attribute deleted in IFC2x2 Pset Addendum: Use IfcSoundProperties instead.  Properties added in IFC4."
  ~~Space heater type common attributes.
SoundLevel attribute deleted in IFC2x2 Pset Addendum: Use IfcSoundProperties instead.  Properties added in IFC4.~~ Space heater type common attributes.\X\0D
SoundLevel attribute deleted in IFC2x2 Pset Addendum: Use IfcSoundProperties instead.  Properties added in IFC4.
* PropertyDefs > PropertyDef [Name="EnergySource"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="HeatTransferDimension"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="HeatTransferMedium"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="PlacementType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="TemperatureClassification"] > Definition "Enumeration defining the temperature classification of the space heater surface temperature.
low temperature - surface temperature is relatively low, usually heated by hot water or electricity.
high temperature - surface temperature is relatively high, usually heated by gas or steam."
  ~~Enumeration defining the temperature classification of the space heater surface temperature.
low temperature - surface temperature is relatively low, usually heated by hot water or electricity.
high temperature - surface temperature is relatively high, usually heated by gas or steam.~~ Enumeration defining the temperature classification of the space heater surface temperature.\X\0D
low temperature - surface temperature is relatively low, usually heated by hot water or electricity.\X\0D
high temperature - surface temperature is relatively high, usually heated by gas or steam.
* PropertyDefs > PropertyDef [Name="TemperatureClassification"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="HeatTransferMedium"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="HeatTransferDimension"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="PlacementType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="EnergySource"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="TemperatureClassification"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Qto_ImpactProtectionDeviceBaseQuantities.xml
============================================

additions
---------
* Definition "$"

modifications
-------------
* QtoDefinitionAliases
  ~~QtoDefinitionAliases~~ ApplicableTypeValue


Pset_TubeBundleTypeCommon.xml
=============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_OutsideDesignCriteria.xml
==============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="BuildingThermalExposure"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="BuildingThermalExposure"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_ChimneyCommon.xml
======================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_PropertyAgreement.xml
==========================

modifications
-------------
* Definition "A property agreement is an agreement that enables the occupation of a property for a period of time.

The objective is to capture the information within an  agreement that is relevant to a facilities manager. Design and construction information associated with the property is not considered. A property agreement may be applied to an instance of IfcSpatialStructureElement including to compositions defined through the IfcSpatialStructureElement.Element.CompositionEnum.

Note that the associated actors are captured by the IfcOccupant class."
  ~~A property agreement is an agreement that enables the occupation of a property for a period of time.

The objective is to capture the information within an  agreement that is relevant to a facilities manager. Design and construction information associated with the property is not considered. A property agreement may be applied to an instance of IfcSpatialStructureElement including to compositions defined through the IfcSpatialStructureElement.Element.CompositionEnum.

Note that the associated actors are captured by the IfcOccupant class.~~ A property agreement is an agreement that enables the occupation of a property for a period of time.\X\0D
\X\0D
The objective is to capture the information within an  agreement that is relevant to a facilities manager. Design and construction information associated with the property is not considered. A property agreement may be applied to an instance of IfcSpatialStructureElement including to compositions defined through the IfcSpatialStructureElement.Element.CompositionEnum.\X\0D
\X\0D
Note that the associated actors are captured by the IfcOccupant class.
* PropertyDefs > PropertyDef [Name="AgreementType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="AgreementType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;



Qto_BurnerBaseQuantities.xml
============================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Pset_SwitchingDeviceTypeEmergencyStop.xml
=========================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="SwitchOperation"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="SwitchOperation"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_MaterialSteel.xml
======================

modifications
-------------
* ApplicableClasses > ClassName "IfcMaterial/Steel"
  ~~IfcMaterial/Steel~~ IfcMaterial
* ApplicableTypeValue "IfcMaterial/Steel"
  ~~IfcMaterial/Steel~~ IfcMaterial
* PropertyDefs > PropertyDef [Name="Relaxations"] > PropertyType
  ~~PropertyType~~ Definition
* PropertyDefs > PropertyDef [Name="Relaxations"] > Definition "Measures of decrease in stress over long time intervals resulting from plastic flow. Different relaxation values for different initial stress levels for a material may be given. It describes the time dependent relative relaxation value for a given initial stress level at constant strain.
Relating values are the "RelaxationValue". Related values are the "InitialStress""
  ~~Definition~~ PropertyType


Qto_LightFixtureBaseQuantities.xml
==================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Pset_ProtectiveDeviceTypeCommon.xml
===================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_ActuatorPHistory.xml
=========================

modifications
-------------
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="Position"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Status"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Quality"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Pset_PipeFittingOccurrence.xml
==============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Color"] > Definition "The color of the pipe segment.

Note: This is typically used only for plastic pipe segments. However, it may be used for any pipe segments with a painted surface which is not otherwise specified as a covering."
  ~~The color of the pipe segment.

Note: This is typically used only for plastic pipe segments. However, it may be used for any pipe segments with a painted surface which is not otherwise specified as a covering.~~ The color of the pipe segment.\X\0D
\X\0D
Note: This is typically used only for plastic pipe segments. However, it may be used for any pipe segments with a painted surface which is not otherwise specified as a covering.
* 
  ~~PSET_OCCURRENCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE


Qto_BeamBaseQuantities.xml
==========================

modifications
-------------
* QtoDefs > QtoDef [Name="GrossSurfaceArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="OuterSurfaceArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="CrossSectionArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetSurfaceArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetVolume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Length"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossVolume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases


Qto_ElectricTimeControlBaseQuantities.xml
=========================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Qto_PipeFittingBaseQuantities.xml
=================================

modifications
-------------
* QtoDefs > QtoDef [Name="OuterSurfaceArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Length"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetCrossSectionArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossCrossSectionArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases


Pset_ProtectiveDeviceTrippingUnitTypeResidualCurrent.xml
========================================================

modifications
-------------
* PropertyDefs
  ~~PropertyDefs~~ ApplicableClasses
* ApplicableClasses
  ~~ApplicableClasses~~ ApplicableTypeValue
* ApplicableTypeValue "IfcProtectiveDeviceTrippingUnit/RESIDUALCURRENT"
  ~~ApplicableTypeValue~~ PropertyDefs

