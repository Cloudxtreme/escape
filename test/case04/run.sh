#!/usr/bin/env bash

CWD="test/case04"

echo -e "\n======================================================================"
echo -e "==                        TEST CASE 4                               =="
echo -e "======================================================================\n"

./escape.py --debug --test --quit --log ${CWD}/escape.log --config ${CWD}/test.config --service ${CWD}/request.nffg