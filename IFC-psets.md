
Missing in output
=================
* Pset_SpaceThermalRequirements.xml
* Pset_PipeFittingTypeJunction.xml
* Pset_PipeFittingTypeBend.xml
* Pset_ThermalLoadAggregate.xml
* Pset_BuildingElementProxyCommon.xml
* Pset_MaterialWoodBasedBeam.xml
* Pset_MaterialWoodBasedPanel.xml
* Pset_CoveringCeiling.xml
* Pset_SpaceThermalDesign.xml
* Pset_SpaceLightingRequirements.xml
* Pset_BuildingElementProxyProvisionForVoid.xml
* Pset_ThermalLoadDesignCriteria.xml

Missing in reference
=================
* Pset_Tiling.xml
* Pset_ProvisionForVoid.xml
* Pset_MechanicalPanelOutOfPlaneNegative.xml
* Pset_MechanicalPanelOutOfPlane.xml
* Pset_MechanicalBeamInPlaneNegative.xml
* Pset_SignCommon.xml
* Pset_BuiltElementProxyCommon.xml
* Pset_SpaceAirHandlingDimensioning.xml
* Pset_SpaceLightingDesign.xml
* Pset_MechanicalBeamInPlane.xml
* Pset_FittingBend.xml
* Pset_ElementSize.xml
* Pset_MechanicalBeamOutOfPlane.xml
* Pset_ThermalLoad.xml
* Pset_Address.xml
* Pset_MaterialWoodBasedStructure.xml
* Pset_FittingJunction.xml
* Pset_SpaceHVACDesign.xml
* Pset_MechanicalPanelInPlane.xml
* Pset_FittingTransition.xml


Pset_MarkingLinesCommon.xml
===========================

modifications
-------------
* ApplicableClasses > ClassName "IfcSurfaceFeature/(.LINEMARKING.)"
  ~~IfcSurfaceFeature/(.LINEMARKING.)~~ IfcSurfaceFeature/LINEMARKING
* ApplicableTypeValue "IfcSurfaceFeature/(.LINEMARKING.)"
  ~~IfcSurfaceFeature/(.LINEMARKING.)~~ IfcSurfaceFeature/LINEMARKING







Pset_CargoCommon.xml
====================

modifications
-------------
* ApplicableTypeValue "IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.CARGO.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.CARGO.)"
  ~~IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.CARGO.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.CARGO.)~~ IfcVehicle/CARGO,IfcVehicle/CARGO
* PropertyDefs > PropertyDef [Name="ProcessItem"] > PropertyType > TypePropertySingleValue > DataType
  ~~PEnum_ProcessItem~~ UNKNOWN
* ApplicableClasses > ClassName "IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.CARGO.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;

deletions
---------
* ApplicableClasses > ClassName "IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.CARGO.)"


Pset_BoilerPHistory.xml
=======================

additions
---------
* PropertyDefs > PropertyDef [Name="CombustionChamberTemperature"]

modifications
-------------
* PropertyDefs > PropertyDef [Name="CombustionTemperature"] > Name "CombustionTemperature"
  ~~CombustionTemperature~~ WorkingPressureHistory

deletions
---------
* PropertyDefs > PropertyDef [Name="WorkingPressure"]










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


Pset_DuctSilencerTypeCommon.xml
===============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Length"] > PropertyType > TypePropertySingleValue > DataType
  ~~IfcLengthMeasure~~ IfcPositiveLengthMeasure









Qto_PictorialSignQuantities.xml
===============================

additions
---------
* ApplicableTypeValue









Qto_SignalBaseQuantities.xml
============================

additions
---------
* ApplicableTypeValue





Pset_ProtectiveDeviceTrippingUnitTimeAdjustment.xml
===================================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="AdjustmentRange"] > Name "AdjustmentRange"
  ~~AdjustmentRange~~ TimeAdjustmentRange
* PropertyDefs > PropertyDef [Name="AdjustmentRangeStepValue"] > Name "AdjustmentRangeStepValue"
  ~~AdjustmentRangeStepValue~~ TimeAdjustmentRangeStepValue
* PropertyDefs > PropertyDef [Name="AdjustmentValues"] > Name "AdjustmentValues"
  ~~AdjustmentValues~~ TimeAdjustmentValues




Pset_LinearReferencingMethod.xml
================================

modifications
-------------
* ApplicableClasses > ClassName "IfcReferent/(.POSITION.)"
  ~~IfcReferent/(.POSITION.)~~ IfcReferent/POSITION
* ApplicableTypeValue "IfcAlignment,IfcReferent/(.POSITION.)"
  ~~IfcAlignment,IfcReferent/(.POSITION.)~~ IfcAlignment,IfcReferent/POSITION


Pset_AirTerminalOccurrence.xml
==============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Location"] > Name "Location"
  ~~Location~~ AirTerminalLocation



Pset_HeatExchangerTypeCommon.xml
================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Arrangement"] > Name "Arrangement"
  ~~Arrangement~~ FlowArrangement


Pset_PavementMillingCommon.xml
==============================

modifications
-------------
* ApplicableClasses > ClassName "IfcEarthworksCut/(.PAVEMENTMILLING.)"
  ~~IfcEarthworksCut/(.PAVEMENTMILLING.)~~ IfcEarthworksCut/PAVEMENTMILLING
* ApplicableTypeValue "IfcEarthworksCut/(.PAVEMENTMILLING.)"
  ~~IfcEarthworksCut/(.PAVEMENTMILLING.)~~ IfcEarthworksCut/PAVEMENTMILLING



Pset_AirTerminalTypeCommon.xml
==============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Shape"] > Name "Shape"
  ~~Shape~~ AirTerminalShape
* PropertyDefs > PropertyDef [Name="MountingType"] > Name "MountingType"
  ~~MountingType~~ AirTerminalMountingType





Pset_PipeSegmentTypeCulvert.xml
===============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="ClearDepth"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="InternalWidth"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;







Pset_DiscreteAccessoryLadderTrussConnector.xml
==============================================

modifications
-------------
* ApplicableClasses > ClassName "IfcDiscreteAccessory/Ladder truss connector"
  ~~IfcDiscreteAccessory/Ladder truss connector~~ IfcDiscreteAccessory
* ApplicableTypeValue "IfcDiscreteAccessory/Ladder truss connector"
  ~~IfcDiscreteAccessory/Ladder truss connector~~ IfcDiscreteAccessory








Pset_ElementAssemblyCommon.xml
==============================

additions
---------
* ApplicableTypeValue "IfcElementAssembly"

deletions
---------
* PropertyDefs > PropertyDef [Name="Reference"]





Pset_MaintenanceStrategy.xml
============================

modifications
-------------
* ApplicableTypeValue "IfcElement,IfcAsset,IfcSystem"
  ~~IfcElement,IfcAsset,IfcSystem~~ IfcAsset,IfcElement,IfcSystem










Pset_ControllerPHistory.xml
===========================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Value"] > Name "Value"
  ~~Value~~ ValueHistory





Pset_AnnotationSurveyArea.xml
=============================

modifications
-------------
* ApplicableClasses > ClassName "IfcAnnotation/SurveyArea"
  ~~IfcAnnotation/SurveyArea~~ IfcAnnotation
* ApplicableTypeValue "IfcAnnotation/SurveyArea"
  ~~IfcAnnotation/SurveyArea~~ IfcAnnotation







