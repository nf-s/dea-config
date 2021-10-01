#!/usr/bin/env bash

set -eu
set -x

for prod_def_yaml in $(find /env/config/products -name '*.yaml'); do
    if [[ $prod_def_yaml != "/env/config/products/baseline_satellite_data/nrt/sentinel/eo_s2_nrt.odc-type.yaml" && $prod_def_yaml != "/env/config/products/land_and_vegetation/mangrove/mangrove.yaml" && $prod_def_yaml != "/env/config/products/land_and_vegetation/fractional-cover/ga_ls_fc_pc_cyear_3.yaml" && $prod_def_yaml != "/env/config/products/land_and_vegetation/fractional-cover/product-definition.yaml" && $prod_def_yaml != *"decomissioned/"* ]]; then
        datacube product add $prod_def_yaml
    fi
done

if [ $(datacube product list | wc -l) -ne 65 ]; then
     exit 1
fi

set +x
