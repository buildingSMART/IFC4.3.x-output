
Missing in output
=================
* PSet_ElementKinematics.xml

Missing in reference
=================
* Pset_MobileTelecommunicationsApplianceTypeEUtranNodeB.xml
* Pset_MobileTelecommunicationsApplianceTypeBasebandUnit.xml
* Pset_TicketProcessing.xml
* Pset_SlabTypeTrackSlab.xml
* Pset_MobileTelecommunicationsApplianceTypeCommon.xml
* Pset_MobileTelecommunicationsApplianceTypeMobileSwitchingCenter.xml
* Pset_UnitaryControlElementTypeControlPanel.xml
* Pset_MobileTelecommunicationsApplianceTypeBaseTransceiverStation.xml
* Pset_EmbeddedTrack.xml
* Pset_MobileTelecommunicationsApplianceTypeMasterUnit.xml
* Pset_MobileTelecommunicationsApplianceTypeAccessPoint.xml
* Pset_TrackBase.xml
* Pset_MobileTelecommunicationsApplianceTypeRemoteUnit.xml
* Pset_MobileTelecommunicationsApplianceTypeMSCServer.xml
* Pset_CessBetweenRails.xml
* Pset_UnitaryControlElementBaseStationController.xml
* Pset_MobileTeleCommunicationsApplianceTypeRemoteRadioUnit.xml
* Pset_ElementKinematics.xml
* Pset_CoveringTypeMembrane.xml























Pset_MaterialWoodBasedBeam.xml
==============================

additions
---------
* PropertyDefs > PropertyDef [Name="OutOfPlane"]

modifications
-------------
* ApplicableClasses > ClassName "IfcMaterial/Wood"
  ~~IfcMaterial/Wood~~ IfcMaterial
* ApplicableTypeValue "IfcMaterial/Wood"
  ~~IfcMaterial/Wood~~ IfcMaterial
* PropertyDefs > PropertyDef [Name="InPlane"] > PropertyType
  ~~&lt;PropertyType&gt;~~ &lt;PropertyType&gt;
* PropertyDefs > PropertyDef [Name="OutOfPlane"] > Name "OutOfPlane"
  ~~&lt;Name&gt;~~ &lt;Name&gt;
* PropertyDefs > PropertyDef [Name="InPlane"] > Name "InPlane"
  ~~&lt;Name&gt;~~ &lt;Name&gt;
* PropertyDefs > PropertyDef [Name="OutOfPlane"] > PropertyType
  ~~&lt;PropertyType&gt;~~ &lt;PropertyType&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="InPlaneNegative"]














Qto_SurfaceFeatureBaseQuantities.xml
====================================

additions
---------
* ApplicableTypeValue


Pset_RampCommon.xml
===================

deletions
---------
* PropertyDefs > PropertyDef [Name="ThermalTransmittance"]
* PropertyDefs > PropertyDef [Name="LoadBearing"]




Pset_BerthCommon.xml
====================

modifications
-------------
* ApplicableTypeValue "IfcSpace/BERTH,IfcSpaceType/BERTH"
  ~~IfcSpace/BERTH,IfcSpaceType/BERTH~~ IfcSpace/BERTH,IfcSpace/BERTH

deletions
---------
* ApplicableClasses > ClassName "IfcSpaceType/BERTH"






Pset_RoadSymbolsCommon.xml
==========================

modifications
-------------
* ApplicableClasses > ClassName "IfcSurfaceFeature/(.SYMBOLMARKING.)"
  ~~IfcSurfaceFeature/(.SYMBOLMARKING.)~~ IfcSurfaceFeature/SYMBOLMARKING
* ApplicableTypeValue "IfcSurfaceFeature/(.SYMBOLMARKING.)"
  ~~IfcSurfaceFeature/(.SYMBOLMARKING.)~~ IfcSurfaceFeature/SYMBOLMARKING













Pset_ProcessCapacity.xml
========================

modifications
-------------
* PropertyDefs > PropertyDef [Name="ProcessItem"] > PropertyType > TypePropertySingleValue > DataType
  ~~PEnum_ProcessItem~~ UNKNOWN
