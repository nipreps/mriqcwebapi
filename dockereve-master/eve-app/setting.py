import os
import re
get_mongo_host = re.match('tcp://(.*):(.*)', os.environ['MONGODB_PORT'])

my_settings = {
    'MONGO_HOST': get_mongo_host.group(1),
    'MONGO_PORT': get_mongo_host.group(2),
    'MONGO_DBNAME': 'scenarios',
    'X_DOMAINS': '*',
    'DOMAIN': {
         'bold': {
            'item_title': 'bold',
            'resource_methods': ['GET', 'POST'],
            'item_methods': ['GET', 'PATCH', 'PUT', 'DELETE'],
            'schema': {
                'modality': {
                        'type': 'string',
                        'required': True
                },
                #if modality == bold, the fields below are required
                'aor': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'bold'}
                },
                'aqi': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'bold'}
                },
                'dvars_nstd': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'bold'}
                },  
                'dvars_std': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'bold'}
                },
                'dvars_vstd': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'bold'}
                },
                'efc': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'bold'}
                },
                'fber': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'bold'}
                },
                'fd_mean': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'bold'}
                },
                'fd_num': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'bold'}
                },
                'fd_perc': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'bold'}
                },
                'fwhm_avg': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'bold'}
                },
                'fwhm_x': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'bold'}
                },
                'fwhm_y': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'bold'}
                },
                'fwhm_z': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'bold'}
                },
                'gcor': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'bold'}
                },
                'gsr_x': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'bold'}
                },
                'gsr_y': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'bold'}
                },
                'task_id': {
                    'type': 'string',
                    'required': True,
                    'dependencies': {'modality': 'bold'}
                },
                'size_t': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'bold'}
                },
                'size_x': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'bold'}
                },
                'size_y': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'bold'}
                },
                'size_z': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'bold'}
                },
                'snr': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'bold'}
                },
                'spacing_tr': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'bold'}
                },
                'spacing_x': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'bold'}
                },  
                'spacing_y': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'bold'}
                },
                'spacing_z': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'bold'}
                },
                'summary_bg_k': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'bold'}
                },
                'summary_bg_mean': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'bold'}
                },
                'summary_bg_p05': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'bold'}
                },
                'summary_bg_p95': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'bold'}
                },
                'summary_bg_stdv': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'bold'}
                },
                'summary_fg_k': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'bold'}   
                },
                'summary_fg_mean': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'bold'}
                },
                'summary_fg_p05': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'bold'}
                },
                'summary_fg_p95': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'bold'}    
                },
                'summary_fg_stdv': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'bold'}
                },
                'tsnr': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'bold'}
                },

               

                # optional data  regardless of modality
                'AccelNumReferenceLines':  {'type': 'integer'},
                'AccelerationFactorPE':  {'type': 'integer'},
                'AcquisitionMatrix':  {'type': 'string'},
                'DeviceSerialNumber': {'type': 'string'},
                'EchoTime': {'type': 'float'},
                'EchoTrainLength': {'type': 'integer'},
                'FlipAngle': {'type': 'integer'},
                'ImageType': {'type': 'string'},
                'ImagingFrequency': {'type': 'integer'},
                'InPlanePhaseEncodingDirection': {'type': 'string'},
                'InversionTime': {'type': 'float'},
                'MRAcquisitionType': {'type': 'string'},
                'MagneticFieldStrength': {'type': 'integer'},
                'ManufacturerModelName': {'type': 'string'},
                'NumberOfAverages': {'type': 'integer'},
                'NumberOfPhaseEncodingSteps': {'type': 'integer'},
                'PatientPosition': {'type': 'string'},
                'PercentPhaseFieldOfView': {'type': 'integer'},
                'PercentSampling': {'type': 'integer'},
                'PhaseEncodingDirection': {'type': 'string'},
                'PixelBandwidth': {'type': 'integer'},
                'ProtocolName': {'type': 'string'},
                'ReceiveCoilName': {'type': 'string'},
                'RepetitionTime': {'type': 'float'},
                'ScanOptions': {'type': 'string'},
                'ScanningSequence': {'type': 'string'},
                'SequenceName': {'type': 'string'},
                'SequenceVariant': {'type': 'string'},
                'SoftwareVersions': {'type': 'string'},
                'TotalScanTimeSec': {'type': 'integer'},
                'TransmitCoilName': {'type': 'string'},
                'VariableFlipAngleFlag': {'type': 'string'},

                'ContrastBolusIngredient':  {'type': 'string'},
                'Manufacturer': {'type': 'string'},
                'HardcopyDeviceSoftwareVersion': {'type': 'string'},
                'GradientSetType': {'type': 'string'},
                'MRTransmitCoilSequence':{'type': 'string'},
                'MatrixCoilMode': {'type': 'string'},
                'CoilCombinationMethod': {'type': 'string'},
                'PulseSequenceType': {'type': 'string'},
                'PulseSequenceDetails': {'type': 'string'},
                'NumberShots' :{'type': 'integer'},
                'ParallelReductionFactorInPlane':{'type': 'float'},
                'ParallelAcquisitionTechnique': {'type': 'string'},
                'PartialFourier' :{'type': 'boolean'},
                'PartialFourierDirection':{'type': 'string'},
                'EffectiveEchoSpacing' :{'type': 'float'},
                'TotalReadoutTime':{'type': 'float'},
                'SliceEncodingDirection': {'type': 'string'},
                'NumberOfVolumesDiscardedByScanner':{'type': 'float'},
                'NumberOfVolumesDiscardedByUser':{'type': 'float'},
                'DelayTime':{'type': 'float'},
                'MultibandAccelerationFactor':{'type': 'float'},
                'Instructions': {'type': 'string'},
                'TaskDescription': {'type': 'string'},
                'CogAtlasID' : {'type': 'string'},
                'CogPOID': {'type': 'string'},
                'InstitutionName': {'type': 'string'},
                'InstitutionAddress': {'type': 'string'},
                'ConversionSoftware': {'type': 'string'},
                'ConversionSoftwareVersion': {'type': 'string'},
            }
        }
        'T1w': {
            'item_title': 'T1w',
            'resource_methods': ['GET', 'POST'],
            'item_methods': ['GET', 'PATCH', 'PUT', 'DELETE'],
            'schema': {
                'modality': {
                        'type': 'string',
                        'required': True
                },
               
                #if modality == T1w, the fields below are required
                'cjv':{
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'T1w'}
                },
                'cnr':{
                    'type':'float',
                    'required': True,
                    'dependencies': {'modality': 'T1w'}
                },
                'efc':{
                    'type':'float',
                    'required': True,
                    'dependencies': {'modality': 'T1w'}
                },
                'fber': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'T1w'}

                },
                'fwhm_avg': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'T1w'}
                },
                'fwhm_x':{
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'T1w'}
                },
                'fwhm_y': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'T1w'}
                },
                'fwhm_z': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'T1w'}
                },
                'icvs_csf': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'T1w'}
                },
                'icvs_gm': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'T1w'}
                },
                'icvs_wm': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'T1w'}
                },
                'inu_med': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'T1w'}
                },
                'inu_range': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'T1w'}
                },

                # required data 
                'md5sum': {
                    'type': 'string',
                    'required': True,
                    'dependencies': {'modality': 'T1w'}
                },
                'modality': {
                    'type': 'string',
                    'required': True,
                    'dependencies': {'modality': 'T1w'}

                },
                'mriqc_pred': {
                    'type': 'integer',
                    'required': True,
                    'dependencies': {'modality': 'T1w'}
                },
                'software': {
                    'type': 'string',
                    'required': True,
                    'dependencies': {'modality': 'T1w'}
                },
                'subject_id': {
                    'type': 'string',
                    'required': True,
                    'dependencies': {'modality': 'T1w'}
                },
                'version': {
                    'type': 'string',
                    'required': True,
                    'dependencies': {'modality': 'T1w'}
                },
           
                'qi_1': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'T1w'}
                },
                'qi_2': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'T1w'}
                },
                'rpve_csf': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'T1w'}
                },
                'rpve_gm': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'T1w'}
                },
                'rpve_wm': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'T1w'}
                },
                'size_x': {
                    'type': 'integer',
                    'required': True,
                    'dependencies': {'modality': 'T1w'}
                },
                'size_y': {
                    'type': 'integer',
                    'required': True,
                    'dependencies': {'modality': 'T1w'}
                },
                'size_z': {
                    'type': 'integer',
                    'required': True,
                    'dependencies': {'modality': 'T1w'}
                },
                'snr_csf': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'T1w'}
                },
                'snr_gm': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'T1w'}
                },
                'snr_total':{
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'T1w'}
                },
                'snr_wm': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'T1w'}
                },
                'snrd_csf': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'T1w'}
                },
                'snrd_gm': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'T1w'}
                },
                'snrd_total': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'T1w'}
                },
                'snrd_wm': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'T1w'}
                },
                'spacing_x': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'T1w'}
                },
                'spacing_y': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'T1w'}
                },
                'spacing_z': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'T1w'}
                },
                'summary_bg_k': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'T1w'}
                },
                'summary_bg_mean': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'T1w'}
                },
                'summary_bg_p05': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'T1w'}
                },
                'summary_bg_p95': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'T1w'}
                },
                'summary_bg_stdv': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'T1w'}
                },
                'summary_csf_k': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'T1w'}
                },
                'summary_csf_mean': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'T1w'}
                },
                'summary_csf_p05': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'T1w'}
                },
                'summary_csf_p95': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'T1w'}
                },
                'summary_csf_stdv': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'T1w'}
                },
                'summary_gm_k': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'T1w'}
                },
                'summary_gm_mean': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'T1w'}
                },
                'summary_gm_p05': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'T1w'}
                },
                'summary_gm_p95': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'T1w'}
                },
                'summary_gm_stdv': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'T1w'}
                },
                'summary_wm_k': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'T1w'}
                },
                'summary_wm_mean':{
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'T1w'}
                },
                'summary_wm_p05': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'T1w'}
                },
                'summary_wm_p95': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'T1w'}
                },
                'summary_wm_stdv': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'T1w'}
                },
                'tpm_overlap_csf':{
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'T1w'}
                },
                'tpm_overlap_gm': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'T1w'}
                },
                'tpm_overlap_wm': {
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'T1w'}
                },
                'wm2max':{
                    'type': 'float',
                    'required': True,
                    'dependencies': {'modality': 'T1w'}
                },

                # optional data  regardless of modality
                'AccelNumReferenceLines':  {'type': 'integer'},
                'AccelerationFactorPE':  {'type': 'integer'},
                'AcquisitionMatrix':  {'type': 'string'},
                'DeviceSerialNumber': {'type': 'string'},
                'EchoTime': {'type': 'float'},
                'EchoTrainLength': {'type': 'integer'},
                'FlipAngle': {'type': 'integer'},
                'ImageType': {'type': 'string'},
                'ImagingFrequency': {'type': 'integer'},
                'InPlanePhaseEncodingDirection': {'type': 'string'},
                'InversionTime': {'type': 'float'},
                'MRAcquisitionType': {'type': 'string'},
                'MagneticFieldStrength': {'type': 'integer'},
                'ManufacturerModelName': {'type': 'string'},
                'NumberOfAverages': {'type': 'integer'},
                'NumberOfPhaseEncodingSteps': {'type': 'integer'},
                'PatientPosition': {'type': 'string'},
                'PercentPhaseFieldOfView': {'type': 'integer'},
                'PercentSampling': {'type': 'integer'},
                'PhaseEncodingDirection': {'type': 'string'},
                'PixelBandwidth': {'type': 'integer'},
                'ProtocolName': {'type': 'string'},
                'ReceiveCoilName': {'type': 'string'},
                'RepetitionTime': {'type': 'float'},
                'ScanOptions': {'type': 'string'},
                'ScanningSequence': {'type': 'string'},
                'SequenceName': {'type': 'string'},
                'SequenceVariant': {'type': 'string'},
                'SoftwareVersions': {'type': 'string'},
                'TotalScanTimeSec': {'type': 'integer'},
                'TransmitCoilName': {'type': 'string'},
                'VariableFlipAngleFlag': {'type': 'string'},

                'ContrastBolusIngredient':  {'type': 'string'},
                'Manufacturer': {'type': 'string'},
                'HardcopyDeviceSoftwareVersion': {'type': 'string'},
                'GradientSetType': {'type': 'string'},
                'MRTransmitCoilSequence':{'type': 'string'},
                'MatrixCoilMode': {'type': 'string'},
                'CoilCombinationMethod': {'type': 'string'},
                'PulseSequenceType': {'type': 'string'},
                'PulseSequenceDetails': {'type': 'string'},
                'NumberShots' :{'type': 'integer'},
                'ParallelReductionFactorInPlane':{'type': 'float'},
                'ParallelAcquisitionTechnique': {'type': 'string'},
                'PartialFourier' :{'type': 'boolean'},
                'PartialFourierDirection':{'type': 'string'},
                'EffectiveEchoSpacing' :{'type': 'float'},
                'TotalReadoutTime':{'type': 'float'},
                'SliceEncodingDirection': {'type': 'string'},
                'NumberOfVolumesDiscardedByScanner':{'type': 'float'},
                'NumberOfVolumesDiscardedByUser':{'type': 'float'},
                'DelayTime':{'type': 'float'},
                'MultibandAccelerationFactor':{'type': 'float'},
                'Instructions': {'type': 'string'},
                'TaskDescription': {'type': 'string'},
                'CogAtlasID' : {'type': 'string'},
                'CogPOID': {'type': 'string'},
                'InstitutionName': {'type': 'string'},
                'InstitutionAddress': {'type': 'string'},
                'ConversionSoftware': {'type': 'string'},
                'ConversionSoftwareVersion': {'type': 'string'},
            }
        }
    }
}
