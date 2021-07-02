import pulumi
import pulumi.dynamic as dynamic

from typing import Dict, Any, Sequence
from attr import dataclass

from typing_extensions import TypedDict


@dataclass
class ExerciseArgs(TypedDict):
    name: pulumi.Input[str]
    track: pulumi.Input[str]
    files: pulumi.Input[Sequence[pulumi.Input[str]]]

    @staticmethod
    def from_inputs(inputs: Dict[str, Any]) -> 'ExerciseArgs':
        exercise_args = inputs['exercise_args']
        return ExerciseArgs(name=exercise_args['name'], track=exercise_args['track'], files=exercise_args['files'])


class ExerciseProvider(dynamic.ResourceProvider):
    def create(self, inputs: Dict[str, Any]) -> dynamic.CreateResult:
        exercise_args = ExerciseArgs.from_inputs(inputs)

        id_ = f'{exercise_args.track}-{exercise_args.name}'
        return dynamic.CreateResult(id_=id_, outs=inputs)


class Exercise(dynamic.Resource):
    uuid: pulumi.Output[str]
    checksum: pulumi.Output[str]

    def __init__(self, name: str, exercise_args: ExerciseArgs, opts: pulumi.ResourceOptions):
        self.exercise_args = exercise_args
        self.uuid = None
        self.checksum = None

        super().__init__(
            ExerciseProvider(),
            name=name,
            props={'exercise_args': exercise_args, 'uuid': None, 'checksum': None},
            opts=opts,
        )