Pset_SumpBusterCommon.xml
=========================

modifications
-------------
* ApplicableClasses > ClassName "IfcElementAssembly/(.SUMPBUSTER.)"
  ~~IfcElementAssembly/(.SUMPBUSTER.)~~ IfcElementAssembly/SUMPBUSTER
* ApplicableTypeValue "IfcElementAssembly/(.SUMPBUSTER.)"
  ~~IfcElementAssembly/(.SUMPBUSTER.)~~ IfcElementAssembly/SUMPBUSTER


Pset_ShadingDeviceCommon.xml
============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="SolarTransmittance"] > PropertyType > TypePropertySingleValue > DataType
  ~~IfcPositiveRatioMeasure~~ IfcNormalisedRatioMeasure
* PropertyDefs > PropertyDef [Name="SolarReflectance"] > PropertyType > TypePropertySingleValue > DataType
  ~~IfcPositiveRatioMeasure~~ IfcNormalisedRatioMeasure
* PropertyDefs > PropertyDef [Name="VisibleLightTransmittance"] > PropertyType > TypePropertySingleValue > DataType
  ~~IfcPositiveRatioMeasure~~ IfcNormalisedRatioMeasure
* PropertyDefs > PropertyDef [Name="VisibleLightReflectance"] > PropertyType > TypePropertySingleValue > DataType
  ~~IfcPositiveRatioMeasure~~ IfcNormalisedRatioMeasure


Pset_DistributionPortPHistoryDuct.xml
=====================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="FlowCondition"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Velocity"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Pressure"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="WetBulbTemperature"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="VolumetricFlowRate"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Temperature"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="MassFlowRate"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;












Pset_Risk.xml
=============

modifications
-------------
* ApplicableTypeValue "IfcProcess,IfcTypeProcess,IfcProduct,IfcTypeProduct,IfcGroup"
  ~~IfcProcess,IfcTypeProcess,IfcProduct,IfcTypeProduct,IfcGroup~~ IfcGroup,IfcProcess,IfcProduct,IfcTypeProcess,IfcTypeProduct


Pset_MarineFacilityTransportation.xml
=====================================

additions
---------
* ApplicableTypeValue "IfcMarineFacility"







Pset_CableCarrierSegmentTypeCableTraySegment.xml
================================================

deletions
---------
* PropertyDefs > PropertyDef [Name="NominalWidth"]
* PropertyDefs > PropertyDef [Name="NominalHeight"]




Pset_CableCarrierSegmentTypeCableLadderSegment.xml
==================================================

deletions
---------
* PropertyDefs > PropertyDef [Name="NominalWidth"]
* PropertyDefs > PropertyDef [Name="NominalHeight"]




Pset_EnvironmentalImpactIndicators.xml
======================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Unit"] > Name "Unit"
  ~~Unit~~ IndicatorsUnit


Pset_ControllerTypeMultiPosition.xml
====================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Range"] > Name "Range"
  ~~Range~~ IntegerRange


Pset_MarineVehicleDesignCriteria.xml
====================================

modifications
-------------
* ApplicableTypeValue "IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.)"
  ~~IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.)~~ IfcVehicle/VEHICLEMARINE,IfcVehicle/VEHICLEMARINE
* ApplicableClasses > ClassName "IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;

deletions
---------
* ApplicableClasses > ClassName "IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.)"



Pset_ElementKinematics.xml
==========================

modifications
-------------
* PropertyDefs > PropertyDef [Name="MaximumConstantSpeed"] > PropertyType > TypePropertySingleValue > DataType
  ~~IfcVelocityMeasure~~ UNKNOWN




Pset_MaterialWood.xml
=====================

modifications
-------------
* ApplicableClasses > ClassName "IfcMaterial/Wood"
  ~~IfcMaterial/Wood~~ IfcMaterial
* ApplicableTypeValue "IfcMaterial/Wood"
  ~~IfcMaterial/Wood~~ IfcMaterial


Pset_UnitaryControlElementTypeIndicatorPanel.xml
================================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Application"] > Name "Application"
  ~~Application~~ UnitaryApplication



Pset_RampCommon.xml
===================

deletions
---------
* PropertyDefs > PropertyDef [Name="ThermalTransmittance"]
* PropertyDefs > PropertyDef [Name="LoadBearing"]


Pset_FurnitureTypeCommon.xml
============================

deletions
---------
* PropertyDefs > PropertyDef [Name="Reference"]



Pset_Condition.xml
==================

modifications
-------------
* ApplicableTypeValue "IfcElement,IfcSystem,IfcAsset"
  ~~IfcElement,IfcSystem,IfcAsset~~ IfcAsset,IfcElement,IfcSystem










Pset_MaterialConcrete.xml
=========================

modifications
-------------
* ApplicableClasses > ClassName "IfcMaterial/Concrete"
  ~~IfcMaterial/Concrete~~ IfcMaterial
* ApplicableTypeValue "IfcMaterial/Concrete"
  ~~IfcMaterial/Concrete~~ IfcMaterial



Qto_SurfaceFeatureBaseQuantities.xml
====================================

additions
---------
* ApplicableTypeValue



Pset_ActuatorPHistory.xml
=========================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Quality"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Position"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Status"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;












Pset_CooledBeamTypeActive.xml
=============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="ConnectionSize"] > PropertyType > TypePropertySingleValue > DataType
  ~~IfcLengthMeasure~~ IfcPositiveLengthMeasure










Pset_TankTypeCommon.xml
=======================

modifications
-------------
* PropertyDefs > PropertyDef [Name="NominalCapacity"] > Name "NominalCapacity"
  ~~NominalCapacity~~ TankNominalCapacity



Pset_ChillerTypeCommon.xml
==========================

modifications
-------------
* PropertyDefs > PropertyDef [Name="NominalCapacity"] > Name "NominalCapacity"
  ~~NominalCapacity~~ ChillerCapacity











Qto_ReinforcedSoilBaseQuantities.xml
====================================

additions
---------
* ApplicableTypeValue






Pset_TankTypePreformed.xml
==========================

modifications
-------------
* ApplicableClasses > ClassName "IfcTank/PREFORMED"
  ~~IfcTank/PREFORMED~~ IfcTank
* ApplicableTypeValue "IfcTank/PREFORMED"
  ~~IfcTank/PREFORMED~~ IfcTank





Pset_SpaceCommon.xml
====================

modifications
-------------
* ApplicableClasses > ClassName "IfcSpace"
  ~~IfcSpace~~ IfcSpatialElement
* ApplicableTypeValue "IfcSpace"
  ~~IfcSpace~~ IfcSpatialElement




Pset_Width.xml
==============

modifications
-------------
* ApplicableClasses > ClassName "IfcAnnotation/(.WIDTHEVENT.)"
  ~~IfcAnnotation/(.WIDTHEVENT.)~~ IfcAnnotation/WIDTHEVENT
* ApplicableTypeValue "IfcAnnotation/(.WIDTHEVENT.)"
  ~~IfcAnnotation/(.WIDTHEVENT.)~~ IfcAnnotation/WIDTHEVENT



Pset_SpaceHeaterPHistory.xml
============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Exponent"] > Name "Exponent"
  ~~Exponent~~ CharacteristicExponent