* PropertyDefs > PropertyDef [Name="ProcessPerformance"] > PropertyType > TypePropertySingleValue > DataType
  ~~IfcDuration ~~ UNKNOWN














Pset_PavementMillingCommon.xml
==============================

modifications
-------------
* ApplicableClasses > ClassName "IfcEarthworksCut/(.PAVEMENTMILLING.)"
  ~~IfcEarthworksCut/(.PAVEMENTMILLING.)~~ IfcEarthworksCut/PAVEMENTMILLING
* ApplicableTypeValue "IfcEarthworksCut/(.PAVEMENTMILLING.)"
  ~~IfcEarthworksCut/(.PAVEMENTMILLING.)~~ IfcEarthworksCut/PAVEMENTMILLING






Pset_TankTypePreformed.xml
==========================

modifications
-------------
* ApplicableClasses > ClassName "IfcTank/PREFORMED"
  ~~IfcTank/PREFORMED~~ IfcTank
* ApplicableTypeValue "IfcTank/PREFORMED"
  ~~IfcTank/PREFORMED~~ IfcTank









Pset_DiscreteAccessoryCornerFixingPlate.xml
===========================================

modifications
-------------
* ApplicableClasses > ClassName "IfcDiscreteAccessory/Corner fixing plate"
  ~~IfcDiscreteAccessory/Corner fixing plate~~ IfcDiscreteAccessory
* ApplicableTypeValue "IfcDiscreteAccessory/Corner fixing plate"
  ~~IfcDiscreteAccessory/Corner fixing plate~~ IfcDiscreteAccessory




Qto_VehicleBaseQuantities.xml
=============================

modifications
-------------
* ApplicableTypeValue "IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLE.),IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLETRACKED.),IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.),IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLEAIR.),IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.ROLLINGSTOCK.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLE.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLETRACKED.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLEAIR.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.ROLLINGSTOCK.)"
  ~~IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLE.),IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLETRACKED.),IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.),IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLEAIR.),IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.ROLLINGSTOCK.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLE.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLETRACKED.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLEAIR.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.ROLLINGSTOCK.)~~ IfcTransportElement/VEHICLE,IfcTransportElement/VEHICLETRACKED,IfcTransportElement/VEHICLEMARINE,IfcTransportElement/VEHICLEAIR,IfcTransportElement/ROLLINGSTOCK,IfcTransportElement/VEHICLE,IfcTransportElement/VEHICLETRACKED,IfcTransportElement/VEHICLEMARINE,IfcTransportElement/VEHICLEAIR,IfcTransportElement/ROLLINGSTOCK
* ApplicableClasses > ClassName "IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLETRACKED.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.ROLLINGSTOCK.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLE.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLEAIR.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;

deletions
---------
* ApplicableClasses > ClassName "IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLE.)"
* ApplicableClasses > ClassName "IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLETRACKED.)"
* ApplicableClasses > ClassName "IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.)"
* ApplicableClasses > ClassName "IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLEAIR.)"
* ApplicableClasses > ClassName "IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.ROLLINGSTOCK.)"


Pset_RoadDesignCriteriaCommon.xml
=================================

