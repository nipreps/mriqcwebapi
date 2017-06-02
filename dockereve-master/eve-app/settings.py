import os
import re
from copy import deepcopy

bids_schema = {
    # BIDS identification bits
    'modality': {
        'type': 'string',
        'required': True
    },
    'subject_id': {
        'type': 'string',
        'required': True
    },
    'session_id': {'type': 'string'},
    'run_id': {'type': 'string'},
    'acq_id': {'type': 'string'},
    'task_id': {'type': 'string'},
    'run_id': {'type': 'string'},
    # BIDS metadata
    'AccelNumReferenceLines': {'type': 'integer'},
    'AccelerationFactorPE': {'type': 'integer'},
    'AcquisitionMatrix': {'type': 'string'},
    'CogAtlasID': {'type': 'string'},
    'CogPOID': {'type': 'string'},
    'CoilCombinationMethod': {'type': 'string'},
    'ContrastBolusIngredient': {'type': 'string'},
    'ConversionSoftware': {'type': 'string'},
    'ConversionSoftwareVersion': {'type': 'string'},
    'DelayTime': {'type': 'float'},
    'DeviceSerialNumber': {'type': 'string'},
    'EchoTime': {'type': 'float'},
    'EchoTrainLength': {'type': 'integer'},
    'EffectiveEchoSpacing': {'type': 'float'},
    'FlipAngle': {'type': 'integer'},
    'GradientSetType': {'type': 'string'},
    'HardcopyDeviceSoftwareVersion': {'type': 'string'},
    'ImageType': {'type': 'string'},
    'ImagingFrequency': {'type': 'integer'},
    'InPlanePhaseEncodingDirection': {'type': 'string'},
    'InstitutionAddress': {'type': 'string'},
    'InstitutionName': {'type': 'string'},
    'Instructions': {'type': 'string'},
    'InversionTime': {'type': 'float'},
    'MRAcquisitionType': {'type': 'string'},
    'MRTransmitCoilSequence': {'type': 'string'},
    'MagneticFieldStrength': {'type': 'integer'},
    'Manufacturer': {'type': 'string'},
    'ManufacturersModelName': {'type': 'string'},
    'MatrixCoilMode': {'type': 'string'},
    'MultibandAccelerationFactor': {'type': 'float'},
    'NumberOfAverages': {'type': 'integer'},
    'NumberOfPhaseEncodingSteps': {'type': 'integer'},
    'NumberOfVolumesDiscardedByScanner': {'type': 'float'},
    'NumberOfVolumesDiscardedByUser': {'type': 'float'},
    'NumberShots': {'type': 'integer'},
    'ParallelAcquisitionTechnique': {'type': 'string'},
    'ParallelReductionFactorInPlane': {'type': 'float'},
    'PartialFourier': {'type': 'boolean'},
    'PartialFourierDirection': {'type': 'string'},
    'PatientPosition': {'type': 'string'},
    'PercentPhaseFieldOfView': {'type': 'integer'},
    'PercentSampling': {'type': 'integer'},
    'PhaseEncodingDirection': {'type': 'string'},
    'PixelBandwidth': {'type': 'integer'},
    'ProtocolName': {'type': 'string'},
    'PulseSequenceDetails': {'type': 'string'},
    'PulseSequenceType': {'type': 'string'},
    'ReceiveCoilName': {'type': 'string'},
    'RepetitionTime': {'type': 'float'},
    'ScanOptions': {'type': 'string'},
    'ScanningSequence': {'type': 'string'},
    'SequenceName': {'type': 'string'},
    'SequenceVariant': {'type': 'string'},
    'SliceEncodingDirection': {'type': 'string'},
    'SoftwareVersions': {'type': 'string'},
    'TaskDescription': {'type': 'string'},
    'TotalReadoutTime': {'type': 'float'},
    'TotalScanTimeSec': {'type': 'integer'},
    'TransmitCoilName': {'type': 'string'},
    'VariableFlipAngleFlag': {'type': 'string'},
}

prov_schema = {
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
    'settings': {
        'type': 'dict',
        'schema': {
            'fd_thres': {'type': 'float'},
            'hmc_fsl': {'type': 'boolean'},
            'testing': {'type': 'boolean'}
        },
    },
    'mriqc_pred': {'type': 'integer'},
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
    'dummy_trs': {'type': 'integer'},
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

struct_iqms_schema = {
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
        'type': 'float'
    },
    'summary_bg_mad': {
        'type': 'float'
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
        'type': 'float'
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
        'type': 'float'
    },
    'summary_csf_mad': {
        'type': 'float'
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
        'type': 'float'
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
        'type': 'float'
    },
    'summary_gm_mad': {
        'type': 'float'
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
        'type': 'float'
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
        'type': 'float'
    },
    'summary_wm_mad': {
        'type': 'float'
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
        'type': 'float'
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


settings = {
    'URL_PREFIX': 'api',
    'API_VERSION': 'v1',
    'ALLOWED_FILTERS': ['*'],
    'MONGO_HOST': os.environ.get('MONGODB_HOST', ''),
    'MONGO_PORT': os.environ.get('MONGODB_PORT', ''),
    'MONGO_DBNAME': 'mriqc_api',
    'PUBLIC_METHODS': ['GET'],
    'PUBLIC_ITEM_METHODS': ['GET'],
    'RESOURCE_METHODS': ['GET', 'POST'],
    'ITEM_METHODS': ['GET'],
    'X_DOMAINS': '*',
    'DOMAIN': {
        'bold': {
            'item_title': 'bold',
        },
        'T1w': {
            'item_title': 'T1w',
        },
        'T2w': {
            'item_title': 'T2w',
        }

    }
}


settings['DOMAIN']['bold']['schema'] = deepcopy(bold_iqms_schema)
settings['DOMAIN']['bold']['schema'].update(
    {
        'bids_meta': {
            'type': 'dict',
            'required': True,
            'schema': deepcopy(bids_schema)
        },
        'provenance': {
            'type': 'dict',
            'required': True,
            'schema': deepcopy(prov_schema)
        }
    }
)

settings['DOMAIN']['bold']['schema']['bids_meta']['schema'].update({
    'TaskName': {
        'type': 'string',
        'required': True
    },
})


settings['DOMAIN']['T1w']['schema'] = deepcopy(struct_iqms_schema)
settings['DOMAIN']['T1w']['schema'].update(
    {
        'bids_meta': {
            'type': 'dict',
            'required': True,
            'schema': deepcopy(bids_schema)
        },
        'provenance': {
            'type': 'dict',
            'required': True,
            'schema': deepcopy(prov_schema)
        }
    }
)

settings['DOMAIN']['T2w']['schema'] = deepcopy(settings['DOMAIN']['T1w']['schema'])

