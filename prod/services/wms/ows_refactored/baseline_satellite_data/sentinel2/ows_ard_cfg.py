from ows_refactored.baseline_satellite_data.sentinel2.band_s2_cfg import \
    bands_sentinel2_ard_nbart
from ows_refactored.baseline_satellite_data.sentinel2.style_s2_cfg import \
    styles_s2_list
from ows_refactored.ows_reslim_cfg import reslim_wms_min_zoom_15_cache_rules

s2b_layer = {
    "name": "s2b_ard_granule_nbar_t",
    "title": "DEA Surface Reflectance (Sentinel-2B MSI)",
    "abstract": """Sentinel-2 Multispectral Instrument - Nadir BRDF Adjusted Reflectance + Terrain Illumination Correction (Sentinel-2B MSI)

This product has been corrected to account for variations caused by atmospheric properties, sun position and sensor view angle at time of image capture.

These corrections have been applied to all satellite imagery in the Sentinel-2 archive. This is undertaken to allow comparison of imagery acquired at different times, in different seasons and in different geographic locations.

These products also indicate where the imagery has been affected by cloud or cloud shadow, contains missing data or has been affected in other ways. The Surface Reflectance products are useful as a fundamental starting point for any further analysis, and underpin all other optical derived Digital Earth Australia products.

This is a definitive archive of daily Sentinel-2 data. This is processed using correct ancillary data to provide a more accurate product than the Near Real Time. The Surface Reflectance product has been corrected to account for variations caused by atmospheric properties, sun position and sensor view angle at time of image capture. These corrections have been applied to all satellite imagery in the Sentinel-2 archive. For more information see http://pid.geoscience.gov.au/dataset/ga/129684 The Normalised Difference Chlorophyll Index (NDCI) is based on the method of Mishra & Mishra 2012, and adapted to bands on the Sentinel-2A & B sensors. The index indicates levels of chlorophyll-a (chl-a) concentrations in complex turbid productive waters such as those encountered in many inland water bodies. The index has not been validated in Australian waters, and there are a range of environmental conditions that may have an effect on the accuracy of the derived index values in this test implementation, including: - Influence on the remote sensing signal from nearby land and/or atmospheric effects - Optically shallow water - Cloud cover Mishra, S., Mishra, D.R., 2012. Normalized difference chlorophyll index: A novel model for remote estimation of chlorophyll-a concentration in turbid productive waters. Remote Sensing of Environment, Remote Sensing of Urban Environments 117, 394–406. https://doi.org/10.1016/j.rse.2011.10.016
https://cmi.ga.gov.au/data-products/dea/190/dea-surface-reflectance-nbart-sentinel-2-msi

For service status information, see https://status.dea.ga.gov.au
""",
    "product_name": "s2b_ard_granule",
    "bands": bands_sentinel2_ard_nbart,
    "resource_limits": reslim_wms_min_zoom_15_cache_rules,
    "dynamic": True,
    "native_crs": "EPSG:3577",
    "native_resolution": [10.0, 10.0],
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "flags": [
        {
            "band": "fmask",
            "product": "s2b_ard_granule",
            "ignore_time": False,
            "ignore_info_flags": []
        },
        {
            "band": "land",
            "product": "geodata_coast_100k",
            "ignore_time": True,
            "ignore_info_flags": []
        },
    ],
    "styling": {"default_style": "simple_rgb", "styles": styles_s2_list},
}