modifications
-------------
* ApplicableTypeValue "IfcRoad,IfcFacilityPart/IfcRoadPartTypeEnum(.ROADSEGMENT.),IfcFacilityPart/IfcFacilityPartCommonTypeEnum(.SEGMENT.),IfcFacilityPart/IfcFacilityPartCommonTypeEnum(.JUNCTION.),IfcFacilityPart/IfcFacilityPartCommonTypeEnum(.LEVELCROSSING.),IfcFacilityPart/IfcRoadPartTypeEnum(.RAILWAYCROSSING.),IfcFacilityPart/IfcRoadPartTypeEnum(.PEDESTRIAN_CROSSING.),IfcFacilityPart/IfcRoadPartTypeEnum(.BICYCLECROSSING.),IfcFacilityPart/IfcRoadPartTypeEnum(.ROUNDABOUT.),IfcFacilityPart/IfcRoadPartTypeEnum(.INTERSECTION.),IfcFacilityPart/IfcRoadPartTypeEnum(.TOLLPLAZA.)"
  ~~IfcRoad,IfcFacilityPart/IfcRoadPartTypeEnum(.ROADSEGMENT.),IfcFacilityPart/IfcFacilityPartCommonTypeEnum(.SEGMENT.),IfcFacilityPart/IfcFacilityPartCommonTypeEnum(.JUNCTION.),IfcFacilityPart/IfcFacilityPartCommonTypeEnum(.LEVELCROSSING.),IfcFacilityPart/IfcRoadPartTypeEnum(.RAILWAYCROSSING.),IfcFacilityPart/IfcRoadPartTypeEnum(.PEDESTRIAN_CROSSING.),IfcFacilityPart/IfcRoadPartTypeEnum(.BICYCLECROSSING.),IfcFacilityPart/IfcRoadPartTypeEnum(.ROUNDABOUT.),IfcFacilityPart/IfcRoadPartTypeEnum(.INTERSECTION.),IfcFacilityPart/IfcRoadPartTypeEnum(.TOLLPLAZA.)~~ IfcRoad,IfcFacilityPart/ROADSEGMENT,IfcFacilityPart/SEGMENT,IfcFacilityPart/JUNCTION,IfcFacilityPart/LEVELCROSSING,IfcFacilityPart/RAILWAYCROSSING,IfcFacilityPart/PEDESTRIAN_CROSSING,IfcFacilityPart/BICYCLECROSSING,IfcFacilityPart/ROUNDABOUT,IfcFacilityPart/INTERSECTION,IfcFacilityPart/TOLLPLAZA
* ApplicableClasses > ClassName "IfcFacilityPart/IfcFacilityPartCommonTypeEnum(.SEGMENT.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcFacilityPart/IfcRoadPartTypeEnum(.ROUNDABOUT.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcFacilityPart/IfcRoadPartTypeEnum(.PEDESTRIAN_CROSSING.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcFacilityPart/IfcFacilityPartCommonTypeEnum(.LEVELCROSSING.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcFacilityPart/IfcRoadPartTypeEnum(.INTERSECTION.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcFacilityPart/IfcRoadPartTypeEnum(.RAILWAYCROSSING.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcFacilityPart/IfcRoadPartTypeEnum(.TOLLPLAZA.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcFacilityPart/IfcFacilityPartCommonTypeEnum(.JUNCTION.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcFacilityPart/IfcRoadPartTypeEnum(.BICYCLECROSSING.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcFacilityPart/IfcRoadPartTypeEnum(.ROADSEGMENT.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;




















Pset_RoofCommon.xml
===================

deletions
---------
* PropertyDefs > PropertyDef [Name="LoadBearing"]




Qto_PavementBaseQuantities.xml
==============================

additions
---------
* ApplicableTypeValue







Pset_SpaceOccupancyRequirements.xml
===================================

modifications
-------------
* ApplicableTypeValue "IfcSpace, IfcSpatialZone, IfcZone"
  ~~IfcSpace, IfcSpatialZone, IfcZone~~ IfcSpace,IfcSpatialZone,IfcZone





Pset_TrenchExcavationCommon.xml
===============================

modifications
-------------
* ApplicableClasses > ClassName "IfcEarthworksCut/(.TRENCH.)"
  ~~IfcEarthworksCut/(.TRENCH.)~~ IfcEarthworksCut/TRENCH
* ApplicableTypeValue "IfcEarthworksCut/(.TRENCH.)"
  ~~IfcEarthworksCut/(.TRENCH.)~~ IfcEarthworksCut/TRENCH












Pset_GateHeadCommon.xml
=======================

modifications
-------------
* ApplicableClasses > ClassName "IfcFacilityPart/IfcMarinePartTypeEnum(.GATEHEAD.)"
  ~~IfcFacilityPart/IfcMarinePartTypeEnum(.GATEHEAD.)~~ IfcFacilityPart/GATEHEAD
