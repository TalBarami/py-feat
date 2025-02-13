"""
py-feat helper functions and variables
"""

import torch

""" DEFINE IMPORTANT VARIABLES """
# FEAT columns
FEAT_EMOTION_MAPPER = {
    0: "anger",
    1: "disgust",
    2: "fear",
    3: "happiness",
    4: "sadness",
    5: "surprise",
    6: "neutral",
}
FEAT_EMOTION_COLUMNS = [
    "anger",
    "disgust",
    "fear",
    "happiness",
    "sadness",
    "surprise",
    "neutral",
]
FEAT_FACEBOX_COLUMNS = [
    "FaceRectX",
    "FaceRectY",
    "FaceRectWidth",
    "FaceRectHeight",
    "FaceScore",
]
FEAT_TIME_COLUMNS = ["frame"]
FEAT_FACEPOSE_COLUMNS_3D = ["Pitch", "Roll", "Yaw"]
FEAT_FACEPOSE_COLUMNS_6D = ["Pitch", "Roll", "Yaw", "X", "Y", "Z"]
FEAT_IDENTITY_COLUMNS = ["Identity"] + [
    f"Identity_{x+1}" for x in range(512)
]  # could add identity embeddings too (512)

MP_BLENDSHAPE_MODEL_LANDMARKS_SUBSET = [
    0,
    1,
    4,
    5,
    6,
    7,
    8,
    10,
    13,
    14,
    17,
    21,
    33,
    37,
    39,
    40,
    46,
    52,
    53,
    54,
    55,
    58,
    61,
    63,
    65,
    66,
    67,
    70,
    78,
    80,
    81,
    82,
    84,
    87,
    88,
    91,
    93,
    95,
    103,
    105,
    107,
    109,
    127,
    132,
    133,
    136,
    144,
    145,
    146,
    148,
    149,
    150,
    152,
    153,
    154,
    155,
    157,
    158,
    159,
    160,
    161,
    162,
    163,
    168,
    172,
    173,
    176,
    178,
    181,
    185,
    191,
    195,
    197,
    234,
    246,
    249,
    251,
    263,
    267,
    269,
    270,
    276,
    282,
    283,
    284,
    285,
    288,
    291,
    293,
    295,
    296,
    297,
    300,
    308,
    310,
    311,
    312,
    314,
    317,
    318,
    321,
    323,
    324,
    332,
    334,
    336,
    338,
    356,
    361,
    362,
    365,
    373,
    374,
    375,
    377,
    378,
    379,
    380,
    381,
    382,
    384,
    385,
    386,
    387,
    388,
    389,
    390,
    397,
    398,
    400,
    402,
    405,
    409,
    415,
    454,
    466,
    468,
    469,
    470,
    471,
    472,
    473,
    474,
    475,
    476,
    477,
]

MP_BLENDSHAPE_NAMES = [
    "_neutral",
    "browDownLeft",
    "browDownRight",
    "browInnerUp",
    "browOuterUpLeft",
    "browOuterUpRight",
    "cheekPuff",
    "cheekSquintLeft",
    "cheekSquintRight",
    "eyeBlinkLeft",
    "eyeBlinkRight",
    "eyeLookDownLeft",
    "eyeLookDownRight",
    "eyeLookInLeft",
    "eyeLookInRight",
    "eyeLookOutLeft",
    "eyeLookOutRight",
    "eyeLookUpLeft",
    "eyeLookUpRight",
    "eyeSquintLeft",
    "eyeSquintRight",
    "eyeWideLeft",
    "eyeWideRight",
    "jawForward",
    "jawLeft",
    "jawOpen",
    "jawRight",
    "mouthClose",
    "mouthDimpleLeft",
    "mouthDimpleRight",
    "mouthFrownLeft",
    "mouthFrownRight",
    "mouthFunnel",
    "mouthLeft",
    "mouthLowerDownLeft",
    "mouthLowerDownRight",
    "mouthPressLeft",
    "mouthPressRight",
    "mouthPucker",
    "mouthRight",
    "mouthRollLower",
    "mouthRollUpper",
    "mouthShrugLower",
    "mouthShrugUpper",
    "mouthSmileLeft",
    "mouthSmileRight",
    "mouthStretchLeft",
    "mouthStretchRight",
    "mouthUpperUpLeft",
    "mouthUpperUpRight",
    "noseSneerLeft",
    "noseSneerRight",
]


