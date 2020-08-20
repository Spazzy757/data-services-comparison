# pytype: skip-file

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import csv
import logging
import sys
import time
from datetime import datetime
import os
import io

import apache_beam as beam
from apache_beam.metrics.metric import Metrics
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import SetupOptions
from beam_nuggets.io import relational_db

def get_csv_reader(readable_file):

    # Return the csv reader
    import csv

    with open('coors.csv', mode='r') as infile:
        reader = csv.reader(infile)
        mydict = {rows[0]:rows[1] for rows in reader}
    return mydict


def run(argv=None, save_main_session=True):
  """Main entry point; defines and runs the pipeline."""
  logging.info("HERE")
  parser = argparse.ArgumentParser()

  parser.add_argument(
      '--input',
      type=str,
      default='dataset/league_of_legends_dataset.csv',
      help='Path to the data file(s) containing game data.'
  )
  parser.add_argument(
      '--database',
      type=str,
      required=True,
      help= 'Database Name'
  )
  parser.add_argument(
      '--database_host',
      type=str,
      required=True,
      help= 'Database Host'
  )
  parser.add_argument(
      '--table_name',
      default='leader_board',
      help='table where to store the data'
  )
  parser.add_argument(
      '--database_user',
      default='postgres',
      help='table where to store the data'
  )
  parser.add_argument(
      '--database_password',
      default='postgres',
      help='table where to store the data'
  )

  args, pipeline_args = parser.parse_known_args(argv)

  options = PipelineOptions(pipeline_args)
  logging.info(pipeline_args)
  source_config = relational_db.SourceConfiguration(
    drivername='postgresql',
    host=args.database_host,
    port=5432,
    create_if_missing=True,
    username=args.database_user,
    password=args.database_password,
    database=args.database
  )

  table_config = relational_db.TableConfiguration(
    name=args.table_name,
    create_if_missing=True,
    primary_key_columns=['gameId']
  )


  with beam.Pipeline(options=options) as p:
    (  # pylint: disable=expression-not-assigned
        p
        | 'Setting Up File' >> beam.Create([args.input])
        | 'Reading Input Data' >> beam.FlatMap(get_csv_reader)
        | 'Writing to DB table' >> relational_db.Write(
            source_config=source_config,
            table_config=table_config
        )
    )


# [END main]

if __name__ == '__main__':
  startTime = datetime.now()
  logging.getLogger().setLevel(logging.INFO)
  run()
  run_time = datetime.now() - startTime
  logging.info('Run Time => {}'.format(run_time))