* ApplicableTypeValue "IfcFacilityPart/IfcMarinePartTypeEnum(.GATEHEAD.)"
  ~~IfcFacilityPart/IfcMarinePartTypeEnum(.GATEHEAD.)~~ IfcFacilityPart/GATEHEAD









Pset_DiscreteAccessoryDiagonalTrussConnector.xml
================================================

modifications
-------------
* ApplicableClasses > ClassName "IfcDiscreteAccessory/Diagonal truss connector"
  ~~IfcDiscreteAccessory/Diagonal truss connector~~ IfcDiscreteAccessory
* ApplicableTypeValue "IfcDiscreteAccessory/Diagonal truss connector"
  ~~IfcDiscreteAccessory/Diagonal truss connector~~ IfcDiscreteAccessory





Pset_MaterialWood.xml
=====================

modifications
-------------
* ApplicableClasses > ClassName "IfcMaterial/Wood"
  ~~IfcMaterial/Wood~~ IfcMaterial
* ApplicableTypeValue "IfcMaterial/Wood"
  ~~IfcMaterial/Wood~~ IfcMaterial



Pset_AnnotationContourLine.xml
==============================

modifications
-------------
* ApplicableClasses > ClassName "IfcAnnotation/ContourLine"
  ~~IfcAnnotation/ContourLine~~ IfcAnnotation
* ApplicableTypeValue "IfcAnnotation/ContourLine"
  ~~IfcAnnotation/ContourLine~~ IfcAnnotation




Pset_TankTypeSectional.xml
==========================

modifications
-------------
* ApplicableClasses > ClassName "IfcTank/SECTIONAL"
  ~~IfcTank/SECTIONAL~~ IfcTank
* ApplicableTypeValue "IfcTank/SECTIONAL"
  ~~IfcTank/SECTIONAL~~ IfcTank









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







Pset_SpaceFireSafetyRequirements.xml
====================================

modifications
-------------
* ApplicableTypeValue "IfcSpace, IfcSpatialZone, IfcZone"
  ~~IfcSpace, IfcSpatialZone, IfcZone~~ IfcSpace,IfcSpatialZone,IfcZone













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



Pset_SoundAttenuation.xml
=========================

modifications
-------------
* ApplicableClasses > ClassName "IfcAnnotation/SOUND"
  ~~IfcAnnotation/SOUND~~ IfcAnnotation
* ApplicableTypeValue "IfcAnnotation/SOUND"
  ~~IfcAnnotation/SOUND~~ IfcAnnotation








Pset_TransitionSectionCommon.xml
================================

modifications
-------------
* ApplicableClasses > ClassName "IfcEarthworksFill/(.TRANSITIONSECTION.)"
  ~~IfcEarthworksFill/(.TRANSITIONSECTION.)~~ IfcEarthworksFill/TRANSITIONSECTION
* ApplicableTypeValue "IfcEarthworksFill/(.TRANSITIONSECTION.)"
  ~~IfcEarthworksFill/(.TRANSITIONSECTION.)~~ IfcEarthworksFill/TRANSITIONSECTION






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







Pset_ChamberCommon.xml
======================

modifications
-------------
* ApplicableClasses > ClassName "IfcFacilityPart/IfcMarinePartTypeEnum(.CHAMBER.)"
  ~~IfcFacilityPart/IfcMarinePartTypeEnum(.CHAMBER.)~~ IfcFacilityPart/CHAMBER
* ApplicableTypeValue "IfcFacilityPart/IfcMarinePartTypeEnum(.CHAMBER.)"
  ~~IfcFacilityPart/IfcMarinePartTypeEnum(.CHAMBER.)~~ IfcFacilityPart/CHAMBER





Pset_SensorTypeLevelSensor.xml
==============================

modifications
-------------
* ApplicableClasses > ClassName "IfcSensor/LEVEL"
  ~~IfcSensor/LEVEL~~ IfcSensor
