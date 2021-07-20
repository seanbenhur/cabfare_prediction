# adopted from the madewithml mlops lesson


from datetime import datetime
from feast import Entity, Feature, FeatureView, ValueType
from feast.data_source import FileSource
from google.protobuf.duration_pb2 import Duration
from pathlib import Path

# Read data
START_TIME = "1970-01-01"
project_details = FileSource(
    path="data/features.parquet",
    event_timestamp_column="time_stamp",
)

# Define an entity for the project
project = Entity(
    name="id",
    value_type=ValueType.INT64,
    description="project id",
)


project_details_view = FeatureView(
    name="project_details",
    entities=["id"],
    ttl=Duration(
        seconds=(datetime.today() - datetime.strptime(START_TIME, "%Y-%m-%d")).days * 24 * 60 * 60
    ),
    features=[
        Feature(name="cab_provider", dtype=ValueType.STRING),
        Feature(name="source", dtype=ValueType.STRING_LIST),
    ],
    online=True,
    input=project_details,
    tags={},
)


