"""
Initialization File
"""

__docformat__ = "restructuredtext"

# Alert users if they are missing key dependencies.
key_dep = ("datetime", "pandas", "numpy", "statistics", "sys", "os", "glob")
miss_dep = []

for dep in key_dep:
    try:
        __import__(dep)
    except ImportError as e:
        miss_dep.append(f"{dep}: {e}")

if miss_dep:
    raise ImportError(
        "Unable to import required dependencies:\n" + "\n".join(miss_dep)
    )
del key_dep, miss_dep, dep

# Import package functions.
from VTP.core.VTP_functions import (
    substring_position,
    parse_date,
    parse_time,
    parse_date_time,
    add_date,
    add_time,
    add_date_time,
    add_isoweekday_from_date_time,
    add_time_from_date_time,
    standardize_by_time,
    average_over_interval,
    assign_vehicle_state,
    return_file_list,
    parse_variables,
    is_numeric,
    summarize_state_variables,
    calculate_distance,
    process_telematics_from_directory
)

# Module level document details.
__doc__ = """
VTP - a package for (v)ehicle (t)elamatics (p)rocessing in Python.
=====================================================================

**VTP** is a Python package that contains functions for processing
vehicle telematics data and applying deterministic rules to
characterize a vehicle's activity.

Main Features
-------------
    - standardize telematics data files containing time-location data
    to equal-time-interval tables.
    - assign vehicle states based on fleet vehicle activities
    - collect variables on the behavior of fleet vehicles in order to
    cluster vehicle-day observations into like duty cycles.
"""