* ApplicableTypeValue "IfcSensor/LEVEL"
  ~~IfcSensor/LEVEL~~ IfcSensor







Pset_AnnotationSurveyArea.xml
=============================

modifications
-------------
* ApplicableClasses > ClassName "IfcAnnotation/SurveyArea"
  ~~IfcAnnotation/SurveyArea~~ IfcAnnotation
* ApplicableTypeValue "IfcAnnotation/SurveyArea"
  ~~IfcAnnotation/SurveyArea~~ IfcAnnotation





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








Pset_FanCentrifugal.xml
=======================

modifications
-------------
* ApplicableClasses > ClassName "IfcFan/CENTRIFUGAL"
  ~~IfcFan/CENTRIFUGAL~~ IfcFan
* ApplicableTypeValue "IfcFan/CENTRIFUGAL"
  ~~IfcFan/CENTRIFUGAL~~ IfcFan











Qto_CourseBaseQuantities.xml
============================

additions
---------
* ApplicableTypeValue



Pset_DiscreteAccessoryLadderTrussConnector.xml
==============================================

modifications
-------------
* ApplicableClasses > ClassName "IfcDiscreteAccessory/Ladder truss connector"
  ~~IfcDiscreteAccessory/Ladder truss connector~~ IfcDiscreteAccessory
* ApplicableTypeValue "IfcDiscreteAccessory/Ladder truss connector"
  ~~IfcDiscreteAccessory/Ladder truss connector~~ IfcDiscreteAccessory





Pset_VesselLineCommon.xml
=========================

modifications
-------------
* ApplicableTypeValue "IfcMechanicalFastener/ROPE,IfcMechanicalFastenerType/ROPE"
  ~~IfcMechanicalFastener/ROPE,IfcMechanicalFastenerType/ROPE~~ IfcMechanicalFastener/ROPE,IfcMechanicalFastener/ROPE

deletions
---------
* ApplicableClasses > ClassName "IfcMechanicalFastenerType/ROPE"





Pset_Width.xml
==============

modifications
-------------
* ApplicableClasses > ClassName "IfcAnnotation/(.WIDTHEVENT.)"
  ~~IfcAnnotation/(.WIDTHEVENT.)~~ IfcAnnotation/WIDTHEVENT
* ApplicableTypeValue "IfcAnnotation/(.WIDTHEVENT.)"
  ~~IfcAnnotation/(.WIDTHEVENT.)~~ IfcAnnotation/WIDTHEVENT



Pset_MaterialSteel.xml
======================

modifications
-------------
* ApplicableClasses > ClassName "IfcMaterial/Steel"
  ~~IfcMaterial/Steel~~ IfcMaterial
* ApplicableTypeValue "IfcMaterial/Steel"
  ~~IfcMaterial/Steel~~ IfcMaterial





Pset_DiscreteAccessoryStandardFixingPlate.xml
=============================================

modifications
-------------
* ApplicableClasses > ClassName "IfcDiscreteAccessory/Standard fixing plate"
  ~~IfcDiscreteAccessory/Standard fixing plate~~ IfcDiscreteAccessory
* ApplicableTypeValue "IfcDiscreteAccessory/Standard fixing plate"
  ~~IfcDiscreteAccessory/Standard fixing plate~~ IfcDiscreteAccessory



Pset_SumpBusterCommon.xml
=========================

modifications
-------------
* ApplicableClasses > ClassName "IfcElementAssembly/(.SUMPBUSTER.)"
  ~~IfcElementAssembly/(.SUMPBUSTER.)~~ IfcElementAssembly/SUMPBUSTER
* ApplicableTypeValue "IfcElementAssembly/(.SUMPBUSTER.)"
  ~~IfcElementAssembly/(.SUMPBUSTER.)~~ IfcElementAssembly/SUMPBUSTER












Pset_VehicleAvailability.xml
============================

