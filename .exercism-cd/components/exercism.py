import pulumi

import providers.exercism as exercism

from typing_extensions import TypedDict
from attr import dataclass


@dataclass
class TrackArgs:
    name: pulumi.Input[str]
    workspace: pulumi.Input[str]

    @staticmethod
    def from_inputs(inputs):
        return TrackArgs(name=inputs['name'], workspace=['workspace'])


class Track(pulumi.ComponentResource):
    def __init__(self, name: str, track_args: TrackArgs, opts: pulumi.ResourceOptions = None):
        super().__init__('exercism:exercism:ExercismTrack', name=name, props={'track_args': {**vars(track_args)}}, opts=opts)

        track_opts = pulumi.ResourceOptions(parent=self)

        track_name = track_args.name
        #exercism_workspace = track_args.workspace

        exercise_name = 'hello-world'
        exercise_files = ['hello-world.py']
        exercism.Exercise(
            f'{track_name}-{exercise_name}',
            exercise_args=exercism.ExerciseArgs(name=exercise_name, track=track_name, files=exercise_files),
            opts=track_opts,
        )

        self.register_outputs({})