Pset_SwitchingDeviceTypePHistory.xml
====================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="SetPoint"] > Name "SetPoint"
  ~~SetPoint~~ SetPointHistory






Pset_DamperTypeFireSmokeDamper.xml
==================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="ControlType"] > Name "ControlType"
  ~~ControlType~~ DamperControlType


Pset_DistributionChamberElementTypeInspectionChamber.xml
========================================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="InvertLevel"] > Name "InvertLevel"
  ~~InvertLevel~~ InspectionChamberInvertLevel



Pset_JunctionBoxTypeCommon.xml
==============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="NumberOfGangs"] > PropertyType > TypePropertySingleValue > DataType
  ~~IfcInteger~~ IfcCountMeasure
* PropertyDefs > PropertyDef [Name="MountingType"] > Name "MountingType"
  ~~MountingType~~ JunctionBoxMountingType




Pset_MaterialSteel.xml
======================

modifications
-------------
* ApplicableClasses > ClassName "IfcMaterial/Steel"
  ~~IfcMaterial/Steel~~ IfcMaterial
* ApplicableTypeValue "IfcMaterial/Steel"
  ~~IfcMaterial/Steel~~ IfcMaterial




Pset_MaintenanceTriggerDuration.xml
===================================

modifications
-------------
* ApplicableTypeValue "IfcElement,IfcAsset,IfcSystem"
  ~~IfcElement,IfcAsset,IfcSystem~~ IfcAsset,IfcElement,IfcSystem



Pset_TrafficCalmingDeviceCommon.xml
===================================

modifications
-------------
* ApplicableClasses > ClassName "IfcElementAssembly/(.TRAFFIC_CALMING_DEVICE.)"
  ~~IfcElementAssembly/(.TRAFFIC_CALMING_DEVICE.)~~ IfcElementAssembly/TRAFFIC_CALMING_DEVICE
* ApplicableTypeValue "IfcElementAssembly/(.TRAFFIC_CALMING_DEVICE.)"
  ~~IfcElementAssembly/(.TRAFFIC_CALMING_DEVICE.)~~ IfcElementAssembly/TRAFFIC_CALMING_DEVICE



Pset_MaintenanceTriggerPerformance.xml
======================================

modifications
-------------
* ApplicableTypeValue "IfcElement,IfcAsset,IfcSystem"
  ~~IfcElement,IfcAsset,IfcSystem~~ IfcAsset,IfcElement,IfcSystem
* PropertyDefs > PropertyDef [Name="MaintenanceLevel"] > Name "MaintenanceLevel"
  ~~MaintenanceLevel~~ PerformanceMaintenanceLevel


Pset_SpaceThermalLoad.xml
=========================

modifications
-------------
* ApplicableClasses > ClassName "IfcSpace"
  ~~IfcSpace~~ IfcSpatialElement
* ApplicableTypeValue "IfcSpace"
  ~~IfcSpace~~ IfcSpatialElement







Pset_RoadDesignCriteriaCommon.xml
=================================

additions
---------
* ApplicableClasses > ClassName "IfcFacilityPartCommon/JUNCTION"

modifications
-------------
* ApplicableTypeValue "IfcRoad,IfcFacilityPart/IfcRoadPartTypeEnum(.ROADSEGMENT.),IfcFacilityPart/IfcFacilityPartCommonTypeEnum(.SEGMENT.),IfcFacilityPart/IfcFacilityPartCommonTypeEnum(.JUNCTION.),IfcFacilityPart/IfcFacilityPartCommonTypeEnum(.LEVELCROSSING.),IfcFacilityPart/IfcRoadPartTypeEnum(.RAILWAYCROSSING.),IfcFacilityPart/IfcRoadPartTypeEnum(.PEDESTRIAN_CROSSING.),IfcFacilityPart/IfcRoadPartTypeEnum(.BICYCLECROSSING.),IfcFacilityPart/IfcRoadPartTypeEnum(.ROUNDABOUT.),IfcFacilityPart/IfcRoadPartTypeEnum(.INTERSECTION.),IfcFacilityPart/IfcRoadPartTypeEnum(.TOLLPLAZA.)"
  ~~IfcRoad,IfcFacilityPart/IfcRoadPartTypeEnum(.ROADSEGMENT.),IfcFacilityPart/IfcFacilityPartCommonTypeEnum(.SEGMENT.),IfcFacilityPart/IfcFacilityPartCommonTypeEnum(.JUNCTION.),IfcFacilityPart/IfcFacilityPartCommonTypeEnum(.LEVELCROSSING.),IfcFacilityPart/IfcRoadPartTypeEnum(.RAILWAYCROSSING.),IfcFacilityPart/IfcRoadPartTypeEnum(.PEDESTRIAN_CROSSING.),IfcFacilityPart/IfcRoadPartTypeEnum(.BICYCLECROSSING.),IfcFacilityPart/IfcRoadPartTypeEnum(.ROUNDABOUT.),IfcFacilityPart/IfcRoadPartTypeEnum(.INTERSECTION.),IfcFacilityPart/IfcRoadPartTypeEnum(.TOLLPLAZA.)~~ IfcFacilityPartCommon/JUNCTION,IfcFacilityPartCommon/LEVELCROSSING,IfcFacilityPartCommon/SEGMENT,IfcRoadPart/BICYCLECROSSING,IfcRoadPart/INTERSECTION,IfcRoadPart/PEDESTRIAN_CROSSING,IfcRoadPart/RAILWAYCROSSING,IfcRoadPart/ROADSEGMENT,IfcRoadPart/ROUNDABOUT,IfcRoadPart/TOLLPLAZA,IfcRoad
* ApplicableClasses > ClassName "IfcFacilityPart/IfcRoadPartTypeEnum(.RAILWAYCROSSING.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcFacilityPart/IfcRoadPartTypeEnum(.PEDESTRIAN_CROSSING.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcFacilityPart/IfcFacilityPartCommonTypeEnum(.LEVELCROSSING.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcFacilityPart/IfcFacilityPartCommonTypeEnum(.JUNCTION.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcFacilityPart/IfcRoadPartTypeEnum(.ROADSEGMENT.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcFacilityPart/IfcRoadPartTypeEnum(.INTERSECTION.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcFacilityPart/IfcFacilityPartCommonTypeEnum(.SEGMENT.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcFacilityPart/IfcRoadPartTypeEnum(.BICYCLECROSSING.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcFacilityPart/IfcRoadPartTypeEnum(.ROUNDABOUT.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;

deletions
---------
* ApplicableClasses > ClassName "IfcFacilityPart/IfcRoadPartTypeEnum(.TOLLPLAZA.)"





Pset_VehicleAvailability.xml
============================

modifications
-------------
* ApplicableTypeValue "IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLE.),IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLETRACKED.),IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.),IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLEAIR.),IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.ROLLINGSTOCK.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLE.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLETRACKED.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLEAIR.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.ROLLINGSTOCK.)"
  ~~IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLE.),IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLETRACKED.),IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.),IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLEAIR.),IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.ROLLINGSTOCK.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLE.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLETRACKED.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLEAIR.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.ROLLINGSTOCK.)~~ IfcVehicle/ROLLINGSTOCK,IfcVehicle/ROLLINGSTOCK,IfcVehicle/VEHICLEAIR,IfcVehicle/VEHICLEAIR,IfcVehicle/VEHICLEMARINE,IfcVehicle/VEHICLEMARINE,IfcVehicle/VEHICLE,IfcVehicle/VEHICLE,IfcVehicle/VEHICLETRACKED,IfcVehicle/VEHICLETRACKED
