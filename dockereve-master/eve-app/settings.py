import os
import re
get_mongo_host = re.match('tcp://(.*):(.*)', os.environ['MONGODB_PORT'])

bids_schema = {
    'modality': {
        'type': 'string',
        'required': True
    },
    'subject_id': {
        'type': 'string',
        'required': True
    },
    'run_id': {'type': 'string'},
    'acq_id': {'type': 'string'},
    'task_id': {'type': 'string'},
    'run_id': {'type': 'string'},
}

settings_schema = {
    'version': {
        'type': 'string',
        'required': True
    },
    'md5sum': {
        'type': 'string',
        'required': True
    },
    'software': {
        'type': 'string',
        'required': True
    },
}

bold_iqms_schema = {
    'aor': {
        'type': 'float',
        'required': True
    },
    'aqi': {
        'type': 'float',
        'required': True

    },
    'dvars_nstd': {
        'type': 'float',
        'required': True

    },
    'dvars_std': {
        'type': 'float',
        'required': True
    },
    'dvars_vstd': {
        'type': 'float',
        'required': True
    },
    'efc': {
        'type': 'float',
        'required': True
    },
    'fber': {
        'type': 'float',
        'required': True
    },
    'fd_mean': {
        'type': 'float',
        'required': True
    },
    'fd_num': {
        'type': 'float',
        'required': True
    },
    'fd_perc': {
        'type': 'float',
        'required': True
    },
    'fwhm_avg': {
        'type': 'float',
        'required': True
    },
    'fwhm_x': {
        'type': 'float',
        'required': True
    },
    'fwhm_y': {
        'type': 'float',
        'required': True
    },
    'fwhm_z': {
        'type': 'float',
        'required': True
    },
    'gcor': {
        'type': 'float',
        'required': True
    },
    'gsr_x': {
        'type': 'float',
        'required': True
    },
    'gsr_y': {
        'type': 'float',
        'required': True
    },
    'task_id': {
        'type': 'string',
        'required': True
    },
    'size_t': {
        'type': 'float',
        'required': True
    },
    'size_x': {
        'type': 'float',
        'required': True
    },
    'size_y': {
        'type': 'float',
        'required': True
    },
    'size_z': {
        'type': 'float',
        'required': True
    },
    'snr': {
        'type': 'float',
        'required': True
    },
    'spacing_tr': {
        'type': 'float',
        'required': True
    },
    'spacing_x': {
        'type': 'float',
        'required': True
    },
    'spacing_y': {
        'type': 'float',
        'required': True
    },
    'spacing_z': {
        'type': 'float',
        'required': True
    },
    'summary_bg_k': {
        'type': 'float',
        'required': True
    },
    'summary_bg_mean': {
        'type': 'float',
        'required': True
    },
    'summary_bg_median': {
        'type': 'float',
        'required': True
    },
    'summary_bg_mad': {
        'type': 'float',
        'required': True
    },
    'summary_bg_p05': {
        'type': 'float',
        'required': True
    },
    'summary_bg_p95': {
        'type': 'float',
        'required': True
    },
    'summary_bg_stdv': {
        'type': 'float',
        'required': True
    },
    'summary_bg_n': {
        'type': 'float',
        'required': True
    },
    'summary_fg_k': {
        'type': 'float',
        'required': True
    },
    'summary_fg_mean': {
        'type': 'float',
        'required': True
    },
    'summary_fg_median': {
        'type': 'float',
        'required': True
    },
    'summary_fg_mad': {
        'type': 'float',
        'required': True
    },
    'summary_fg_p05': {
        'type': 'float',
        'required': True
    },
    'summary_fg_p95': {
        'type': 'float',
        'required': True
    },
    'summary_fg_stdv': {
        'type': 'float',
        'required': True
    },
    'summary_fg_n': {
        'type': 'float',
        'required': True
    },
    'tsnr': {
        'type': 'float',
        'required': True
    },

}

