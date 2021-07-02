"""A Python Pulumi program"""

import pulumi

import components.exercism as exercism


track_name = "python"

exercism.Track(
    track_name, track_args=exercism.TrackArgs(name=track_name, workspace="../"), opts=pulumi.ResourceOptions()
)