* ApplicableClasses > ClassName "IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLETRACKED.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLEAIR.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.ROLLINGSTOCK.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLE.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;

deletions
---------
* ApplicableClasses > ClassName "IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLETRACKED.)"
* ApplicableClasses > ClassName "IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLEAIR.)"
* ApplicableClasses > ClassName "IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLE.)"
* ApplicableClasses > ClassName "IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.)"
* ApplicableClasses > ClassName "IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.ROLLINGSTOCK.)"





Pset_DiscreteAccessoryEdgeFixingPlate.xml
=========================================

modifications
-------------
* ApplicableClasses > ClassName "IfcDiscreteAccessory/Edge fixing plate"
  ~~IfcDiscreteAccessory/Edge fixing plate~~ IfcDiscreteAccessory
* ApplicableTypeValue "IfcDiscreteAccessory/Edge fixing plate"
  ~~IfcDiscreteAccessory/Edge fixing plate~~ IfcDiscreteAccessory







Pset_TransportElementCommon.xml
===============================

modifications
-------------
* ApplicableClasses > ClassName "IfcTransportElement"
  ~~IfcTransportElement~~ IfcTransportationDevice
* ApplicableTypeValue "IfcTransportElement"
  ~~IfcTransportElement~~ IfcTransportationDevice















Pset_ActorCommon.xml
====================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Category"] > Name "Category"
  ~~Category~~ ActorCategory







Pset_GeotechnicalAssemblyCommon.xml
===================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Purpose"] > Name "Purpose"
  ~~Purpose~~ BoreHolePurpose



Pset_MarineVehicleCommon.xml
============================

modifications
-------------
* ApplicableTypeValue "IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.)"
  ~~IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.)~~ IfcVehicle/VEHICLEMARINE,IfcVehicle/VEHICLEMARINE
* 
  ~~QTO_TYPEDRIVENOVERRIDE~~ PSET_TYPEDRIVENOVERRIDE
* ApplicableClasses > ClassName "IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;

deletions
---------
* ApplicableClasses > ClassName "IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.)"


Pset_CableCarrierSegmentTypeConduitSegment.xml
==============================================

deletions
---------
* PropertyDefs > PropertyDef [Name="NominalWidth"]
* PropertyDefs > PropertyDef [Name="NominalHeight"]


Pset_DoorWindowGlazingType.xml
==============================

modifications
-------------
* ApplicableTypeValue "IfcDoor, IfcWindow"
  ~~IfcDoor, IfcWindow~~ IfcDoor,IfcWindow





Pset_ActuatorTypeCommon.xml
===========================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Status"] > Name "Status"
  ~~Status~~ ActuatorStatus
* PropertyDefs > PropertyDef [Name="Application"] > Name "Application"
  ~~Application~~ ActuatorApplication


Pset_SpaceOccupancyRequirements.xml
===================================

modifications
-------------
* ApplicableClasses > ClassName "IfcSpace"
  ~~IfcSpace~~ IfcSpatialElement
* ApplicableTypeValue "IfcSpace, IfcSpatialZone, IfcZone"
  ~~IfcSpace, IfcSpatialZone, IfcZone~~ IfcSpatialElement,IfcSpatialZone,IfcZone




Pset_FanCentrifugal.xml
=======================

modifications
-------------
* ApplicableClasses > ClassName "IfcFan/CENTRIFUGAL"
  ~~IfcFan/CENTRIFUGAL~~ IfcFan
* ApplicableTypeValue "IfcFan/CENTRIFUGAL"
  ~~IfcFan/CENTRIFUGAL~~ IfcFan
* PropertyDefs > PropertyDef [Name="Arrangement"] > Name "Arrangement"
  ~~Arrangement~~ FanArrangement











Pset_GateHeadCommon.xml
=======================

modifications
-------------
* ApplicableClasses > ClassName "IfcFacilityPart/IfcMarinePartTypeEnum(.GATEHEAD.)"
  ~~IfcFacilityPart/IfcMarinePartTypeEnum(.GATEHEAD.)~~ IfcMarinePart/GATEHEAD
* ApplicableTypeValue "IfcFacilityPart/IfcMarinePartTypeEnum(.GATEHEAD.)"
  ~~IfcFacilityPart/IfcMarinePartTypeEnum(.GATEHEAD.)~~ IfcMarinePart/GATEHEAD



Pset_BoreholeCommon.xml
=======================

modifications
-------------
* PropertyDefs > PropertyDef [Name="BoreholeState"] > PropertyType > TypePropertySingleValue > DataType
  ~~IfcBoreholeState~~ UNKNOWN








Pset_AlarmTypeCommon.xml
========================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Condition"] > Name "Condition"
  ~~Condition~~ AlarmCondition















Pset_PrecastConcreteElementGeneral.xml
======================================

modifications
-------------
* ApplicableClasses > ClassName "IfcBuildingElementProxy"
  ~~IfcBuildingElementProxy~~ IfcBuiltElementProxy
* ApplicableTypeValue "IfcBeam,IfcBuildingElementProxy,IfcChimney,IfcColumn,IfcFooting,IfcMember,IfcPile,IfcPlate,IfcRamp,IfcRampFlight,IfcRoof,IfcSlab,IfcStair,IfcStairFlight,IfcWall,IfcCivilElement"
  ~~IfcBeam,IfcBuildingElementProxy,IfcChimney,IfcColumn,IfcFooting,IfcMember,IfcPile,IfcPlate,IfcRamp,IfcRampFlight,IfcRoof,IfcSlab,IfcStair,IfcStairFlight,IfcWall,IfcCivilElement~~ IfcBeam,IfcBuiltElementProxy,IfcChimney,IfcCivilElement,IfcColumn,IfcFooting,IfcMember,IfcPile,IfcPlate,IfcRampFlight,IfcRamp,IfcRoof,IfcSlab,IfcStairFlight,IfcStair,IfcWall



Pset_TankTypeSectional.xml
==========================

modifications
-------------
* ApplicableClasses > ClassName "IfcTank/SECTIONAL"
  ~~IfcTank/SECTIONAL~~ IfcTank
* ApplicableTypeValue "IfcTank/SECTIONAL"
  ~~IfcTank/SECTIONAL~~ IfcTank






Pset_CableCarrierSegmentTypeCableTrunkingSegment.xml
====================================================

deletions
---------
* PropertyDefs > PropertyDef [Name="NominalWidth"]
* PropertyDefs > PropertyDef [Name="NominalHeight"]














Qto_SignBaseQuantities.xml
==========================

additions
---------
* ApplicableTypeValue






Pset_SensorTypeLevelSensor.xml
==============================

modifications
-------------
* ApplicableClasses > ClassName "IfcSensor/LEVEL"
  ~~IfcSensor/LEVEL~~ IfcSensor
* ApplicableTypeValue "IfcSensor/LEVEL"
  ~~IfcSensor/LEVEL~~ IfcSensor


Pset_DiscreteAccessoryCornerFixingPlate.xml
===========================================

