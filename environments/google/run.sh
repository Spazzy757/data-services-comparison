
#!/usr/bin/env bash

echo "First Run"
echo "#############################################"
python scripts/main.py \
       --setup_file scripts/setup.py \
       --database league_of_legends \
       --temp_location gs://$GOOGLE_BUCKET/tmp/ \
       --runner DataflowRunner \
       --project $GOOGLE_PROJECT \
       --input gs://$GOOGLE_BUCKET/league_of_legends_updated.csv \
       --region $GOOGLE_REGION \
       --database_host $DATABASE_HOST \
       --table_name league_game_board \
       --database_user $DATABASE_USERNAME \
       --database_password $DATABASE_PASSWORD \
       --no_use_public_ips \
       --subnetwork $SUBNET_URL
