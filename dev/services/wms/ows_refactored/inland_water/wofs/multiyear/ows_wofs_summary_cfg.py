from ows_refactored.inland_water.wofs.bands_wo_cfg import (bands_wofs_filt_sum,
                                                           bands_wofs_sum)
from ows_refactored.ows_legend_cfg import (legend_idx_percentage_by_20,
                                           legend_idx_percentage_by_25)
from ows_refactored.ows_reslim_cfg import reslim_wms_min_zoom_15_cache_rules

style_wofs_count_wet = {
    "name": "water_observations",
    "title": "Wet Count",
    "abstract": "WOfS summary showing the count of water observations",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "count_wet",
        },
    },
    "needed_bands": ["count_wet"],
    "include_in_feature_info": False,
    "color_ramp": [
        {"value": 0, "color": "#666666", "alpha": 0},
        {"value": 2, "color": "#890000"},
        {"value": 5, "color": "#990000"},
        {"value": 10, "color": "#E38400"},
        {"value": 25, "color": "#E3DF00"},
        {"value": 50, "color": "#A6E300"},
        {"value": 100, "color": "#00E32D"},
        {"value": 150, "color": "#00E3C8"},
        {"value": 200, "color": "#0097E3"},
        {"value": 250, "color": "#005FE3"},
        {"value": 300, "color": "#000FE3"},
        {"value": 350, "color": "#000EA9"},
        {
            "value": 400,
            "color": "#5700E3",
        },
    ],
    "legend": {
        "begin": "0",
        "end": "400",
        "decimal_places": 0,
        "ticks_every": 100,
        "tick_labels": {
            "400": {"prefix": ">"},
        },
    },
}

style_wofs_count_clear = {
    "name": "clear_observations",
    "title": "Clear Count",
    "abstract": "WOfS summary showing the count of clear observations",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "count_clear",
        },
    },
    "needed_bands": ["count_clear"],
    "include_in_feature_info": False,
    "color_ramp": [
        {"value": 0, "color": "#FFFFFF", "alpha": 0},
        {
            # purely for legend display
            # we should not get fractional
            # values in this styles
            "value": 10,
            "color": "#b21800",
            "alpha": 1,
        },
        {"value": 100, "color": "#ef8500"},
        {"value": 200, "color": "#ffb800"},
        {"value": 300, "color": "#ffd300"},
        {"value": 400, "color": "#ffe300"},
        {"value": 500, "color": "#fff300"},
        {"value": 600, "color": "#d0f800"},
        {"value": 700, "color": "#a0fd00"},
        {"value": 800, "color": "#6ee100"},
        {"value": 901, "color": "#39a500"},
        {
            "value": 1000,
            "color": "#026900",
        },
    ],
    "legend": {
        "begin": "0",
        "end": "1000",
        "decimal_places": 0,
        "ticks_every": 100,
        "strip_location": [0.05, 0.5, 0.89, 0.15],
        "tick_labels": {
            "1000": {"prefix": ">"},
        },
    },
}

style_wofs_frequency = {
    "name": "WOfS_frequency",
    "title": " Water Summary",
    "abstract": "WOfS summary showing the frequency of Wetness",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "frequency",
        },
    },
    "needed_bands": ["frequency"],
    "include_in_feature_info": False,
    "color_ramp": [
        {"value": 0.0, "color": "#000000", "alpha": 0.0},
        {"value": 0.002, "color": "#000000", "alpha": 0.0},
        {"value": 0.005, "color": "#8e0101", "alpha": 0.25},
        {"value": 0.01, "color": "#cf2200", "alpha": 0.75},
        {"value": 0.02, "color": "#e38400"},
        {"value": 0.05, "color": "#e3df00"},
        {"value": 0.1, "color": "#a6e300"},
        {"value": 0.2, "color": "#62e300"},
        {"value": 0.3, "color": "#00e32d"},
        {"value": 0.4, "color": "#00e384"},
        {"value": 0.5, "color": "#00e3c8"},
        {"value": 0.6, "color": "#00c5e3"},
        {"value": 0.7, "color": "#0097e3"},
        {"value": 0.8, "color": "#005fe3"},
        {"value": 0.9, "color": "#000fe3"},
        {"value": 1.0, "color": "#5700e3"},
    ],
    "legend": {
        "url": "https://data.dea.ga.gov.au/WOfS/filtered_summary/v2.1.0/wofs_full_summary_legend.png",
    },
}

style_wofs_frequency_blue = {
    "name": "WOfS_frequency_blues_transparent",
    "title": "Water Summary (Blue)",
    "abstract": "WOfS summary showing the frequency of Wetness",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "frequency",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["frequency"],
    "color_ramp": [
        {
            "value": 0.0,
            "color": "#ffffff",
            "alpha": 0.0,
        },
        {
            "value": 0.001,
            "color": "#d5fef9",
            "alpha": 0.0,
        },
        {
            "value": 0.02,
            "color": "#d5fef9",
        },
        {"value": 0.2, "color": "#71e3ff"},
        {"value": 0.4, "color": "#01ccff"},
        {"value": 0.6, "color": "#0178ff"},
        {"value": 0.8, "color": "#2701ff"},
        {"value": 1.0, "color": "#5700e3"},
    ],
    "legend": legend_idx_percentage_by_20,
}

c3_wofs_layer = {
    "title": "DEA Water Observations Multi Year (Landsat, C3)",
    "name": "ga_ls_wo_fq_myear_3",
    "abstract": """Geoscience Australia Landsat Water Observations Frequency Multi Year Collection 3
For service status information, see https://status.dea.ga.gov.au
""",
    "product_name": "ga_ls_wo_fq_myear_3",
    "bands": bands_wofs_sum,
    "resource_limits": reslim_wms_min_zoom_15_cache_rules,
    "native_crs": "EPSG:3577",
    "native_resolution": [30, -30],
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "styling": {
        "default_style": "WOfS_frequency",
        "styles": [
            style_wofs_frequency,
            style_wofs_frequency_blue,
            style_wofs_count_wet,
            style_wofs_count_clear,
        ],
    },
}
