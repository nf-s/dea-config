from ows_refactored.inland_water.wofs.bands_wo_cfg import bands_wofs_sum
from ows_refactored.ows_legend_cfg import (legend_idx_percentage_by_20,
                                           legend_idx_thirtyplus_4ticks,
                                           legend_idx_twentyplus_3ticks)
from ows_refactored.ows_reslim_cfg import reslim_wms_min_zoom_15_cache_rules

style_wofs_seasonal_wet = {
    "name": "seasonal_water_observations",
    "title": "Wet Count",
    "abstract": "WOfS seasonal summary showing the count of water observations",
    "needed_bands": ["count_wet"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "count_wet",
        },
    },
    "color_ramp": [
        {"value": 0, "color": "#666666", "alpha": 0},
        {
            # purely for legend display
            # we should not get fractional
            # values in this styles
            "value": 0.2,
            "color": "#990000",
            "alpha": 1,
        },
        {"value": 2, "color": "#990000"},
        {"value": 4, "color": "#E38400"},
        {"value": 6, "color": "#E3DF00"},
        {"value": 8, "color": "#00E32D"},
        {"value": 10, "color": "#00E3C8"},
        {"value": 12, "color": "#0097E3"},
        {"value": 14, "color": "#005FE3"},
        {"value": 16, "color": "#000FE3"},
        {"value": 18, "color": "#000EA9"},
        {
            "value": 20,
            "color": "#5700E3",
        },
    ],
    "legend": legend_idx_twentyplus_3ticks,
}

style_wofs_seasonal_clear = {
    "name": "seasonal_clear_observations",
    "title": "Clear Count",
    "abstract": "WOfS seasonal summary showing the count of clear observations",
    "needed_bands": ["count_clear"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "count_clear",
        },
    },
    "color_ramp": [
        {"value": 0, "color": "#FFFFFF", "alpha": 0},
        {
            # purely for legend display
            # we should not get fractional
            # values in this styles
            "value": 0.2,
            "color": "#B21800",
            "alpha": 1,
        },
        {"value": 1, "color": "#B21800"},
        {"value": 4, "color": "#ef8500"},
        {"value": 8, "color": "#ffb800"},
        {"value": 10, "color": "#ffd000"},
        {"value": 13, "color": "#fff300"},
        {"value": 16, "color": "#fff300"},
        {"value": 20, "color": "#c1ec00"},
        {"value": 24, "color": "#6ee100"},
        {"value": 28, "color": "#39a500"},
        {
            "value": 30,
            "color": "#026900",
        },
    ],
    "legend": legend_idx_thirtyplus_4ticks,
}

style_seasonal_wofs_summary_frequency = {
    "name": "seasonal_WOfS_frequency",
    "title": " Water Summary",
    "abstract": "WOfS seasonal summary showing the frequency of Wetness",
    "needed_bands": ["frequency"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "frequency",
        },
    },
    "color_ramp": [
        {"value": 0.0, "color": "#000000", "alpha": 0.0},
        {"value": 0.02, "color": "#000000", "alpha": 0.0},
        {"value": 0.05, "color": "#8e0101", "alpha": 0.25},
        {"value": 0.1, "color": "#cf2200", "alpha": 0.75},
        {"value": 0.2, "color": "#e38400"},
        {"value": 0.3, "color": "#e3df00"},
        {"value": 0.4, "color": "#62e300"},
        {"value": 0.5, "color": "#00e32d"},
        {"value": 0.6, "color": "#00e3c8"},
        {"value": 0.7, "color": "#0097e3"},
        {"value": 0.8, "color": "#005fe3"},
        {"value": 0.9, "color": "#000fe3"},
        {"value": 1.0, "color": "#5700e3"},
    ],
    "legend": legend_idx_percentage_by_20,
}

style_seasonal_wofs_summary_frequency_blue = {
    "name": "seasonal_WOfS_frequency_blues_transparent",
    "title": "Water Summary (Blue)",
    "abstract": "WOfS seasonal summary showing the frequency of Wetness",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "frequency",
        },
    },
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