modifications
-------------
* ApplicableTypeValue "IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLE.),IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLETRACKED.),IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.),IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLEAIR.),IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.ROLLINGSTOCK.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLE.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLETRACKED.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLEAIR.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.ROLLINGSTOCK.)"
  ~~IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLE.),IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLETRACKED.),IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.),IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLEAIR.),IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.ROLLINGSTOCK.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLE.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLETRACKED.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLEAIR.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.ROLLINGSTOCK.)~~ IfcTransportElement/VEHICLE,IfcTransportElement/VEHICLETRACKED,IfcTransportElement/VEHICLEMARINE,IfcTransportElement/VEHICLEAIR,IfcTransportElement/ROLLINGSTOCK,IfcTransportElement/VEHICLE,IfcTransportElement/VEHICLETRACKED,IfcTransportElement/VEHICLEMARINE,IfcTransportElement/VEHICLEAIR,IfcTransportElement/ROLLINGSTOCK
* ApplicableClasses > ClassName "IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLEAIR.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLE.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLETRACKED.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.ROLLINGSTOCK.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;

deletions
---------
* ApplicableClasses > ClassName "IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLE.)"
* ApplicableClasses > ClassName "IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLETRACKED.)"
* ApplicableClasses > ClassName "IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.)"
* ApplicableClasses > ClassName "IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLEAIR.)"
* ApplicableClasses > ClassName "IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.ROLLINGSTOCK.)"










Pset_LinearReferencingMethod.xml
================================

modifications
-------------
* ApplicableClasses > ClassName "IfcReferent/(.POSITION.)"
  ~~IfcReferent/(.POSITION.)~~ IfcReferent/POSITION
* ApplicableTypeValue "IfcAlignment,IfcReferent/(.POSITION.)"
  ~~IfcAlignment,IfcReferent/(.POSITION.)~~ IfcAlignment,IfcReferent/POSITION






Qto_SignalBaseQuantities.xml
============================

additions
---------
* ApplicableTypeValue

























Pset_MarineFacilityTransportation.xml
=====================================

additions
---------
* ApplicableTypeValue
























Pset_DoorWindowGlazingType.xml
==============================

modifications
-------------
* ApplicableTypeValue "IfcDoor, IfcWindow"
  ~~IfcDoor, IfcWindow~~ IfcDoor,IfcWindow



Pset_TrafficCalmingDeviceCommon.xml
===================================

modifications
-------------
* ApplicableClasses > ClassName "IfcElementAssembly/(.TRAFFIC_CALMING_DEVICE.)"
  ~~IfcElementAssembly/(.TRAFFIC_CALMING_DEVICE.)~~ IfcElementAssembly/TRAFFIC_CALMING_DEVICE
* ApplicableTypeValue "IfcElementAssembly/(.TRAFFIC_CALMING_DEVICE.)"
  ~~IfcElementAssembly/(.TRAFFIC_CALMING_DEVICE.)~~ IfcElementAssembly/TRAFFIC_CALMING_DEVICE













Pset_ElementAssemblyCommon.xml
==============================

additions
---------
* ApplicableTypeValue

deletions
---------
* PropertyDefs > PropertyDef [Name="Reference"]


















Pset_RoadGuardElement.xml
=========================

modifications
-------------
* ApplicableTypeValue "IfcRailing/(.GUARDRAIL.),IfcWall/(.PARAPET.)"
  ~~IfcRailing/(.GUARDRAIL.),IfcWall/(.PARAPET.)~~ IfcRailing/GUARDRAIL,IfcWall/PARAPET
* ApplicableClasses > ClassName "IfcRailing/(.GUARDRAIL.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcWall/(.PARAPET.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;



























Pset_SpatialZoneCommon.xml
==========================

additions
---------
* ApplicableTypeValue

deletions
---------
* PropertyDefs > PropertyDef [Name="Reference"]












Qto_ReinforcedSoilBaseQuantities.xml
====================================

additions
---------
* ApplicableTypeValue




Pset_TransportElementElevator.xml
=================================

modifications
-------------
* ApplicableClasses > ClassName "IfcTransportElement/ELEVATOR"
  ~~IfcTransportElement/ELEVATOR~~ IfcTransportElement