modifications
-------------
* ApplicableClasses > ClassName "IfcDiscreteAccessory/Corner fixing plate"
  ~~IfcDiscreteAccessory/Corner fixing plate~~ IfcDiscreteAccessory
* ApplicableTypeValue "IfcDiscreteAccessory/Corner fixing plate"
  ~~IfcDiscreteAccessory/Corner fixing plate~~ IfcDiscreteAccessory


Pset_AirTerminalPHistory.xml
============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="AirFlowRate"] > Name "AirFlowRate"
  ~~AirFlowRate~~ AirFlowRateHistory



Pset_AlarmPHistory.xml
======================

additions
---------
* PropertyDefs > PropertyDef [Name="UserHistory"]

modifications
-------------
* PropertyDefs > PropertyDef [Name="User"] > Name "User"
  ~~User~~ ConditionHistory

deletions
---------
* PropertyDefs > PropertyDef [Name="Condition"]


Pset_UnitaryControlElementTypeCommon.xml
========================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Mode"] > Name "Mode"
  ~~Mode~~ OperationMode










Pset_MaterialOptical.xml
========================

modifications
-------------
* PropertyDefs > PropertyDef [Name="VisibleReflectanceBack"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="ThermalIrEmissivityBack"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="SolarReflectanceFront"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="SolarReflectanceBack"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="VisibleTransmittance"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="SolarTransmittance"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="ThermalIrEmissivityFront"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="ThermalIrTransmittance"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="VisibleReflectanceFront"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;










Pset_GeotechnicalStratumCommon.xml
==================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Colour"] > Name "Colour"
  ~~Colour~~ StratumColour





Pset_TransitionSectionCommon.xml
================================

modifications
-------------
* ApplicableClasses > ClassName "IfcEarthworksFill/(.TRANSITIONSECTION.)"
  ~~IfcEarthworksFill/(.TRANSITIONSECTION.)~~ IfcEarthworksFill/TRANSITIONSECTION
* ApplicableTypeValue "IfcEarthworksFill/(.TRANSITIONSECTION.)"
  ~~IfcEarthworksFill/(.TRANSITIONSECTION.)~~ IfcEarthworksFill/TRANSITIONSECTION





Pset_TransportElementElevator.xml
=================================

modifications
-------------
* ApplicableClasses > ClassName "IfcTransportElement/ELEVATOR"
  ~~IfcTransportElement/ELEVATOR~~ IfcTransportationDevice
* ApplicableTypeValue "IfcTransportElement/ELEVATOR"
  ~~IfcTransportElement/ELEVATOR~~ IfcTransportationDevice








Pset_RoadSymbolsCommon.xml
==========================

modifications
-------------
* ApplicableClasses > ClassName "IfcSurfaceFeature/(.SYMBOLMARKING.)"
  ~~IfcSurfaceFeature/(.SYMBOLMARKING.)~~ IfcSurfaceFeature/SYMBOLMARKING
* ApplicableTypeValue "IfcSurfaceFeature/(.SYMBOLMARKING.)"
  ~~IfcSurfaceFeature/(.SYMBOLMARKING.)~~ IfcSurfaceFeature/SYMBOLMARKING









Pset_SolidStratumCapacity.xml
=============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="HydraulicConductivity"] > PropertyType > TypePropertySingleValue > DataType
  ~~IfcVelocityMeasure~~ UNKNOWN
* PropertyDefs > PropertyDef [Name="LoadbearingCapacity"] > PropertyType > TypePropertySingleValue > DataType
  ~~PressureMeasure~~ IfcPlanarForceMeasure
* PropertyDefs > PropertyDef [Name="PwaveVelocity"] > PropertyType > TypePropertySingleValue > DataType
  ~~IfcVelocityMeasure~~ UNKNOWN
* PropertyDefs > PropertyDef [Name="SwaveVelocity"] > PropertyType > TypePropertySingleValue > DataType
  ~~IfcVelocityMeasure~~ UNKNOWN




Pset_PumpPHistory.xml
=====================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Power"] > Name "Power"
  ~~Power~~ PowerHistory


Pset_AirSideSystemInformation.xml
=================================

modifications
-------------
* ApplicableClasses > ClassName "IfcSpace"
  ~~IfcSpace~~ IfcSpatialElement
* ApplicableTypeValue "IfcSpace,IfcZone,IfcSpatialZone"
  ~~IfcSpace,IfcZone,IfcSpatialZone~~ IfcSpatialElement,IfcSpatialZone,IfcZone
* PropertyDefs > PropertyDef [Name="Description"] > PropertyType > TypePropertySingleValue > DataType
  ~~IfcLabel~~ IfcText

deletions
---------
* PropertyDefs > PropertyDef [Name="Name"]
* PropertyDefs > PropertyDef [Name="LightingDiversity"]
* PropertyDefs > PropertyDef [Name="LoadSafetyFactor"]


Pset_BoilerTypeSteam.xml
========================

modifications
-------------
* PropertyDefs > PropertyDef [Name="NominalEfficiency"] > Name "NominalEfficiency"
  ~~NominalEfficiency~~ NominalEfficiencyTable








Pset_DiscreteAccessoryDiagonalTrussConnector.xml
================================================

modifications
-------------
* ApplicableClasses > ClassName "IfcDiscreteAccessory/Diagonal truss connector"
  ~~IfcDiscreteAccessory/Diagonal truss connector~~ IfcDiscreteAccessory
* ApplicableTypeValue "IfcDiscreteAccessory/Diagonal truss connector"
  ~~IfcDiscreteAccessory/Diagonal truss connector~~ IfcDiscreteAccessory



Pset_HumidifierTypeCommon.xml
=============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Application"] > Name "Application"
  ~~Application~~ HumidifierApplication





Pset_TubeBundleTypeCommon.xml
=============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="NumberOfRows"] > PropertyType > TypePropertySingleValue > DataType
  ~~IfcInteger~~ IfcCountMeasure
* PropertyDefs > PropertyDef [Name="NumberOfCircuits"] > PropertyType > TypePropertySingleValue > DataType
  ~~IfcInteger~~ IfcCountMeasure










Pset_DuctSegmentTypeCommon.xml
==============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Shape"] > Name "Shape"
  ~~Shape~~ CrossSectionShape



Pset_ConcreteElementGeneral.xml
===============================

modifications
-------------
* ApplicableClasses > ClassName "IfcBuildingElementProxy"
  ~~IfcBuildingElementProxy~~ IfcBuiltElementProxy
* ApplicableTypeValue "IfcBeam,IfcBuildingElementProxy,IfcChimney,IfcColumn,IfcFooting,IfcMember,IfcPile,IfcPlate,IfcRailing,IfcRamp,IfcRampFlight,IfcRoof,IfcSlab,IfcStair,IfcStairFlight,IfcWall,IfcCivilElement"
  ~~IfcBeam,IfcBuildingElementProxy,IfcChimney,IfcColumn,IfcFooting,IfcMember,IfcPile,IfcPlate,IfcRailing,IfcRamp,IfcRampFlight,IfcRoof,IfcSlab,IfcStair,IfcStairFlight,IfcWall,IfcCivilElement~~ IfcBeam,IfcBuiltElementProxy,IfcChimney,IfcCivilElement,IfcColumn,IfcFooting,IfcMember,IfcPile,IfcPlate,IfcRailing,IfcRampFlight,IfcRamp,IfcRoof,IfcSlab,IfcStairFlight,IfcStair,IfcWall