style_wofs_seasonal_wet_c3 = {
    "name": "seasonal_water_observations_c3",
    "title": "Wet Count",
    "abstract": "WOfS seasonal summary showing the count of water observations",
    "needed_bands": ["count_wet"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "count_wet",
        },
    },
    "color_ramp": [
        {"value": 0, "color": "#666666", "alpha": 0},
        {
            # purely for legend display
            # we should not get fractional
            # values in this styles
            "value": 0.2,
            "color": "#990000",
            "alpha": 1,
        },
        {"value": 2, "color": "#990000"},
        {"value": 4, "color": "#E38400"},
        {"value": 6, "color": "#E3DF00"},
        {"value": 8, "color": "#00E32D"},
        {"value": 10, "color": "#00E3C8"},
        {"value": 12, "color": "#0097E3"},
        {"value": 14, "color": "#005FE3"},
        {"value": 16, "color": "#000FE3"},
        {"value": 18, "color": "#000EA9"},
        {
            "value": 20,
            "color": "#5700E3",
        },
    ],
    "pq_masks": [
        {
            "band": "land",
            "invert": True,
            "enum": 0,
        }
    ],
    "legend": legend_idx_twentyplus_3ticks,
}

style_wofs_seasonal_clear_c3 = {
    "name": "seasonal_clear_observations_c3",
    "title": "Clear Count",
    "abstract": "WOfS seasonal summary showing the count of clear observations",
    "needed_bands": ["count_clear"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "count_clear",
        },
    },
    "color_ramp": [
        {"value": 0, "color": "#FFFFFF", "alpha": 0},
        {
            # purely for legend display
            # we should not get fractional
            # values in this styles
            "value": 0.2,
            "color": "#B21800",
            "alpha": 1,
        },
        {"value": 1, "color": "#B21800"},
        {"value": 4, "color": "#ef8500"},
        {"value": 8, "color": "#ffb800"},
        {"value": 10, "color": "#ffd000"},
        {"value": 13, "color": "#fff300"},
        {"value": 16, "color": "#fff300"},
        {"value": 20, "color": "#c1ec00"},
        {"value": 24, "color": "#6ee100"},
        {"value": 28, "color": "#39a500"},
        {
            "value": 30,
            "color": "#026900",
        },
    ],
    "pq_masks": [
        {
            "band": "land",
            "invert": True,
            "enum": 0,
        }
    ],
    "legend": legend_idx_thirtyplus_4ticks,
}

style_seasonal_wofs_summary_frequency_c3 = {
    "name": "seasonal_WOfS_frequency_c3",
    "title": " Water Summary",
    "abstract": "WOfS seasonal summary showing the frequency of Wetness",
    "needed_bands": ["frequency"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "frequency",
        },
    },
    "color_ramp": [
        {"value": 0.0, "color": "#000000", "alpha": 0.0},
        {"value": 0.02, "color": "#000000", "alpha": 0.0},
        {"value": 0.05, "color": "#8e0101", "alpha": 0.25},
        {"value": 0.1, "color": "#cf2200", "alpha": 0.75},
        {"value": 0.2, "color": "#e38400"},
        {"value": 0.3, "color": "#e3df00"},
        {"value": 0.4, "color": "#62e300"},
        {"value": 0.5, "color": "#00e32d"},
        {"value": 0.6, "color": "#00e3c8"},
        {"value": 0.7, "color": "#0097e3"},
        {"value": 0.8, "color": "#005fe3"},
        {"value": 0.9, "color": "#000fe3"},
        {"value": 1.0, "color": "#5700e3"},
    ],
    "pq_masks": [
        {
            "band": "land",
            "invert": True,
            "enum": 0,
        }
    ],
    "legend": legend_idx_percentage_by_20,
}

style_seasonal_wofs_summary_frequency_blue_c3 = {
    "name": "seasonal_WOfS_frequency_blues_transparent_c3",
    "title": "Water Summary (Blue)",
    "abstract": "WOfS seasonal summary showing the frequency of Wetness",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "frequency",
        },
    },
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
    "pq_masks": [
        {
            "band": "land",
            "invert": True,
            "enum": 0,
        }
    ],
    "legend": legend_idx_percentage_by_20,
}

