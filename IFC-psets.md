
Missing in output
=================
* Pset_CoveringCeiling.xml

Missing in reference
=================
* Pset_Tiling.xml



Pset_TrenchExcavationCommon.xml
===============================

modifications
-------------
* ApplicableClasses > ClassName "IfcEarthworksCut/(.TRENCH.)"
  ~~IfcEarthworksCut/(.TRENCH.)~~ IfcEarthworksCut/TRENCH
* ApplicableTypeValue "IfcEarthworksCut/(.TRENCH.)"
  ~~IfcEarthworksCut/(.TRENCH.)~~ IfcEarthworksCut/TRENCH


























Pset_SumpBusterCommon.xml
=========================

modifications
-------------
* ApplicableClasses > ClassName "IfcElementAssembly/(.SUMPBUSTER.)"
  ~~IfcElementAssembly/(.SUMPBUSTER.)~~ IfcElementAssembly/SUMPBUSTER
* ApplicableTypeValue "IfcElementAssembly/(.SUMPBUSTER.)"
  ~~IfcElementAssembly/(.SUMPBUSTER.)~~ IfcElementAssembly/SUMPBUSTER








Pset_ConcreteElementGeneral.xml
===============================

modifications
-------------
* ApplicableTypeValue "IfcBeam,IfcBuildingElementProxy,IfcChimney,IfcColumn,IfcFooting,IfcMember,IfcPile,IfcPlate,IfcRailing,IfcRamp,IfcRampFlight,IfcRoof,IfcSlab,IfcStair,IfcStairFlight,IfcWall,IfcCivilElement"
  ~~IfcBeam,IfcBuildingElementProxy,IfcChimney,IfcColumn,IfcFooting,IfcMember,IfcPile,IfcPlate,IfcRailing,IfcRamp,IfcRampFlight,IfcRoof,IfcSlab,IfcStair,IfcStairFlight,IfcWall,IfcCivilElement~~ IfcBeam,IfcBuildingElementProxy,IfcChimney,IfcCivilElement,IfcColumn,IfcFooting,IfcMember,IfcPile,IfcPlate,IfcRailing,IfcRampFlight,IfcRamp,IfcRoof,IfcSlab,IfcStairFlight,IfcStair,IfcWall
























Pset_CivilElementCommon.xml
===========================

additions
---------
* ApplicableTypeValue

deletions
---------
* PropertyDefs > PropertyDef [Name="Reference"]


Pset_LinearReferencingMethod.xml
================================

modifications
-------------
* ApplicableClasses > ClassName "IfcReferent/(.POSITION.)"
  ~~IfcReferent/(.POSITION.)~~ IfcReferent/POSITION
* ApplicableTypeValue "IfcAlignment,IfcReferent/(.POSITION.)"
  ~~IfcAlignment,IfcReferent/(.POSITION.)~~ IfcAlignment,IfcReferent/POSITION










Pset_MaterialSteel.xml
======================

modifications
-------------
* ApplicableClasses > ClassName "IfcMaterial/Steel"
  ~~IfcMaterial/Steel~~ IfcMaterial
* ApplicableTypeValue "IfcMaterial/Steel"
  ~~IfcMaterial/Steel~~ IfcMaterial




Qto_SignalBaseQuantities.xml
============================

additions
---------
* ApplicableTypeValue



Pset_RoadGuardElement.xml
=========================

modifications
-------------
* ApplicableTypeValue "IfcRailing/(.GUARDRAIL.),IfcWall/(.PARAPET.)"
  ~~IfcRailing/(.GUARDRAIL.),IfcWall/(.PARAPET.)~~ IfcRailing/GUARDRAIL,IfcWall/PARAPET
* ApplicableClasses > ClassName "IfcWall/(.PARAPET.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcRailing/(.GUARDRAIL.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;


Pset_Width.xml
==============

modifications
-------------
* ApplicableClasses > ClassName "IfcAnnotation/(.WIDTHEVENT.)"
  ~~IfcAnnotation/(.WIDTHEVENT.)~~ IfcAnnotation/WIDTHEVENT
* ApplicableTypeValue "IfcAnnotation/(.WIDTHEVENT.)"
  ~~IfcAnnotation/(.WIDTHEVENT.)~~ IfcAnnotation/WIDTHEVENT




Pset_DiscreteAccessoryFixingSocket.xml
======================================

modifications
-------------
* ApplicableClasses > ClassName "IfcDiscreteAccessory/Fixing socket"
  ~~IfcDiscreteAccessory/Fixing socket~~ IfcDiscreteAccessory
* ApplicableTypeValue "IfcDiscreteAccessory/Fixing socket"
  ~~IfcDiscreteAccessory/Fixing socket~~ IfcDiscreteAccessory


Pset_TrafficCalmingDeviceCommon.xml
===================================

