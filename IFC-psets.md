
Missing in output
=================
* Pset_DiscreteAccessoryFixingSocket.xml
* Pset_CivilElementCommon.xml
* Pset_TankTypePreformed.xml
* Pset_BuildingSystemCommon.xml
* Pset_AnnotationContourLine.xml
* Pset_AnnotationLineOfSight.xml
* Pset_MaterialWood.xml
* Pset_MaterialSteel.xml
* Pset_SpatialZoneCommon.xml
* Pset_MaterialWoodBasedPanel.xml
* Pset_ElementAssemblyCommon.xml
* Pset_DiscreteAccessoryWireLoop.xml
* Pset_DiscreteAccessoryDiagonalTrussConnector.xml
* Pset_DiscreteAccessoryEdgeFixingPlate.xml
* Pset_MaterialConcrete.xml
* Pset_MaterialWoodBasedBeam.xml
* Pset_SensorTypeLevelSensor.xml
* Pset_TankTypeSectional.xml
* Pset_DiscreteAccessoryCornerFixingPlate.xml
* Pset_DiscreteAccessoryStandardFixingPlate.xml
* Pset_DiscreteAccessoryLadderTrussConnector.xml

Missing in reference
=================
* Pset_FacilityPartGateHead.xml
* Pset_MaintenanceStrategy.xml
* Pset_MarineVehicleCommon.xml
* Pset_DiscreteAccessoryOccurenceCableArranger.xml
* Pset_FenderCommon.xml
* Pset_EnvironmentalEmissions.xml
* Pset_DataTransmissionUnit.xml
* Pset_EnergyRequirements.xml
* Pset_OpticalCableFittingGeneral.xml
* Pset_MaintenanceTriggerCondition.xml
* Pset_CopperCableGeneral.xml
* Pset_ElectricApplianceTypeVendingMachine.xml
* Pset_RailwayEnergyFacility.xml
* Pset_CableSegmentTypeWirePair.xml
* Pset_MaintenanceTriggerPerformance.xml
* Pset_BuiltElementCommon.xml
* Pset_OpticalNetworkUnit.xml
* Pset_CableFittingTypeJunction.xml
* Pset_OpticalFiberFittingGeneral.xml
* Pset_PatchCordCableGeneral.xml
* Pset_SensorTypeEarthquake.xml
* Pset_CommunicationsApplianceTypeTelephonyExchange.xml
* Pset_SensorTypeForeignObjectDetectionSensor.xml
* Pset_Railpad.xml
* Pset_RailwayPart.xml
* Pset_SuspensionAssemblyCantilever.xml
* Pset_OnSiteControlUnit.xml
* PSet_ShipyardCommon.xml
* Qto_FacilityPartBaseQuantities.xml
* PSet_QuayCommon.xml
* PSet_ShiplockDesignCriteria.xml
* Pset_SpringTensioner.xml
* Pset_CommunicationsApplianceTypeAntenna.xml
* Pset_CoxialCableGeneral.xml
* Pset_MaintenanceTriggerDuration.xml
* Pset_OutletTypePower.xml
* Pset_RailFasteningGeneral.xml
* Pset_TelecomActiveEquipmentGeneral.xml
* Pset_TransportElementCargo.xml
* Pset_WirelessCommunicationsApplianceGeneral.xml
* Pset_Blade.xml
* Pset_SimpleSuspensionAssembly.xml
* Pset_StockRail.xml
* Pset_CommunicationsApplianceTypeComputer.xml
* Pset_FenderDesignCriteria.xml
* PSet_VehicleAvailability.xml
* Pset_MooringDeviceCommon.xml
* Pset_BreakwaterCommon.xml
* Pset_TelecomTower.xml
* Pset_BuiltSystemCommon.xml
* Pset_IpNetworkEquipment.xml
* Pset_FacilityPartChamber.xml
* Pset_BalanceWeightTensioner.xml
* Pset_CopperCableFittingGeneral.xml
* Pset_CommunicationsApplianceOccuranceTransportEquipment.xml
* Pset_CableSegmentTypeFiberSegment.xml
* Pset_SensorTypeRainGauge.xml
* Pset_CableFittingTypeTransition.xml
* Qto_MarineFacilityBaseQuantities.xml
* Pset_NaturalSectionInsulator.xml
* Pset_QuayDesignCriteria.xml
* Pset_CableSegmentOccuranceFiberSegment.xml
* Pset_CableSegmentTypeOpticalCableSegment.xml
* PSet_ProcessCapacity.xml
* Pset_HydraulicTensioner.xml
* PSet_ShiplockComplex.xml
* Pset_MarineVehicleDesignCriteria.xml
* Pset_CommunicationsApplianceTypeTransportEquipment.xml
* Pset_JettyDesignCriteria.xml
* Qto_VehicleBaseQuantities.xml
* Pset_RailwaySubstationSecondaryZone.xml
* Pset_SlidingChair.xml
* Pset_RailwayFacility.xml
* PSet_ShiplockCommon.xml
* Pset_JettyCommon.xml
* PSet_VesselLineCommon.xml
* Pset_PostProtectionAndSafety.xml
* Pset_CommunicationsApplianceTypeModem.xml
* PSet_RevetmentCommon.xml
* Pset_ControlPanelDC.xml
* Pset_SensorTypeWind.xml
* Qto_MarineFacilityTransportationQuantities.xml
* Pset_SectionInsulator.xml
* Pset_SensorTypeSnowDepth.xml
* Pset_MobileTelecommunicationsApplianceTypeMasterUnit.xml
* Pset_RailwaySubstationPrimaryZone.xml
* Pset_DistributionBoardTypeDistributionFrame.xml
* Pset_BerthCommon.xml
* Pset_ControlPanelAC.xml