layers = {
    "title": "DEA April-October Water Observations Source Data (C2)",
    "abstract": "WOfS",
    "layers": [
        {
            "title": "DEA April-October Wet Observation Statistics (Landsat, C2)",
            "name": "wofs_apr_oct_summary_wet",
            "abstract": """Water Observations from Space Statistics 25m 2.1.5 (Landsat, April - October, Wet)
Water Observations from Space - April to October Statistics is a set of seasonal statistical summaries of the water observations contained in WOfS. The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time.

This product is Water Observations from Space - April to October Statistics, a set of seasonal statistical summaries of the WOfS product that combines the many years of WOfS observations into summary products that help the understanding of surface water across Australia. As no confidence filtering is applied to this product, it is affected by noise where misclassifications have occurred in the WOfS water classifications, and hence can be difficult to interpret on its own.
The confidence layer and filtered summary are contained in the Water Observations from Space Statistics - Filtered Summary product, which provide a noise-reduced view of the water summary.

This layer contains Water Summary: what percentage of clear observations were detected as wet (ie. the ratio of wet to clear as a percentage). No clear observations of water causes an area to appear transparent, 1-50 total clear observations of water correlate with red and yellow colours, 100 clear observations of water correlate with green, 200 clear observations of water correlates with light blue, 300 clear observations of water correlates to deep blue and 400 and over observations of clear water correlate to purple.
https://cmi.ga.gov.au/data-products/dea/143/dea-water-observations-statistics-landsat
For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "wofs_apr_oct_summary",
            "bands": bands_wofs_sum,
            "resource_limits": reslim_wms_min_zoom_15_cache_rules,
            "native_crs": "EPSG:3577",
            "native_resolution": [25, -25],
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "styling": {
                "default_style": "seasonal_water_observations",
                "styles": [
                    style_wofs_seasonal_wet,
                ],
            },
        },
        {
            "title": "DEA April-October Clear Observation Statistics (Landsat, C2)",
            "name": "wofs_apr_oct_summary_clear",
            "abstract": """Water Observations from Space Statistics 25m 2.1.5 (Landsat, April - October, Clear)
Water Observations from Space - April to October Statistics is a set of seasonal statistical summaries of the water observations contained in WOfS. The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time. This product is Water Observations from Space - April to October Statistics, a set of seasonal statistical summaries of the WOfS product that combines the many years of WOfS observations into summary products that help the understanding of surface water across Australia. As no confidence filtering is applied to this product, it is affected by noise where misclassifications have occurred in the WOfS water classifications, and hence can be difficult to interpret on its own. The confidence layer and filtered summary are contained in the Water Observations from Space Statistics - Filtered Summary product, which provide a noise-reduced view of the water summary. This layer contains Water Summary: what percentage of clear observations were detected as wet (ie. the ratio of wet to clear as a percentage). No clear observations causes an area to appear transparent, 1-300 total clear observations of water correlate with red and yellow colours, 400 clear observations correlates with light green, 800 clear observations and above correlates with dark green.
https://cmi.ga.gov.au/data-products/dea/143/dea-water-observations-statistics-landsat
For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "wofs_apr_oct_summary",
            "bands": bands_wofs_sum,
            "resource_limits": reslim_wms_min_zoom_15_cache_rules,
            "native_crs": "EPSG:3577",
            "native_resolution": [25, -25],
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "styling": {
                "default_style": "seasonal_clear_observations",
                "styles": [
                    style_wofs_seasonal_clear,
                ],
            },
        },
    ],
}

statistics_layer = {
    "title": "DEA April-October Seasonal Water Observations (Landsat, C2)",
    "name": "wofs_apr_oct_summary_statistics",
    "abstract": """Water Observations from Space Statistics 25m 2.1.5 (Landsat, April - October, Frequency)
Water Observations from Space - Seasonal Statistics is a set of seasonal statistical summaries of the water observations contained in WOfS. The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time. This product is Water Observations from Space - April to October Statistics, a set of seasonal statistical summaries of the WOfS product that combines the many years of WOfS observations into summary products that help the understanding of surface water across Australia. As no confidence filtering is applied to this product, it is affected by noise where misclassifications have occurred in the WOfS water classifications, and hence can be difficult to interpret on its own. The confidence layer and filtered summary are contained in the Water Observations from Space Statistics - Filtered Summary product, which provide a noise-reduced view of the water summary. This layer contains Water Summary: what percentage of clear observations were detected as wet (ie. the ratio of wet to clear as a percentage). No clear observations of water causes an area to appear transparent, few clear observations of water correlate with red and yellow colours, deep blue and purple correspond to an area being wet through 90%-100% of clear observations.
https://cmi.ga.gov.au/data-products/dea/143/dea-water-observations-statistics-landsat
For service status information, see https://status.dea.ga.gov.au
""",
    "product_name": "wofs_apr_oct_summary",
    "bands": bands_wofs_sum,
    "resource_limits": reslim_wms_min_zoom_15_cache_rules,
    "native_crs": "EPSG:3577",
    "native_resolution": [25, -25],
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "styling": {
        "default_style": "seasonal_WOfS_frequency",
        "styles": [
            style_seasonal_wofs_summary_frequency,
            style_seasonal_wofs_summary_frequency_blue,
        ],
    },
}