modifications
-------------
* ApplicableClasses > ClassName "IfcElementAssembly/(.TRAFFIC_CALMING_DEVICE.)"
  ~~IfcElementAssembly/(.TRAFFIC_CALMING_DEVICE.)~~ IfcElementAssembly/TRAFFIC_CALMING_DEVICE
* ApplicableTypeValue "IfcElementAssembly/(.TRAFFIC_CALMING_DEVICE.)"
  ~~IfcElementAssembly/(.TRAFFIC_CALMING_DEVICE.)~~ IfcElementAssembly/TRAFFIC_CALMING_DEVICE












Pset_MarineVehicleDesignCriteria.xml
====================================

modifications
-------------
* ApplicableTypeValue "IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.)"
  ~~IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.)~~ IfcTransportElement/VEHICLEMARINE,IfcTransportElement/VEHICLEMARINE
* ApplicableClasses > ClassName "IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;

deletions
---------
* ApplicableClasses > ClassName "IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.)"





Pset_RoadDesignCriteriaCommon.xml
=================================

additions
---------
* ApplicableClasses > ClassName "IfcFacilityPart/JUNCTION"

modifications
-------------
* ApplicableTypeValue "IfcRoad,IfcFacilityPart/IfcRoadPartTypeEnum(.ROADSEGMENT.),IfcFacilityPart/IfcFacilityPartCommonTypeEnum(.SEGMENT.),IfcFacilityPart/IfcFacilityPartCommonTypeEnum(.JUNCTION.),IfcFacilityPart/IfcFacilityPartCommonTypeEnum(.LEVELCROSSING.),IfcFacilityPart/IfcRoadPartTypeEnum(.RAILWAYCROSSING.),IfcFacilityPart/IfcRoadPartTypeEnum(.PEDESTRIAN_CROSSING.),IfcFacilityPart/IfcRoadPartTypeEnum(.BICYCLECROSSING.),IfcFacilityPart/IfcRoadPartTypeEnum(.ROUNDABOUT.),IfcFacilityPart/IfcRoadPartTypeEnum(.INTERSECTION.),IfcFacilityPart/IfcRoadPartTypeEnum(.TOLLPLAZA.)"
  ~~IfcRoad,IfcFacilityPart/IfcRoadPartTypeEnum(.ROADSEGMENT.),IfcFacilityPart/IfcFacilityPartCommonTypeEnum(.SEGMENT.),IfcFacilityPart/IfcFacilityPartCommonTypeEnum(.JUNCTION.),IfcFacilityPart/IfcFacilityPartCommonTypeEnum(.LEVELCROSSING.),IfcFacilityPart/IfcRoadPartTypeEnum(.RAILWAYCROSSING.),IfcFacilityPart/IfcRoadPartTypeEnum(.PEDESTRIAN_CROSSING.),IfcFacilityPart/IfcRoadPartTypeEnum(.BICYCLECROSSING.),IfcFacilityPart/IfcRoadPartTypeEnum(.ROUNDABOUT.),IfcFacilityPart/IfcRoadPartTypeEnum(.INTERSECTION.),IfcFacilityPart/IfcRoadPartTypeEnum(.TOLLPLAZA.)~~ IfcFacilityPart/JUNCTION,IfcFacilityPart/LEVELCROSSING,IfcFacilityPart/SEGMENT,IfcFacilityPart/BICYCLECROSSING,IfcFacilityPart/INTERSECTION,IfcFacilityPart/PEDESTRIAN_CROSSING,IfcFacilityPart/RAILWAYCROSSING,IfcFacilityPart/ROADSEGMENT,IfcFacilityPart/ROUNDABOUT,IfcFacilityPart/TOLLPLAZA,IfcRoad
* ApplicableClasses > ClassName "IfcFacilityPart/IfcFacilityPartCommonTypeEnum(.SEGMENT.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcFacilityPart/IfcRoadPartTypeEnum(.BICYCLECROSSING.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcFacilityPart/IfcFacilityPartCommonTypeEnum(.LEVELCROSSING.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcFacilityPart/IfcRoadPartTypeEnum(.RAILWAYCROSSING.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcFacilityPart/IfcRoadPartTypeEnum(.ROUNDABOUT.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcFacilityPart/IfcFacilityPartCommonTypeEnum(.JUNCTION.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcFacilityPart/IfcRoadPartTypeEnum(.INTERSECTION.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcFacilityPart/IfcRoadPartTypeEnum(.PEDESTRIAN_CROSSING.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcFacilityPart/IfcRoadPartTypeEnum(.ROADSEGMENT.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;

deletions
---------
* ApplicableClasses > ClassName "IfcFacilityPart/IfcRoadPartTypeEnum(.TOLLPLAZA.)"






















Pset_AnnotationLineOfSight.xml
==============================

modifications
-------------
* ApplicableClasses > ClassName "IfcAnnotation/LineOfSight"
  ~~IfcAnnotation/LineOfSight~~ IfcAnnotation
