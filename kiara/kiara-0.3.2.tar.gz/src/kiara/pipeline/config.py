# -*- coding: utf-8 -*-

#  Copyright (c) 2021, University of Luxembourg / DHARPA project
#  Copyright (c) 2021, Markus Binsteiner
#
#  Mozilla Public License, version 2.0 (see LICENSE or https://www.mozilla.org/en-US/MPL/2.0/)

import logging
import typing
from pydantic import BaseModel, Extra, Field, root_validator, validator
from rich.console import Console, ConsoleOptions, RenderResult
from slugify import slugify

from kiara.module_config import ModuleConfig, ModuleTypeConfigSchema
from kiara.pipeline import StepValueAddress
from kiara.pipeline.structure import PipelineStep, PipelineStructure
from kiara.pipeline.utils import ensure_step_value_addresses

if typing.TYPE_CHECKING:
    from kiara.kiara import Kiara
    from kiara.pipeline.controller import PipelineController
    from kiara.pipeline.module import PipelineModule

log = logging.getLogger("kiara")


class PipelineStepConfig(ModuleConfig):
    """A class to hold the configuration of one module within a [PipelineModule][kiara.pipeline.module.PipelineModule]."""

    class Config:
        extra = Extra.forbid
        validate_assignment = True

    step_id: str = Field(description="The id of the step.")
    input_links: typing.Dict[str, typing.List[StepValueAddress]] = Field(
        default_factory=dict,
        description="The map with the name of an input link as key, and the connected module output name(s) as value.",
    )

    @root_validator(pre=True)
    def create_step_id(cls, values):

        if "module_type" not in values:
            raise ValueError("No 'module_type' specified.")
        if "step_id" not in values or not values["step_id"]:
            values["step_id"] = slugify(values["module_type"])

        return values

    @validator("step_id")
    def ensure_valid_id(cls, v):

        # TODO: check with regex
        if "." in v or " " in v:
            raise ValueError(
                f"Step id can't contain special characters or whitespaces: {v}"
            )

        return v

    @validator("module_config", pre=True)
    def ensure_dict(cls, v):

        if v is None:
            v = {}
        return v

    @validator("input_links", pre=True)
    def ensure_input_links_valid(cls, v):

        if v is None:
            v = {}

        result = {}
        for input_name, output in v.items():

            input_links = ensure_step_value_addresses(
                default_field_name=input_name, link=output
            )
            result[input_name] = input_links

        return result


# class PipelineStructureConfig(BaseModel):
#
#     parent_id: str = Field(description="The id of the parent of this structure.")
#     steps: typing.List[PipelineStepConfig] = Field(description="The steps and their connections that define this pipeline.")
#     input_aliases: typing.Union[None, str, typing.Dict[str, str]] = Field(description="A map that allows to rename the auto-generated inputs of this pipeline.", default=None)
#     output_aliases: typing.Union[None, str, typing.Dict[str, str]] = Field(description="A map that allows to rename the auto-generated outputs of this pipeline.", default=None)