* ApplicableTypeValue "IfcTransportElement/ELEVATOR"
  ~~IfcTransportElement/ELEVATOR~~ IfcTransportElement


















Qto_KerbBaseQuantities.xml
==========================

additions
---------
* ApplicableTypeValue




























Pset_StairCommon.xml
====================

deletions
---------
* PropertyDefs > PropertyDef [Name="ThermalTransmittance"]
* PropertyDefs > PropertyDef [Name="LoadBearing"]




Pset_RoadMarkingCommon.xml
==========================

modifications
-------------
* ApplicableTypeValue "IfcSurfaceFeature/(.HATCHMARKING.),IfcSurfaceFeature/(.LINEMARKING.),IfcSurfaceFeature/(.PAVEMENTSURFACEMARKING.),IfcSurfaceFeature/(.SYMBOLMARKING.)"
  ~~IfcSurfaceFeature/(.HATCHMARKING.),IfcSurfaceFeature/(.LINEMARKING.),IfcSurfaceFeature/(.PAVEMENTSURFACEMARKING.),IfcSurfaceFeature/(.SYMBOLMARKING.)~~ IfcSurfaceFeature/HATCHMARKING,IfcSurfaceFeature/LINEMARKING,IfcSurfaceFeature/PAVEMENTSURFACEMARKING,IfcSurfaceFeature/SYMBOLMARKING
* ApplicableClasses > ClassName "IfcSurfaceFeature/(.HATCHMARKING.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcSurfaceFeature/(.LINEMARKING.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcSurfaceFeature/(.SYMBOLMARKING.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcSurfaceFeature/(.PAVEMENTSURFACEMARKING.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="MaterialColour"]






Qto_SignBaseQuantities.xml
==========================

additions
---------
* ApplicableTypeValue






Qto_EarthworksFillBaseQuantities.xml
====================================

additions
---------
* ApplicableTypeValue











Pset_MarkingLinesCommon.xml
===========================

modifications
-------------
* ApplicableClasses > ClassName "IfcSurfaceFeature/(.LINEMARKING.)"
  ~~IfcSurfaceFeature/(.LINEMARKING.)~~ IfcSurfaceFeature/LINEMARKING
* ApplicableTypeValue "IfcSurfaceFeature/(.LINEMARKING.)"
  ~~IfcSurfaceFeature/(.LINEMARKING.)~~ IfcSurfaceFeature/LINEMARKING




Pset_SpaceLightingRequirements.xml
==================================

modifications
-------------
* ApplicableTypeValue "IfcSpace, IfcSpatialZone, IfcZone"
  ~~IfcSpace, IfcSpatialZone, IfcZone~~ IfcSpace,IfcSpatialZone,IfcZone


























Pset_CoveringFlooring.xml
=========================

modifications
-------------
* ApplicableTypeValue "IfcCovering/FLOORING,"
  ~~IfcCovering/FLOORING,~~ IfcCovering/FLOORING

deletions
---------
* ApplicableClasses > ClassName



Qto_PictorialSignQuantities.xml
===============================

additions
---------
* ApplicableTypeValue



Pset_DiscreteAccessoryEdgeFixingPlate.xml
=========================================

modifications
-------------
* ApplicableClasses > ClassName "IfcDiscreteAccessory/Edge fixing plate"
  ~~IfcDiscreteAccessory/Edge fixing plate~~ IfcDiscreteAccessory
* ApplicableTypeValue "IfcDiscreteAccessory/Edge fixing plate"
  ~~IfcDiscreteAccessory/Edge fixing plate~~ IfcDiscreteAccessory




Qto_EarthworksCutBaseQuantities.xml
===================================

additions
---------
* ApplicableTypeValue






Pset_MaterialConcrete.xml
=========================

modifications
-------------
* ApplicableClasses > ClassName "IfcMaterial/Concrete"
  ~~IfcMaterial/Concrete~~ IfcMaterial
* ApplicableTypeValue "IfcMaterial/Concrete"
  ~~IfcMaterial/Concrete~~ IfcMaterial















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