* ApplicableTypeValue "IfcAnnotation/LineOfSight"
  ~~IfcAnnotation/LineOfSight~~ IfcAnnotation







Pset_TankTypeSectional.xml
==========================

modifications
-------------
* ApplicableClasses > ClassName "IfcTank/SECTIONAL"
  ~~IfcTank/SECTIONAL~~ IfcTank
* ApplicableTypeValue "IfcTank/SECTIONAL"
  ~~IfcTank/SECTIONAL~~ IfcTank












Pset_PavementMillingCommon.xml
==============================

modifications
-------------
* ApplicableClasses > ClassName "IfcEarthworksCut/(.PAVEMENTMILLING.)"
  ~~IfcEarthworksCut/(.PAVEMENTMILLING.)~~ IfcEarthworksCut/PAVEMENTMILLING
* ApplicableTypeValue "IfcEarthworksCut/(.PAVEMENTMILLING.)"
  ~~IfcEarthworksCut/(.PAVEMENTMILLING.)~~ IfcEarthworksCut/PAVEMENTMILLING














Pset_MaterialConcrete.xml
=========================

modifications
-------------
* ApplicableClasses > ClassName "IfcMaterial/Concrete"
  ~~IfcMaterial/Concrete~~ IfcMaterial
* ApplicableTypeValue "IfcMaterial/Concrete"
  ~~IfcMaterial/Concrete~~ IfcMaterial










Pset_StairCommon.xml
====================

deletions
---------
* PropertyDefs > PropertyDef [Name="ThermalTransmittance"]
* PropertyDefs > PropertyDef [Name="LoadBearing"]



















Pset_Superelevation.xml
=======================

modifications
-------------
* ApplicableClasses > ClassName "IfcAnnotation/(.SUPERELEVATIONEVENT.)"
  ~~IfcAnnotation/(.SUPERELEVATIONEVENT.)~~ IfcAnnotation/SUPERELEVATIONEVENT
* ApplicableTypeValue "IfcAnnotation/(.SUPERELEVATIONEVENT.)"
  ~~IfcAnnotation/(.SUPERELEVATIONEVENT.)~~ IfcAnnotation/SUPERELEVATIONEVENT










Pset_DiscreteAccessoryLadderTrussConnector.xml
==============================================

modifications
-------------
* ApplicableClasses > ClassName "IfcDiscreteAccessory/Ladder truss connector"
  ~~IfcDiscreteAccessory/Ladder truss connector~~ IfcDiscreteAccessory
* ApplicableTypeValue "IfcDiscreteAccessory/Ladder truss connector"
  ~~IfcDiscreteAccessory/Ladder truss connector~~ IfcDiscreteAccessory






Qto_ReinforcedSoilBaseQuantities.xml
====================================

additions
---------
* ApplicableTypeValue



Pset_AirSideSystemInformation.xml
=================================

modifications
-------------
* ApplicableTypeValue "IfcSpace,IfcZone,IfcSpatialZone"
  ~~IfcSpace,IfcZone,IfcSpatialZone~~ IfcSpace,IfcSpatialZone,IfcZone



Pset_Condition.xml
==================

modifications
-------------
* ApplicableTypeValue "IfcElement,IfcSystem,IfcAsset"
  ~~IfcElement,IfcSystem,IfcAsset~~ IfcAsset,IfcElement,IfcSystem



















Pset_GateHeadCommon.xml
=======================

modifications
-------------
* ApplicableClasses > ClassName "IfcFacilityPart/IfcMarinePartTypeEnum(.GATEHEAD.)"
  ~~IfcFacilityPart/IfcMarinePartTypeEnum(.GATEHEAD.)~~ IfcFacilityPart/GATEHEAD
* ApplicableTypeValue "IfcFacilityPart/IfcMarinePartTypeEnum(.GATEHEAD.)"
  ~~IfcFacilityPart/IfcMarinePartTypeEnum(.GATEHEAD.)~~ IfcFacilityPart/GATEHEAD












Pset_SolidStratumCapacity.xml
=============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="HydraulicConductivity"] > PropertyType > TypePropertySingleValue > DataType
  ~~IfcVelocityMeasure~~ UNKNOWN
* PropertyDefs > PropertyDef [Name="LoadbearingCapacity"] > PropertyType > TypePropertySingleValue > DataType
  ~~PressureMeasure~~ UNKNOWN
* PropertyDefs > PropertyDef [Name="PwaveVelocity"] > PropertyType > TypePropertySingleValue > DataType
  ~~IfcVelocityMeasure~~ UNKNOWN
* PropertyDefs > PropertyDef [Name="SwaveVelocity"] > PropertyType > TypePropertySingleValue > DataType
  ~~IfcVelocityMeasure~~ UNKNOWN













Pset_VesselLineCommon.xml
=========================

modifications
-------------
* ApplicableTypeValue "IfcMechanicalFastener/ROPE,IfcMechanicalFastenerType/ROPE"
  ~~IfcMechanicalFastener/ROPE,IfcMechanicalFastenerType/ROPE~~ IfcMechanicalFastener/ROPE,IfcMechanicalFastener/ROPE

