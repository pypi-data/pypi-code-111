import importlib

import rich.markdown

import mdpeditor.mdpblocks.provide


def mdp_options_list():
    """Extract All documented .mdp options
    """

    # debugging help:
    # with open("./mdpeditor/parameterhelp/mdp-options.rst") as f:
    #     mdp_options = f.read()

    mdp_options = importlib.resources.read_text(__package__, "mdp-options.rst")

    parameter_tag = "\n.. mdp:: "

    list_of_options = []
    end = 0
    # keep searching for parameter_tag in mdp_options until none found
    # then return
    while True:
        try:
            start = mdp_options.index(parameter_tag, end) + len(parameter_tag)
            end = mdp_options.index("\n", start)
            list_of_options += [mdp_options[start:end].strip()]
        except ValueError:
            return list_of_options


def mdp_section(parameter_name):
    """Extract user guide section about a specific mdp parameter

       :raises ValueError: if parameter_name is not found in .mdp options

    Args:
        parameter_name (str): the mdp option to be looked for
    """
    # we read the file every time we parse a parameter
    # might be worth moving up to module startup if this is slow
    mdp_options = importlib.resources.read_text(__package__, "mdp-options.rst")

    parameter_tag = ".. mdp:: "
    start = mdp_options.index(parameter_tag + parameter_name +
                              "\n") + len(parameter_tag)

    # find the end of the parameter description:
    #   - new option
    #   - new section

    # use find so we don't raise an error if at the end of the file
    next_tag_position = mdp_options[start:].find(parameter_tag)

    # two newlines mark a new section
    section_tag = "\n\n\n"
    next_section_position = mdp_options[start:].find(section_tag)

    # if there is no next tag set this to next section so that end(..) works
    if next_tag_position == -1:
        next_tag_position = next_section_position

    if next_section_position == -1:
        next_section_position = next_tag_position

    # whatever comes first
    end = min(next_section_position, next_tag_position)

    return mdp_options[start + len(parameter_name):start + end].strip()


def help_explain_string(predefined_blocks):
    help_string = ("Use as [italic]explain PARAMETER[/] "
                   "where [italic]PARAMETER[/] is "
                   "\n - an .mdp option like [bold]integrator[/] or "
                   "\n - one of these predefined parameter blocks")

    help_string += ("\n[bold]" + predefined_blocks + "[/]\n")

    help_string += ("\nExamples:"
                    "\n\t[italic]explain density_guided.vanilla"
                    "\n\t[italic]explain integrator\n")

    return help_string


def run_explain(explain_string):

    if not explain_string or explain_string.strip() == "help":
        return help_explain_string(
            mdpeditor.mdpblocks.provide.formatted_blocks())

    explain_string = explain_string.strip()
    try:
        return rich.markdown.Markdown(
            mdp_section(explain_string))
    except ValueError:
        pass

    try:
        plain_string = mdpeditor.mdpblocks.provide.description_string(
            explain_string)
        return rich.markdown.Markdown(plain_string)

    except FileNotFoundError:
        pass
    except IndexError:
        pass
    except ModuleNotFoundError:
        pass

    raise SystemExit(f"[bold]{explain_string}[/] is neither an "
                     f".mdp option nor a predefined block")
