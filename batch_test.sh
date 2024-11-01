#!/bin/bash

for ((i=1;i<=35;i++))
do
	printf "%d " $i
	python test.py --test_epoch $i > log_test.log
	head -n 1 log_test.log
done