deletions
---------
* ApplicableClasses > ClassName "IfcMechanicalFastenerType/ROPE"















Pset_FurnitureTypeCommon.xml
============================

deletions
---------
* PropertyDefs > PropertyDef [Name="Reference"]

















Pset_DiscreteAccessoryEdgeFixingPlate.xml
=========================================

modifications
-------------
* ApplicableClasses > ClassName "IfcDiscreteAccessory/Edge fixing plate"
  ~~IfcDiscreteAccessory/Edge fixing plate~~ IfcDiscreteAccessory
* ApplicableTypeValue "IfcDiscreteAccessory/Edge fixing plate"
  ~~IfcDiscreteAccessory/Edge fixing plate~~ IfcDiscreteAccessory






Pset_ElementAssemblyCommon.xml
==============================

additions
---------
* ApplicableTypeValue

deletions
---------
* PropertyDefs > PropertyDef [Name="Reference"]




Pset_CoveringFlooring.xml
=========================

modifications
-------------
* ApplicableTypeValue "IfcCovering/FLOORING,"
  ~~IfcCovering/FLOORING,~~ IfcCovering/FLOORING

deletions
---------
* ApplicableClasses > ClassName












Pset_ElementKinematics.xml
==========================

modifications
-------------
* PropertyDefs > PropertyDef [Name="MaximumConstantSpeed"] > PropertyType > TypePropertySingleValue > DataType
  ~~IfcVelocityMeasure~~ UNKNOWN







Pset_DoorWindowGlazingType.xml
==============================

modifications
-------------
* ApplicableTypeValue "IfcDoor, IfcWindow"
  ~~IfcDoor, IfcWindow~~ IfcDoor,IfcWindow









Pset_ProcessCapacity.xml
========================

modifications
-------------
* ApplicableTypeValue "IfcSpatialElement,IfcSpatialElementType,IfcTransportElement,IfcTransportElementType,IfcBuiltSystem,IfcDistributionSystem,IfcZone,IfcDoor"
  ~~IfcSpatialElement,IfcSpatialElementType,IfcTransportElement,IfcTransportElementType,IfcBuiltSystem,IfcDistributionSystem,IfcZone,IfcDoor~~ IfcBuiltSystem,IfcDistributionSystem,IfcDoor,IfcSpatialElement,IfcSpatialElementType,IfcTransportElement,IfcTransportElementType,IfcZone
* PropertyDefs > PropertyDef [Name="ProcessItem"] > PropertyType > TypePropertySingleValue > DataType
  ~~PEnum_ProcessItem~~ UNKNOWN
* PropertyDefs > PropertyDef [Name="ProcessPerformance"] > PropertyType > TypePropertySingleValue > DataType
  ~~IfcDuration ~~ UNKNOWN










Pset_RoadSymbolsCommon.xml
==========================

modifications
-------------
* ApplicableClasses > ClassName "IfcSurfaceFeature/(.SYMBOLMARKING.)"
  ~~IfcSurfaceFeature/(.SYMBOLMARKING.)~~ IfcSurfaceFeature/SYMBOLMARKING
* ApplicableTypeValue "IfcSurfaceFeature/(.SYMBOLMARKING.)"
  ~~IfcSurfaceFeature/(.SYMBOLMARKING.)~~ IfcSurfaceFeature/SYMBOLMARKING

















Pset_MaintenanceTriggerCondition.xml
====================================

modifications
-------------
* ApplicableTypeValue "IfcElement,IfcAsset,IfcSystem"
  ~~IfcElement,IfcAsset,IfcSystem~~ IfcAsset,IfcElement,IfcSystem









Pset_FanCentrifugal.xml
=======================

modifications
-------------
* ApplicableClasses > ClassName "IfcFan/CENTRIFUGAL"
  ~~IfcFan/CENTRIFUGAL~~ IfcFan
* ApplicableTypeValue "IfcFan/CENTRIFUGAL"
  ~~IfcFan/CENTRIFUGAL~~ IfcFan



Pset_Risk.xml
=============

modifications
-------------
* ApplicableTypeValue "IfcProcess,IfcTypeProcess,IfcProduct,IfcTypeProduct,IfcGroup"
  ~~IfcProcess,IfcTypeProcess,IfcProduct,IfcTypeProduct,IfcGroup~~ IfcGroup,IfcProcess,IfcProduct,IfcTypeProcess,IfcTypeProduct





Pset_MarkingLinesCommon.xml
===========================

modifications
-------------
* ApplicableClasses > ClassName "IfcSurfaceFeature/(.LINEMARKING.)"
  ~~IfcSurfaceFeature/(.LINEMARKING.)~~ IfcSurfaceFeature/LINEMARKING
