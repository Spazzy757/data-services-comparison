#!/usr/bin/env bash

echo "First Run"
echo "#############################################"
python scripts/main.py \
       --runner SparkRunner \
       --spark-master-url spark://spark:7077 \
       --database postgres \
       --input dataset/league_of_legends.csv \
       --database_host db \
       --table_name league_game_board \
       --database_user postgres \
       --database_password postgres