class PipelineConfig(ModuleTypeConfigSchema):
    """A class to hold the configuration for a [PipelineModule][kiara.pipeline.module.PipelineModule].

    If you want to control the pipeline input and output names, you need to have to provide a map that uses the
    autogenerated field name ([step_id]__[field_name] -- 2 underscores!!) as key, and the desired field name
    as value. The reason that schema for the autogenerated field names exist is that it's hard to ensure
    the uniqueness of each field; some steps can have the same input field names, but will need different input
    values. In some cases, some inputs of different steps need the same input. Those sorts of things.
    So, to make sure that we always use the right values, I chose to implement a conservative default approach,
    accepting that in some cases the user will be prompted for duplicate inputs for the same value.

    To remedy that, the pipeline creator has the option to manually specify a mapping to rename some or all of
    the input/output fields.

    Further, because in a lot of cases there won't be any overlapping fields, the creator can specify ``auto``,
    in which case *Kiara* will automatically create a mapping that tries to map autogenerated field names
    to the shortest possible names for each case.

    Examples:

        Configuration for a pipeline module that functions as a ``nand`` logic gate (in Python):

        ``` python
        and_step = PipelineStepConfig(module_type="and", step_id="and")
        not_step = PipelineStepConfig(module_type="not", step_id="not", input_links={"a": ["and.y"]}
        nand_p_conf = PipelineConfig(doc="Returns 'False' if both inputs are 'True'.",
                            steps=[and_step, not_step],
                            input_aliases={
                                "and__a": "a",
                                "and__b": "b"
                            },
                            output_aliases={
                                "not__y": "y"
                            }}
        ```

        Or, the same thing in json:

        ``` json
        {
          "module_type_name": "nand",
          "doc": "Returns 'False' if both inputs are 'True'.",
          "steps": [
            {
              "module_type": "and",
              "step_id": "and"
            },
            {
              "module_type": "not",
              "step_id": "not",
              "input_links": {
                "a": "and.y"
              }
            }
          ],
          "input_aliases": {
            "and__a": "a",
            "and__b": "b"
          },
          "output_aliases": {
            "not__y": "y"
          }
        }
        ```
    """

    # @classmethod
    # def from_file(cls, path: typing.Union[str, Path]):
    #
    #     content = get_data_from_file(path)
    #     return PipelineConfig(**content)

    @classmethod
    def create_pipeline_config(
        cls,
        config: typing.Union[ModuleConfig, typing.Mapping[str, typing.Any], str],
        module_config: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        kiara: typing.Optional["Kiara"] = None,
    ) -> "PipelineConfig":
        """Create a PipelineModule instance.

        The main 'config' argument here can be either:

          - a string: in which case it needs to be (in that order):
            - a module id
            - an operation id
            - a path to a local file
          - a [ModuleConfig][kiara.module_config.ModuleConfig] object
          - a dict (to create a `ModuleInstsanceConfig` from


        Arguments:
            kiara: the kiara context
            config: the 'main' config object
            module_config: in case the 'main' config object was a module id, this argument is used to instantiate the module
            kiara: the kiara context (will use default context instance if not provided)

        """

        if kiara is None:
            from kiara.kiara import Kiara

            kiara = Kiara.instance()

        module_config_obj = ModuleConfig.create_module_config(
            config=config, module_config=module_config, kiara=kiara
        )

        if not module_config_obj.module_type == "pipeline":
            raise Exception(f"Not a valid pipeline configuration: {config}")

        # TODO: this is a bit round-about, to create a module config first, but it probably doesn't matter
        pipeline_config_data = module_config_obj.module_config

        module: PipelineConfig = PipelineConfig(**pipeline_config_data)
        return module

    class Config:
        extra = Extra.allow
        validate_assignment = True

    steps: typing.List[PipelineStepConfig] = Field(
        default_factory=list,
        description="A list of steps/modules of this pipeline, and their connections.",
    )
    input_aliases: typing.Union[str, typing.Dict[str, str]] = Field(
        default_factory=dict,
        description="A map of input aliases, with the calculated (<step_id>__<input_name> -- double underscore!) name as key, and a string (the resulting workflow input alias) as value. Check the documentation for the config class for which marker strings can be used to automatically create this map if possible.",
    )
    output_aliases: typing.Union[str, typing.Dict[str, str]] = Field(
        default_factory=dict,
        description="A map of output aliases, with the calculated (<step_id>__<output_name> -- double underscore!) name as key, and a string (the resulting workflow output alias) as value.  Check the documentation for the config class for which marker strings can be used to automatically create this map if possible.",
    )
    documentation: str = Field(
        default="-- n/a --", description="Documentation about what the pipeline does."
    )

    context: typing.Dict[str, typing.Any] = Field(
        default_factory=dict, description="Metadata for this workflow."
    )

    @validator("steps", pre=True)
    def _validate_steps(cls, v):

        steps = []
        for step in v:
            if isinstance(step, PipelineStepConfig):
                steps.append(step)
            elif isinstance(step, typing.Mapping):
                steps.append(PipelineStepConfig(**step))
            else:
                raise TypeError(step)
        return steps

    def create_pipeline_structure(
        self, kiara: typing.Optional["Kiara"] = None
    ) -> "PipelineStructure":
        from kiara import Kiara, PipelineStructure

        if kiara is None:
            kiara = Kiara.instance()

        ps = PipelineStructure(
            config=self,
            kiara=kiara,
        )
        return ps

    def create_pipeline(
        self,
        controller: typing.Optional["PipelineController"] = None,
        kiara: typing.Optional["Kiara"] = None,
    ):

        # if parent_id is None:
        #     parent_id = DEFAULT_PIPELINE_PARENT_ID
        structure = self.create_pipeline_structure(kiara=kiara)

        from kiara import Pipeline

        pipeline = Pipeline(
            structure=structure,
            controller=controller,
        )
        return pipeline

    def create_pipeline_module(
        self,
        module_id: typing.Optional[str] = None,
        parent_id: typing.Optional[str] = None,
        kiara: typing.Optional["Kiara"] = None,
    ) -> "PipelineModule":

        if kiara is None:
            from kiara.kiara import Kiara

            kiara = Kiara.instance()

        from kiara.pipeline.module import PipelineModule

        module = PipelineModule(
            id=module_id,
            parent_id=parent_id,
            module_config=self,
            kiara=kiara,
        )
        return module

    # def __rich_console__(
    #     self, console: Console, options: ConsoleOptions
    # ) -> RenderResult:
    #
    #     table = Table(show_header=False, box=box.SIMPLE)


class StepDesc(BaseModel):
    """Details of a single [PipelineStep][kiara.pipeline.structure.PipelineStep] (which lives within a [Pipeline][kiara.pipeline.pipeline.Pipeline]"""

    class Config:
        allow_mutation = False
        extra = Extra.forbid

    step: PipelineStep = Field(description="Attributes of the step itself.")
    processing_stage: int = Field(
        description="The processing stage of this step within a Pipeline."
    )
    input_connections: typing.Dict[str, typing.List[str]] = Field(
        description="""A map that explains what elements connect to this steps inputs. A connection could either be a Pipeline input (indicated by the ``__pipeline__`` token), or another steps output.

Example:
``` json
input_connections: {
    "a": ["__pipeline__.a"],
    "b": ["step_one.a"]
}

```
        """
    )
    output_connections: typing.Dict[str, typing.List[str]] = Field(
        description="A map that explains what elemnts connect to this steps outputs. A connection could be either a Pipeline output, or another steps input."
    )
    required: bool = Field(
        description="Whether this step is always required, or potentially could be skipped in case some inputs are not available."
    )

    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult:

        yield f"[b]Step: {self.step.step_id}[\b]"