* ApplicableTypeValue "IfcSurfaceFeature/(.LINEMARKING.)"
  ~~IfcSurfaceFeature/(.LINEMARKING.)~~ IfcSurfaceFeature/LINEMARKING





Pset_DiscreteAccessoryDiagonalTrussConnector.xml
================================================

modifications
-------------
* ApplicableClasses > ClassName "IfcDiscreteAccessory/Diagonal truss connector"
  ~~IfcDiscreteAccessory/Diagonal truss connector~~ IfcDiscreteAccessory
* ApplicableTypeValue "IfcDiscreteAccessory/Diagonal truss connector"
  ~~IfcDiscreteAccessory/Diagonal truss connector~~ IfcDiscreteAccessory


Pset_FenderCommon.xml
=====================

modifications
-------------
* ApplicableTypeValue "IfcImpactProtectionDevice/IfcImpactProtectionDeviceTypeEnum(.FENDER.),IfcImpactProtectionDeviceType/IfcImpactProtectionDeviceTypeEnum(.FENDER.)"
  ~~IfcImpactProtectionDevice/IfcImpactProtectionDeviceTypeEnum(.FENDER.),IfcImpactProtectionDeviceType/IfcImpactProtectionDeviceTypeEnum(.FENDER.)~~ IfcImpactProtectionDevice/FENDER,IfcImpactProtectionDevice/FENDER
* ApplicableClasses > ClassName "IfcImpactProtectionDevice/IfcImpactProtectionDeviceTypeEnum(.FENDER.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;

deletions
---------
* ApplicableClasses > ClassName "IfcImpactProtectionDeviceType/IfcImpactProtectionDeviceTypeEnum(.FENDER.)"











Pset_MarineVehicleCommon.xml
============================

modifications
-------------
* ApplicableTypeValue "IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.)"
  ~~IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.)~~ IfcTransportElement/VEHICLEMARINE,IfcTransportElement/VEHICLEMARINE
* 
  ~~QTO_TYPEDRIVENOVERRIDE~~ PSET_TYPEDRIVENOVERRIDE
* ApplicableClasses > ClassName "IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;

deletions
---------
* ApplicableClasses > ClassName "IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.)"





Pset_SensorTypeLevelSensor.xml
==============================

modifications
-------------
* ApplicableClasses > ClassName "IfcSensor/LEVEL"
  ~~IfcSensor/LEVEL~~ IfcSensor
* ApplicableTypeValue "IfcSensor/LEVEL"
  ~~IfcSensor/LEVEL~~ IfcSensor






Pset_DiscreteAccessoryWireLoop.xml
==================================

modifications
-------------
* ApplicableClasses > ClassName "IfcDiscreteAccessory/Wire loop"
  ~~IfcDiscreteAccessory/Wire loop~~ IfcDiscreteAccessory
* ApplicableTypeValue "IfcDiscreteAccessory/Wire loop"
  ~~IfcDiscreteAccessory/Wire loop~~ IfcDiscreteAccessory



Pset_AnnotationContourLine.xml
==============================

modifications
-------------
* ApplicableClasses > ClassName "IfcAnnotation/ContourLine"
  ~~IfcAnnotation/ContourLine~~ IfcAnnotation
* ApplicableTypeValue "IfcAnnotation/ContourLine"
  ~~IfcAnnotation/ContourLine~~ IfcAnnotation


Qto_ImpactProtectionDeviceBaseQuantities.xml
============================================

additions
---------
* ApplicableTypeValue


Pset_PrecastConcreteElementGeneral.xml
======================================

modifications
-------------
* ApplicableTypeValue "IfcBeam,IfcBuildingElementProxy,IfcChimney,IfcColumn,IfcFooting,IfcMember,IfcPile,IfcPlate,IfcRamp,IfcRampFlight,IfcRoof,IfcSlab,IfcStair,IfcStairFlight,IfcWall,IfcCivilElement"
  ~~IfcBeam,IfcBuildingElementProxy,IfcChimney,IfcColumn,IfcFooting,IfcMember,IfcPile,IfcPlate,IfcRamp,IfcRampFlight,IfcRoof,IfcSlab,IfcStair,IfcStairFlight,IfcWall,IfcCivilElement~~ IfcBeam,IfcBuildingElementProxy,IfcChimney,IfcCivilElement,IfcColumn,IfcFooting,IfcMember,IfcPile,IfcPlate,IfcRampFlight,IfcRamp,IfcRoof,IfcSlab,IfcStairFlight,IfcStair,IfcWall




Pset_MaintenanceStrategy.xml
============================

modifications
-------------
* ApplicableTypeValue "IfcElement,IfcAsset,IfcSystem"
  ~~IfcElement,IfcAsset,IfcSystem~~ IfcAsset,IfcElement,IfcSystem






Pset_SpaceThermalRequirements.xml
=================================

modifications
-------------
* ApplicableTypeValue "IfcSpace, IfcSpatialZone, IfcZone"
  ~~IfcSpace, IfcSpatialZone, IfcZone~~ IfcSpace,IfcSpatialZone,IfcZone