# Collection 3 layers
c3_layers = {
    "title": "DEA April-October Water Observations Source Data (C3)",
    "abstract": "WOfS",
    "layers": [
        {
            "title": "DEA April-October Wet Observation Statistics (Landsat, C3)",
            "name": "wofs_apr_oct_summary_wet_c3",
            "abstract": """DEA Water Observations Statistics 30m 3.1.6 (Landsat, April - October, Wet)
The DEA Water Observations Statistic, April to October is a set of seasonal statistical summaries of the DEA Water Observations product that combines the many years of observations into summary products that help the understanding of surface water across Australia. The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time.

This layer contains wet observation count: how many times water was detected in observations that were clear.

No clear observations of water causes an area to appear transparent,
1-6 total clear observations of water correlate with red and yellow colours,
7-12 clear observations of water correlate with green through to light blue,
12+ clear observations of water correlates with increasingly dark shades of blue.

https://cmi.ga.gov.au/data-products/dea/686/dea-water-observations-statistics-landsat
For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "ga_ls_wo_fq_apr_oct_3",
            "bands": bands_wofs_sum,
            "resource_limits": reslim_wms_min_zoom_15_cache_rules,
            "time_resolution": "month",
            "native_crs": "EPSG:3577",
            "native_resolution": [30, -30],
            "flags": [
                {
                    "band": "land",
                    "product": "geodata_coast_100k",
                    "ignore_time": True,
                    "ignore_info_flags": [],
                },
            ],
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "styling": {
                "default_style": "seasonal_water_observations_c3",
                "styles": [
                    style_wofs_seasonal_wet_c3,
                ],
            },
        },
        {
            "title": "DEA April-October Clear Observation Statistics (Landsat, C3)",
            "name": "wofs_apr_oct_summary_clear_c3",
            "abstract": """Water Observations from Space Statistics 30m 3.1.6 (Landsat, April - October, Clear)
The DEA Water Observations Statistic, April to October is a set of seasonal statistical summaries of the DEA Water Observations product that combines the many years of observations into summary products that help the understanding of surface water across Australia. The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time.

This layer contains clear observation count: how many times an area could be clearly seen (i.e. not affected by clouds, shadows or other satellite observation problems)

No clear observations causes an area to appear transparent,
1-15 total clear observations correlates with red and yellow colours,
18-22 clear observations correlates with light green,
23+ clear observations correlates with inreasingly dark shades of green.

https://cmi.ga.gov.au/data-products/dea/686/dea-water-observations-statistics-landsat
For service status information, see https://status.dea.ga.gov.au
""",
            "product_name": "ga_ls_wo_fq_apr_oct_3",
            "bands": bands_wofs_sum,
            "resource_limits": reslim_wms_min_zoom_15_cache_rules,
            "time_resolution": "month",
            "native_crs": "EPSG:3577",
            "native_resolution": [30, -30],
            "flags": [
                {
                    "band": "land",
                    "product": "geodata_coast_100k",
                    "ignore_time": True,
                    "ignore_info_flags": [],
                },
            ],
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "styling": {
                "default_style": "seasonal_clear_observations_c3",
                "styles": [
                    style_wofs_seasonal_clear_c3,
                ],
            },
        },
    ],
}

c3_statistics_layer = {
    "title": "DEA April-October Seasonal Water Observations (Landsat, C3)",
    "name": "wofs_apr_oct_summary_statistics_c3",
    "abstract": """DEA Water Observations Statistics 30m 3.1.6 (Landsat, April - October, Frequency)
The DEA Water Observations April to October Statistic is a set of seasonal statistical summaries of the DEA Water Observations product that combines the many years of observations into summary products that help the understanding of surface water across Australia. The layers available are: the count of clear observations; the count of wet observations; the percentage of wet observations over time.

This layer contains Water Summary: what percentage of clear observations were detected as wet (ie. the ratio of wet to clear as a percentage).

No clear observations of water causes an area to appear transparent,
red through to yellow represent areas seen to be wet up to 30% of the time,
green through to light blue represent areas seen to be wet 40-60% of the time,
deep blue and purple correspond to an area being wet through 80%-100% of clear observations.

https://cmi.ga.gov.au/data-products/dea/686/dea-water-observations-statistics-landsat
For service status information, see https://status.dea.ga.gov.au
""",
    "product_name": "ga_ls_wo_fq_apr_oct_3",
    "bands": bands_wofs_sum,
    "resource_limits": reslim_wms_min_zoom_15_cache_rules,
    "native_crs": "EPSG:3577",
    "native_resolution": [30, -30],
    "time_resolution": "month",
    "flags": [
        {
            "band": "land",
            "product": "geodata_coast_100k",
            "ignore_time": True,
            "ignore_info_flags": [],
        }
    ],
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "styling": {
        "default_style": "seasonal_WOfS_frequency_c3",
        "styles": [
            style_seasonal_wofs_summary_frequency_c3,
            style_seasonal_wofs_summary_frequency_blue_c3,
        ],
    },
}