Pset_SpaceThermalRequirements.xml
=================================

modifications
-------------
* ApplicableTypeValue "IfcSpace, IfcSpatialZone, IfcZone"
  ~~IfcSpace, IfcSpatialZone, IfcZone~~ IfcSpace,IfcSpatialZone,IfcZone













Pset_BoreholeCommon.xml
=======================

modifications
-------------
* PropertyDefs > PropertyDef [Name="BoreholeState"] > PropertyType > TypePropertySingleValue > DataType
  ~~IfcBoreholeState~~ UNKNOWN









Pset_FurnitureTypeCommon.xml
============================

deletions
---------
* PropertyDefs > PropertyDef [Name="Reference"]




Pset_AnnotationLineOfSight.xml
==============================

modifications
-------------
* ApplicableClasses > ClassName "IfcAnnotation/LineOfSight"
  ~~IfcAnnotation/LineOfSight~~ IfcAnnotation
* ApplicableTypeValue "IfcAnnotation/LineOfSight"
  ~~IfcAnnotation/LineOfSight~~ IfcAnnotation



Pset_MaterialWoodBasedPanel.xml
===============================

additions
---------
* PropertyDefs > PropertyDef [Name="OutOfPlaneNegative"]

modifications
-------------
* ApplicableClasses > ClassName "IfcMaterial/Wood"
  ~~IfcMaterial/Wood~~ IfcMaterial
* ApplicableTypeValue "IfcMaterial/Wood"
  ~~IfcMaterial/Wood~~ IfcMaterial
* PropertyDefs > PropertyDef [Name="OutOfPlaneNegative"] > PropertyType
  ~~&lt;PropertyType&gt;~~ &lt;PropertyType&gt;
* PropertyDefs > PropertyDef [Name="InPlane"] > PropertyType
  ~~&lt;PropertyType&gt;~~ &lt;PropertyType&gt;
* PropertyDefs > PropertyDef [Name="InPlane"] > Name "InPlane"
  ~~&lt;Name&gt;~~ &lt;Name&gt;
* PropertyDefs > PropertyDef [Name="OutOfPlaneNegative"] > Name "OutOfPlaneNegative"
  ~~&lt;Name&gt;~~ &lt;Name&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="OutOfPlane"]













Pset_DiscreteAccessoryFixingSocket.xml
======================================

modifications
-------------
* ApplicableClasses > ClassName "IfcDiscreteAccessory/Fixing socket"
  ~~IfcDiscreteAccessory/Fixing socket~~ IfcDiscreteAccessory
* ApplicableTypeValue "IfcDiscreteAccessory/Fixing socket"
  ~~IfcDiscreteAccessory/Fixing socket~~ IfcDiscreteAccessory








Pset_Superelevation.xml
=======================

modifications
-------------
* ApplicableClasses > ClassName "IfcAnnotation/(.SUPERELEVATIONEVENT.)"
  ~~IfcAnnotation/(.SUPERELEVATIONEVENT.)~~ IfcAnnotation/SUPERELEVATIONEVENT
* ApplicableTypeValue "IfcAnnotation/(.SUPERELEVATIONEVENT.)"
  ~~IfcAnnotation/(.SUPERELEVATIONEVENT.)~~ IfcAnnotation/SUPERELEVATIONEVENT




Qto_ImpactProtectionDeviceBaseQuantities.xml
============================================

additions
---------
* ApplicableTypeValue





























Pset_DiscreteAccessoryWireLoop.xml
==================================

modifications
-------------
* ApplicableClasses > ClassName "IfcDiscreteAccessory/Wire loop"
  ~~IfcDiscreteAccessory/Wire loop~~ IfcDiscreteAccessory
* ApplicableTypeValue "IfcDiscreteAccessory/Wire loop"
  ~~IfcDiscreteAccessory/Wire loop~~ IfcDiscreteAccessory



Pset_CivilElementCommon.xml
===========================

additions
---------
* ApplicableTypeValue

deletions
---------
* PropertyDefs > PropertyDef [Name="Reference"]