Pset_SoundAttenuation.xml
=========================

modifications
-------------
* ApplicableClasses > ClassName "IfcAnnotation/SOUND"
  ~~IfcAnnotation/SOUND~~ IfcAnnotation
* ApplicableTypeValue "IfcAnnotation/SOUND"
  ~~IfcAnnotation/SOUND~~ IfcAnnotation



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




Pset_DiscreteAccessoryWireLoop.xml
==================================

modifications
-------------
* ApplicableClasses > ClassName "IfcDiscreteAccessory/Wire loop"
  ~~IfcDiscreteAccessory/Wire loop~~ IfcDiscreteAccessory
* ApplicableTypeValue "IfcDiscreteAccessory/Wire loop"
  ~~IfcDiscreteAccessory/Wire loop~~ IfcDiscreteAccessory






Qto_KerbBaseQuantities.xml
==========================

additions
---------
* ApplicableTypeValue






Qto_VehicleBaseQuantities.xml
=============================

modifications
-------------
* ApplicableTypeValue "IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLE.),IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLETRACKED.),IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.),IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLEAIR.),IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.ROLLINGSTOCK.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLE.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLETRACKED.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLEAIR.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.ROLLINGSTOCK.)"
  ~~IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLE.),IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLETRACKED.),IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.),IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLEAIR.),IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.ROLLINGSTOCK.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLE.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLETRACKED.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLEAIR.),IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.ROLLINGSTOCK.)~~ IfcVehicle/ROLLINGSTOCK,IfcVehicle/ROLLINGSTOCK,IfcVehicle/VEHICLEAIR,IfcVehicle/VEHICLEAIR,IfcVehicle/VEHICLEMARINE,IfcVehicle/VEHICLEMARINE,IfcVehicle/VEHICLE,IfcVehicle/VEHICLE,IfcVehicle/VEHICLETRACKED,IfcVehicle/VEHICLETRACKED
* ApplicableClasses > ClassName "IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLEAIR.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.ROLLINGSTOCK.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLE.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLETRACKED.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;

deletions
---------
* ApplicableClasses > ClassName "IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLETRACKED.)"
* ApplicableClasses > ClassName "IfcTransportElement/IfcTransportElementNonFixedTypeEnum(.VEHICLEAIR.)"
* ApplicableClasses > ClassName "IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLE.)"
* ApplicableClasses > ClassName "IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.VEHICLEMARINE.)"
* ApplicableClasses > ClassName "IfcTransportElementType/IfcTransportElementNonFixedTypeEnum(.ROLLINGSTOCK.)"




Pset_RoofCommon.xml
===================

deletions
---------
* PropertyDefs > PropertyDef [Name="LoadBearing"]


Pset_UnitaryControlElementPHistory.xml
======================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Mode"] > Name "Mode"
  ~~Mode~~ OperationModeHistory




Pset_AudioVisualAppliancePHistory.xml
=====================================

additions
---------
* PropertyDefs > PropertyDef [Name="AudioVolumeHistory"]

modifications
-------------
* PropertyDefs > PropertyDef [Name="AudioVolume"] > Name "AudioVolume"
  ~~AudioVolume~~ MediaSourceHistory

deletions
---------
* PropertyDefs > PropertyDef [Name="MediaSource"]







Pset_StairCommon.xml
====================

deletions
---------
* PropertyDefs > PropertyDef [Name="ThermalTransmittance"]
* PropertyDefs > PropertyDef [Name="LoadBearing"]



Pset_AnnotationContourLine.xml
==============================

modifications
-------------
* ApplicableClasses > ClassName "IfcAnnotation/ContourLine"
  ~~IfcAnnotation/ContourLine~~ IfcAnnotation
* ApplicableTypeValue "IfcAnnotation/ContourLine"
  ~~IfcAnnotation/ContourLine~~ IfcAnnotation






Qto_BuildingElementProxyQuantities.xml
======================================

modifications
-------------
* ApplicableClasses > ClassName "IfcBuildingElementProxy"
  ~~IfcBuildingElementProxy~~ IfcBuiltElementProxy
* ApplicableTypeValue "IfcBuildingElementProxy"
  ~~IfcBuildingElementProxy~~ IfcBuiltElementProxy



Pset_CoilPHistory.xml
=====================

additions
---------
* PropertyDefs > PropertyDef [Name="SoundCurveHistory"]

modifications
-------------
* PropertyDefs > PropertyDef [Name="SoundCurve"] > Name "SoundCurve"
  ~~SoundCurve~~ AirPressureDropCurveHistory

deletions
---------
* PropertyDefs > PropertyDef [Name="AirPressureDropCurve"]





Pset_SpaceThermalLoadPHistory.xml
=================================

modifications
-------------
* ApplicableClasses > ClassName "IfcSpace"
  ~~IfcSpace~~ IfcSpatialElement
* ApplicableTypeValue "IfcSpace"
  ~~IfcSpace~~ IfcSpatialElement