Pset_ChamberCommon.xml
======================

modifications
-------------
* ApplicableClasses > ClassName "IfcFacilityPart/IfcMarinePartTypeEnum(.CHAMBER.)"
  ~~IfcFacilityPart/IfcMarinePartTypeEnum(.CHAMBER.)~~ IfcFacilityPart/CHAMBER
* ApplicableTypeValue "IfcFacilityPart/IfcMarinePartTypeEnum(.CHAMBER.)"
  ~~IfcFacilityPart/IfcMarinePartTypeEnum(.CHAMBER.)~~ IfcFacilityPart/CHAMBER





























Qto_KerbBaseQuantities.xml
==========================

additions
---------
* ApplicableTypeValue
















Pset_SpaceLightingRequirements.xml
==================================

modifications
-------------
* ApplicableTypeValue "IfcSpace, IfcSpatialZone, IfcZone"
  ~~IfcSpace, IfcSpatialZone, IfcZone~~ IfcSpace,IfcSpatialZone,IfcZone


Qto_VehicleBaseQuantities.xml
=============================

modifications
-------------
* ApplicableTypeValue "IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLE.),IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLETRACKED.),IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.),IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLEAIR.),IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.ROLLINGSTOCK.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLE.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLETRACKED.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLEAIR.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.ROLLINGSTOCK.)"
  ~~IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLE.),IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLETRACKED.),IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.),IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLEAIR.),IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.ROLLINGSTOCK.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLE.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLETRACKED.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLEAIR.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.ROLLINGSTOCK.)~~ IfcTransportElement/ROLLINGSTOCK,IfcTransportElement/ROLLINGSTOCK,IfcTransportElement/VEHICLEAIR,IfcTransportElement/VEHICLEAIR,IfcTransportElement/VEHICLEMARINE,IfcTransportElement/VEHICLEMARINE,IfcTransportElement/VEHICLE,IfcTransportElement/VEHICLE,IfcTransportElement/VEHICLETRACKED,IfcTransportElement/VEHICLETRACKED
* ApplicableClasses > ClassName "IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.ROLLINGSTOCK.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLETRACKED.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLE.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLEAIR.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;

deletions
---------
* ApplicableClasses > ClassName "IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLETRACKED.)"
* ApplicableClasses > ClassName "IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLEAIR.)"
* ApplicableClasses > ClassName "IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLE.)"
* ApplicableClasses > ClassName "IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.)"
* ApplicableClasses > ClassName "IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.ROLLINGSTOCK.)"




Pset_RampCommon.xml
===================

deletions
---------
* PropertyDefs > PropertyDef [Name="ThermalTransmittance"]
* PropertyDefs > PropertyDef [Name="LoadBearing"]


















Pset_MaterialWoodBasedPanel.xml
===============================

modifications
-------------
* ApplicableClasses > ClassName "IfcMaterial/Wood"
  ~~IfcMaterial/Wood~~ IfcMaterial
* ApplicableTypeValue "IfcMaterial/Wood"
  ~~IfcMaterial/Wood~~ IfcMaterial


Pset_PrecastConcreteElementFabrication.xml
==========================================

modifications
-------------
* ApplicableTypeValue "IfcBeam,IfcBuildingElementProxy,IfcChimney,IfcColumn,IfcFooting,IfcMember,IfcPile,IfcPlate,IfcRamp,IfcRampFlight,IfcRoof,IfcSlab,IfcStair,IfcStairFlight,IfcWall,IfcCivilElement"
  ~~IfcBeam,IfcBuildingElementProxy,IfcChimney,IfcColumn,IfcFooting,IfcMember,IfcPile,IfcPlate,IfcRamp,IfcRampFlight,IfcRoof,IfcSlab,IfcStair,IfcStairFlight,IfcWall,IfcCivilElement~~ IfcBeam,IfcBuildingElementProxy,IfcChimney,IfcCivilElement,IfcColumn,IfcFooting,IfcMember,IfcPile,IfcPlate,IfcRampFlight,IfcRamp,IfcRoof,IfcSlab,IfcStairFlight,IfcStair,IfcWall
















Pset_PlantCommon.xml
====================

modifications
-------------
* ApplicableClasses > ClassName "IfcPlant"
  ~~IfcPlant~~ IfcVegetation
* ApplicableTypeValue "IfcPlant"
  ~~IfcPlant~~ IfcVegetation







Pset_BerthCommon.xml
====================

modifications
-------------
* ApplicableTypeValue "IfcSpace/BERTH,IfcSpaceType/BERTH"
  ~~IfcSpace/BERTH,IfcSpaceType/BERTH~~ IfcSpace/BERTH,IfcSpace/BERTH

deletions
---------
* ApplicableClasses > ClassName "IfcSpaceType/BERTH"





Pset_SpatialZoneCommon.xml
==========================

additions
---------
* ApplicableTypeValue

