#!/usr/bin/env bash

echo "First Run"
echo "#############################################"
python scripts/main.py \
       --runner FlinkRunner \
       --flink_master localhost:8081 \
       --setup_file scripts/setup.py \
       --environment_type EXTERNAL \
       --environment_config localhost:50000 \
       --database postgres \
       --input /dataset/league_of_legends.csv \
       --database_host db \
       --table_name league_game_board \
       --database_user postgres \
       --database_password postgres