t1w_iqms_schema = {
    'cjv': {
        'type': 'float',
        'required': True
    },
    'cnr': {
        'type': 'float',
        'required': True
    },
    'efc': {
        'type': 'float',
        'required': True
    },
    'fber': {
        'type': 'float',
        'required': True

    },
    'fwhm_avg': {
        'type': 'float',
        'required': True
    },
    'fwhm_x': {
        'type': 'float',
        'required': True
    },
    'fwhm_y': {
        'type': 'float',
        'required': True
    },
    'fwhm_z': {
        'type': 'float',
        'required': True
    },
    'icvs_csf': {
        'type': 'float',
        'required': True
    },
    'icvs_gm': {
        'type': 'float',
        'required': True
    },
    'icvs_wm': {
        'type': 'float',
        'required': True
    },
    'inu_med': {
        'type': 'float',
        'required': True
    },
    'inu_range': {
        'type': 'float',
        'required': True
    },
    'mriqc_pred': {
        'type': 'integer',
        'required': True
    },
    'qi_1': {
        'type': 'float',
        'required': True
    },
    'qi_2': {
        'type': 'float',
        'required': True
    },
    'rpve_csf': {
        'type': 'float',
        'required': True
    },
    'rpve_gm': {
        'type': 'float',
        'required': True
    },
    'rpve_wm': {
        'type': 'float',
        'required': True
    },
    'size_x': {
        'type': 'integer',
        'required': True
    },
    'size_y': {
        'type': 'integer',
        'required': True
    },
    'size_z': {
        'type': 'integer',
        'required': True
    },
    'snr_csf': {
        'type': 'float',
        'required': True
    },
    'snr_gm': {
        'type': 'float',
        'required': True
    },
    'snr_total': {
        'type': 'float',
        'required': True
    },
    'snr_wm': {
        'type': 'float',
        'required': True
    },
    'snrd_csf': {
        'type': 'float',
        'required': True
    },
    'snrd_gm': {
        'type': 'float',
        'required': True
    },
    'snrd_total': {
        'type': 'float',
        'required': True
    },
    'snrd_wm': {
        'type': 'float',
        'required': True
    },
    'spacing_x': {
        'type': 'float',
        'required': True
    },
    'spacing_y': {
        'type': 'float',
        'required': True
    },
    'spacing_z': {
        'type': 'float',
        'required': True
    },
    'summary_bg_k': {
        'type': 'float',
        'required': True
    },
    'summary_bg_mean': {
        'type': 'float',
        'required': True
    },
    'summary_bg_median': {
        'type': 'float',
        'required': True
    },
    'summary_bg_mad': {
        'type': 'float',
        'required': True
    },
    'summary_bg_p05': {
        'type': 'float',
        'required': True
    },
    'summary_bg_p95': {
        'type': 'float',
        'required': True
    },
    'summary_bg_stdv': {
        'type': 'float',
        'required': True
    },
    'summary_bg_n': {
        'type': 'float',
        'required': True
    },
    'summary_csf_k': {
        'type': 'float',
        'required': True
    },
    'summary_csf_mean': {
        'type': 'float',
        'required': True
    },
    'summary_csf_median': {
        'type': 'float',
        'required': True
    },
    'summary_csf_mad': {
        'type': 'float',
        'required': True
    },
    'summary_csf_p05': {
        'type': 'float',
        'required': True
    },
    'summary_csf_p95': {
        'type': 'float',
        'required': True
    },
    'summary_csf_stdv': {
        'type': 'float',
        'required': True
    },
    'summary_csf_n': {
        'type': 'float',
        'required': True
    },
    'summary_gm_k': {
        'type': 'float',
        'required': True
    },
    'summary_gm_mean': {
        'type': 'float',
        'required': True
    },
    'summary_gm_median': {
        'type': 'float',
        'required': True
    },
    'summary_gm_mad': {
        'type': 'float',
        'required': True
    },
    'summary_gm_p05': {
        'type': 'float',
        'required': True
    },
    'summary_gm_p95': {
        'type': 'float',
        'required': True
    },
    'summary_gm_stdv': {
        'type': 'float',
        'required': True
    },
    'summary_gm_n': {
        'type': 'float',
        'required': True
    },
    'summary_wm_k': {
        'type': 'float',
        'required': True
    },
    'summary_wm_mean': {
        'type': 'float',
        'required': True
    },
    'summary_wm_median': {
        'type': 'float',
        'required': True
    },
    'summary_wm_mad': {
        'type': 'float',
        'required': True
    },
    'summary_wm_p05': {
        'type': 'float',
        'required': True
    },
    'summary_wm_p95': {
        'type': 'float',
        'required': True
    },
    'summary_wm_stdv': {
        'type': 'float',
        'required': True
    },
    'summary_wm_n': {
        'type': 'float',
        'required': True
    },
    'tpm_overlap_csf': {
        'type': 'float',
        'required': True
    },
    'tpm_overlap_gm': {
        'type': 'float',
        'required': True
    },
    'tpm_overlap_wm': {
        'type': 'float',
        'required': True
    },
    'wm2max': {
        'type': 'float',
        'required': True
    },
}


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
                # if modality == bold, the fields below are required
                'TaskName': {
                    'type': 'string',
                    'required': True
                },
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
                'MRTransmitCoilSequence': {'type': 'string'},
                'MatrixCoilMode': {'type': 'string'},
                'CoilCombinationMethod': {'type': 'string'},
                'PulseSequenceType': {'type': 'string'},
                'PulseSequenceDetails': {'type': 'string'},
                'NumberShots': {'type': 'integer'},
                'ParallelReductionFactorInPlane': {'type': 'float'},
                'ParallelAcquisitionTechnique': {'type': 'string'},
                'PartialFourier': {'type': 'boolean'},
                'PartialFourierDirection': {'type': 'string'},
                'EffectiveEchoSpacing': {'type': 'float'},
                'TotalReadoutTime': {'type': 'float'},
                'SliceEncodingDirection': {'type': 'string'},
                'NumberOfVolumesDiscardedByScanner': {'type': 'float'},
                'NumberOfVolumesDiscardedByUser': {'type': 'float'},
                'DelayTime': {'type': 'float'},
                'MultibandAccelerationFactor': {'type': 'float'},
                'Instructions': {'type': 'string'},
                'TaskDescription': {'type': 'string'},
                'CogAtlasID': {'type': 'string'},
                'CogPOID': {'type': 'string'},
                'InstitutionName': {'type': 'string'},
                'InstitutionAddress': {'type': 'string'},
                'ConversionSoftware': {'type': 'string'},
                'ConversionSoftwareVersion': {'type': 'string'},
            }  # end of schema
        },  # end of bold
        'T1w': {
            'item_title': 'T1w',
            'resource_methods': ['GET', 'POST'],
            'item_methods': ['GET', 'PATCH', 'PUT', 'DELETE'],
            'schema': {
                # if modality == T1w, the fields below are required
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
                'MRTransmitCoilSequence': {'type': 'string'},
                'MatrixCoilMode': {'type': 'string'},
                'CoilCombinationMethod': {'type': 'string'},
                'PulseSequenceType': {'type': 'string'},
                'PulseSequenceDetails': {'type': 'string'},
                'NumberShots': {'type': 'integer'},
                'ParallelReductionFactorInPlane': {'type': 'float'},
                'ParallelAcquisitionTechnique': {'type': 'string'},
                'PartialFourier': {'type': 'boolean'},
                'PartialFourierDirection': {'type': 'string'},
                'EffectiveEchoSpacing': {'type': 'float'},
                'TotalReadoutTime': {'type': 'float'},
                'SliceEncodingDirection': {'type': 'string'},
                'NumberOfVolumesDiscardedByScanner': {'type': 'float'},
                'NumberOfVolumesDiscardedByUser': {'type': 'float'},
                'DelayTime': {'type': 'float'},
                'MultibandAccelerationFactor': {'type': 'float'},
                'Instructions': {'type': 'string'},
                'TaskDescription': {'type': 'string'},
                'CogAtlasID': {'type': 'string'},
                'CogPOID': {'type': 'string'},
                'InstitutionName': {'type': 'string'},
                'InstitutionAddress': {'type': 'string'},
                'ConversionSoftware': {'type': 'string'},
                'ConversionSoftwareVersion': {'type': 'string'},
            }  # end of schema
        }  # end of T1w

    }
}


my_settings['DOMAIN']['bold']['schema'].update(bids_schema)
my_settings['DOMAIN']['bold']['schema'].update(settings_schema)
my_settings['DOMAIN']['bold']['schema'].update(bold_iqms_schema)

my_settings['DOMAIN']['T1w']['schema'].update(bids_schema)
my_settings['DOMAIN']['T1w']['schema'].update(settings_schema)
my_settings['DOMAIN']['T1w']['schema'].update(t1w_iqms_schema)
