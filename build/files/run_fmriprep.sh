#!/bin/bash

source /etc/fsl/fsl.sh
source /etc/afni/afni.sh
source activate crnenv

fmriprep $@