Qto_UnitaryControlElementBaseQuantities.xml
===========================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Pset_WindowCommon.xml
=====================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


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
* PropertyDefs > PropertyDef [Name="BulbLiquidColor"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="Activation"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="Response"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_TransponderGeneral.xml
===========================

additions
---------
* Definition

modifications
-------------
* ApplicableClasses > ClassName "IfcComm/TRANSPONDER"
  ~~IfcComm/TRANSPONDER~~ IfcCommunicationsAppliance/TRANSPONDER
* ApplicableTypeValue "IfcComm/TRANSPONDER"
  ~~IfcComm/TRANSPONDER~~ IfcCommunicationsAppliance/TRANSPONDER


Qto_AlarmBaseQuantities.xml
===========================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Pset_DistributionBoardOccurrence.xml
====================================

additions
---------
* ApplicableClasses > ClassName "IfcDistributionBoard"

modifications
-------------
* 
  ~~PSET_OCCURRENCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE


Pset_RailwayReservation.xml
===========================

additions
---------
* Definition

modifications
-------------
* ApplicableClasses > ClassName "IfcSpat/RESERVATION"
  ~~IfcSpat/RESERVATION~~ IfcSpatialZone/RESERVATION
* ApplicableTypeValue "IfcSpat/RESERVATION"
  ~~IfcSpat/RESERVATION~~ IfcSpatialZone/RESERVATION





Pset_DistributionBoardTypeCommon.xml
====================================

additions
---------
* ApplicableClasses > ClassName "IfcDistributionBoard"

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


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



Pset_ActionRequest.xml
======================

deletions
---------
* PropertyDefs > PropertyDef [Name="RequestSourceName"] > PropertyType


Pset_GeotechnicalStratumCommon.xml
==================================

modifications
-------------
* Definition "Properties describing the characteristics of any solid, water or void stratum. A status of "New" should not be associated to a _IfcGeotechnicalAssembly_  or _IfcSolidStratum_, as other entities are used for earthworks and courses."
  ~~Properties describing the characteristics of any solid, water or void stratum. A status of "New" should not be associated to a _IfcGeotechnicalAssembly_  or _IfcSolidStratum_, as other entities are used for earthworks and courses.~~ Properties describing the characteristics of any solid, water or void stratum. A status of &#8216;New&#8217; should not be associated to a IfcGeotechnicalAssembly  or IfcSolidStratum , as other entities are used for earthworks and courses.
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Qto_ChimneyBaseQuantities.xml
=============================

deletions
---------
* QtoDefs > QtoDef [Name="Length"] > NameAliases
* QtoDefs > QtoDef [Name="Length"] > DefinitionAliases
* QtoDefinitionAliases


Pset_CourseApplicationConditions.xml
====================================

additions
---------
* ApplicableClasses > ClassName "IfcCourseType"

modifications
-------------
* ApplicableTypeValue "IfcCourse"
  ~~IfcCourse~~ IfcCourseType


Pset_SwitchingDeviceTypeSelectorSwitch.xml
==========================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="SwitchActivation"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="SelectorType"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="SwitchUsage"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Pset_DistributionPortTypePipe.xml
=================================

modifications
-------------
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


Qto_PumpBaseQuantities.xml
==========================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases



Pset_RailwaySignalGeneral.xml
=============================

additions
---------
* Definition
* Applicability



Pset_MemberCommon.xml
=====================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_SensorTypePHSensor.xml
===========================

modifications
-------------
* PropertyDefs > PropertyDef [Name="SetPointPH"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue




Pset_PavementMillingCommon.xml
==============================

modifications
-------------
* ApplicableClasses > ClassName "IfcEarthworksCut/(.PAVEMENTMILLING.)"
  ~~IfcEarthworksCut/(.PAVEMENTMILLING.)~~ IfcEarthworksCut/PAVEMENTMILLING
* ApplicableTypeValue "IfcEarthworksCut/(.PAVEMENTMILLING.)"
  ~~IfcEarthworksCut/(.PAVEMENTMILLING.)~~ IfcEarthworksCut/PAVEMENTMILLING
* PropertyDefs > PropertyDef [Name="NominalDepth"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="NominalWidth"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Pset_CableConduitGeneral.xml
============================

additions
---------
* Definition

modifications
-------------
* ApplicableClasses > ClassName "IfcCabl/CONDUITSEGMENT"
  ~~IfcCabl/CONDUITSEGMENT~~ IfcCableCarrierSegment/CONDUITSEGMENT
* ApplicableTypeValue "IfcCabl/CONDUITSEGMENT"
  ~~IfcCabl/CONDUITSEGMENT~~ IfcCableCarrierSegment/CONDUITSEGMENT


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
* PropertyDefs > PropertyDef [Name="I2TApplicability"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="AdjustmentValueType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Qto_CompressorBaseQuantities.xml
================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


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



Pset_EnvironmentalImpactIndicators.xml
======================================

additions
---------
* PropertyDefs > PropertyDef [Name="ExpectedServiceLife"] > PropertyType > TypePropertySingleValue > DataType
* PropertyDefs > PropertyDef [Name="ExpectedServiceLife"] > PropertyType > TypePropertySingleValue > DataType

modifications
-------------
* Definition "Environmental impact indicators are related to a given &#8220;functional unit&#8221; (ISO 14040 concept). An example of functional unit is a "Double glazing window with PVC frame" and the unit to consider is "one square meter of opening elements filled by this product&#8221;.
Indicators values are valid for the whole life cycle or only a specific phase (see LifeCyclePhase property). Values of all the indicators are expressed per year according to the expected service life. The first five properties capture the characteristics of the functional unit. The following properties are related to environmental indicators.
There is a consensus agreement international for the five one. Last ones are not yet fully and formally agreed at the international level."
  ~~Environmental impact indicators are related to a given &#8220;functional unit&#8221; (ISO 14040 concept). An example of functional unit is a "Double glazing window with PVC frame" and the unit to consider is "one square meter of opening elements filled by this product&#8221;.
Indicators values are valid for the whole life cycle or only a specific phase (see LifeCyclePhase property). Values of all the indicators are expressed per year according to the expected service life. The first five properties capture the characteristics of the functional unit. The following properties are related to environmental indicators.
There is a consensus agreement international for the five one. Last ones are not yet fully and formally agreed at the international level.~~ Environmental impact indicators are related to a given \X2\201C\X0\functional unit\X2\201D\X0\ (ISO 14040 concept). An example of functional unit is a "Double glazing window with PVC frame" and the unit to consider is "one square meter of opening elements filled by this product\X2\201D\X0\.
Indicators values are valid for the whole life cycle or only a specific phase (see LifeCyclePhase property). Values of all the indicators are expressed per year according to the expected service life. The first five properties capture the characteristics of the functional unit. The following properties are related to environmental indicators.
There is a consensus agreement international for the five one. Last ones are not yet fully and formally agreed at the international level.
* PropertyDefs > PropertyDef [Name="LifeCyclePhase"] > PropertyType > TypePropertyEnumeratedValue > EnumList > EnumItem "NOTDEFINED"
  ~~NOTDEFINED~~ OTHER

deletions
---------
* PropertyDefs > PropertyDef [Name="LifeCyclePhase"] > PropertyType > TypePropertyEnumeratedValue > EnumList > EnumItem "USERDEFINED"


Pset_SanitaryTerminalTypeWashHandBasin.xml
==========================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Mounting"] > Definition "Selection of the form of mounting from the enumerated list of mountings where:-

BackToWall: 	A pedestal mounted sanitary terminal that fits flush to the wall at the rear to cover its service connections.
Pedestal: 	A floor mounted sanitary terminal that has an integral base
CounterTop: 	A sanitary terminal that is installed into a horizontal surface that is installed into a horizontal surface. Note: When applied to a wash hand basin, the term more normally used is &#8216;vanity&#8217;. See also Wash Hand Basin Type specification.
WallHung: 	A sanitary terminal cantilevered clear of the floor."
  ~~Selection of the form of mounting from the enumerated list of mountings where:-

BackToWall: 	A pedestal mounted sanitary terminal that fits flush to the wall at the rear to cover its service connections.
Pedestal: 	A floor mounted sanitary terminal that has an integral base
CounterTop: 	A sanitary terminal that is installed into a horizontal surface that is installed into a horizontal surface. Note: When applied to a wash hand basin, the term more normally used is &#8216;vanity&#8217;. See also Wash Hand Basin Type specification.
WallHung: 	A sanitary terminal cantilevered clear of the floor.~~ Selection of the form of mounting from the enumerated list of mountings where:-

BackToWall: \X\09A pedestal mounted sanitary terminal that fits flush to the wall at the rear to cover its service connections.
Pedestal: \X\09A floor mounted sanitary terminal that has an integral base
CounterTop: \X\09A sanitary terminal that is installed into a horizontal surface that is installed into a horizontal surface. Note: When applied to a wash hand basin, the term more normally used is \X2\2018\X0\vanity\X2\2019\X0\. See also Wash Hand Basin Type specification.
WallHung: \X\09A sanitary terminal cantilevered clear of the floor.
* PropertyDefs > PropertyDef [Name="Mounting"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Mounting"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_SensorTypeCO2Sensor.xml
============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="SetPointConcentration"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue


Pset_HeatExchangerTypeCommon.xml
================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Arrangement"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Arrangement"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;



Pset_SensorTypeLightSensor.xml
==============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="SetPointIlluminance"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue


Pset_ControllerTypeProgrammable.xml
===================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Application"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="ControlType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="ControlType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="Application"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_RadiiKerbStone.xml
=======================

additions
---------
* ApplicableClasses > ClassName "IfcKerbType"

modifications
-------------
* PropertyDefs > PropertyDef [Name="CurveShape"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="CurveShape"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Qto_VolumetricStratumBaseQuantities.xml
=======================================

modifications
-------------
* Definition "Quantity measures associated to volumetric stratum such as in a geotechnical model. Uncertainty is documented in _Pset_Uncertainty_."
  ~~Quantity measures associated to volumetric stratum such as in a geotechnical model. Uncertainty is documented in _Pset_Uncertainty_.~~ Quantity measures associated to volumetric stratum such as in a geotechnical model. Uncertainty is documented in Pset_Uncertainty.
* QtoDefs > QtoDef [Name="Area"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="PlanArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Volume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Mass"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases


Qto_SpaceBaseQuantities.xml
===========================

modifications
-------------
* QtoDefs > QtoDef [Name="FinishCeilingHeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetVolume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetWallArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossFloorArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Height"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossWallArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossVolume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossPerimeter"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetFloorArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetCeilingArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="FinishFloorHeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossCeilingArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetPerimeter"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases


Pset_ProtectiveDeviceBreakerUnitI2TFuseCurve.xml
================================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="BreakerUnitFuseMeltingCurve"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="VoltageLevel"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="BreakerUnitFuseBreakingingCurve"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Pset_DistributionPortTypeDuct.xml
=================================

additions
---------
* PropertyDefs > PropertyDef [Name="ConnectionType"]

modifications
-------------
* PropertyDefs > PropertyDef [Name="DryBulbTemperature"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Pressure"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="NominalThickness"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="VolumetricFlowRate"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Velocity"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="WetBulbTemperature"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="NominalWidth"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="ConnectionType"]


Pset_SanitaryTerminalTypeCommon.xml
===================================

additions
---------
* PropertyDefs > PropertyDef [Name="NominalDepth"] > Definition "Nominal or quoted depth of the object."

modifications
-------------
* PropertyDefs > PropertyDef [Name="NominalDepth"] > Definition "Nominal Depth of the object"
  ~~Nominal Depth of the object~~ Nominal or quoted depth of the object.
* PropertyDefs > PropertyDef [Name="NominalDepth"] > PropertyType > TypePropertySingleValue > DataType
  ~~IfcNonNegativeLengthMeasure~~ IfcPositiveLengthMeasure
* PropertyDefs > PropertyDef [Name="NominalLength"] > Definition "Nominal length of the object"
  ~~Nominal length of the object~~ Nominal or quoted length of the object.
* PropertyDefs > PropertyDef [Name="NominalLength"] > PropertyType > TypePropertySingleValue > DataType
  ~~IfcNonNegativeLengthMeasure~~ IfcPositiveLengthMeasure
* PropertyDefs > PropertyDef [Name="NominalWidth"] > Definition "The nominal width of the object."
  ~~The nominal width of the object.~~ Nominal or quoted width of the object.
* PropertyDefs > PropertyDef [Name="NominalWidth"] > PropertyType > TypePropertySingleValue > DataType
  ~~IfcNonNegativeLengthMeasure~~ IfcPositiveLengthMeasure
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_StackTerminalTypeCommon.xml
================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;




Pset_ReinforcementBarPitchOfWall.xml
====================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="BarAllocationType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="BarAllocationType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;




Pset_SwitchingDeviceTypeCommon.xml
==================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="SetPoint"] > PropertyType > TypePropertyTableValue
  ~~TypePropertyTableValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="SwitchFunction"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="SetPoint"] > PropertyType > TypePropertyTableValue > Expression
  ~~&lt;Expression&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="SwitchFunction"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="SetPoint"] > PropertyType > TypePropertyTableValue > DefiningValue
* PropertyDefs > PropertyDef [Name="SetPoint"] > PropertyType > TypePropertyTableValue > DefinedValue


Pset_SoundGeneration.xml
========================

modifications
-------------
* PropertyDefs > PropertyDef [Name="SoundCurve"] > PropertyType
  ~~PropertyType~~ Definition
* PropertyDefs > PropertyDef [Name="SoundCurve"] > Definition "Table of sound frequencies and sound power measured in decibels at a reference power of 1 picowatt(10\^(-12) watt) for the referenced octave band frequency."
  ~~Definition~~ PropertyType


Qto_CoveringBaseQuantities.xml
==============================

modifications
-------------
* QtoDefs > QtoDef [Name="GrossArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Width"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases


Pset_JunctionBoxTypeCommon.xml
==============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="MountingType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="PlacingType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="ShapeType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="MountingType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="PlacingType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="ShapeType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_RoadDesignCriteriaCommon.xml
=================================

additions
---------
* ApplicableTypeValue "IfcAnnotation/USERDEFINED"

modifications
-------------
* PropertyDefs > PropertyDef [Name="DesignSpeed"] > Definition "Speed selected in designing a new road or in modernizing, strengthening or rehabilitating an existing road section, to determine the various geometric design features of the carriageway that allow a car to travel safely at that speed, under normal road surface and weather conditions. 

>NOTE&nbsp; Definition according to PIARC. 
>
>NOTE&nbsp; The design speed is not constant, but may vary depending on the conditions of relief (plain, hill, mountain)."
  ~~Speed selected in designing a new road or in modernizing, strengthening or rehabilitating an existing road section, to determine the various geometric design features of the carriageway that allow a car to travel safely at that speed, under normal road surface and weather conditions. 

>NOTE&nbsp; Definition according to PIARC. 
>
>NOTE&nbsp; The design speed is not constant, but may vary depending on the conditions of relief (plain, hill, mountain).~~ NOTE Definition from PIARC: Speed selected in designing a new road or in modernizing, strengthening or rehabilitating an existing road section, to determine the various geometric design features of the carriageway that allow a car to travel safely at that speed, under normal road surface and weather conditions. Note: the design speed is not constant, but may vary depending on the conditions of relief (plain, hill, mountain).


Pset_AlarmPHistory.xml
======================

modifications
-------------
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="Enabled"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Severity"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Condition"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Acknowledge"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="User"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;



Pset_SwitchingDeviceTypeToggleSwitch.xml
========================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="ToggleSwitchType"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="SwitchActivation"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="SwitchUsage"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Pset_RoadSymbolsCommon.xml
==========================

modifications
-------------
* ApplicableClasses > ClassName "IfcSurfaceFeature/(.SYMBOLMARKING.)"
  ~~IfcSurfaceFeature/(.SYMBOLMARKING.)~~ IfcSurfaceFeature/SYMBOLMARKING
* ApplicableTypeValue "IfcSurfaceFeature/(.SYMBOLMARKING.)"
  ~~IfcSurfaceFeature/(.SYMBOLMARKING.)~~ IfcSurfaceFeature/SYMBOLMARKING
* PropertyDefs > PropertyDef [Name="TypeDesignation"] > Name "TypeDesignation"
  ~~TypeDesignation~~ Type
* PropertyDefs > PropertyDef [Name="TypeDesignation"] > Definition "Type designator according to local standards"
  ~~Type designator according to local standards~~ A symbol designator with content according to local standards, e.g.  'BycycleCrossing', 'RoadStuds', 'SpeedBump', 'TransverseBar', 'BusStop', 'Chevron', 'Hatched', 'KeepClear', 'BoxJunction', 'EmergencyExit', 'Intersection', 'Junction'


Qto_ProtectiveDeviceTrippingUnitBaseQuantities.xml
==================================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Pset_Sleeper.xml
================

additions
---------
* Definition
* ApplicableTypeValue "IfcTrackElement/SLEEPER"


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


Pset_PavementSurfaceCommon.xml
==============================

additions
---------
* ApplicableClasses > ClassName "IfcPavementType"

modifications
-------------
* PropertyDefs > PropertyDef [Name="PavementTexture"] > Definition "Characterization of pavement texture by mean profile depth

>NOTE&nbsp; Definition according to ISO 13473-1:2019"
  ~~Characterization of pavement texture by mean profile depth

>NOTE&nbsp; Definition according to ISO 13473-1:2019~~ Characterization of pavement texture by mean profile depth (ISO 13473-1:2019)


Pset_PrecastKerbStone.xml
=========================

additions
---------
* ApplicableClasses > ClassName "IfcKerbType"

modifications
-------------
* ApplicableTypeValue "IfcKerb"
  ~~IfcKerb~~ IfcKerbType
* PropertyDefs > PropertyDef [Name="NominalWidth"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="NominalHeight"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="NominalLength"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="TypeDesignation"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Qto_CurtainWallQuantities.xml
=============================

modifications
-------------
* QtoDefs > QtoDef [Name="Width"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossSideArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Length"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetSideArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Height"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases


Pset_DistributionSystemTypeVentilation.xml
==========================================

modifications
-------------
* ApplicableClasses > ClassName "IfcDistributionSystem/VENTILATION"
  ~~IfcDistributionSystem/VENTILATION~~ IfcDistributionPort/VENTILATION
* ApplicableTypeValue "IfcDistributionSystem/VENTILATION"
  ~~IfcDistributionSystem/VENTILATION~~ IfcDistributionPort/VENTILATION

deletions
---------
* PropertyDefs > PropertyDef [Name="DuctSealant"] > PropertyType


Pset_RailJoint.xml
==================

modifications
-------------
* ApplicableClasses > ClassName "IfcMech/RAILJOINT"
  ~~IfcMech/RAILJOINT~~ IfcMechanicalFastener/RAILJOINT
* ApplicableTypeValue "IfcMech/RAILJOINT"
  ~~IfcMech/RAILJOINT~~ IfcMechanicalFastener/RAILJOINT


Pset_FilterTypeWaterFilter.xml
==============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="WaterFilterType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="WaterFilterType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_ChimneyCommon.xml
======================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Qto_JunctionBoxBaseQuantities.xml
=================================

modifications
-------------
* QtoDefs > QtoDef [Name="NumberOfGangs"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases


Pset_DiscretizedPointListCommon.xml
===================================

additions
---------
* Definition


Pset_HumidifierPHistory.xml
===========================

modifications
-------------
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="SaturationEfficiency"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="AtmosphericPressure"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Qto_StairFlightBaseQuantities.xml
=================================

modifications
-------------
* QtoDefs > QtoDef [Name="Length"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossVolume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetVolume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases



Pset_SpaceLightingRequirements.xml
==================================

modifications
-------------
* ApplicableTypeValue "IfcSpace, IfcSpatialZone, IfcZone"
  ~~IfcSpace, IfcSpatialZone, IfcZone~~ IfcSpace

deletions
---------
* ApplicableClasses > ClassName "IfcSpatialZone"
* ApplicableClasses > ClassName "IfcZone"


Pset_CoolingTowerTypeCommon.xml
===============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="CapacityControl"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="CircuitType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="ControlStrategy"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="FlowArrangement"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="SprayType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="FlowArrangement"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="CapacityControl"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="SprayType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="CircuitType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="ControlStrategy"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_CableCarrierSegmentTypeCableTrunkingSegment.xml
====================================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="NominalWidth"] > Definition "The nominal width of the object."
  ~~The nominal width of the object.~~ The nominal width of the segment.
* PropertyDefs > PropertyDef [Name="NominalWidth"] > PropertyType > TypePropertySingleValue > DataType
  ~~IfcNonNegativeLengthMeasure~~ IfcPositiveLengthMeasure


Pset_CableFittingTypeCommon.xml
===============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;




Pset_AudioVisualApplianceTypeRailwayCommunicationTerminal.xml
=============================================================

additions
---------
* Definition

modifications
-------------
* ApplicableTypeValue "IfcAudi/RAILWAY_COMMUNICATION_TERMINAL, IfcAudi/TELEPHONE"
  ~~IfcAudi/RAILWAY_COMMUNICATION_TERMINAL, IfcAudi/TELEPHONE~~ IfcAudioVisualAppliance/TELEPHONE
* ApplicableClasses > ClassName "IfcAudi/RAILWAY_COMMUNICATION_TERMINAL"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcAudi/TELEPHONE"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;


Pset_GeotechnicalAssemblyCommon.xml
===================================

modifications
-------------
* Definition "Properties describing the characteristics of any geotechnical model. A Status of "New" should not be associated to a _IfcGeotechnicalAssembly_ or _IfcGeotechnicalStratum_, as other entities are used for earthworks and courses."
  ~~Properties describing the characteristics of any geotechnical model. A Status of "New" should not be associated to a _IfcGeotechnicalAssembly_ or _IfcGeotechnicalStratum_, as other entities are used for earthworks and courses.~~ Properties describing the characteristics of any geotechnical model. A Status of &#8216;New&#8217; should not be associated to a IfcGeotechnicalAssembly or IfcGeotechnicalStratum, as other entities are used for earthworks and courses.
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Purpose"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Purpose"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_SpaceHeaterPHistory.xml
============================

modifications
-------------
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="SpaceAirTemperature"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="HeatOutputRate"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="FractionRadiantHeatTransfer"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Exponent"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="OutputCapacityCurve"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="UACurve"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Effectiveness"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="AuxiliaryEnergySourceConsumption"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="FractionConvectiveHeatTransfer"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="SpaceMeanRadiantTemperature"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="SurfaceTemperature"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="AirResistanceCurve"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;



Pset_Condition.xml
==================

modifications
-------------
* ApplicableTypeValue "IfcElement,IfcSystem,IfcAsset"
  ~~IfcElement,IfcSystem,IfcAsset~~ IfcAsset
* PropertyDefs > PropertyDef [Name="AssessmentMethod"] > PropertyType > TypePropertyReferenceValue
  ~~TypePropertyReferenceValue~~ TypePropertySingleValue


Pset_OutletTypeCommon.xml
=========================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_ValveTypeFaucet.xml
========================

modifications
-------------
* PropertyDefs > PropertyDef [Name="FaucetOperation"] > Definition "Defines the range of ways in which a faucet can be operated that may be specified where:

CeramicDisc: Quick action faucet with a ceramic seal to open or close the orifice
.
LeverHandle: Quick action faucet that is operated by a lever handle
.
NonConcussiveSelfClosing:	 Self closing faucet that does not induce surge pressure
.
QuarterTurn: Quick action faucet that can be fully opened or shut by turning the operating mechanism through 90 degrees.
QuickAction: Faucet that can be opened or closed fully with a single small movement of the operating mechanism
.
ScrewDown: Faucet in which a plate or disc is moved, by the rotation of a screwed spindle, to close or open the orifice.
SelfClosing: Faucet that is opened by pressure of the top of an operating spindle and is closed under the action of a spring or weight when the pressure is released.
TimedSelfClosing: 	Self closing faucet that discharges for a predetermined period of time
."
  ~~Defines the range of ways in which a faucet can be operated that may be specified where:

CeramicDisc: Quick action faucet with a ceramic seal to open or close the orifice
.
LeverHandle: Quick action faucet that is operated by a lever handle
.
NonConcussiveSelfClosing:	 Self closing faucet that does not induce surge pressure
.
QuarterTurn: Quick action faucet that can be fully opened or shut by turning the operating mechanism through 90 degrees.
QuickAction: Faucet that can be opened or closed fully with a single small movement of the operating mechanism
.
ScrewDown: Faucet in which a plate or disc is moved, by the rotation of a screwed spindle, to close or open the orifice.
SelfClosing: Faucet that is opened by pressure of the top of an operating spindle and is closed under the action of a spring or weight when the pressure is released.
TimedSelfClosing: 	Self closing faucet that discharges for a predetermined period of time
.~~ Defines the range of ways in which a faucet can be operated that may be specified where:

CeramicDisc: Quick action faucet with a ceramic seal to open or close the orifice
.
LeverHandle: Quick action faucet that is operated by a lever handle
.
NonConcussiveSelfClosing:\X\09 Self closing faucet that does not induce surge pressure
.
QuarterTurn: Quick action faucet that can be fully opened or shut by turning the operating mechanism through 90 degrees.
QuickAction: Faucet that can be opened or closed fully with a single small movement of the operating mechanism
.
ScrewDown: Faucet in which a plate or disc is moved, by the rotation of a screwed spindle, to close or open the orifice.
SelfClosing: Faucet that is opened by pressure of the top of an operating spindle and is closed under the action of a spring or weight when the pressure is released.
TimedSelfClosing: \X\09Self closing faucet that discharges for a predetermined period of time
.
* PropertyDefs > PropertyDef [Name="FaucetType"] > Definition "Defines the range of faucet types that may be specified where:

Bib:	 Faucet with a horizontal inlet and a nozzle that discharges downwards.
Globe:	 Faucet fitted through the end of a bath, with a horizontal inlet, a partially spherical body and a vertical nozzle.
Diverter: 	Combination faucet assembly with a valve to enable the flow of mixed water to be transferred to a showerhead.
DividedFlowCombination:	 Combination faucet assembly in which hot and cold water are kept separate until emerging from a common nozzle
.
Pillar:	 Faucet that has a vertical inlet and a nozzle that discharges downwards
.
SingleOutletCombination =	 Combination faucet assembly in which hot and cold water mix before emerging from a common nozzle
.
Spray:	 Faucet with a spray outlet
.
SprayMixing:	 Spray faucet connected to hot and cold water supplies that delivers water at a temperature determined during use."
  ~~Defines the range of faucet types that may be specified where:

Bib:	 Faucet with a horizontal inlet and a nozzle that discharges downwards.
Globe:	 Faucet fitted through the end of a bath, with a horizontal inlet, a partially spherical body and a vertical nozzle.
Diverter: 	Combination faucet assembly with a valve to enable the flow of mixed water to be transferred to a showerhead.
DividedFlowCombination:	 Combination faucet assembly in which hot and cold water are kept separate until emerging from a common nozzle
.
Pillar:	 Faucet that has a vertical inlet and a nozzle that discharges downwards
.
SingleOutletCombination =	 Combination faucet assembly in which hot and cold water mix before emerging from a common nozzle
.
Spray:	 Faucet with a spray outlet
.
SprayMixing:	 Spray faucet connected to hot and cold water supplies that delivers water at a temperature determined during use.~~ Defines the range of faucet types that may be specified where:

Bib:\X\09 Faucet with a horizontal inlet and a nozzle that discharges downwards.
Globe:\X\09 Faucet fitted through the end of a bath, with a horizontal inlet, a partially spherical body and a vertical nozzle.
Diverter: \X\09Combination faucet assembly with a valve to enable the flow of mixed water to be transferred to a showerhead.
DividedFlowCombination:\X\09 Combination faucet assembly in which hot and cold water are kept separate until emerging from a common nozzle
.
Pillar:\X\09 Faucet that has a vertical inlet and a nozzle that discharges downwards
.
SingleOutletCombination =\X\09 Combination faucet assembly in which hot and cold water mix before emerging from a common nozzle
.
Spray:\X\09 Faucet with a spray outlet
.
SprayMixing:\X\09 Spray faucet connected to hot and cold water supplies that delivers water at a temperature determined during use.




Pset_AudioVisualApplianceTypeSpeaker.xml
========================================

additions
---------
* PropertyDefs > PropertyDef [Name="SpeakerType"]

modifications
-------------
* PropertyDefs > PropertyDef [Name="SpeakerDriverSize"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="SpeakerType"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="FrequencyResponse"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="SpeakerMounting"]


Qto_PlateBaseQuantities.xml
===========================

modifications
-------------
* QtoDefs > QtoDef [Name="GrossVolume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetVolume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Width"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Perimeter"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases


Qto_FlowMeterBaseQuantities.xml
===============================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Pset_ProtectiveDeviceTypeFuseDisconnector.xml
=============================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="VoltageLevel"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="VoltageLevel"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;



Qto_FlowInstrumentBaseQuantities.xml
====================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases



Qto_OpeningElementBaseQuantities.xml
====================================

modifications
-------------
* QtoDefs > QtoDef [Name="Volume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Depth"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Height"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Area"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Width"]
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




Pset_VibrationIsolatorTypeCommon.xml
====================================

additions
---------
* ApplicableClasses > ClassName "IfcVibrationIsolator/COMPRESSION"
* ApplicableClasses > ClassName "IfcVibrationIsolator/SPRING"
* PropertyDefs > PropertyDef [Name="IsolatorStaticDeflection"] > Definition "Static deflection of the vibration isolator."

modifications
-------------
* ApplicableTypeValue "IfcVibrationIsolator"
  ~~IfcVibrationIsolator~~ IfcVibrationIsolator/SPRING
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* ApplicableClasses > ClassName "IfcVibrationIsolator"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Qto_BuildingBaseQuantities.xml
==============================

modifications
-------------
* QtoDefs > QtoDef [Name="GrossFloorArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetFloorArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetVolume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Height"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="FootprintArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossVolume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="EavesHeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases


Pset_SensorTypeMoistureSensor.xml
=================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="SetPointMoisture"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue


Pset_PipeSegmentOccurrence.xml
==============================

modifications
-------------
* 
  ~~PSET_OCCURRENCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE


Pset_TransformerTypeCommon.xml
==============================

additions
---------
* PropertyDefs > PropertyDef [Name="SecondaryCurrent"] > PropertyType > TypePropertySingleValue > DataType

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;



Pset_UnitaryControlElementTypeThermostat.xml
============================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="TemperatureSetPoint"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue




Pset_ChillerTypeCommon.xml
==========================

additions
---------
* PropertyDefs > PropertyDef [Name="FullLoadRatioCurve"]

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="FullLoadRatioCurve"] > Name "FullLoadRatioCurve"
  ~~&lt;Name&gt;~~ &lt;Name&gt;
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="FullLoadRatioCurve"] > PropertyType
  ~~&lt;PropertyType&gt;~~ &lt;PropertyType&gt;
* PropertyDefs > PropertyDef [Name="CapacityCurve"] > Name "CapacityCurve"
  ~~&lt;Name&gt;~~ &lt;Name&gt;
* PropertyDefs > PropertyDef [Name="FullLoadRatioCurve"] > Definition "Ratio of actual power to full load power as a quadratic function of part load, at certain condensing and evaporating temperature, FracFullLoadPower = f ( PartLoadRatio)."
  ~~&lt;Definition&gt;~~ &lt;Definition&gt;
* PropertyDefs > PropertyDef [Name="CapacityCurve"] > PropertyType
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


Qto_SensorBaseQuantities.xml
============================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Pset_RoadGuardElement.xml
=========================

modifications
-------------
* Definition "Properties assigned to IfcWall/PARAPET or IfcRailing/GUARDRAIL when assigned as road guard elements."
  ~~Properties assigned to IfcWall/PARAPET or IfcRailing/GUARDRAIL when assigned as road guard elements.~~ Properties assigned to IfcWall/PARAPET or IfcRailing/GUARDRAIL.
* ApplicableTypeValue "IfcRailing/(.GUARDRAIL.),IfcWall/(.PARAPET.)"
  ~~IfcRailing/(.GUARDRAIL.),IfcWall/(.PARAPET.)~~ IfcRailing/GUARDRAIL
* ApplicableClasses > ClassName "IfcWall/(.PARAPET.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcRailing/(.GUARDRAIL.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;


Pset_RailJoint_Welded.xml
=========================

additions
---------
* ApplicableTypeValue "IfcFastener/WELD"



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

Note that BackToWall, Pedestal and WallHung are allowable values for a bidet.~~ The property enumeration Pset_SanitaryMountingEnum defines the forms of mounting or fixing of the sanitary terminal that may be specified within property sets used to define sanitary terminals (WC\X2\2019\X0\s, basins, sinks, etc.) where:-

BackToWall: \X\09A pedestal mounted sanitary terminal that fits flush to the wall at the rear to cover its service connections
.
Pedestal: \X\09A floor mounted sanitary terminal that has an integral base
.
CounterTop: \X\09A sanitary terminal that is installed into a horizontal surface that is installed into a horizontal surface. Note: When applied to a wash hand basin, the term more normally used is \X2\2018\X0\vanity\X2\2019\X0\. See also Wash Hand Basin Type specification.
WallHung: \X\09A sanitary terminal cantilevered clear of the floor.

Note that BackToWall, Pedestal and WallHung are allowable values for a bidet.
* PropertyDefs > PropertyDef [Name="Mounting"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Mounting"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_RailwayEnergyReservation.xml
=================================

additions
---------
* Definition

modifications
-------------
* ApplicableClasses > ClassName "IfcSpat/RESERVATION"
  ~~IfcSpat/RESERVATION~~ IfcSpatialZone/RESERVATION
* ApplicableTypeValue "IfcSpat/RESERVATION"
  ~~IfcSpat/RESERVATION~~ IfcSpatialZone/RESERVATION


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


Pset_CoilTypeCommon.xml
=======================

modifications
-------------
* PropertyDefs > PropertyDef [Name="AirflowRateRange"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="OperationalTemperatureRange"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="PlacementType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="PlacementType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


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



Pset_AudioVisualApplianceTypeReceiver.xml
=========================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="AudioMode"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="ReceiverType"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="AudioAmplification"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Pset_UnitaryControlElementTypeCommon.xml
========================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Mode"] > PropertyType > TypePropertyTableValue
  ~~TypePropertyTableValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="Mode"] > PropertyType > TypePropertyTableValue > Expression
  ~~&lt;Expression&gt;~~ &lt;DataType&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="Mode"] > PropertyType > TypePropertyTableValue > DefiningValue
* PropertyDefs > PropertyDef [Name="Mode"] > PropertyType > TypePropertyTableValue > DefinedValue


Pset_FilterTypeAirParticleFilter.xml
====================================

additions
---------
* PropertyDefs > PropertyDef [Name="WeightedEfficiencyCurve"]

modifications
-------------
* PropertyDefs > PropertyDef [Name="AirParticleFilterType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="SeparationType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="WeightedEfficiencyCurve"] > PropertyType
  ~~&lt;PropertyType&gt;~~ &lt;PropertyType&gt;
* PropertyDefs > PropertyDef [Name="WeightedEfficiencyCurve"] > Definition "Weighted efficiency curve as a function of dust holding weight, efficiency = f (dust holding weight)."
  ~~&lt;Definition&gt;~~ &lt;Definition&gt;
* PropertyDefs > PropertyDef [Name="PressureDropCurve"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="WeightedEfficiencyCurve"] > Name "WeightedEfficiencyCurve"
  ~~&lt;Name&gt;~~ &lt;Name&gt;
* PropertyDefs > PropertyDef [Name="AirParticleFilterType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="SeparationType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="FrameMaterial"] > PropertyType
* PropertyDefs > PropertyDef [Name="CountedEfficiencyCurve"]


Pset_SensorTypeHumiditySensor.xml
=================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="SetPointHumidity"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue


Pset_SystemFurnitureElementTypePanel.xml
========================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="FurniturePanelType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="NominalThickness"] > Definition "The nominal  thickness of the entity."
  ~~The nominal  thickness of the entity.~~ The nominal thickness of the panel.
* PropertyDefs > PropertyDef [Name="NominalThickness"] > PropertyType > TypePropertySingleValue > DataType
  ~~IfcNonNegativeLengthMeasure~~ IfcPositiveLengthMeasure
* PropertyDefs > PropertyDef [Name="FurniturePanelType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_SensorTypeCommon.xml
=========================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_ElectricApplianceTypeCommon.xml
====================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;



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


Pset_WasteTerminalTypeCommon.xml
================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_TankOccurrence.xml
=======================

modifications
-------------
* 
  ~~PSET_OCCURRENCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE





Pset_DamperOccurrence.xml
=========================

modifications
-------------
* PropertyDefs > PropertyDef [Name="SizingMethod"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* 
  ~~PSET_OCCURRENCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="SizingMethod"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_AirTerminalBoxTypeCommon.xml
=================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="AirflowRateRange"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="AirPressureRange"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
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
* PropertyDefs > PropertyDef [Name="ReheatType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="ArrangementType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;



Pset_ControllerTypeMultiPosition.xml
====================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="ControlType"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Range"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Labels"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Value"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Pset_DistributionChamberElementTypeInspectionChamber.xml
========================================================

deletions
---------
* PropertyDefs > PropertyDef [Name="AccessCoverMaterial"] > PropertyType
* PropertyDefs > PropertyDef [Name="BaseMaterial"] > PropertyType
* PropertyDefs > PropertyDef [Name="WallMaterial"] > PropertyType


Pset_ServiceLifeFactors.xml
===========================

modifications
-------------
* 
  ~~PSET_OCCURRENCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="MaintenanceLevel"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="QualityOfComponents"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="DesignLevel"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="InUseConditions"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="IndoorEnvironment"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="OutdoorEnvironment"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="WorkExecutionLevel"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Pset_PumpPHistory.xml
=====================

modifications
-------------
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="Flowrate"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="OverallEfficiency"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Power"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="MechanicalEfficiency"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="PressureRise"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="RotationSpeed"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;



Qto_InterceptorBaseQuantities.xml
=================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases



Pset_SpaceThermalRequirements.xml
=================================

modifications
-------------
* ApplicableTypeValue "IfcSpace, IfcSpatialZone, IfcZone"
  ~~IfcSpace, IfcSpatialZone, IfcZone~~ IfcSpace

deletions
---------
* ApplicableClasses > ClassName "IfcSpatialZone"
* ApplicableClasses > ClassName "IfcZone"




Pset_SwitchingDeviceTypePHistory.xml
====================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="SetPoint"] > PropertyType > TypePropertyReferenceValue
  ~~TypePropertyReferenceValue~~ TypePropertySingleValue
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE


Pset_BuildingElementProxyCommon.xml
===================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_DuctFittingPHistory.xml
============================

modifications
-------------
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="AirFlowLeakage"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="AtmosphericPressure"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="LossCoefficient"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;



Pset_SwitchingDeviceTypeKeypad.xml
==================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="KeypadType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="KeypadType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
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
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="DeliveryType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="CorrosionTreatment"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;



Qto_TankBaseQuantities.xml
==========================

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


Pset_ActuatorTypeCommon.xml
===========================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Application"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="Application"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;





Pset_CableSegmentOccurrence.xml
===============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="DesignAmbientTemperature"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="MountingMethod"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* 
  ~~PSET_OCCURRENCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="MountingMethod"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Qto_BuildingElementProxyQuantities.xml
======================================

modifications
-------------
* QtoDefinitionAliases
  ~~QtoDefinitionAliases~~ Definition
* QtoDefs > QtoDef [Name="NetVolume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetSurfaceArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;


Qto_HeatExchangerBaseQuantities.xml
===================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases



Pset_AudioVisualApplianceTypeAmplifier.xml
==========================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="AudioAmplification"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="AudioMode"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="AmplifierType"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;



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
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="HeatTransferTypeEnum"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Qto_CableSegmentBaseQuantities.xml
==================================

modifications
-------------
* QtoDefs > QtoDef [Name="Length"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="OuterSurfaceArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="CrossSectionArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases


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


Pset_DamperTypeFireDamper.xml
=============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="ActuationType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="ClosureRatingEnum"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="ActuationType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="ClosureRatingEnum"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_PipeFittingOccurrence.xml
==============================

modifications
-------------
* 
  ~~PSET_OCCURRENCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE


Pset_ControllerTypeProportional.xml
===================================

modifications
-------------
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


Qto_ValveBaseQuantities.xml
===========================

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


Qto_ElectricTimeControlBaseQuantities.xml
=========================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Qto_CableCarrierSegmentBaseQuantities.xml
=========================================

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


Qto_LightFixtureBaseQuantities.xml
==================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Pset_WallCommon.xml
===================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_Asset.xml
==============

additions
---------
* PropertyDefs > PropertyDef [Name="Owner"]
* PropertyDefs > PropertyDef [Name="Operator"]
* PropertyDefs > PropertyDef [Name="ResponsiblePerson"]
* PropertyDefs > PropertyDef [Name="OriginalValue"]
* PropertyDefs > PropertyDef [Name="CurrentValue"]
* PropertyDefs > PropertyDef [Name="DepreciatedValue"]



Pset_EngineTypeCommon.xml
=========================

modifications
-------------
* PropertyDefs > PropertyDef [Name="EnergySource"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="EnergySource"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_MechanicalFastener.xml
===========================

additions
---------
* Definition


Pset_KerbCommon.xml
===================

additions
---------
* ApplicableClasses > ClassName "IfcKerbType"


Qto_DuctSilencerBaseQuantities.xml
==================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Pset_StructuralSurfaceMemberVaryingThickness.xml
================================================

additions
---------
* PropertyDefs > PropertyDef [Name="Location2Local"]

modifications
-------------
* PropertyDefs > PropertyDef [Name="Location2Global"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Location3Global"] > Definition "Global X,Y,Z coordinates of the point in which Thickness3 is given"
  ~~&lt;Definition&gt;~~ &lt;Definition&gt;
* PropertyDefs > PropertyDef [Name="Location2Local"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Location3Global"] > PropertyType
  ~~&lt;PropertyType&gt;~~ &lt;PropertyType&gt;
* PropertyDefs > PropertyDef [Name="Location1Global"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Location1Local"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Location3Global"] > Name "Location3Global"
  ~~&lt;Name&gt;~~ &lt;Name&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="Location3Local"]


Pset_VoltageAndCurrentTransformer.xml
=====================================

additions
---------
* Definition

modifications
-------------
* ApplicableClasses > ClassName "IfcTran/COMBINED"
  ~~IfcTran/COMBINED~~ IfcTransformer/COMBINED
* ApplicableTypeValue "IfcTran/COMBINED"
  ~~IfcTran/COMBINED~~ IfcTransformer/COMBINED


Pset_SwitchingDeviceTypeDimmerSwitch.xml
========================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="DimmerType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="DimmerType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_FlowInstrumentTypeCommon.xml
=================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_SensorTypeFlowSensor.xml
=============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="SetPointFlow"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue


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


Pset_AudioVisualApplianceTypePlayer.xml
=======================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="PlayerMediaFormat"] > PropertyType > TypePropertyTableValue
  ~~TypePropertyTableValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="PlayerType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="PlayerMediaFormat"] > PropertyType > TypePropertyTableValue > Expression
  ~~&lt;Expression&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="PlayerType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="PlayerMediaFormat"] > PropertyType > TypePropertyTableValue > DefiningValue
* PropertyDefs > PropertyDef [Name="PlayerMediaFormat"] > PropertyType > TypePropertyTableValue > DefinedValue


Pset_ProtectiveDeviceTypeCommon.xml
===================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_OutsideDesignCriteria.xml
==============================

additions
---------
* PropertyDefs > PropertyDef [Name="PrevailingWindVelocity"] > PropertyType > TypePropertySingleValue > DataType


Pset_DuctSegmentOccurrence.xml
==============================

modifications
-------------
* 
  ~~PSET_OCCURRENCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE


Pset_ProtectiveDeviceBreakerUnitIPICurve.xml
============================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="BreakerUnitIPICurve"] > PropertyType
  ~~PropertyType~~ Definition
* PropertyDefs > PropertyDef [Name="BreakerUnitIPICurve"] > Definition "A curve that establishes the let through peak current of a breaker unit when a particular prospective current is applied.  Note that the breaker unit IPI curve is defined within a Cartesian coordinate system and this fact must be asserted within the property set:

(1) Defining value: A list of minimum 2 and maximum 16 numbers providing the currents in [A] for points in the I/&#206; log/log coordinate space. The curve is drawn as a straight line between two consecutive points.
(2) Defined value: A list of minimum 2 and maximum 16 numbers providing the let-through peak currents, &#206;, in [A] for points in the I/&#206; log/log coordinate space. The curve is drawn as a straight line between two consecutive points."
  ~~Definition~~ PropertyType
* PropertyDefs > PropertyDef [Name="VoltageLevel"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="VoltageLevel"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;



Qto_ChillerBaseQuantities.xml
=============================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Pset_AirTerminalTypeCommon.xml
==============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="AirFlowrateRange"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="AirFlowrateVersusFlowControlElement"] > PropertyType > TypePropertyTableValue
  ~~TypePropertyTableValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="CoreType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
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
* PropertyDefs > PropertyDef [Name="MountingType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Shape"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="TemperatureRange"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Shape"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="FlowControlType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="FaceType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="DischargeDirection"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="MountingType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="CoreType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="FinishType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="FlowPattern"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="AirFlowrateVersusFlowControlElement"] > PropertyType > TypePropertyTableValue > Expression
  ~~&lt;Expression&gt;~~ &lt;DataType&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="AirFlowrateVersusFlowControlElement"] > PropertyType > TypePropertyTableValue > DefiningValue
* PropertyDefs > PropertyDef [Name="AirFlowrateVersusFlowControlElement"] > PropertyType > TypePropertyTableValue > DefinedValue


Pset_CooledBeamPHistory.xml
===========================

modifications
-------------
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="SupplyWaterTemperatureHeating"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="CorrectionFactorForHeating"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="CorrectionFactorForCooling"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="TotalHeatingCapacity"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="HeatingWaterFlowRate"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="BeamHeatingCapacity"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="ReturnWaterTemperatureCooling"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="CoolingWaterFlowRate"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="WaterPressureDropCurves"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="SupplyWaterTemperatureCooling"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="TotalCoolingCapacity"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="ReturnWaterTemperatureHeating"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="BeamCoolingCapacity"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Qto_WallBaseQuantities.xml
==========================

modifications
-------------
* QtoDefs > QtoDef [Name="GrossVolume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetFootprintArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Length"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Width"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossSideArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossFootprintArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Height"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetVolume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetSideArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases



Pset_RailwaySignGeneral.xml
===========================

additions
---------
* Definition
* Applicability

modifications
-------------
* ApplicableTypeValue "IfcSign"
  ~~IfcSign~~ IfcSignType


Pset_UnitaryControlElementPHistory.xml
======================================

modifications
-------------
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="Fan"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Mode"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Temperature"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="SetPoint"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Pset_ProtectiveDeviceBreakerUnitI2TCurve.xml
============================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="BreakerUnitCurve"] > PropertyType > TypePropertyTableValue
  ~~TypePropertyTableValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="VoltageLevel"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="VoltageLevel"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="BreakerUnitCurve"] > PropertyType > TypePropertyTableValue > Expression
  ~~&lt;Expression&gt;~~ &lt;DataType&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="BreakerUnitCurve"] > PropertyType > TypePropertyTableValue > DefiningValue
* PropertyDefs > PropertyDef [Name="BreakerUnitCurve"] > PropertyType > TypePropertyTableValue > DefinedValue


Pset_ElectricalDeviceCommon.xml
===============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="ConductorFunction"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="IK_Code"] > Definition "IK Code according to IEC 62262 (2002) is a numeric classification for the degree of protection provided by enclosures for electrical equipment against external mechanical impacts.
> NOTE&nbsp; In earlier labeling, the third numeral (1..) had been occasionally added to the closely related IP Code on ingress protection, to indicate the level of impact protection."
  ~~IK Code according to IEC 62262 (2002) is a numeric classification for the degree of protection provided by enclosures for electrical equipment against external mechanical impacts.
> NOTE&nbsp; In earlier labeling, the third numeral (1..) had been occasionally added to the closely related IP Code on ingress protection, to indicate the level of impact protection.~~ IK Code according to IEC 62262 (2002) is a numeric classification for the degree of protection provided by enclosures for electrical equipment against external mechanical impacts.
> NOTE&#160; In earlier labeling, the third numeral (1..) had been occasionally added to the closely related IP Code on ingress protection, to indicate the level of impact protection.
* PropertyDefs > PropertyDef [Name="NominalFrequencyRange"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="RatedCurrent"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="RatedVoltage"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="ConductorFunction"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="IK_Code"] > PropertyType


Pset_PumpOccurrence.xml
=======================

modifications
-------------
* PropertyDefs > PropertyDef [Name="BaseType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="DriveConnectionType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* 
  ~~PSET_OCCURRENCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="BaseType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="DriveConnectionType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_EvaporatorTypeCommon.xml
=============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="RefrigerantClass"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="RefrigerantClass"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


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


Pset_SwitchingDeviceTypeEmergencyStop.xml
=========================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="SwitchOperation"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="SwitchOperation"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_TrenchExcavationCommon.xml
===============================

modifications
-------------
* ApplicableClasses > ClassName "IfcEarthworksCut/(.TRENCH.)"
  ~~IfcEarthworksCut/(.TRENCH.)~~ IfcEarthworksCut/TRENCH
* ApplicableTypeValue "IfcEarthworksCut/(.TRENCH.)"
  ~~IfcEarthworksCut/(.TRENCH.)~~ IfcEarthworksCut/TRENCH
* PropertyDefs > PropertyDef [Name="NominalWidth"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="NominalDepth"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


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


Qto_ConstructionEquipmentResourceBaseQuantities.xml
===================================================

modifications
-------------
* QtoDefs > QtoDef [Name="OperatingTime"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="UsageTime"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases


Pset_Risk.xml
=============

modifications
-------------
* Definition "An indication of exposure to mischance, peril, menace, hazard or loss. Documentation of a potential hazard, likilihood and consequence aligned with AS/NZS 4360 and BS PAS 1192-6:2017, which can be assigned to or associated with a product, activity and/or location. Alternatively it may be assigned to an ISO 3864 annotation symbol.

HISTORY: Extended in IFC2x3, Revised IFC4x3 

There are various types of risk that may be encountered and there may be several instances of Pset_Risk associated to an instance or type."
  ~~An indication of exposure to mischance, peril, menace, hazard or loss. Documentation of a potential hazard, likilihood and consequence aligned with AS/NZS 4360 and BS PAS 1192-6:2017, which can be assigned to or associated with a product, activity and/or location. Alternatively it may be assigned to an ISO 3864 annotation symbol.

HISTORY: Extended in IFC2x3, Revised IFC4x3 

There are various types of risk that may be encountered and there may be several instances of Pset_Risk associated to an instance or type.~~ An indication of exposure to mischance, peril, menace, hazard or loss. 
HISTORY:  Extended in IFC2x3
  Refactored in IFC4.3
There are various types of risk that may be encountered and there may be several instances of Pset_Risk associated in an instance of an IfcProcess.
Specification of this property set incorporates the values of the Incom risk analysis matrix (satisfying AS/NZS 4360) together with additional identified requirements including UK PAS 1192-6.
* ApplicableClasses > ClassName "IfcGroup"
  ~~IfcGroup~~ IfcGeotechnicalElement
* ApplicableTypeValue "IfcProcess,IfcTypeProcess,IfcProduct,IfcTypeProduct,IfcGroup"
  ~~IfcProcess,IfcTypeProcess,IfcProduct,IfcTypeProduct,IfcGroup~~ IfcProcess
* PropertyDefs > PropertyDef [Name="AssociatedProduct"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="UnmitigatedRiskLikelihood"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="NatureOfRisk"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="RiskName"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="AssociatedLocation"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="AssociatedActivity"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="RiskAssessmentMethodology"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="MitigatedRiskConsequence"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="UnmitigatedRiskConsequence"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="UnmitigatedRiskSignificance"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="MitigationProposed"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="MitigationPlanned"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="MitigatedRiskLikelihood"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="MitigatedRiskSignificance"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="RiskType"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;

deletions
---------
* ApplicableClasses > ClassName "IfcTypeProcess"
* ApplicableClasses > ClassName "IfcTypeProduct"


Pset_FanTypeCommon.xml
======================

additions
---------
* PropertyDefs > PropertyDef [Name="PressureCurve"]

modifications
-------------
* PropertyDefs > PropertyDef [Name="CapacityControlType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="EfficiencyCurve"] > PropertyType > TypePropertyTableValue
  ~~TypePropertyTableValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="MotorDriveType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="OperationTemperatureRange"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="EfficiencyCurve"] > PropertyType > TypePropertyTableValue > Expression
  ~~&lt;Expression&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="MotorDriveType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="CapacityControlType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="EfficiencyCurve"] > PropertyType > TypePropertyTableValue > DefiningValue
* PropertyDefs > PropertyDef [Name="EfficiencyCurve"] > PropertyType > TypePropertyTableValue > DefinedValue
* PropertyDefs > PropertyDef [Name="PressureCurve"]


Qto_ReinforcingElementBaseQuantities.xml
========================================

modifications
-------------
* QtoDefs > QtoDef [Name="Weight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Count"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Length"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases


Pset_ProtectiveDeviceTrippingUnitTypeElectronic.xml
===================================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="NominalCurrents"] > PropertyType > TypePropertyListValue
  ~~TypePropertyListValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="NominalCurrents"] > PropertyType > TypePropertyListValue > ListValue
  ~~ListValue~~ DataType


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


Pset_RampCommon.xml
===================

modifications
-------------
* PropertyDefs > PropertyDef [Name="LoadBearing"] > PropertyType
  ~~PropertyType~~ Definition
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="ThermalTransmittance"] > PropertyType
  ~~PropertyType~~ Definition
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;



Pset_ElectricMotorTypeCommon.xml
================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;




Pset_FlowInstrumentPHistory.xml
===============================

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


Qto_EvaporativeCoolerBaseQuantities.xml
=======================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Pset_RailwayPowerSupplyFacility.xml
===================================

additions
---------
* Definition


Qto_UnitaryEquipmentBaseQuantities.xml
======================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Pset_FilterPHistory.xml
=======================

modifications
-------------
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="WeightedEfficiency"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="ParticleMassHolding"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="CountedEfficiency"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;



Pset_CableCarrierSegmentTypeCableLadderSegment.xml
==================================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="NominalWidth"] > Definition "The nominal width of the object."
  ~~The nominal width of the object.~~ The nominal width of the segment.
* PropertyDefs > PropertyDef [Name="NominalWidth"] > PropertyType > TypePropertySingleValue > DataType
  ~~IfcNonNegativeLengthMeasure~~ IfcPositiveLengthMeasure


Pset_SpaceHeaterTypeRadiator.xml
================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="RadiatorType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="RadiatorType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Qto_BurnerBaseQuantities.xml
============================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Pset_DoorTypeTurnstile.xml
==========================

additions
---------
* Definition


Qto_StackTerminalBaseQuantities.xml
===================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Qto_DoorBaseQuantities.xml
==========================

modifications
-------------
* QtoDefs > QtoDef [Name="Height"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Width"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Area"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Perimeter"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases



Pset_LampTypeCommon.xml
=======================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Spectrum"] > PropertyType > TypePropertyTableValue
  ~~TypePropertyTableValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Spectrum"] > PropertyType > TypePropertyTableValue > Expression
  ~~&lt;Expression&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
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
* PropertyDefs > PropertyDef [Name="Water"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Steam"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Electricity"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Heat"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Fuel"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Pset_SolarDeviceTypeCommon.xml
==============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
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
* PropertyDefs > PropertyDef [Name="RegeneratedSoundCurve"] > Name "RegeneratedSoundCurve"
  ~~&lt;Name&gt;~~ &lt;Name&gt;
* PropertyDefs > PropertyDef [Name="RegeneratedSoundCurve"] > Definition "Regenerated sound versus air flow rate."
  ~~&lt;Definition&gt;~~ &lt;Definition&gt;
* PropertyDefs > PropertyDef [Name="Orientation"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="BladeEdge"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="RegeneratedSoundCurve"] > PropertyType
  ~~&lt;PropertyType&gt;~~ &lt;PropertyType&gt;
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="BladeShape"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="Operation"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="BladeAction"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="LossCoefficentCurve"]
* PropertyDefs > PropertyDef [Name="LeakageCurve"]


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


Qto_VibrationIsolatorBaseQuantities.xml
=======================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Qto_BoilerBaseQuantities.xml
============================

modifications
-------------
* QtoDefs > QtoDef [Name="TotalSurfaceArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases


Pset_DistributionChamberElementTypeValveChamber.xml
===================================================

deletions
---------
* PropertyDefs > PropertyDef [Name="AccessCoverMaterial"] > PropertyType
* PropertyDefs > PropertyDef [Name="BaseMaterial"] > PropertyType
* PropertyDefs > PropertyDef [Name="WallMaterial"] > PropertyType


Pset_Superelevation.xml
=======================

additions
---------
* ApplicableClasses
* ApplicableClasses

modifications
-------------
* PropertyDefs
  ~~PropertyDefs~~ ApplicableClasses
* ApplicableTypeValue "IfcAnnotation/(.SUPERELEVATIONEVENT.)"
  ~~IfcAnnotation/(.SUPERELEVATIONEVENT.)~~ IfcAnnotation/SUPERELEVATIONEVENT
* ApplicableClasses
  ~~ApplicableClasses~~ PropertyDefs
* ApplicableClasses > ClassName "IfcAnnotation/(.SUPERELEVATIONEVENT.)"
  ~~&lt;ClassName&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Side"]
  ~~&lt;PropertyDef&gt;~~ &lt;ClassName&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="Superelevation"]
* PropertyDefs > PropertyDef [Name="TransitionSuperelevation"]


Pset_AirTerminalPHistory.xml
============================

modifications
-------------
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="AirFlowRate"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="CenterlineAirVelocity"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="SupplyAirTemperatureHeating"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="InductionRatio"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="SupplyAirTemperatureCooling"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="PressureDrop"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="NeckAirVelocity"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Pset_LightFixtureTypeCommon.xml
===============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


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
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="Shape"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_DistributionPortPHistoryCable.xml
======================================

modifications
-------------
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="Voltage"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="PowerFactor"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="DataReceived"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Current"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="DataTransmitted"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="ReactivePower"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="RealPower"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="ApparentPower"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


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



Pset_DistributionPortPHistoryDuct.xml
=====================================

modifications
-------------
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="VolumetricFlowRate"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="MassFlowRate"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="FlowCondition"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Pressure"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="WetBulbTemperature"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Velocity"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Temperature"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


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



Pset_FilterTypeCompressedAirFilter.xml
======================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="ParticleAbsorptionCurve"] > PropertyType > TypePropertyTableValue
  ~~TypePropertyTableValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="ParticleAbsorptionCurve"] > PropertyType > TypePropertyTableValue > Expression
  ~~&lt;Expression&gt;~~ &lt;DataType&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="ParticleAbsorptionCurve"] > PropertyType > TypePropertyTableValue > DefiningValue
* PropertyDefs > PropertyDef [Name="ParticleAbsorptionCurve"] > PropertyType > TypePropertyTableValue > DefinedValue


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


Pset_ElectricApplianceTypeElectricCooker.xml
============================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="ElectricCookerType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="ElectricCookerType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_ElectricGeneratorTypeCommon.xml
====================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
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


Qto_CableFittingBaseQuantities.xml
==================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Pset_FireSuppressionTerminalTypeFireHydrant.xml
===============================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="FireHydrantType"] > Definition "Defines the range of hydrant types from which the required type can be selected where.

DryBarrel:	 A hydrant that has isolating valves fitted below ground and that may be used where the possibility of water freezing is a consideration.
WetBarrel:	 A hydrant that has isolating valves fitted above ground and that may be used where there is no possibility of water freezing."
  ~~Defines the range of hydrant types from which the required type can be selected where.

DryBarrel:	 A hydrant that has isolating valves fitted below ground and that may be used where the possibility of water freezing is a consideration.
WetBarrel:	 A hydrant that has isolating valves fitted above ground and that may be used where there is no possibility of water freezing.~~ Defines the range of hydrant types from which the required type can be selected where.

DryBarrel:\X\09 A hydrant that has isolating valves fitted below ground and that may be used where the possibility of water freezing is a consideration.
WetBarrel:\X\09 A hydrant that has isolating valves fitted above ground and that may be used where there is no possibility of water freezing.


Qto_ColumnBaseQuantities.xml
============================

modifications
-------------
* QtoDefs > QtoDef [Name="GrossVolume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetVolume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetSurfaceArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="OuterSurfaceArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Length"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="CrossSectionArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossSurfaceArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases


Qto_FilterBaseQuantities.xml
============================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Qto_ActuatorBaseQuantities.xml
==============================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Pset_TrafficCalmingDeviceCommon.xml
===================================

modifications
-------------
* ApplicableClasses > ClassName "IfcElementAssembly/(.TRAFFIC_CALMING_DEVICE.)"
  ~~IfcElementAssembly/(.TRAFFIC_CALMING_DEVICE.)~~ IfcElementAssembly/TRAFFIC_CALMING_DEVICE
* ApplicableTypeValue "IfcElementAssembly/(.TRAFFIC_CALMING_DEVICE.)"
  ~~IfcElementAssembly/(.TRAFFIC_CALMING_DEVICE.)~~ IfcElementAssembly/TRAFFIC_CALMING_DEVICE
* PropertyDefs > PropertyDef [Name="TypeDesignation"] > Name "TypeDesignation"
  ~~TypeDesignation~~ Type
* PropertyDefs > PropertyDef [Name="TypeDesignation"] > Definition "Type designator according to local standards"
  ~~Type designator according to local standards~~ Traffic Calming Device designator according to local standards


Pset_DistributionChamberElementTypeMeterChamber.xml
===================================================

deletions
---------
* PropertyDefs > PropertyDef [Name="AccessCoverMaterial"] > PropertyType
* PropertyDefs > PropertyDef [Name="BaseMaterial"] > PropertyType
* PropertyDefs > PropertyDef [Name="WallMaterial"] > PropertyType


Pset_MarkingLinesCommon.xml
===========================

modifications
-------------
* ApplicableClasses > ClassName "IfcSurfaceFeature/(.LINEMARKING.)"
  ~~IfcSurfaceFeature/(.LINEMARKING.)~~ IfcSurfaceFeature/LINEMARKING
* ApplicableTypeValue "IfcSurfaceFeature/(.LINEMARKING.)"
  ~~IfcSurfaceFeature/(.LINEMARKING.)~~ IfcSurfaceFeature/LINEMARKING
* PropertyDefs > PropertyDef [Name="NominalWidth"] > Name "NominalWidth"
  ~~&lt;Name&gt;~~ &lt;Name&gt;
* PropertyDefs > PropertyDef [Name="NominalWidth"] > PropertyType
  ~~&lt;PropertyType&gt;~~ &lt;PropertyType&gt;
* PropertyDefs > PropertyDef [Name="NominalWidth"] > Definition "The nominal width of the object."
  ~~&lt;Definition&gt;~~ &lt;Definition&gt;


Pset_CompressorTypeCommon.xml
=============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="PowerSource"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="RefrigerantClass"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="PowerSource"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="RefrigerantClass"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


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


Pset_CourseCommon.xml
=====================

additions
---------
* ApplicableClasses > ClassName "IfcCourseType"

modifications
-------------
* PropertyDefs > PropertyDef [Name="NominalLength"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="NominalThickness"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="NominalWidth"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


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


Pset_AudioVisualApplianceTypeTuner.xml
======================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="TunerMode"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="TunerFrequency"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="TunerChannel"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="TunerType"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;




Pset_ElectricAppliancePHistory.xml
==================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="PowerState"] > PropertyType > TypePropertyReferenceValue
  ~~TypePropertyReferenceValue~~ TypePropertySingleValue
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE


Pset_ConcreteElementGeneral.xml
===============================

modifications
-------------
* ApplicableTypeValue "IfcBeam,IfcBuildingElementProxy,IfcChimney,IfcColumn,IfcFooting,IfcMember,IfcPile,IfcPlate,IfcRailing,IfcRamp,IfcRampFlight,IfcRoof,IfcSlab,IfcStair,IfcStairFlight,IfcWall,IfcCivilElement"
  ~~IfcBeam,IfcBuildingElementProxy,IfcChimney,IfcColumn,IfcFooting,IfcMember,IfcPile,IfcPlate,IfcRailing,IfcRamp,IfcRampFlight,IfcRoof,IfcSlab,IfcStair,IfcStairFlight,IfcWall,IfcCivilElement~~ IfcSlab


Qto_AirTerminalBoxTypeBaseQuantities.xml
========================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases



Pset_CoveringFlooring.xml
=========================

modifications
-------------
* ApplicableTypeValue "IfcCovering/FLOORING,"
  ~~IfcCovering/FLOORING,~~ IfcCovering/FLOORING

deletions
---------
* ApplicableClasses > ClassName


Pset_DuctSegmentPHistory.xml
============================

modifications
-------------
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="LossCoefficient"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="AtmosphericPressure"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="LeakageCurve"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="FluidFlowLeakage"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Pset_ColumnCommon.xml
=====================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


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


Pset_AudioVisualAppliancePHistory.xml
=====================================

modifications
-------------
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="MediaContent"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="AudioVolume"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="MediaSource"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="PowerState"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Qto_PipeSegmentBaseQuantities.xml
=================================

modifications
-------------
* QtoDefs > QtoDef [Name="GrossWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetCrossSectionArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="OuterSurfaceArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossCrossSectionArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Length"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases


Qto_ArealStratumBaseQuantities.xml
==================================

modifications
-------------
* Definition "Quantity measures associated to areal stratum such as in a geotechnical slice. Uncertainty is documented in _Pset_Uncertainty_."
  ~~Quantity measures associated to areal stratum such as in a geotechnical slice. Uncertainty is documented in _Pset_Uncertainty_.~~ Quantity measures associated to areal stratum such as in a geotechnical slice. Uncertainty is documented in Pset_Uncertainty.
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

additions
---------
* PropertyDefs > PropertyDef [Name="Reference"] > PropertyType > TypePropertySingleValue > DataType

modifications
-------------
* PropertyDefs > PropertyDef [Name="ReinforcementBarType"] > PropertyType > TypePropertyEnumeratedValue > EnumList > EnumItem "NOTDEFINED"
  ~~NOTDEFINED~~ NOTKNOWN

deletions
---------
* PropertyDefs > PropertyDef [Name="ReinforcementBarType"] > PropertyType > TypePropertyEnumeratedValue > EnumList > EnumItem "USERDEFINED"


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


Pset_ChillerPHistory.xml
========================

modifications
-------------
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="Capacity"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="EnergyEfficiencyRatio"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="CoefficientOfPerformance"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


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


Pset_StairFlightCommon.xml
==========================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_SensorTypeSmokeSensor.xml
==============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="SetPointConcentration"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue


Qto_ElectricMotorBaseQuantities.xml
===================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Pset_OnSiteCastKerb.xml
=======================

additions
---------
* ApplicableClasses > ClassName "IfcKerbType"

modifications
-------------
* ApplicableTypeValue "IfcKerb"
  ~~IfcKerb~~ IfcKerbType
* PropertyDefs > PropertyDef [Name="NominalHeight"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="NominalWidth"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;



Pset_PlateCommon.xml
====================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_ControllerTypeTwoPosition.xml
==================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="ControlType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Labels"] > PropertyType > TypePropertyTableValue
  ~~TypePropertyTableValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="ControlType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="Labels"] > PropertyType > TypePropertyTableValue > Expression
  ~~&lt;Expression&gt;~~ &lt;DataType&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="Labels"] > PropertyType > TypePropertyTableValue > DefiningValue
* PropertyDefs > PropertyDef [Name="Labels"] > PropertyType > TypePropertyTableValue > DefinedValue


Pset_PropertyAgreement.xml
==========================

modifications
-------------
* PropertyDefs > PropertyDef [Name="AgreementType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="AgreementType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_DamperTypeControlDamper.xml
================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="TorqueRange"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue


Pset_PrecastConcreteElementFabrication.xml
==========================================

modifications
-------------
* ApplicableTypeValue "IfcBeam,IfcBuildingElementProxy,IfcChimney,IfcColumn,IfcFooting,IfcMember,IfcPile,IfcPlate,IfcRamp,IfcRampFlight,IfcRoof,IfcSlab,IfcStair,IfcStairFlight,IfcWall,IfcCivilElement"
  ~~IfcBeam,IfcBuildingElementProxy,IfcChimney,IfcColumn,IfcFooting,IfcMember,IfcPile,IfcPlate,IfcRamp,IfcRampFlight,IfcRoof,IfcSlab,IfcStair,IfcStairFlight,IfcWall,IfcCivilElement~~ IfcSlab
* PropertyDefs > PropertyDef [Name="AsBuiltLocationNumber"] > Definition "Defines a unique location within a structure, the &#8216;slot&#8217; into which the piece was installed. Where pieces share the same piece mark, they can be interchanged. The value is only known after erection."
  ~~Defines a unique location within a structure, the &#8216;slot&#8217; into which the piece was installed. Where pieces share the same piece mark, they can be interchanged. The value is only known after erection.~~ Defines a unique location within a structure, the \X2\2018\X0\slot\X2\2019\X0\ into which the piece was installed. Where pieces share the same piece mark, they can be interchanged. The value is only known after erection.
* PropertyDefs > PropertyDef [Name="PieceMark"] > Definition "Defines a unique piece for production purposes. All pieces with the same piece mark value are identical and interchangeable. The piece mark may be composed of sub-parts that have specific locally defined meaning (e.g. B-1A may denote a beam, of generic type &#8216;1&#8217; and specific shape &#8216;A&#8217;)."
  ~~Defines a unique piece for production purposes. All pieces with the same piece mark value are identical and interchangeable. The piece mark may be composed of sub-parts that have specific locally defined meaning (e.g. B-1A may denote a beam, of generic type &#8216;1&#8217; and specific shape &#8216;A&#8217;).~~ Defines a unique piece for production purposes. All pieces with the same piece mark value are identical and interchangeable. The piece mark may be composed of sub-parts that have specific locally defined meaning (e.g. B-1A may denote a beam, of generic type \X2\2018\X0\1\X2\2019\X0\ and specific shape \X2\2018\X0\A\X2\2019\X0\).
* PropertyDefs > PropertyDef [Name="TypeDesignation"] > Name "TypeDesignation"
  ~~TypeDesignation~~ TypeDesignator
* PropertyDefs > PropertyDef [Name="TypeDesignation"] > Definition "Type designator according to local standards"
  ~~Type designator according to local standards~~ Type designator for the precast concrete element. The content depends on local standards. For instance in Finland it usually a one-letter acronym, e.g. P=Column, K=reinforced concrete beam,etc.


Pset_CableSegmentTypeConductorSegment.xml
=========================================

additions
---------
* PropertyDefs > PropertyDef [Name="Construction"]

modifications
-------------
* PropertyDefs > PropertyDef [Name="Construction"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Material"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Shape"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="Function"]


Pset_SystemFurnitureElementTypeWorkSurface.xml
==============================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="NominalThickness"] > Definition "The nominal  thickness of the entity."
  ~~The nominal  thickness of the entity.~~ The nominal thickness of the work surface.
* PropertyDefs > PropertyDef [Name="NominalThickness"] > PropertyType > TypePropertySingleValue > DataType
  ~~IfcNonNegativeLengthMeasure~~ IfcPositiveLengthMeasure
* PropertyDefs > PropertyDef [Name="SupportType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="SupportType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_CableSegmentTypeCommon.xml
===============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_SpaceHeaterTypeCommon.xml
==============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="EnergySource"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="HeatTransferDimension"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="PlacementType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="TemperatureClassification"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="PlacementType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="HeatTransferDimension"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="TemperatureClassification"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="EnergySource"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_SpaceOccupancyRequirements.xml
===================================

modifications
-------------
* ApplicableTypeValue "IfcSpace, IfcSpatialZone, IfcZone"
  ~~IfcSpace, IfcSpatialZone, IfcZone~~ IfcSpace

deletions
---------
* ApplicableClasses > ClassName "IfcSpatialZone"
* ApplicableClasses > ClassName "IfcZone"


Pset_DoorWindowGlazingType.xml
==============================

modifications
-------------
* ApplicableTypeValue "IfcDoor, IfcWindow"
  ~~IfcDoor, IfcWindow~~ IfcDoor
* PropertyDefs > PropertyDef [Name="SolarHeatGainTransmittance"] > Definition "(SHGC): The ratio of incident solar radiation that contributes to the heat gain of the interior, it is the solar radiation that directly passes (Tsol or &#964;e) plus the part of the absorbed radiation that is distributed to the interior (qi). The SHGC is refered to also as g-value (g = &#964;e + qi)."
  ~~(SHGC): The ratio of incident solar radiation that contributes to the heat gain of the interior, it is the solar radiation that directly passes (Tsol or &#964;e) plus the part of the absorbed radiation that is distributed to the interior (qi). The SHGC is refered to also as g-value (g = &#964;e + qi).~~ (SHGC): The ratio of incident solar radiation that contributes to the heat gain of the interior, it is the solar radiation that directly passes (Tsol or \X2\03C4\X0\e) plus the part of the absorbed radiation that is distributed to the interior (qi). The SHGC is refered to also as g-value (g = \X2\03C4\X0\e + qi).
* PropertyDefs > PropertyDef [Name="SolarReflectance"] > Definition "(Rsol): The ratio of incident solar radiation that is reflected by a glazing system (also named &#961;e). Note the following equation Asol + Rsol + Tsol = 1"
  ~~(Rsol): The ratio of incident solar radiation that is reflected by a glazing system (also named &#961;e). Note the following equation Asol + Rsol + Tsol = 1~~ (Rsol): The ratio of incident solar radiation that is reflected by a glazing system (also named \X2\03C1\X0\e). Note the following equation Asol + Rsol + Tsol = 1
* PropertyDefs > PropertyDef [Name="SolarTransmittance"] > Definition "(Tsol): The ratio of incident solar radiation that directly passes through a glazing system (also named &#964;e). Note the following equation Asol + Rsol + Tsol = 1"
  ~~(Tsol): The ratio of incident solar radiation that directly passes through a glazing system (also named &#964;e). Note the following equation Asol + Rsol + Tsol = 1~~ (Tsol): The ratio of incident solar radiation that directly passes through a glazing system (also named \X2\03C4\X0\e). Note the following equation Asol + Rsol + Tsol = 1

deletions
---------
* ApplicableClasses > ClassName "IfcWindow"


Pset_CoveringCommon.xml
=======================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_SanitaryTerminalTypeToiletPan.xml
======================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="PanMounting"] > Definition "The property enumeration Pset_SanitaryMountingEnum defines the forms of mounting or fixing of the sanitary terminal that may be specified within property sets used to define sanitary terminals (WC&#8217;s, basins, sinks, etc.) where:-

BackToWall: 	A pedestal mounted sanitary terminal that fits flush to the wall at the rear to cover its service connections.
Pedestal: 	A floor mounted sanitary terminal that has an integral base.
CounterTop: 	A sanitary terminal that is installed into a horizontal surface that is installed into a horizontal surface. Note: When applied to a wash hand basin, the term more normally used is &#8216;vanity&#8217;. See also Wash Hand Basin Type specification.
WallHung: 	A sanitary terminal cantilevered clear of the floor."
  ~~The property enumeration Pset_SanitaryMountingEnum defines the forms of mounting or fixing of the sanitary terminal that may be specified within property sets used to define sanitary terminals (WC&#8217;s, basins, sinks, etc.) where:-

BackToWall: 	A pedestal mounted sanitary terminal that fits flush to the wall at the rear to cover its service connections.
Pedestal: 	A floor mounted sanitary terminal that has an integral base.
CounterTop: 	A sanitary terminal that is installed into a horizontal surface that is installed into a horizontal surface. Note: When applied to a wash hand basin, the term more normally used is &#8216;vanity&#8217;. See also Wash Hand Basin Type specification.
WallHung: 	A sanitary terminal cantilevered clear of the floor.~~ The property enumeration Pset_SanitaryMountingEnum defines the forms of mounting or fixing of the sanitary terminal that may be specified within property sets used to define sanitary terminals (WC\X2\2019\X0\s, basins, sinks, etc.) where:-

BackToWall: \X\09A pedestal mounted sanitary terminal that fits flush to the wall at the rear to cover its service connections.
Pedestal: \X\09A floor mounted sanitary terminal that has an integral base.
CounterTop: \X\09A sanitary terminal that is installed into a horizontal surface that is installed into a horizontal surface. Note: When applied to a wash hand basin, the term more normally used is \X2\2018\X0\vanity\X2\2019\X0\. See also Wash Hand Basin Type specification.
WallHung: \X\09A sanitary terminal cantilevered clear of the floor.
* PropertyDefs > PropertyDef [Name="PanMounting"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="ToiletPanType"] > Definition "The property enumeration Pset_ToiletPanTypeEnum defines the types of toilet pan that may be specified within the property set Pset_Toilet:-

Siphonic: 	Toilet pan in which excrement is removed by siphonage induced by the flushing water.
Squat: 	Toilet pan with an elongated bowl installed with its top edge at or near floor level, so that the user has to squat.
WashDown: 	Toilet pan in which excrement is removed by the momentum of the flushing water.
WashOut: 	A washdown toilet pan in which excrement falls first into a shallow water filled bowl."
  ~~The property enumeration Pset_ToiletPanTypeEnum defines the types of toilet pan that may be specified within the property set Pset_Toilet:-

Siphonic: 	Toilet pan in which excrement is removed by siphonage induced by the flushing water.
Squat: 	Toilet pan with an elongated bowl installed with its top edge at or near floor level, so that the user has to squat.
WashDown: 	Toilet pan in which excrement is removed by the momentum of the flushing water.
WashOut: 	A washdown toilet pan in which excrement falls first into a shallow water filled bowl.~~ The property enumeration Pset_ToiletPanTypeEnum defines the types of toilet pan that may be specified within the property set Pset_Toilet:-

Siphonic: \X\09Toilet pan in which excrement is removed by siphonage induced by the flushing water.
Squat: \X\09Toilet pan with an elongated bowl installed with its top edge at or near floor level, so that the user has to squat.
WashDown: \X\09Toilet pan in which excrement is removed by the momentum of the flushing water.
WashOut: \X\09A washdown toilet pan in which excrement falls first into a shallow water filled bowl.
* PropertyDefs > PropertyDef [Name="ToiletType"] > Definition "Enumeration that defines the types of toilet (water closet) arrangements that may be specified where:-

BedPanWasher: Enclosed soil appliance in which bedpans and urinal bottles are emptied and cleansed.
Chemical: Portable receptacle or soil appliance that receives and retains excrement in either an integral or a separate container, in which it is chemically treated and from which it has to be emptied periodically.
CloseCoupled: 	Toilet suite in which a flushing cistern is connected directly to the water closet pan.
LooseCoupled: 	Toilet arrangement in which a flushing cistern is connected to the water closet pan through a flushing pipe.
SlopHopper: 	Hopper shaped soil appliance with a flushing rim and outlet similar to those of a toilet pan, into which human excrement is emptied for disposal."
  ~~Enumeration that defines the types of toilet (water closet) arrangements that may be specified where:-

BedPanWasher: Enclosed soil appliance in which bedpans and urinal bottles are emptied and cleansed.
Chemical: Portable receptacle or soil appliance that receives and retains excrement in either an integral or a separate container, in which it is chemically treated and from which it has to be emptied periodically.
CloseCoupled: 	Toilet suite in which a flushing cistern is connected directly to the water closet pan.
LooseCoupled: 	Toilet arrangement in which a flushing cistern is connected to the water closet pan through a flushing pipe.
SlopHopper: 	Hopper shaped soil appliance with a flushing rim and outlet similar to those of a toilet pan, into which human excrement is emptied for disposal.~~ Enumeration that defines the types of toilet (water closet) arrangements that may be specified where:-

BedPanWasher: Enclosed soil appliance in which bedpans and urinal bottles are emptied and cleansed.
Chemical: Portable receptacle or soil appliance that receives and retains excrement in either an integral or a separate container, in which it is chemically treated and from which it has to be emptied periodically.
CloseCoupled: \X\09Toilet suite in which a flushing cistern is connected directly to the water closet pan.
LooseCoupled: \X\09Toilet arrangement in which a flushing cistern is connected to the water closet pan through a flushing pipe.
SlopHopper: \X\09Hopper shaped soil appliance with a flushing rim and outlet similar to those of a toilet pan, into which human excrement is emptied for disposal.
* PropertyDefs > PropertyDef [Name="PanMounting"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_EvaporativeCoolerPHistory.xml
==================================

modifications
-------------
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="LatentHeatTransferRate"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="SensibleHeatTransferRate"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="TotalHeatTransferRate"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Effectiveness"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="WaterSumpTemperature"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Pset_AudioVisualApplianceTypeCamera.xml
=======================================

additions
---------
* PropertyDefs > PropertyDef [Name="PanHorizontal"]
* PropertyDefs > PropertyDef [Name="PanTiltZoomPreset"]

modifications
-------------
* PropertyDefs > PropertyDef [Name="PanHorizontal"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="PanTiltZoomPreset"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="CameraType"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="VideoResolutionMode"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Zoom"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="VideoCaptureInterval"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="TiltHorizontal"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="PanVertical"]
* PropertyDefs > PropertyDef [Name="TiltVertical"]


Qto_ElectricApplianceBaseQuantities.xml
=======================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases



Pset_PackingInstructions.xml
============================

deletions
---------
* PropertyDefs > PropertyDef [Name="ContainerMaterial"] > PropertyType
* PropertyDefs > PropertyDef [Name="WrappingMaterial"] > PropertyType


Qto_CoilBaseQuantities.xml
==========================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases



Pset_FanCentrifugal.xml
=======================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Arrangement"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="DirectionOfRotation"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="DischargePosition"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;



Pset_UnitaryEquipmentTypeCommon.xml
===================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Qto_DistributionChamberElementBaseQuantities.xml
================================================

modifications
-------------
* QtoDefs > QtoDef [Name="GrossSurfaceArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossVolume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetVolume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetSurfaceArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases


Qto_CoolingTowerBaseQuantities.xml
==================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Pset_DistributionChamberElementCommon.xml
=========================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Qto_MotorConnectionBaseQuantities.xml
=====================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Pset_OpeningElementCommon.xml
=============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_HumidifierTypeCommon.xml
=============================

additions
---------
* PropertyDefs > PropertyDef [Name="SaturationEfficiencyCurve"]

modifications
-------------
* PropertyDefs > PropertyDef [Name="AirPressureDropCurve"] > PropertyType > TypePropertyTableValue
  ~~TypePropertyTableValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Application"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="InternalControl"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Application"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="AirPressureDropCurve"] > PropertyType > TypePropertyTableValue > Expression
  ~~&lt;Expression&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="InternalControl"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="AirPressureDropCurve"] > PropertyType > TypePropertyTableValue > DefiningValue
* PropertyDefs > PropertyDef [Name="AirPressureDropCurve"] > PropertyType > TypePropertyTableValue > DefinedValue
* PropertyDefs > PropertyDef [Name="SaturationEfficiencyCurve"]


Pset_DamperTypeFireSmokeDamper.xml
==================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="ActuationType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="ClosureRatingEnum"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="ActuationType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="ClosureRatingEnum"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_FurnitureTypeCommon.xml
============================

additions
---------
* PropertyDefs > PropertyDef [Name="IsBuiltIn"] > PropertyType

modifications
-------------
* PropertyDefs > PropertyDef [Name="NominalDepth"] > Definition "Nominal Depth of the object"
  ~~Nominal Depth of the object~~ The nominal depth of the furniture of this type. The size information is provided in addition to the shape representation and the geometric parameters used within. In cases of inconsistency between the geometric parameters and the size properties, provided in the attached property set, the geometric parameters take precedence.
* PropertyDefs > PropertyDef [Name="NominalDepth"] > PropertyType > TypePropertySingleValue > DataType
  ~~IfcNonNegativeLengthMeasure~~ IfcPositiveLengthMeasure
* PropertyDefs > PropertyDef [Name="NominalLength"] > Definition "Nominal length of the object"
  ~~Nominal length of the object~~ The nominal length of the furniture of this type. The size information is provided in addition to the shape representation and the geometric parameters used within. In cases of inconsistency between the geometric parameters and the size properties, provided in the attached property set, the geometric parameters take precedence.
* PropertyDefs > PropertyDef [Name="NominalLength"] > PropertyType > TypePropertySingleValue > DataType
  ~~IfcNonNegativeLengthMeasure~~ IfcPositiveLengthMeasure
* PropertyDefs > PropertyDef [Name="Status"] > Name "Status"
  ~~&lt;Name&gt;~~ &lt;Name&gt;
* PropertyDefs > PropertyDef [Name="Reference"] > Name "Reference"
  ~~&lt;Name&gt;~~ &lt;Name&gt;
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType
  ~~&lt;PropertyType&gt;~~ &lt;Definition&gt;
* PropertyDefs > PropertyDef [Name="Reference"] > PropertyType
  ~~&lt;PropertyType&gt;~~ &lt;Definition&gt;


Pset_CoilTypeHydronic.xml
=========================

modifications
-------------
* PropertyDefs > PropertyDef [Name="FluidPressureRange"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="TotalUACurves"] > Name "TotalUACurves"
  ~~&lt;Name&gt;~~ &lt;Name&gt;
* PropertyDefs > PropertyDef [Name="WaterPressureDropCurve"] > PropertyType
  ~~&lt;PropertyType&gt;~~ &lt;PropertyType&gt;
* PropertyDefs > PropertyDef [Name="TotalUACurves"] > Definition "Total UA curves, UA - air and water velocities, UA = [(C1 \* AirFlowRate\^0.8)\^-1 + (C2 \* WaterFlowRate\^0.8)\^-1]\^-1.  Note: as two variables are used, DefiningValues and DefinedValues are null, and values are stored in IfcTable in the following order: AirFlowRate,WaterFlowRate,UA.  The IfcTable is related to IfcPropertyTableValue using IfcMetric and IfcPropertyConstraintRelationship."
  ~~&lt;Definition&gt;~~ &lt;Definition&gt;
* PropertyDefs > PropertyDef [Name="WaterPressureDropCurve"] > Name "WaterPressureDropCurve"
  ~~&lt;Name&gt;~~ &lt;Name&gt;
* PropertyDefs > PropertyDef [Name="TotalUACurves"] > PropertyType
  ~~&lt;PropertyType&gt;~~ &lt;PropertyType&gt;
* PropertyDefs > PropertyDef [Name="WaterPressureDropCurve"] > Definition "Water pressure drop curve, pressure drop &#8211; flow rate curve, WaterPressureDrop = f(WaterflowRate)."
  ~~&lt;Definition&gt;~~ &lt;Definition&gt;


Pset_CommunicationsApplianceTypeCommon.xml
==========================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_ValveTypeMixing.xml
========================

modifications
-------------
* PropertyDefs > PropertyDef [Name="MixerControl"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="MixerControl"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_ManufacturerTypeInformation.xml
====================================

additions
---------
* PropertyDefs > PropertyDef [Name="PerformanceCertificate"]

modifications
-------------
* PropertyDefs > PropertyDef [Name="AssemblyPlace"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="PerformanceCertificate"] > PropertyType
  ~~&lt;PropertyType&gt;~~ &lt;PropertyType&gt;
* PropertyDefs > PropertyDef [Name="PerformanceCertificate"] > Definition "Manufacturer's performance certificate"
  ~~&lt;Definition&gt;~~ &lt;Definition&gt;
* PropertyDefs > PropertyDef [Name="AssemblyPlace"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="OperationalDocument"] > Definition "Manufacturer's operational document"
  ~~&lt;Definition&gt;~~ &lt;Definition&gt;
* PropertyDefs > PropertyDef [Name="OperationalDocument"] > PropertyType
  ~~&lt;PropertyType&gt;~~ &lt;PropertyType&gt;
* PropertyDefs > PropertyDef [Name="PerformanceCertificate"] > Name "PerformanceCertificate"
  ~~&lt;Name&gt;~~ &lt;Name&gt;
* PropertyDefs > PropertyDef [Name="OperationalDocument"] > Name "OperationalDocument"
  ~~&lt;Name&gt;~~ &lt;Name&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="SafetyDocument"]


Pset_FanOccurrence.xml
======================

modifications
-------------
* PropertyDefs > PropertyDef [Name="ApplicationOfFan"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="CoilPosition"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="DischargeType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="MotorPosition"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* 
  ~~PSET_OCCURRENCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="ApplicationOfFan"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="MotorPosition"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="CoilPosition"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="DischargeType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_ControllerTypeCommon.xml
=============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_PrecastConcreteElementGeneral.xml
======================================

modifications
-------------
* ApplicableTypeValue "IfcBeam,IfcBuildingElementProxy,IfcChimney,IfcColumn,IfcFooting,IfcMember,IfcPile,IfcPlate,IfcRamp,IfcRampFlight,IfcRoof,IfcSlab,IfcStair,IfcStairFlight,IfcWall,IfcCivilElement"
  ~~IfcBeam,IfcBuildingElementProxy,IfcChimney,IfcColumn,IfcFooting,IfcMember,IfcPile,IfcPlate,IfcRamp,IfcRampFlight,IfcRoof,IfcSlab,IfcStair,IfcStairFlight,IfcWall,IfcCivilElement~~ IfcColumn
* PropertyDefs > PropertyDef [Name="DesignLocationNumber"] > Definition "Defines a unique location within a structure, the &#8216;slot&#8217; for which the piece was designed."
  ~~Defines a unique location within a structure, the &#8216;slot&#8217; for which the piece was designed.~~ Defines a unique location within a structure, the \X2\2018\X0\slot\X2\2019\X0\ for which the piece was designed.
* PropertyDefs > PropertyDef [Name="PieceMark"] > Definition "Defines a unique piece for production purposes. All pieces with the same piece mark value are identical and interchangeable. The piece mark may be composed of sub-parts that have specific locally defined meaning (e.g. B-1A may denote a beam, of generic type &#8216;1&#8217; and specific shape &#8216;A&#8217;)."
  ~~Defines a unique piece for production purposes. All pieces with the same piece mark value are identical and interchangeable. The piece mark may be composed of sub-parts that have specific locally defined meaning (e.g. B-1A may denote a beam, of generic type &#8216;1&#8217; and specific shape &#8216;A&#8217;).~~ Defines a unique piece for production purposes. All pieces with the same piece mark value are identical and interchangeable. The piece mark may be composed of sub-parts that have specific locally defined meaning (e.g. B-1A may denote a beam, of generic type \X2\2018\X0\1\X2\2019\X0\ and specific shape \X2\2018\X0\A\X2\2019\X0\).
* PropertyDefs > PropertyDef [Name="Twisting"] > Definition "The angle, in radians, through which the end face of a precast piece is rotated with respect to its starting face, along its longitudinal axis, as a result of non-aligned supports. This measure is also termed the &#8216;warping&#8217; angle."
  ~~The angle, in radians, through which the end face of a precast piece is rotated with respect to its starting face, along its longitudinal axis, as a result of non-aligned supports. This measure is also termed the &#8216;warping&#8217; angle.~~ The angle, in radians, through which the end face of a precast piece is rotated with respect to its starting face, along its longitudinal axis, as a result of non-aligned supports. This measure is also termed the \X2\2018\X0\warping\X2\2019\X0\ angle.
* PropertyDefs > PropertyDef [Name="TypeDesignation"] > Name "TypeDesignation"
  ~~TypeDesignation~~ TypeDesignator
* PropertyDefs > PropertyDef [Name="TypeDesignation"] > Definition "Type designator according to local standards"
  ~~Type designator according to local standards~~ Type designator for the precast concrete element. The content depends on local standards. For instance in Finland it usually a one-letter acronym, e.g. P=Column, K=reinforced concrete beam,etc.

deletions
---------
* PropertyDefs > PropertyDef [Name="SupportDuringTransportDocReference"] > PropertyType


Pset_SensorTypeMovementSensor.xml
=================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="SetPointMovement"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue


Pset_AirToAirHeatRecoveryPHistory.xml
=====================================

modifications
-------------
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="DefrostTemperatureEffectiveness"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="SensibleEffectiveness"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="TotalHeatTransferRate"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="SensibleEffectivenessTable"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="TemperatureEffectiveness"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="TotalEffectiveness"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="LatentHeatTransferRate"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="HumidityEffectiveness"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="SensibleHeatTransferRate"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="AirPressureDropCurves"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="TotalEffectivenessTable"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


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


Pset_SumpBusterCommon.xml
=========================

modifications
-------------
* ApplicableClasses > ClassName "IfcElementAssembly/(.SUMPBUSTER.)"
  ~~IfcElementAssembly/(.SUMPBUSTER.)~~ IfcElementAssembly/SUMPBUSTER
* ApplicableTypeValue "IfcElementAssembly/(.SUMPBUSTER.)"
  ~~IfcElementAssembly/(.SUMPBUSTER.)~~ IfcElementAssembly/SUMPBUSTER
* PropertyDefs > PropertyDef [Name="TypeDesignation"] > Name "TypeDesignation"
  ~~TypeDesignation~~ Type
* PropertyDefs > PropertyDef [Name="TypeDesignation"] > Definition "Type designator according to local standards"
  ~~Type designator according to local standards~~ Sump buster designator according to local standards


Pset_RailingCommon.xml
======================

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
* PropertyDefs > PropertyDef [Name="Quality"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Value"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Direction"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Status"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;




Pset_SensorTypeSoundSensor.xml
==============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="SetPointSound"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue


Pset_ProjectOrderMaintenanceWorkOrder.xml
=========================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="FaultPriorityType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="LocationPriorityType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="MaintenaceType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="FaultPriorityType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="MaintenaceType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="LocationPriorityType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;



Pset_CableCarrierSegmentTypeCommon.xml
======================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_CompressorPHistory.xml
===========================

modifications
-------------
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="CompressionEfficiency"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="CoefficientOfPerformance"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="InputPower"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="FullLoadRatio"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="ShaftPower"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="IsentropicEfficiency"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="LubricantPumpHeatGain"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="FrictionHeatGain"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="CompressorTotalHeatGain"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="CompressorCapacity"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="EnergyEfficiencyRatio"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="MechanicalEfficiency"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="CompressorTotalEfficiency"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="VolumetricEfficiency"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Pset_FireSuppressionTerminalTypeCommon.xml
==========================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;




Pset_UnitaryControlElementTypeIndicatorPanel.xml
================================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Application"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Application"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Qto_RampFlightBaseQuantities.xml
================================

modifications
-------------
* QtoDefs > QtoDef [Name="GrossVolume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Width"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetVolume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Length"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases



Qto_MemberBaseQuantities.xml
============================

modifications
-------------
* QtoDefs > QtoDef [Name="NetVolume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="CrossSectionArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossVolume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossSurfaceArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetSurfaceArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Length"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="OuterSurfaceArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases



Pset_SpaceThermalLoadPHistory.xml
=================================

modifications
-------------
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="RelativeHumidity"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="TotalLatentLoad"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="TotalRadiantLoad"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="AirExchangeRate"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="VentilationIndoorAir"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="People"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="TotalSensibleLoad"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="VentilationOutdoorAir"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="RecirculatedAir"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="EquipmentSensible"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="ExhaustAir"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="InfiltrationSensible"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Lighting"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="DryBulbTemperature"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;



Pset_CableCarrierSegmentTypeCableTraySegment.xml
================================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="NominalWidth"] > Definition "The nominal width of the object."
  ~~The nominal width of the object.~~ The nominal width of the segment.
* PropertyDefs > PropertyDef [Name="NominalWidth"] > PropertyType > TypePropertySingleValue > DataType
  ~~IfcNonNegativeLengthMeasure~~ IfcPositiveLengthMeasure


Pset_MotorConnectionTypeCommon.xml
==================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Qto_CableCarrierFittingBaseQuantities.xml
=========================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Qto_FootingBaseQuantities.xml
=============================

modifications
-------------
* QtoDefs > QtoDef [Name="Height"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetVolume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossVolume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="OuterSurfaceArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossSurfaceArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="CrossSectionArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Width"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Length"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases





Pset_DoorCommon.xml
===================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Qto_ElectricFlowStorageDeviceBaseQuantities.xml
===============================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


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


Pset_DamperPHistory.xml
=======================

modifications
-------------
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="AirFlowRate"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="PressureDrop"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="DamperPosition"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="PressureLossCoefficient"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Leakage"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="BladePositionAngle"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Qto_LinearStratumBaseQuantities.xml
===================================

modifications
-------------
* Definition "Quantity measures associated to a linear stratum such as in a borehole. Uncertainty is documented in _Pset_Uncertainty_."
  ~~Quantity measures associated to a linear stratum such as in a borehole. Uncertainty is documented in _Pset_Uncertainty_.~~ Quantity measures associated to a linear stratum such as in a borehole. Uncertainty is documented in Pset_Uncertainty.
* QtoDefs > QtoDef [Name="Diameter"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Length"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases


Pset_TransportElementElevator.xml
=================================

modifications
-------------
* ApplicableClasses > ClassName "IfcTransportElement/ELEVATOR"
  ~~IfcTransportElement/ELEVATOR~~ ELEVATOR
* ApplicableTypeValue "IfcTransportElement/ELEVATOR"
  ~~IfcTransportElement/ELEVATOR~~ ELEVATOR


Pset_BridgeCommon.xml
=====================

additions
---------
* PropertyDefs

modifications
-------------
* PropertyDefs
  ~~PropertyDefs~~ Definition



Pset_PrecastSlab.xml
====================

additions
---------
* PropertyDefs > PropertyDef [Name="TypeDesignator"]

modifications
-------------
* PropertyDefs > PropertyDef [Name="AngleToFirstAxis"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="ToppingType"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="EdgeDistanceToFirstAxis"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="NominalThickness"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="DistanceBetweenComponentAxes"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="TypeDesignation"]


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


Pset_CurtainWallCommon.xml
==========================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;



Qto_OutletBaseQuantities.xml
============================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Qto_FanBaseQuantities.xml
=========================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Pset_TankTypeCommon.xml
=======================

modifications
-------------
* PropertyDefs > PropertyDef [Name="AccessType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="EndShapeType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="NominalDepth"] > Definition "Nominal Depth of the object"
  ~~Nominal Depth of the object~~ The nominal depth of the tank.

Note: Not required for a horizontal cylindrical tank.
* PropertyDefs > PropertyDef [Name="NominalDepth"] > PropertyType > TypePropertySingleValue > DataType
  ~~IfcNonNegativeLengthMeasure~~ IfcPositiveLengthMeasure
* PropertyDefs > PropertyDef [Name="PatternType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="StorageType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="EndShapeType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="AccessType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="StorageType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="PatternType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


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
WallHung: 	A sanitary terminal cantilevered clear of the floor.~~ Selection of the form of mounting of the sink from the enumerated list of mountings where:-

BackToWall: A pedestal mounted sanitary terminal that fits flush to the wall at the rear to cover its service connections.
Pedestal: \X\09A floor mounted sanitary terminal that has an integral base.
CounterTop: \X\09A sanitary terminal that is installed into a horizontal surface that is installed into a horizontal surface. Note: When applied to a wash hand basin, the term more normally used is \X2\2018\X0\vanity\X2\2019\X0\. See also Wash Hand Basin Type specification.
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
.~~ Selection of the type of sink from the enumerated list of types where:-

Belfast: \X\09Deep sink that has a plain edge and a weir overflow
.
Bucket: \X\09Sink at low level, with protected front edge, that facilitates filling and emptying buckets, usually with a hinged grid on which to stand them.
Cleaners:\X\09 Sink, usually fixed at normal height (900mm), with protected front edge.
Combination_Left:\X\09 Sink with integral drainer on left hand side
.
Combination_Right: Sink with integral drainer on right hand side
.
Combination_Double: \X\09Sink with integral drainer on both sides
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
VegetablePreparation: \X\09Large metal sink, with a standing waste, for washing and preparing vegetables
.
* PropertyDefs > PropertyDef [Name="Mounting"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;



Qto_HumidifierBaseQuantities.xml
================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


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



Qto_FireSuppressionTerminalBaseQuantities.xml
=============================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Pset_DuctSilencerTypeCommon.xml
===============================

modifications
-------------
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


Pset_SpaceHeaterTypeConvector.xml
=================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="ConvectorType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="ConvectorType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_BoilerTypeSteam.xml
========================

additions
---------
* PropertyDefs > PropertyDef [Name="NominalEfficiency"]

modifications
-------------
* PropertyDefs > PropertyDef [Name="HeatOutput"] > PropertyType > TypePropertyTableValue
  ~~TypePropertyTableValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="HeatOutput"] > PropertyType > TypePropertyTableValue > Expression
  ~~&lt;Expression&gt;~~ &lt;DataType&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="HeatOutput"] > PropertyType > TypePropertyTableValue > DefiningValue
* PropertyDefs > PropertyDef [Name="HeatOutput"] > PropertyType > TypePropertyTableValue > DefinedValue
* PropertyDefs > PropertyDef [Name="NominalEfficiency"]


Pset_ProtectiveDeviceTrippingUnitTypeCommon.xml
===============================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;



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


Pset_MedicalDeviceTypeCommon.xml
================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_SensorTypeContactSensor.xml
================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="SetPointContact"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue



Pset_KerbStone.xml
==================

additions
---------
* ApplicableClasses > ClassName "IfcKerbType"
* PropertyDefs > PropertyDef [Name="Height"]

modifications
-------------
* PropertyDefs > PropertyDef [Name="TypeDesignation"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="NominalHeight"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="NominalWidth"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="NominalLength"]


Pset_CooledBeamTypeCommon.xml
=============================

modifications
-------------
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
* PropertyDefs > PropertyDef [Name="IntegratedLightingType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="WaterFlowControlSystemType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="PipeConnection"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Qto_EvaporatorBaseQuantities.xml
================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Pset_ValveTypeCommon.xml
========================

additions
---------
* PropertyDefs > PropertyDef [Name="FlowCoefficient"] > Definition "Flow coefficient (the quantity of fluid that passes through a fully open valve at unit pressure drop), typically expressed as the Kv or Cv value for the valve."

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


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
Tunnel: 	Shower that has a succession of shower heads or spreaders that operate simultaneously along its length.~~ Selection of the type of shower from the enumerated list of types where:-

Drench:  \X\09Shower that rapidly gives a thorough soaking in an emergency.
Individual: \X\09Shower unit that is typically enclosed and is for the use of one person at a time.
Tunnel: \X\09Shower that has a succession of shower heads or spreaders that operate simultaneously along its length.


PSet_ElementKinematics.xml
==========================

additions
---------
* PropertyDefs > PropertyDef [Name="LinearPath"]

modifications
-------------
* Name "Pset_ElementKinematics"
  ~~Pset_ElementKinematics~~ PSet_ElementKinematics
* Definition "Information confirming that the element has cyclic and/or pathed kinematic behaviour. The resulting envelope may be availabe as a 'clearance' shape representation."
  ~~Information confirming that the element has cyclic and/or pathed kinematic behaviour. The resulting envelope may be availabe as a 'clearance' shape representation.~~ Definition from IAI: Information confirming that the element has cyclic and/or pathed kinematic behaviour. The resulting envelope may be availabe as a 'clearance' shape representation.
* ApplicableTypeValue "IfcElement,IfcElementType"
  ~~IfcElement,IfcElementType~~ IfcTransportElementType
* PropertyDefs > PropertyDef [Name="CyclicRange"] > PropertyType > TypePropertySingleValue > DataType
  ~~IfcPlaneAngleMeasure~~ IfcPlanarAngleMeasure
* PropertyDefs > PropertyDef [Name="LinearPath"] > Name "LinearPath"
  ~~&lt;Name&gt;~~ &lt;Name&gt;
* PropertyDefs > PropertyDef [Name="LinearPath"] > PropertyType
  ~~&lt;PropertyType&gt;~~ &lt;PropertyType&gt;
* ApplicableClasses > ClassName "IfcElementType"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* PropertyDefs > PropertyDef [Name="LinearPath"] > Definition "Represents the time:distance table of the kinematic behaviour."
  ~~&lt;Definition&gt;~~ &lt;Definition&gt;
* ApplicableClasses > ClassName "IfcElement"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="CyclicPath"]


Pset_BoundedCourseCommon.xml
============================

additions
---------
* ApplicableClasses > ClassName "IfcCourseType"

modifications
-------------
* ApplicableTypeValue "IfcCourse"
  ~~IfcCourse~~ IfcCourseType


Qto_WindowBaseQuantities.xml
============================

modifications
-------------
* QtoDefs > QtoDef [Name="Height"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Width"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Area"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Perimeter"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases


Pset_StairCommon.xml
====================

modifications
-------------
* PropertyDefs > PropertyDef [Name="LoadBearing"] > PropertyType
  ~~PropertyType~~ Definition
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="ThermalTransmittance"] > PropertyType
  ~~PropertyType~~ Definition
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_SoundAttenuation.xml
=========================

modifications
-------------
* PropertyDefs > PropertyDef [Name="SoundScale"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="SoundPressure"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="SoundFrequency"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;



Qto_PipeFittingBaseQuantities.xml
=================================

modifications
-------------
* QtoDefs > QtoDef [Name="GrossCrossSectionArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="OuterSurfaceArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Length"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetCrossSectionArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases



Pset_SensorTypeRadioactivitySensor.xml
======================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="SetPointRadioactivity"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue


Pset_ProtectiveDeviceOccurrence.xml
===================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="ShortTimei2tFunction"] > Definition "Applying short time i2t function. A flag indicating that the I2t short time function of the device is used. The value should be set to TRUE only if the I2t function &#160;is explicitly selected for the device."
  ~~Applying short time i2t function. A flag indicating that the I2t short time function of the device is used. The value should be set to TRUE only if the I2t function &#160;is explicitly selected for the device.~~ Applying short time i2t function. A flag indicating that the I2t short time function of the device is used. The value should be set to TRUE only if the I2t function \S\ is explicitly selected for the device.
* 
  ~~PSET_OCCURRENCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE


Pset_BurnerTypeCommon.xml
=========================

modifications
-------------
* PropertyDefs > PropertyDef [Name="EnergySource"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="EnergySource"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_DistributionChamberElementTypeManhole.xml
==============================================

deletions
---------
* PropertyDefs > PropertyDef [Name="AccessCoverMaterial"] > PropertyType
* PropertyDefs > PropertyDef [Name="BaseMaterial"] > PropertyType
* PropertyDefs > PropertyDef [Name="WallMaterial"] > PropertyType


Pset_WasteTerminalTypeFloorTrap.xml
===================================

additions
---------
* PropertyDefs > PropertyDef [Name="NominalBodyLength"] > PropertyType > TypePropertySingleValue > DataType
* PropertyDefs > PropertyDef [Name="NominalBodyLength"] > PropertyType > TypePropertySingleValue > DataType

modifications
-------------
* PropertyDefs > PropertyDef [Name="InletPatternType"] > PropertyType > TypePropertyEnumeratedValue > EnumList > EnumItem "NONE"
  ~~NONE~~ OTHER
* PropertyDefs > PropertyDef [Name="TrapType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="TrapType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="CoverMaterial"] > PropertyType


Pset_EvaporativeCoolerTypeCommon.xml
====================================

additions
---------
* PropertyDefs > PropertyDef [Name="EffectivenessTable"]

modifications
-------------
* PropertyDefs > PropertyDef [Name="FlowArrangement"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="OperationTemperatureRange"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="AirPressureDropCurve"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="WaterPressDropCurve"] > PropertyType
  ~~&lt;PropertyType&gt;~~ &lt;PropertyType&gt;
* PropertyDefs > PropertyDef [Name="FlowArrangement"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="WaterPressDropCurve"] > Definition "Water pressure drop as function of water flow rate."
  ~~&lt;Definition&gt;~~ &lt;Definition&gt;
* PropertyDefs > PropertyDef [Name="WaterPressDropCurve"] > Name "WaterPressDropCurve"
  ~~&lt;Name&gt;~~ &lt;Name&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="EffectivenessTable"]


Qto_ProtectiveDeviceBaseQuantities.xml
======================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Pset_ElectricApplianceTypeDishwasher.xml
========================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="DishwasherType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="DishwasherType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_SensorTypeTemperatureSensor.xml
====================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="SetPointTemperature"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue


Pset_CondenserTypeCommon.xml
============================

additions
---------
* PropertyDefs > PropertyDef [Name="InternalRefrigerantVolume"] > Definition "Internal volume of condenser (refrigerant side)."

modifications
-------------
* PropertyDefs > PropertyDef [Name="RefrigerantClass"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="RefrigerantClass"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_ConstructionResource.xml
=============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="ActualCompletion"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="ActualCost"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="ActualWork"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="RemainingWork"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="ScheduleWork"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="RemainingCost"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="ScheduleCost"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="ScheduleCompletion"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Qto_BuildingStoreyBaseQuantities.xml
====================================

modifications
-------------
* QtoDefs > QtoDef [Name="NetVolume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetFloorArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossFloorArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossVolume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetHeigtht"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossHeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossPerimeter"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases



Pset_CableCarrierSegmentTypeConduitSegment.xml
==============================================

additions
---------
* PropertyDefs > PropertyDef [Name="IsUnderground"]

modifications
-------------
* PropertyDefs > PropertyDef [Name="NominalWidth"] > Definition "The nominal width of the object."
  ~~The nominal width of the object.~~ The nominal width of the segment.
* PropertyDefs > PropertyDef [Name="NominalWidth"] > PropertyType > TypePropertySingleValue > DataType
  ~~IfcNonNegativeLengthMeasure~~ IfcPositiveLengthMeasure


Pset_RoofCommon.xml
===================

modifications
-------------
* PropertyDefs > PropertyDef [Name="LoadBearing"] > PropertyType
  ~~PropertyType~~ Definition
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_ManufacturerOccurrence.xml
===============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="AssemblyPlace"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* 
  ~~PSET_OCCURRENCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="AssemblyPlace"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_Uncertainty.xml
====================

additions
---------
* ApplicableClasses > ClassName "IfcAnnotation/ASSUMEDAREA"
* ApplicableClasses > ClassName "IfcGeotechnicalElement"
* ApplicableClasses > ClassName "IfcGeotechnicalAssembly"
* ApplicableClasses > ClassName "IfcAnnotation/ASSUMEDLINE"

modifications
-------------
* ApplicableTypeValue "IfcProduct,IfcTypeProduct"
  ~~IfcProduct,IfcTypeProduct~~ IfcAnnotation/ASSUMEDLINE
* PropertyDefs > PropertyDef [Name="UncertaintyDescription"] > Name "UncertaintyDescription"
  ~~UncertaintyDescription~~ Description
* PropertyDefs > PropertyDef [Name="UncertaintyBasis"] > Name "UncertaintyBasis"
  ~~UncertaintyBasis~~ Basis
* PropertyDefs > PropertyDef [Name="UncertaintyBasis"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* ApplicableClasses > ClassName "IfcTypeProduct"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcProduct"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* PropertyDefs > PropertyDef [Name="UncertaintyBasis"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Qto_AirToAirHeatRecoveryBaseQuantities.xml
==========================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Pset_FanPHistory.xml
====================

modifications
-------------
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="FanRotationSpeed"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="OverallEfficiency"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="ShaftPowerRate"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="DrivePowerLoss"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="FanPowerRate"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="DischargePressureLoss"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="WheelTipSpeed"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="FanEfficiency"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="DischargeVelocity"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Pset_DistributionPortTypeCable.xml
==================================

additions
---------
* PropertyDefs > PropertyDef [Name="ConnectionGender"]
* PropertyDefs > PropertyDef [Name="Current"]

modifications
-------------
* PropertyDefs > PropertyDef [Name="Power"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="ConductorFunction"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Protocols"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="ConnectionType"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Voltage"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="ConnectionGender"]
* PropertyDefs > PropertyDef [Name="Current"]


Pset_CoilOccurrence.xml
=======================

modifications
-------------
* 
  ~~PSET_OCCURRENCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE


Qto_TransformerBaseQuantities.xml
=================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Qto_BeamBaseQuantities.xml
==========================

modifications
-------------
* QtoDefs > QtoDef [Name="OuterSurfaceArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetVolume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossVolume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossSurfaceArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="CrossSectionArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Length"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetSurfaceArea"]
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
* PropertyDefs > PropertyDef [Name="CoolingAirFlowRate"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="VentilationAirFlowRate"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="ExhaustAirFlowRate"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="SpaceRelativeHumidity"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Pset_ProtectiveDeviceBreakerUnitTypeMCB.xml
===========================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="NominalCurrents"] > PropertyType > TypePropertyListValue
  ~~TypePropertyListValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="NominalCurrents"] > PropertyType > TypePropertyListValue > ListValue
  ~~ListValue~~ DataType
* PropertyDefs > PropertyDef [Name="VoltageLevel"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="VoltageLevel"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_SensorTypePressureSensor.xml
=================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="SetPointPressure"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue


Qto_ConstructionMaterialResourceBaseQuantities.xml
==================================================

modifications
-------------
* QtoDefs > QtoDef [Name="NetWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossVolume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetVolume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases


Qto_RoofBaseQuantities.xml
==========================

modifications
-------------
* QtoDefs > QtoDef [Name="GrossArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="ProjectedArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases



Pset_SolidStratumCapacity.xml
=============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="FrictionAngle"] > Definition "Friction angle is the tested inclination angle from horizontal."
  ~~Friction angle is the tested inclination angle from horizontal.~~ Friction Angle is the tested inclination angle from horizontal.


Pset_SensorTypeConductanceSensor.xml
====================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="SetPointConductance"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue


Pset_SensorTypeFrostSensor.xml
==============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="SetPointFrost"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue


Qto_CondenserBaseQuantities.xml
===============================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Qto_DuctSegmentBaseQuantities.xml
=================================

modifications
-------------
* QtoDefs > QtoDef [Name="GrossCrossSectionArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetCrossSectionArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Length"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="OuterSurfaceArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases



Pset_SensorTypeRadiationSensor.xml
==================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="SetPointRadiation"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue


Qto_DistributionBoardBaseQuantities.xml
=======================================

additions
---------
* ApplicableClasses > ClassName "IfcDistributionBoard"

modifications
-------------
* QtoDefs > QtoDef [Name="GrossWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NumberOfCircuits"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases


Qto_SolarDeviceBaseQuantities.xml
=================================

modifications
-------------
* QtoDefs > QtoDef [Name="GrossArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases


Qto_ElectricGeneratorBaseQuantities.xml
=======================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases




Qto_CommunicationsApplianceBaseQuantities.xml
=============================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Qto_ProjectionElementBaseQuantities.xml
=======================================

modifications
-------------
* QtoDefs > QtoDef [Name="Volume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Area"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases


Pset_CooledBeamPHistoryActive.xml
=================================

modifications
-------------
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="Throw"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="AirPressureDropCurves"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="AirFlowRate"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Pset_SensorTypeGasSensor.xml
============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="SetPointConcentration"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue


Pset_SensorTypeHeatSensor.xml
=============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="SetPointTemperature"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue


Pset_WasteTerminalTypeGullyTrap.xml
===================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="BackInletPatternType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="GullyType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="TrapType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="BackInletPatternType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="GullyType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="TrapType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Qto_CooledBeamBaseQuantities.xml
================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Qto_RailingBaseQuantities.xml
=============================

deletions
---------
* QtoDefs > QtoDef [Name="Length"] > NameAliases
* QtoDefs > QtoDef [Name="Length"] > DefinitionAliases
* QtoDefinitionAliases


Pset_SensorTypeIonConcentrationSensor.xml
=========================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="SetPointConcentration"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue


Pset_SanitaryTerminalTypeUrinal.xml
===================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Mounting"] > Definition "Selection of the form of mounting from the enumerated list of mountings where:-

BackToWall =	A pedestal mounted sanitary terminal that fits flush to the wall at the rear to cover its service connections
Pedestal =	A floor mounted sanitary terminal that has an integral base
CounterTop =	A sanitary terminal that is installed into a horizontal surface that is installed into a horizontal surface. Note: When applied to a wash hand basin, the term more normally used is &#8216;vanity&#8217;. See also Wash Hand Basin Type specification.
WallHung =	A sanitary terminal cantilevered clear of the floor
.

Note that BackToWall, Pedestal and WallHung are allowable values for a urinal."
  ~~Selection of the form of mounting from the enumerated list of mountings where:-

BackToWall =	A pedestal mounted sanitary terminal that fits flush to the wall at the rear to cover its service connections
Pedestal =	A floor mounted sanitary terminal that has an integral base
CounterTop =	A sanitary terminal that is installed into a horizontal surface that is installed into a horizontal surface. Note: When applied to a wash hand basin, the term more normally used is &#8216;vanity&#8217;. See also Wash Hand Basin Type specification.
WallHung =	A sanitary terminal cantilevered clear of the floor
.

Note that BackToWall, Pedestal and WallHung are allowable values for a urinal.~~ Selection of the form of mounting from the enumerated list of mountings where:-

BackToWall =\X\09A pedestal mounted sanitary terminal that fits flush to the wall at the rear to cover its service connections
Pedestal =\X\09A floor mounted sanitary terminal that has an integral base
CounterTop =\X\09A sanitary terminal that is installed into a horizontal surface that is installed into a horizontal surface. Note: When applied to a wash hand basin, the term more normally used is \X2\2018\X0\vanity\X2\2019\X0\. See also Wash Hand Basin Type specification.
WallHung =\X\09A sanitary terminal cantilevered clear of the floor
.

Note that BackToWall, Pedestal and WallHung are allowable values for a urinal.
* PropertyDefs > PropertyDef [Name="Mounting"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Mounting"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_FireSuppressionTerminalTypeBreechingInlet.xml
==================================================

additions
---------
* PropertyDefs > PropertyDef [Name="BreechingInletType"] > PropertyType > TypePropertyEnumeratedValue > EnumList > EnumItem "UNSET"

modifications
-------------
* PropertyDefs > PropertyDef [Name="BreechingInletType"] > PropertyType > TypePropertyEnumeratedValue > EnumList > EnumItem "NOTDEFINED"
  ~~NOTDEFINED~~ NOTKNOWN
* PropertyDefs > PropertyDef [Name="CouplingType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="CouplingType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="BreechingInletType"] > PropertyType > TypePropertyEnumeratedValue > EnumList > EnumItem "USERDEFINED"


Pset_DistributionSystemTypeElectrical.xml
=========================================

modifications
-------------
* ApplicableClasses > ClassName "IfcDistributionSystem/ELECTRICAL"
  ~~IfcDistributionSystem/ELECTRICAL~~ IfcDistributionPort/ELECTRICAL
* ApplicableTypeValue "IfcDistributionSystem/ELECTRICAL"
  ~~IfcDistributionSystem/ELECTRICAL~~ IfcDistributionPort/ELECTRICAL
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
&#8226;IT type system, a system having no direct connection between live parts and Earth, the exposed conductive parts of the electrical installation being earthed.~~ For certain purposes of electrical regulations, IEC 60364 defines types of system using type identifiers. Assignment of identifiers depends upon the relationship of the source, and of exposed conductive parts of the installation, to Ground (Earth).   Identifiers that may be assigned through IEC 60364 are: 

\X2\2022\X0\TN type system, a system having one or more points of the source of energy directly earthed, the exposed conductive parts of the installation being connected to that point by protective conductors, 
\X2\2022\X0\TN C type system, a TN type system in which neutral and protective functions are combined in a single conductor throughout the system, 
\X2\2022\X0\TN S type system, a TN type system having separate neutral and protective conductors throughout the system, 
\X2\2022\X0\TN C S type system, a TN type system in which neutral and protective functions are combined in a single conductor in part of the system, 
\X2\2022\X0\TT type system, a system having one point of the source of energy directly earthed, the exposed conductive parts of the installation being connected to earth electrodes electrically independent of the earth electrodes of the source, 
\X2\2022\X0\IT type system, a system having no direct connection between live parts and Earth, the exposed conductive parts of the electrical installation being earthed.
* PropertyDefs > PropertyDef [Name="ElectricalSystemType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="ElectricalSystemCategory"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="ElectricalSystemType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_SpaceThermalLoad.xml
=========================

modifications
-------------
* PropertyDefs > PropertyDef [Name="RelativeHumidity"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="VentilationOutdoorAir"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Lighting"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="VentilationIndoorAir"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="InfiltrationSensible"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="ExhaustAir"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="DryBulbTemperature"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="TotalRadiantLoad"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="People"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="EquipmentSensible"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="TotalSensibleLoad"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="TotalLatentLoad"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="RecirculatedAir"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="AirExchangeRate"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Pset_LightFixtureTypeSecurityLighting.xml
=========================================

additions
---------
* PropertyDefs > PropertyDef [Name="BackupSupplySystem"]

modifications
-------------
* PropertyDefs > PropertyDef [Name="SecurityLightingType"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="PictogramEscapeDirection"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="BackupSupplySystem"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Addressablility"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="SelfTestFunction"]


Pset_ProtectiveDeviceTrippingCurve.xml
======================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="TrippingCurve"] > PropertyType > TypePropertyTableValue
  ~~TypePropertyTableValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="TrippingCurve"] > PropertyType > TypePropertyTableValue > Expression
  ~~&lt;Expression&gt;~~ &lt;DataType&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="TrippingCurve"] > PropertyType > TypePropertyTableValue > DefiningValue
* PropertyDefs > PropertyDef [Name="TrippingCurve"] > PropertyType > TypePropertyTableValue > DefinedValue


Pset_Width.xml
==============

modifications
-------------
* ApplicableClasses > ClassName "IfcAnnotation/(.WIDTHEVENT.)"
  ~~IfcAnnotation/(.WIDTHEVENT.)~~ IfcAnnotation/WIDTHEVENT
* ApplicableTypeValue "IfcAnnotation/(.WIDTHEVENT.)"
  ~~IfcAnnotation/(.WIDTHEVENT.)~~ IfcAnnotation/WIDTHEVENT
* PropertyDefs > PropertyDef [Name="NominalWidth"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Side"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="TransitionWidth"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Pset_ProtectiveDeviceTypeCircuitBreaker.xml
===========================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="PerformanceClasses"] > PropertyType > TypePropertyListValue
  ~~TypePropertyListValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="PerformanceClasses"] > PropertyType > TypePropertyListValue > ListValue
  ~~ListValue~~ DataType
* PropertyDefs > PropertyDef [Name="VoltageLevel"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="VoltageLevel"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_FootingCommon.xml
======================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_CondenserPHistory.xml
==========================

modifications
-------------
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="CompressorCondenserPressureDrop"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="CompressorCondenserHeatGain"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="RefrigerantFoulingResistance"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="WaterFoulingResistance"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="ExteriorHeatTransferCoefficient"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="CondenserMeanVoidFraction"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="LogarithmicMeanTemperatureDifference"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="InteriorHeatTransferCoefficient"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="CondensingTemperature"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="HeatRejectionRate"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="UAcurves"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


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



Qto_WasteTerminalBaseQuantities.xml
===================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Pset_ControllerTypeFloating.xml
===============================

modifications
-------------
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


Pset_EvaporatorPHistory.xml
===========================

modifications
-------------
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="CompressorEvaporatorPressureDrop"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="EvaporatorMeanVoidFraction"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="ExteriorHeatTransferCoefficient"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="InteriorHeatTransferCoefficient"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="RefrigerantFoulingResistance"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="EvaporatingTemperature"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="WaterFoulingResistance"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="HeatRejectionRate"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="LogarithmicMeanTemperatureDifference"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="UAcurves"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="CompressorEvaporatorHeatGain"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Qto_ControllerBaseQuantities.xml
================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Pset_BoreholeCommon.xml
=======================

modifications
-------------
* Definition "Properties describing the features of a borehole (If not modelled separately)."
  ~~Properties describing the features of a borehole (If not modelled separately).~~ Properties describing the features of a borehole (if not modelled separately).



Pset_SpaceFireSafetyRequirements.xml
====================================

modifications
-------------
* ApplicableTypeValue "IfcSpace, IfcSpatialZone, IfcZone"
  ~~IfcSpace, IfcSpatialZone, IfcZone~~ IfcSpace

deletions
---------
* ApplicableClasses > ClassName "IfcSpatialZone"
* ApplicableClasses > ClassName "IfcZone"





Pset_TransitionSectionCommon.xml
================================

additions
---------
* ApplicableTypeValue "IfcEarthworksFill/TRANSITIONSECTION"

modifications
-------------
* PropertyDefs
  ~~PropertyDefs~~ Definition
* ApplicableClasses > ClassName "IfcEarthworksFill/(.TRANSITIONSECTION.)"
  ~~IfcEarthworksFill/(.TRANSITIONSECTION.)~~ IfcEarthworksFill/TRANSITIONSECTION
* ApplicableTypeValue "IfcEarthworksFill/(.TRANSITIONSECTION.)"
  ~~ApplicableTypeValue~~ PropertyDefs

deletions
---------
* Definition "Properties for a transition section."


Pset_BoilerTypeCommon.xml
=========================

modifications
-------------
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
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="EnergySource"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="PartialLoadEfficiencyCurves"] > PropertyType > TypePropertyTableValue > Expression
  ~~&lt;Expression&gt;~~ &lt;DataType&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="PartialLoadEfficiencyCurves"] > PropertyType > TypePropertyTableValue > DefiningValue
* PropertyDefs > PropertyDef [Name="PartialLoadEfficiencyCurves"] > PropertyType > TypePropertyTableValue > DefinedValue


Pset_DuctFittingOccurrence.xml
==============================

modifications
-------------
* 
  ~~PSET_OCCURRENCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE


Pset_SystemFurnitureElementTypeCommon.xml
=========================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="NominalWidth"] > Definition "The nominal width of the object."
  ~~The nominal width of the object.~~ The nominal width of the system furniture elements of this type. The size information is provided in addition to the shape representation and the geometric parameters used within. In cases of inconsistency between the geometric parameters and the size properties, provided in the attached property set, the geometric parameters take precedence.
* PropertyDefs > PropertyDef [Name="NominalWidth"] > PropertyType > TypePropertySingleValue > DataType
  ~~IfcNonNegativeLengthMeasure~~ IfcPositiveLengthMeasure


Pset_WasteTerminalTypeWasteTrap.xml
===================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="WasteTrapType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="WasteTrapType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_SolidStratumComposition.xml
================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="CompositeFractions"] > Definition "Denomination into soil groups by composite fractions"
  ~~Denomination into soil groups by composite fractions~~ Denomination into soil groups by composite fractions.
* PropertyDefs > PropertyDef [Name="CompositeFractions"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="CompositeFractions"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_RoadMarkingCommon.xml
==========================

modifications
-------------
* ApplicableTypeValue "IfcSurfaceFeature/(.HATCHMARKING.),IfcSurfaceFeature/(.LINEMARKING.),IfcSurfaceFeature/(.PAVEMENTSURFACEMARKING.),IfcSurfaceFeature/(.SYMBOLMARKING.)"
  ~~IfcSurfaceFeature/(.HATCHMARKING.),IfcSurfaceFeature/(.LINEMARKING.),IfcSurfaceFeature/(.PAVEMENTSURFACEMARKING.),IfcSurfaceFeature/(.SYMBOLMARKING.)~~ IfcSurfaceFeature/SYMBOLMARKING
* ApplicableClasses > ClassName "IfcSurfaceFeature/(.PAVEMENTSURFACEMARKING.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcSurfaceFeature/(.LINEMARKING.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcSurfaceFeature/(.HATCHMARKING.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcSurfaceFeature/(.SYMBOLMARKING.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="MaterialColour"] > PropertyType


Qto_DamperBaseQuantities.xml
============================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Qto_AudioVisualApplianceBaseQuantities.xml
==========================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Pset_SwitchingDeviceTypeMomentarySwitch.xml
===========================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="MomentaryType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="MomentaryType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_BeamCommon.xml
===================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_FlowMeterTypeWaterMeter.xml
================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Type"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Type"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="BackflowPreventerType"] > PropertyType > TypePropertyEnumeratedValue > EnumList > EnumItem "NONE"


Pset_ProtectiveDeviceBreakerUnitTypeMotorProtection.xml
=======================================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="PerformanceClasses"] > PropertyType > TypePropertyListValue
  ~~TypePropertyListValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="PerformanceClasses"] > PropertyType > TypePropertyListValue > ListValue
  ~~ListValue~~ DataType
* PropertyDefs > PropertyDef [Name="VoltageLevel"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="VoltageLevel"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;



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



Pset_AirSideSystemInformation.xml
=================================

modifications
-------------
* ApplicableTypeValue "IfcSpace,IfcZone,IfcSpatialZone"
  ~~IfcSpace,IfcZone,IfcSpatialZone~~ IfcZone


Pset_RailwayAlignmentCommon.xml
===============================

additions
---------
* Definition

modifications
-------------
* PropertyDefs > PropertyDef [Name="VerticalReferenceAxis"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="CantRotationAxis"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Pset_BoilerTypeWater.xml
========================

modifications
-------------
* PropertyDefs > PropertyDef [Name="NominalEfficiency"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="HeatOutput"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Pset_TransportElementCommon.xml
===============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_SanitaryTerminalTypeCistern.xml
====================================

modifications
-------------
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
Sensor: Flush is activated through an automatic sensing mechanism.~~ The property enumeration Pset_FlushTypeEnum defines the types of flushing mechanism that may be specified for cisterns and sanitary terminals where:-

Lever: \X\09Flushing is achieved by twisting a lever that causes a predetermined flow of water to be passed from a cistern to the sanitary terminal.
Pull: \X\09Flushing is achieved by pulling a handle or knob vertically upwards that causes a predetermined flow of water to be passed from a cistern to the sanitary terminal.
Push: \X\09Flushing is achieved by pushing a button or plate that causes a predetermined flow of water to be passed from a cistern to the sanitary terminal.
Sensor: Flush is activated through an automatic sensing mechanism.

deletions
---------
* PropertyDefs > PropertyDef [Name="CisternHeight"] > PropertyType > TypePropertyEnumeratedValue > EnumList > EnumItem "NONE"


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


Pset_InterceptorTypeCommon.xml
==============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_SanitaryTerminalTypeSanitaryFountain.xml
=============================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="FountainType"] > Definition "Selection of the type of fountain from the enumerated list of types where:-

DrinkingWater: 	Sanitary appliance that provides a low pressure jet of drinking water.
Eyewash: 	Waste water appliance, usually installed in work places where there is a risk of injury to eyes by solid particles or dangerous liquids, with which the user can wash the eyes without touching them."
  ~~Selection of the type of fountain from the enumerated list of types where:-

DrinkingWater: 	Sanitary appliance that provides a low pressure jet of drinking water.
Eyewash: 	Waste water appliance, usually installed in work places where there is a risk of injury to eyes by solid particles or dangerous liquids, with which the user can wash the eyes without touching them.~~ Selection of the type of fountain from the enumerated list of types where:-

DrinkingWater: \X\09Sanitary appliance that provides a low pressure jet of drinking water.
Eyewash: \X\09Waste water appliance, usually installed in work places where there is a risk of injury to eyes by solid particles or dangerous liquids, with which the user can wash the eyes without touching them.
* PropertyDefs > PropertyDef [Name="Mounting"] > Definition "Selection of the form of mounting of the fountain from the enumerated list of mountings where:-

BackToWall: 	A pedestal mounted sanitary terminal that fits flush to the wall at the rear to cover its service connections.
Pedestal: 	A floor mounted sanitary terminal that has an integral base
.
CounterTop: 	A sanitary terminal that is installed into a horizontal surface that is installed into a horizontal surface. Note: When applied to a wash hand basin, the term more normally used is &#8216;vanity&#8217;. See also Wash Hand Basin Type specification.
WallHung: 	A sanitary terminal cantilevered clear of the floor."
  ~~Selection of the form of mounting of the fountain from the enumerated list of mountings where:-

BackToWall: 	A pedestal mounted sanitary terminal that fits flush to the wall at the rear to cover its service connections.
Pedestal: 	A floor mounted sanitary terminal that has an integral base
.
CounterTop: 	A sanitary terminal that is installed into a horizontal surface that is installed into a horizontal surface. Note: When applied to a wash hand basin, the term more normally used is &#8216;vanity&#8217;. See also Wash Hand Basin Type specification.
WallHung: 	A sanitary terminal cantilevered clear of the floor.~~ Selection of the form of mounting of the fountain from the enumerated list of mountings where:-

BackToWall: \X\09A pedestal mounted sanitary terminal that fits flush to the wall at the rear to cover its service connections.
Pedestal: \X\09A floor mounted sanitary terminal that has an integral base
.
CounterTop: \X\09A sanitary terminal that is installed into a horizontal surface that is installed into a horizontal surface. Note: When applied to a wash hand basin, the term more normally used is \X2\2018\X0\vanity\X2\2019\X0\. See also Wash Hand Basin Type specification.
WallHung: \X\09A sanitary terminal cantilevered clear of the floor.
* PropertyDefs > PropertyDef [Name="Mounting"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Mounting"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Qto_SwitchingDeviceBaseQuantities.xml
=====================================

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



Pset_PipeFittingTypeJunction.xml
================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="JunctionType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="JunctionType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_BoilerPHistory.xml
=======================

modifications
-------------
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="PartLoadRatio"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="CombustionTemperature"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="WorkingPressure"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="PrimaryEnergyConsumption"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="CombustionEfficiency"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="EnergySourceConsumption"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Load"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="AuxiliaryEnergyConsumption"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="OperationalEfficiency"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Pset_SensorTypeIdentifierSensor.xml
===================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="SetPointIdentifier"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue


Pset_ServiceLife.xml
====================

modifications
-------------
* PropertyDefs > PropertyDef [Name="ServiceLifeDuration"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue


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


Pset_AirTerminalBoxPHistory.xml
===============================

modifications
-------------
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="Sound"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="AirflowCurve"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="AtmosphericPressure"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="DamperPosition"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Pset_CableSegmentTypeCableSegment.xml
=====================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="RatedTemperature"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="RatedVoltage"] > PropertyType > TypePropertyBoundedValue
  ~~TypePropertyBoundedValue~~ TypePropertySingleValue



Pset_CoilPHistory.xml
=====================

modifications
-------------
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="AtmosphericPressure"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="FaceVelocity"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="SoundCurve"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="AirPressureDropCurve"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


Pset_WasteTerminalTypeGullySump.xml
===================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="BackInletPatternType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="GullyType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="TrapType"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="TrapType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="BackInletPatternType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;
* PropertyDefs > PropertyDef [Name="GullyType"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_AnnotationSurveyArea.xml
=============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="AcquisitionMethod"] > PropertyType > TypePropertyEnumeratedValue > EnumList > EnumItem "USERDEFINED"
  ~~USERDEFINED~~ OTHER



Qto_SlabBaseQuantities.xml
==========================

modifications
-------------
* QtoDefs > QtoDef [Name="Width"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossVolume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Depth"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetVolume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Perimeter"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Length"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases


Pset_TubeBundleTypeCommon.xml
=============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_CableCarrierFittingTypeCommon.xml
======================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_RampFlightCommon.xml
=========================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Qto_SanitaryTerminalBaseQuantities.xml
======================================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Qto_LampBaseQuantities.xml
==========================

deletions
---------
* QtoDefs > QtoDef [Name="GrossWeight"] > NameAliases
* QtoDefs > QtoDef [Name="GrossWeight"] > DefinitionAliases
* QtoDefinitionAliases


Pset_WasteTerminalTypeWasteDisposalUnit.xml
===========================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="NominalDepth"] > Definition "Nominal Depth of the object"
  ~~Nominal Depth of the object~~ Nominal or quoted depth of the object measured from the inlet drain connection to the base of the unit.
* PropertyDefs > PropertyDef [Name="NominalDepth"] > PropertyType > TypePropertySingleValue > DataType
  ~~IfcNonNegativeLengthMeasure~~ IfcPositiveLengthMeasure


Qto_PileBaseQuantities.xml
==========================

modifications
-------------
* QtoDefs > QtoDef [Name="NetWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="CrossSectionArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Length"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossSurfaceArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="NetVolume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="OuterSurfaceArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossVolume"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases


Qto_DuctFittingBaseQuantities.xml
=================================

modifications
-------------
* QtoDefs > QtoDef [Name="NetCrossSectionArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossCrossSectionArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="GrossWeight"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="Length"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;
* QtoDefs > QtoDef [Name="OuterSurfaceArea"]
  ~~&lt;QtoDef&gt;~~ &lt;QtoDef&gt;

deletions
---------
* QtoDefinitionAliases


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



Pset_SlabCommon.xml
===================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue
  ~~TypePropertyEnumeratedValue~~ TypePropertySingleValue
* PropertyDefs > PropertyDef [Name="Status"] > PropertyType > TypePropertyEnumeratedValue > EnumList
  ~~&lt;EnumList&gt;~~ &lt;DataType&gt;


Pset_OutletTypeCommunication.xml
================================

additions
---------
* Definition

modifications
-------------
* ApplicableClasses > ClassName "IfcOutl/COMMUNICATIONSOUTLET"
  ~~IfcOutl/COMMUNICATIONSOUTLET~~ IfcOutlet/COMMUNICATIONSOUTLET
* ApplicableTypeValue "IfcOutl/COMMUNICATIONSOUTLET"
  ~~IfcOutl/COMMUNICATIONSOUTLET~~ IfcOutlet/COMMUNICATIONSOUTLET


Pset_ValvePHistory.xml
======================

modifications
-------------
* 
  ~~PSET_PERFORMANCEDRIVEN~~ PSET_TYPEDRIVENOVERRIDE
* PropertyDefs > PropertyDef [Name="MeasuredPressureDrop"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="PercentageOpen"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="MeasuredFlowRate"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;