# Mediapipe FaceMesh Coordinates
def generate_coordinate_names(num_points=478):
    """
    Generates a list of names for x, y, z coordinates for a given number of points.

    Args:
        num_points (int): Number of points (478 in this case).

    Returns:
        list: List of coordinate names like ['x_1', 'y_1', 'z_1', ..., 'x_n', 'y_n', 'z_n'].
    """
    coordinate_names = []
    for i in range(0, num_points):
        coordinate_names.extend([f"x_{i}", f"y_{i}", f"z_{i}"])

    return coordinate_names


MP_LANDMARK_COLUMNS = generate_coordinate_names(num_points=478)

# OpenFace columns
landmark_length = 68

openface_2d_landmark_columns = [f"x_{i}" for i in range(landmark_length)] + [
    f"y_{i}" for i in range(landmark_length)
]
openface_3d_landmark_columns = (
    [f"X_{i}" for i in range(landmark_length)]
    + [f"Y_{i}" for i in range(landmark_length)]
    + [f"Z_{i}" for i in range(landmark_length)]
)

openface_AU_list = [1, 2, 4, 5, 6, 7, 9, 10, 12, 14, 15, 17, 20, 23, 25, 26, 45]
openface_AU_intensity = ["AU" + str(i).zfill(2) + "_r" for i in openface_AU_list]
openface_AU_presence = ["AU" + str(i).zfill(2) + "_c" for i in openface_AU_list + [28]]
openface_AU_presence.sort()
openface_AU_columns = openface_AU_intensity + openface_AU_presence
openface_time_columns = ["frame", "timestamp"]
openface_gaze_columns = [
    "gaze_0_x",
    "gaze_0_y",
    "gaze_0_z",
    "gaze_1_x",
    "gaze_1_y",
    "gaze_1_z",
]
openface_facepose_columns = [
    "pose_Tx",
    "pose_Ty",
    "pose_Tz",
    "pose_Rx",
    "pose_Ry",
    "pose_Rz",
]
OPENFACE_ORIG_COLUMNS = (
    openface_time_columns
    + ["confidence", "success"]
    + openface_gaze_columns
    + openface_facepose_columns
    + openface_2d_landmark_columns
    + openface_3d_landmark_columns
    + [
        "p_scale",
        "p_rx",
        "p_ry",
        "p_rz",
        "p_tx",
        "p_ty",
        "p_0",
        "p_1",
        "p_2",
        "p_3",
        "p_4",
        "p_5",
        "p_6",
        "p_7",
        "p_8",
        "p_9",
        "p_10",
        "p_11",
        "p_12",
        "p_13",
        "p_14",
        "p_15",
        "p_16",
        "p_17",
        "p_18",
        "p_19",
        "p_20",
        "p_21",
        "p_22",
        "p_23",
        "p_24",
        "p_25",
        "p_26",
        "p_27",
        "p_28",
        "p_29",
        "p_30",
        "p_31",
        "p_32",
        "p_33",
    ]
    + openface_AU_columns
)


def set_torch_device(device="cpu"):
    """Helper function to set device for pytorch model"""

    if not isinstance(device, torch.device):
        if device not in ["cpu", "cuda", "mps", "auto"]:
            raise ValueError("Device must be ['cpu', 'cuda', 'mps', 'auto']")

        if device == "auto":
            # FIXME: This currently doesn't work on mac's where mps is available because
            # it results in a mix of cpu and mps operations which cause failures. E.g.
            # when we call torch.cat() inside of image_operations.decode from
            # FaceBoxes_tests.py(128)

            # In this case priors are on `cpu`, loc is on `mps`, variances is a list (so
            # cpu I assume). loc also contains all nans

            # This causes retinaface to fail to detect a face properly and tests to fail

            if torch.cuda.is_available():
                device = "cuda"
            elif hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
                device = "mps"
            else:
                device = "cpu"
        else:
            device = device
        return torch.device(device)

    else:
        return device


# TODO: Refactor the output of each detector into a reliable dataclass with the same
# structure to avoid utility functions like this
def is_list_of_lists_empty(list_of_lists):
    """Helper function to check if list of lists is empty"""
    return not any(list_of_lists)


def flatten_list(data):
    """Helper function to flatten a list of lists"""
    flat_list = []
    for row in data:
        flat_list += row
    return flat_list