* PropertyDefs > PropertyDef [Name="DryBulbTemperature"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="RecirculatedAir"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="VentilationOutdoorAir"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="Lighting"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="EquipmentSensible"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="ExhaustAir"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="InfiltrationSensible"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="AirExchangeRate"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="People"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="TotalLatentLoad"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="TotalSensibleLoad"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="RelativeHumidity"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="VentilationIndoorAir"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;
* PropertyDefs > PropertyDef [Name="TotalRadiantLoad"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;








Pset_DiscreteAccessoryFixingSocket.xml
======================================

modifications
-------------
* ApplicableClasses > ClassName "IfcDiscreteAccessory/Fixing socket"
  ~~IfcDiscreteAccessory/Fixing socket~~ IfcDiscreteAccessory
* ApplicableTypeValue "IfcDiscreteAccessory/Fixing socket"
  ~~IfcDiscreteAccessory/Fixing socket~~ IfcDiscreteAccessory








Pset_FlowMeterOccurrence.xml
============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Purpose"] > Name "Purpose"
  ~~Purpose~~ FlowMeterOurpose




Qto_EarthworksCutBaseQuantities.xml
===================================

additions
---------
* ApplicableTypeValue



Qto_ImpactProtectionDeviceBaseQuantities.xml
============================================

additions
---------
* ApplicableTypeValue



Pset_PrecastConcreteElementFabrication.xml
==========================================

modifications
-------------
* ApplicableClasses > ClassName "IfcBuildingElementProxy"
  ~~IfcBuildingElementProxy~~ IfcBuiltElementProxy
* ApplicableTypeValue "IfcBeam,IfcBuildingElementProxy,IfcChimney,IfcColumn,IfcFooting,IfcMember,IfcPile,IfcPlate,IfcRamp,IfcRampFlight,IfcRoof,IfcSlab,IfcStair,IfcStairFlight,IfcWall,IfcCivilElement"
  ~~IfcBeam,IfcBuildingElementProxy,IfcChimney,IfcColumn,IfcFooting,IfcMember,IfcPile,IfcPlate,IfcRamp,IfcRampFlight,IfcRoof,IfcSlab,IfcStair,IfcStairFlight,IfcWall,IfcCivilElement~~ IfcBeam,IfcBuiltElementProxy,IfcChimney,IfcCivilElement,IfcColumn,IfcFooting,IfcMember,IfcPile,IfcPlate,IfcRampFlight,IfcRamp,IfcRoof,IfcSlab,IfcStairFlight,IfcStair,IfcWall





Pset_DistributionPortPHistoryCable.xml
======================================

additions
---------
* PropertyDefs > PropertyDef [Name="PowerFactorHistory"]

modifications
-------------
* PropertyDefs > PropertyDef [Name="PowerFactor"] > Name "PowerFactor"
  ~~PowerFactor~~ CurrentHistory
* PropertyDefs > PropertyDef [Name="Voltage"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="Current"]


Pset_Superelevation.xml
=======================

modifications
-------------
* ApplicableClasses > ClassName "IfcAnnotation/(.SUPERELEVATIONEVENT.)"
  ~~IfcAnnotation/(.SUPERELEVATIONEVENT.)~~ IfcAnnotation/SUPERELEVATIONEVENT
* ApplicableTypeValue "IfcAnnotation/(.SUPERELEVATIONEVENT.)"
  ~~IfcAnnotation/(.SUPERELEVATIONEVENT.)~~ IfcAnnotation/SUPERELEVATIONEVENT






Pset_CableSegmentTypeConductorSegment.xml
=========================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Material"] > Name "Material"
  ~~Material~~ ConductorMaterial
* PropertyDefs > PropertyDef [Name="Shape"] > Name "Shape"
  ~~Shape~~ ConductorShape



Pset_SpatialZoneCommon.xml
==========================

additions
---------
* ApplicableTypeValue "IfcSpatialZone"

deletions
---------
* PropertyDefs > PropertyDef [Name="Reference"]


Pset_ProtectiveDeviceTrippingUnitCurrentAdjustment.xml
======================================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="AdjustmentRange"] > Name "AdjustmentRange"
  ~~AdjustmentRange~~ CurrentAdjustmentRange
* PropertyDefs > PropertyDef [Name="AdjustmentRangeStepValue"] > Name "AdjustmentRangeStepValue"
  ~~AdjustmentRangeStepValue~~ CurrentAdjustmentRangeStepValue
* PropertyDefs > PropertyDef [Name="AdjustmentValues"] > Name "AdjustmentValues"
  ~~AdjustmentValues~~ CurrentAdjustmentValues





Pset_CivilElementCommon.xml
===========================

additions
---------
* ApplicableTypeValue "IfcCivilElement"

deletions
---------
* PropertyDefs > PropertyDef [Name="Reference"]




Qto_PavementBaseQuantities.xml
==============================

additions
---------
* ApplicableTypeValue







Pset_MaintenanceTriggerCondition.xml
====================================

modifications
-------------
* ApplicableTypeValue "IfcElement,IfcAsset,IfcSystem"
  ~~IfcElement,IfcAsset,IfcSystem~~ IfcAsset,IfcElement,IfcSystem




Pset_SpaceHeaterTypeCommon.xml
==============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="PlacementType"] > Name "PlacementType"
  ~~PlacementType~~ SpaceHeaterPlacement



Pset_SpaceFireSafetyRequirements.xml
====================================

modifications
-------------
* ApplicableClasses > ClassName "IfcSpace"
  ~~IfcSpace~~ IfcSpatialElement
* ApplicableTypeValue "IfcSpace, IfcSpatialZone, IfcZone"
  ~~IfcSpace, IfcSpatialZone, IfcZone~~ IfcSpatialElement,IfcSpatialZone,IfcZone




Qto_EarthworksFillBaseQuantities.xml
====================================

additions
---------
* ApplicableTypeValue


Pset_SpaceThermalPHistory.xml
=============================

additions
---------
* PropertyDefs > PropertyDef [Name="SpaceTemperatureHistory"]

modifications
-------------
* ApplicableClasses > ClassName "IfcSpace"
  ~~IfcSpace~~ IfcSpatialElement
* ApplicableTypeValue "IfcSpace"
  ~~IfcSpace~~ IfcSpatialElement
* PropertyDefs > PropertyDef [Name="SpaceTemperature"] > Name "SpaceTemperature"
  ~~SpaceTemperature~~ VentilationAirFlowRateHistory

deletions
---------
* PropertyDefs > PropertyDef [Name="VentilationAirFlowRate"]







Pset_SensorTypeIonConcentrationSensor.xml
=========================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="SetPointConcentration"] > Name "SetPointConcentration"
  ~~SetPointConcentration~~ SetPointIonConcentration





Pset_VesselLineCommon.xml
=========================

modifications
-------------
* ApplicableTypeValue "IfcMechanicalFastener/ROPE,IfcMechanicalFastenerType/ROPE"
  ~~IfcMechanicalFastener/ROPE,IfcMechanicalFastenerType/ROPE~~ IfcMechanicalFastener/ROPE,IfcMechanicalFastener/ROPE

deletions
---------
* ApplicableClasses > ClassName "IfcMechanicalFastenerType/ROPE"










Pset_PlantCommon.xml
====================

modifications
-------------
* ApplicableClasses > ClassName "IfcPlant"
  ~~IfcPlant~~ IfcVegetation
* ApplicableTypeValue "IfcPlant"
  ~~IfcPlant~~ IfcVegetation


Pset_DistributionChamberElementTypeSump.xml
===========================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="InvertLevel"] > Name "InvertLevel"
  ~~InvertLevel~~ SumpInvertLevel








Pset_RoadMarkingCommon.xml
==========================

modifications
-------------
* ApplicableTypeValue "IfcSurfaceFeature/(.HATCHMARKING.),IfcSurfaceFeature/(.LINEMARKING.),IfcSurfaceFeature/(.PAVEMENTSURFACEMARKING.),IfcSurfaceFeature/(.SYMBOLMARKING.)"
  ~~IfcSurfaceFeature/(.HATCHMARKING.),IfcSurfaceFeature/(.LINEMARKING.),IfcSurfaceFeature/(.PAVEMENTSURFACEMARKING.),IfcSurfaceFeature/(.SYMBOLMARKING.)~~ IfcSurfaceFeature/HATCHMARKING,IfcSurfaceFeature/LINEMARKING,IfcSurfaceFeature/PAVEMENTSURFACEMARKING,IfcSurfaceFeature/SYMBOLMARKING
* ApplicableClasses > ClassName "IfcSurfaceFeature/(.PAVEMENTSURFACEMARKING.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcSurfaceFeature/(.HATCHMARKING.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcSurfaceFeature/(.SYMBOLMARKING.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;
* ApplicableClasses > ClassName "IfcSurfaceFeature/(.LINEMARKING.)"
  ~~&lt;ClassName&gt;~~ &lt;ClassName&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="MaterialColour"]





Pset_SensorTypeCO2Sensor.xml
============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="SetPointConcentration"] > Name "SetPointConcentration"
  ~~SetPointConcentration~~ SetPointCO2Concentration












Pset_DiscreteAccessoryStandardFixingPlate.xml
=============================================

modifications
-------------
* ApplicableClasses > ClassName "IfcDiscreteAccessory/Standard fixing plate"
  ~~IfcDiscreteAccessory/Standard fixing plate~~ IfcDiscreteAccessory
* ApplicableTypeValue "IfcDiscreteAccessory/Standard fixing plate"
  ~~IfcDiscreteAccessory/Standard fixing plate~~ IfcDiscreteAccessory