s2a_layer = {
    "name": "s2a_ard_granule_nbar_t",
    "title": "DEA Surface Reflectance (Sentinel-2A MSI)",
    "abstract": """Sentinel-2 Multispectral Instrument - Nadir BRDF Adjusted Reflectance + Terrain Illumination Correction (Sentinel-2A MSI)

This product has been corrected to account for variations caused by atmospheric properties, sun position and sensor view angle at time of image capture.

These corrections have been applied to all satellite imagery in the Sentinel-2 archive. This is undertaken to allow comparison of imagery acquired at different times, in different seasons and in different geographic locations.

These products also indicate where the imagery has been affected by cloud or cloud shadow, contains missing data or has been affected in other ways. The Surface Reflectance products are useful as a fundamental starting point for any further analysis, and underpin all other optical derived Digital Earth Australia products.

This is a definitive archive of daily Sentinel-2 data. This is processed using correct ancillary data to provide a more accurate product than the Near Real Time. The Surface Reflectance product has been corrected to account for variations caused by atmospheric properties, sun position and sensor view angle at time of image capture. These corrections have been applied to all satellite imagery in the Sentinel-2 archive. For more information see http://pid.geoscience.gov.au/dataset/ga/129684 The Normalised Difference Chlorophyll Index (NDCI) is based on the method of Mishra & Mishra 2012, and adapted to bands on the Sentinel-2A & B sensors. The index indicates levels of chlorophyll-a (chl-a) concentrations in complex turbid productive waters such as those encountered in many inland water bodies. The index has not been validated in Australian waters, and there are a range of environmental conditions that may have an effect on the accuracy of the derived index values in this test implementation, including: - Influence on the remote sensing signal from nearby land and/or atmospheric effects - Optically shallow water - Cloud cover Mishra, S., Mishra, D.R., 2012. Normalized difference chlorophyll index: A novel model for remote estimation of chlorophyll-a concentration in turbid productive waters. Remote Sensing of Environment, Remote Sensing of Urban Environments 117, 394–406. https://doi.org/10.1016/j.rse.2011.10.016
https://cmi.ga.gov.au/data-products/dea/190/dea-surface-reflectance-nbart-sentinel-2-msi

For service status information, see https://status.dea.ga.gov.au
""",
    "product_name": "s2a_ard_granule",
    "bands": bands_sentinel2_ard_nbart,
    "resource_limits": reslim_wms_min_zoom_15_cache_rules,
    "dynamic": True,
    "native_crs": "EPSG:3577",
    "native_resolution": [10.0, 10.0],
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "flags": [
        {
            "band": "fmask",
            "product": "s2a_ard_granule",
            "ignore_time": False,
            "ignore_info_flags": []
        },
        {
            "band": "land",
            "product": "geodata_coast_100k",
            "ignore_time": True,
            "ignore_info_flags": []
        },
    ],
    "styling": {"default_style": "simple_rgb", "styles": styles_s2_list},
}

combined_layer = {
    "title": "DEA Surface Reflectance (Sentinel-2)",
    "name": "s2_ard_granule_nbar_t",
    "abstract": """Sentinel-2 Multispectral Instrument - Nadir BRDF Adjusted Reflectance + Terrain Illumination Correction (Sentinel-2 MSI)

This product has been corrected to account for variations caused by atmospheric properties, sun position and sensor view angle at time of image capture.

These corrections have been applied to all satellite imagery in the Sentinel-2 archive. This is undertaken to allow comparison of imagery acquired at different times, in different seasons and in different geographic locations.

These products also indicate where the imagery has been affected by cloud or cloud shadow, contains missing data or has been affected in other ways. The Surface Reflectance products are useful as a fundamental starting point for any further analysis, and underpin all other optical derived Digital Earth Australia products.

This is a definitive archive of daily Sentinel-2 data. This is processed using correct ancillary data to provide a more accurate product than the Near Real Time.
The Surface Reflectance product has been corrected to account for variations caused by atmospheric properties, sun position and sensor view angle at time of image capture. These corrections have been applied to all satellite imagery in the Sentinel-2 archive.
The Normalised Difference Chlorophyll Index (NDCI) is based on the method of Mishra & Mishra 2012, and adapted to bands on the Sentinel-2A & B sensors.
The index indicates levels of chlorophyll-a (chl-a) concentrations in complex turbid productive waters such as those encountered in many inland water bodies. The index has not been validated in Australian waters, and there are a range of environmental conditions that may have an effect on the accuracy of the derived index values in this test implementation, including:
- Influence on the remote sensing signal from nearby land and/or atmospheric effects
- Optically shallow water
- Cloud cover
Mishra, S., Mishra, D.R., 2012. Normalized difference chlorophyll index: A novel model for remote estimation of chlorophyll-a concentration in turbid productive waters. Remote Sensing of Environment, Remote Sensing of Urban Environments 117, 394–406. https://doi.org/10.1016/j.rse.2011.10.016

For more information see http://pid.geoscience.gov.au/dataset/ga/129684
https://cmi.ga.gov.au/data-products/dea/190/dea-surface-reflectance-nbart-sentinel-2-msi

For service status information, see https://status.dea.ga.gov.au
""",
    "multi_product": True,
    "product_names": ["s2a_ard_granule", "s2b_ard_granule"],
    "bands": bands_sentinel2_ard_nbart,
    "resource_limits": reslim_wms_min_zoom_15_cache_rules,
    "dynamic": True,
    "native_crs": "EPSG:3577",
    "native_resolution": [10.0, 10.0],
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "flags": [
        {
            "band": "fmask",
            "products": ["s2a_ard_granule", "s2b_ard_granule"],
            "ignore_time": False,
            "ignore_info_flags": []
        },
        {
            "band": "land",
            "products": ["geodata_coast_100k", "geodata_coast_100k"],
            "ignore_time": True,
            "ignore_info_flags": []
        },
    ],
    "styling": {"default_style": "simple_rgb", "styles": styles_s2_list},
}