deletions
---------
* PropertyDefs > PropertyDef [Name="Reference"]



Qto_EarthworksCutBaseQuantities.xml
===================================

additions
---------
* ApplicableTypeValue



Pset_RoadMarkingCommon.xml
==========================

modifications
-------------
* ApplicableTypeValue "IfcSurfaceFeature/(.HATCHMARKING.),IfcSurfaceFeature/(.LINEMARKING.),IfcSurfaceFeature/(.PAVEMENTSURFACEMARKING.),IfcSurfaceFeature/(.SYMBOLMARKING.)"
  ~~IfcSurfaceFeature/(.HATCHMARKING.),IfcSurfaceFeature/(.LINEMARKING.),IfcSurfaceFeature/(.PAVEMENTSURFACEMARKING.),IfcSurfaceFeature/(.SYMBOLMARKING.)~~ IfcSurfaceFeature/HATCHMARKING,IfcSurfaceFeature/LINEMARKING,IfcSurfaceFeature/PAVEMENTSURFACEMARKING,IfcSurfaceFeature/SYMBOLMARKING
* ApplicableClasses > ClassName "IfcSurfaceFeature/(.LINEMARKING.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcSurfaceFeature/(.HATCHMARKING.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcSurfaceFeature/(.SYMBOLMARKING.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcSurfaceFeature/(.PAVEMENTSURFACEMARKING.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="MaterialColour"]





Pset_MaintenanceTriggerDuration.xml
===================================

modifications
-------------
* ApplicableTypeValue "IfcElement,IfcAsset,IfcSystem"
  ~~IfcElement,IfcAsset,IfcSystem~~ IfcAsset,IfcElement,IfcSystem


Pset_SoundAttenuation.xml
=========================

modifications
-------------
* ApplicableClasses > ClassName "IfcAnnotation/SOUND"
  ~~IfcAnnotation/SOUND~~ IfcAnnotation
* ApplicableTypeValue "IfcAnnotation/SOUND"
  ~~IfcAnnotation/SOUND~~ IfcAnnotation



Pset_TankTypePreformed.xml
==========================

modifications
-------------
* ApplicableClasses > ClassName "IfcTank/PREFORMED"
  ~~IfcTank/PREFORMED~~ IfcTank
* ApplicableTypeValue "IfcTank/PREFORMED"
  ~~IfcTank/PREFORMED~~ IfcTank










Pset_SpaceFireSafetyRequirements.xml
====================================

modifications
-------------
* ApplicableTypeValue "IfcSpace, IfcSpatialZone, IfcZone"
  ~~IfcSpace, IfcSpatialZone, IfcZone~~ IfcSpace,IfcSpatialZone,IfcZone





Pset_SpaceOccupancyRequirements.xml
===================================

modifications
-------------
* ApplicableTypeValue "IfcSpace, IfcSpatialZone, IfcZone"
  ~~IfcSpace, IfcSpatialZone, IfcZone~~ IfcSpace,IfcSpatialZone,IfcZone


Pset_VehicleAvailability.xml
============================

modifications
-------------
* ApplicableTypeValue "IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLE.),IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLETRACKED.),IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.),IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLEAIR.),IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.ROLLINGSTOCK.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLE.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLETRACKED.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLEAIR.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.ROLLINGSTOCK.)"
  ~~IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLE.),IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLETRACKED.),IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.),IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLEAIR.),IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.ROLLINGSTOCK.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLE.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLETRACKED.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLEAIR.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.ROLLINGSTOCK.)~~ IfcTransportElement/ROLLINGSTOCK,IfcTransportElement/ROLLINGSTOCK,IfcTransportElement/VEHICLEAIR,IfcTransportElement/VEHICLEAIR,IfcTransportElement/VEHICLEMARINE,IfcTransportElement/VEHICLEMARINE,IfcTransportElement/VEHICLE,IfcTransportElement/VEHICLE,IfcTransportElement/VEHICLETRACKED,IfcTransportElement/VEHICLETRACKED
* ApplicableClasses > ClassName "IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.ROLLINGSTOCK.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLETRACKED.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLE.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLEAIR.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;

deletions
---------
* ApplicableClasses > ClassName "IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLETRACKED.)"
* ApplicableClasses > ClassName "IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLEAIR.)"
* ApplicableClasses > ClassName "IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLE.)"
* ApplicableClasses > ClassName "IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.)"
* ApplicableClasses > ClassName "IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.ROLLINGSTOCK.)"





















Pset_MaterialWoodBasedBeam.xml
==============================

modifications
-------------
* ApplicableClasses > ClassName "IfcMaterial/Wood"
  ~~IfcMaterial/Wood~~ IfcMaterial
* ApplicableTypeValue "IfcMaterial/Wood"
  ~~IfcMaterial/Wood~~ IfcMaterial






Pset_TransportElementElevator.xml
=================================