Qto_CourseBaseQuantities.xml
============================

additions
---------
* ApplicableTypeValue




Pset_EnergyRequirements.xml
===========================

modifications
-------------
* ApplicableClasses > ClassName "IfcTransportElement"
  ~~IfcTransportElement~~ IfcTransportationDevice
* ApplicableTypeValue "IfcDistributionElement,IfcDistributionElementType,IfcTransportElement,IfcTransportElementType"
  ~~IfcDistributionElement,IfcDistributionElementType,IfcTransportElement,IfcTransportElementType~~ IfcDistributionElement,IfcDistributionElementType,IfcTransportationDevice,IfcTransportElementType
* PropertyDefs > PropertyDef [Name="EnergySource"] > Name "EnergySource"
  ~~EnergySource~~ EnergySourceLabel






Pset_ProcessCapacity.xml
========================

additions
---------
* ApplicableClasses > ClassName "IfcTransportationDevice"

modifications
-------------
* ApplicableClasses > ClassName "IfcTransportElement"
  ~~IfcTransportElement~~ IfcSpace
* ApplicableTypeValue "IfcSpatialElement,IfcSpatialElementType,IfcTransportElement,IfcTransportElementType,IfcBuiltSystem,IfcDistributionSystem,IfcZone,IfcDoor"
  ~~IfcSpatialElement,IfcSpatialElementType,IfcTransportElement,IfcTransportElementType,IfcBuiltSystem,IfcDistributionSystem,IfcZone,IfcDoor~~ IfcBuiltSystem,IfcDistributionSystem,IfcDoor,IfcSpace,IfcSpatialElementType,IfcTransportationDevice,IfcTransportElementType,IfcZone
* PropertyDefs > PropertyDef [Name="ProcessItem"] > PropertyType > TypePropertySingleValue > DataType
  ~~PEnum_ProcessItem~~ UNKNOWN
* PropertyDefs > PropertyDef [Name="ProcessPerformance"] > PropertyType > TypePropertySingleValue > DataType
  ~~IfcDuration ~~ UNKNOWN

deletions
---------
* ApplicableClasses > ClassName "IfcSpatialElement"













Pset_ChamberCommon.xml
======================

modifications
-------------
* ApplicableClasses > ClassName "IfcFacilityPart/IfcMarinePartTypeEnum(.CHAMBER.)"
  ~~IfcFacilityPart/IfcMarinePartTypeEnum(.CHAMBER.)~~ IfcMarinePart/CHAMBER
* ApplicableTypeValue "IfcFacilityPart/IfcMarinePartTypeEnum(.CHAMBER.)"
  ~~IfcFacilityPart/IfcMarinePartTypeEnum(.CHAMBER.)~~ IfcMarinePart/CHAMBER


Pset_CableSegmentTypeCableSegment.xml
=====================================

modifications
-------------
* PropertyDefs > PropertyDef [Name="NumberOfCores"] > PropertyType > TypePropertySingleValue > DataType
  ~~IfcInteger~~ IfcCountMeasure










Pset_AnnotationLineOfSight.xml
==============================

modifications
-------------
* ApplicableClasses > ClassName "IfcAnnotation/LineOfSight"
  ~~IfcAnnotation/LineOfSight~~ IfcAnnotation
* ApplicableTypeValue "IfcAnnotation/LineOfSight"
  ~~IfcAnnotation/LineOfSight~~ IfcAnnotation






Pset_DuctSegmentPHistory.xml
============================

modifications
-------------
* PropertyDefs > PropertyDef [Name="LeakageCurve"] > Name "LeakageCurve"
  ~~LeakageCurve~~ LeakageCurveHistory


Pset_TicketProcessing.xml
=========================

modifications
-------------
* ApplicableTypeValue "IfcDoor/TURNSTILE,IfcDoor/BOOM_BARRIER"
  ~~IfcDoor/TURNSTILE,IfcDoor/BOOM_BARRIER~~ IfcDoor/BOOM_BARRIER,IfcDoor/TURNSTILE




Pset_PropertyAgreement.xml
==========================

modifications
-------------
* PropertyDefs > PropertyDef [Name="Identifier"] > Name "Identifier"
  ~~Identifier~~ TrackingIdentifier
* PropertyDefs > PropertyDef [Name="Version"] > Name "Version"
  ~~Version~~ AgreementVersion
* PropertyDefs > PropertyDef [Name="VersionDate"] > Name "VersionDate"
  ~~VersionDate~~ AgreementDate








Pset_BerthCommon.xml
====================

modifications
-------------
* ApplicableTypeValue "IfcSpace/BERTH,IfcSpaceType/BERTH"
  ~~IfcSpace/BERTH,IfcSpaceType/BERTH~~ IfcSpace/BERTH,IfcSpace/BERTH

deletions
---------
* ApplicableClasses > ClassName "IfcSpaceType/BERTH"



Pset_CoveringFlooring.xml
=========================

modifications
-------------
* ApplicableTypeValue "IfcCovering/FLOORING,"
  ~~IfcCovering/FLOORING,~~ IfcCovering/FLOORING

deletions
---------
* ApplicableClasses > ClassName









Pset_EnvironmentalEmissions.xml
===============================

modifications
-------------
* ApplicableClasses > ClassName "IfcTransportElement"
  ~~IfcTransportElement~~ IfcTransportationDevice
* ApplicableTypeValue "IfcDistributionElement,IfcDistributionElementType,IfcTransportElement,IfcTransportElementType"
  ~~IfcDistributionElement,IfcDistributionElementType,IfcTransportElement,IfcTransportElementType~~ IfcDistributionElement,IfcDistributionElementType,IfcTransportationDevice,IfcTransportElementType


Pset_SpaceCoveringRequirements.xml
==================================

modifications
-------------
* ApplicableClasses > ClassName "IfcSpace"
  ~~IfcSpace~~ IfcSpatialElement
* ApplicableTypeValue "IfcSpace"
  ~~IfcSpace~~ IfcSpatialElement


Pset_CoilTypeCommon.xml
=======================

modifications
-------------
* PropertyDefs > PropertyDef [Name="PlacementType"] > Name "PlacementType"
  ~~PlacementType~~ CoilPlacement


Pset_ConstructionResource.xml
=============================

additions
---------
* PropertyDefs > PropertyDef [Name="RemainingWorkProgression"]

modifications
-------------
* PropertyDefs > PropertyDef [Name="RemainingWork"] > Name "RemainingWork"
  ~~RemainingWork~~ ScheduleWorkProgression
* PropertyDefs > PropertyDef [Name="ActualWork"]
  ~~&lt;PropertyDef&gt;~~ &lt;PropertyDef&gt;

deletions
---------
* PropertyDefs > PropertyDef [Name="ScheduleWork"]





Pset_TrenchExcavationCommon.xml
===============================

modifications
-------------
* ApplicableClasses > ClassName "IfcEarthworksCut/(.TRENCH.)"
  ~~IfcEarthworksCut/(.TRENCH.)~~ IfcEarthworksCut/TRENCH
* ApplicableTypeValue "IfcEarthworksCut/(.TRENCH.)"
  ~~IfcEarthworksCut/(.TRENCH.)~~ IfcEarthworksCut/TRENCH

