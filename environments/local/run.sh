#!/usr/bin/env bash
echo "First Run"
echo "#############################################"
python scripts/main.py \
       --database postgres \
       --input dataset/league_of_legends.csv \
       --database_host 127.0.0.1 \
       --table_name league_game_board \
       --database_user postgres \
       --database_password postgres
echo "#############################################"
echo "Second Run With Updates"
echo "#############################################"
python scripts/main.py \
       --database postgres \
       --input dataset/league_of_legends_updated.csv \
       --database_host 127.0.0.1 \
       --table_name league_game_board \
       --database_user postgres \
       --database_password postgres