modifications
-------------
* ApplicableClasses > ClassName "IfcTransportElement/ELEVATOR"
  ~~IfcTransportElement/ELEVATOR~~ IfcTransportElement
* ApplicableTypeValue "IfcTransportElement/ELEVATOR"
  ~~IfcTransportElement/ELEVATOR~~ IfcTransportElement


Pset_DiscreteAccessoryStandardFixingPlate.xml
=============================================

modifications
-------------
* ApplicableClasses > ClassName "IfcDiscreteAccessory/Standard fixing plate"
  ~~IfcDiscreteAccessory/Standard fixing plate~~ IfcDiscreteAccessory
* ApplicableTypeValue "IfcDiscreteAccessory/Standard fixing plate"
  ~~IfcDiscreteAccessory/Standard fixing plate~~ IfcDiscreteAccessory







Qto_SurfaceFeatureBaseQuantities.xml
====================================

additions
---------
* ApplicableTypeValue













Pset_RoofCommon.xml
===================

deletions
---------
* PropertyDefs > PropertyDef [Name="LoadBearing"]






Pset_TransitionSectionCommon.xml
================================

modifications
-------------
* ApplicableClasses > ClassName "IfcEarthworksFill/(.TRANSITIONSECTION.)"
  ~~IfcEarthworksFill/(.TRANSITIONSECTION.)~~ IfcEarthworksFill/TRANSITIONSECTION
* ApplicableTypeValue "IfcEarthworksFill/(.TRANSITIONSECTION.)"
  ~~IfcEarthworksFill/(.TRANSITIONSECTION.)~~ IfcEarthworksFill/TRANSITIONSECTION


Qto_SignBaseQuantities.xml
==========================

additions
---------
* ApplicableTypeValue


Pset_MaintenanceTriggerPerformance.xml
======================================

modifications
-------------
* ApplicableTypeValue "IfcElement,IfcAsset,IfcSystem"
  ~~IfcElement,IfcAsset,IfcSystem~~ IfcAsset,IfcElement,IfcSystem










Pset_DiscreteAccessoryCornerFixingPlate.xml
===========================================

modifications
-------------
* ApplicableClasses > ClassName "IfcDiscreteAccessory/Corner fixing plate"
  ~~IfcDiscreteAccessory/Corner fixing plate~~ IfcDiscreteAccessory
* ApplicableTypeValue "IfcDiscreteAccessory/Corner fixing plate"
  ~~IfcDiscreteAccessory/Corner fixing plate~~ IfcDiscreteAccessory











Pset_BoreholeCommon.xml
=======================

modifications
-------------
* PropertyDefs > PropertyDef [Name="BoreholeState"] > PropertyType > TypePropertySingleValue > DataType
  ~~IfcBoreholeState~~ UNKNOWN













Qto_PictorialSignQuantities.xml
===============================

additions
---------
* ApplicableTypeValue











Pset_AnnotationSurveyArea.xml
=============================

modifications
-------------
* ApplicableClasses > ClassName "IfcAnnotation/SurveyArea"
  ~~IfcAnnotation/SurveyArea~~ IfcAnnotation
* ApplicableTypeValue "IfcAnnotation/SurveyArea"
  ~~IfcAnnotation/SurveyArea~~ IfcAnnotation






Qto_EarthworksFillBaseQuantities.xml
====================================

additions
---------
* ApplicableTypeValue



Pset_MarineFacilityTransportation.xml
=====================================

additions
---------
* ApplicableTypeValue


Pset_MaterialWood.xml
=====================

modifications
-------------
* ApplicableClasses > ClassName "IfcMaterial/Wood"
  ~~IfcMaterial/Wood~~ IfcMaterial
* ApplicableTypeValue "IfcMaterial/Wood"
  ~~IfcMaterial/Wood~~ IfcMaterial


Qto_PavementBaseQuantities.xml
==============================

additions
---------
* ApplicableTypeValue


















Qto_CourseBaseQuantities.xml
============================

additions
---------
* ApplicableTypeValue


Pset_CargoCommon.xml
====================

modifications
-------------
* ApplicableTypeValue "IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.CARGO.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.CARGO.)"
  ~~IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.CARGO.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.CARGO.)~~ IfcTransportElement/CARGO,IfcTransportElement/CARGO
* PropertyDefs > PropertyDef [Name="ProcessItem"] > PropertyType > TypePropertySingleValue > DataType
  ~~PEnum_ProcessItem~~ UNKNOWN
* ApplicableClasses > ClassName "IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.CARGO.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;

deletions
---------
* ApplicableClasses > ClassName "IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.CARGO.)"


Pset_TicketProcessing.xml
=========================

modifications
-------------
* ApplicableTypeValue "IfcDoor/TURNSTILE,IfcDoor/BOOM_BARRIER"
  ~~IfcDoor/TURNSTILE,IfcDoor/BOOM_BARRIER~~ IfcDoor/BOOM_BARRIER,IfcDoor/TURNSTILE







