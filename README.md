# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2055#issuecomment-2643704539) in [crewAIInc/crewAI] on 2025-02-07.
  > *AI Summary: @Vidit-Ostwal has suggested that the issue may have been fixed already. They recommend updating the crew version to check. Additionally, they have provided a link to PR #2055, which may contain more information about the fix.*
- [Commented](https://github.com/crewAIInc/crewAI/pull/2047#issuecomment-2643616523) in [crewAIInc/crewAI] on 2025-02-07.
  > *AI Summary: @Vidit-Ostwal suggests expanding CrewAI to include built-in evaluations that assess tool outputs, agent performance, and task results against specific criteria such as factual accuracy. They highlight the work of RAGAS in structured evaluations for retrieval-augmented generation as a potential inspiration for how this could be implemented within CrewAI.*
- [Commented](https://github.com/crewAIInc/crewAI/pull/2047#issuecomment-2641883649) in [crewAIInc/crewAI] on 2025-02-07.
  > *AI Summary: @Vidit-Ostwal suggests expanding the code to include a `get_crew` functionality that can be directly linked to the current crew instance via a CLI command. This would allow for easier management of crews using the CLI.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2023#issuecomment-2640720257) in [crewAIInc/crewAI] on 2025-02-06.
  > *AI Summary: @Vidit-Ostwal has suggested that there might be an initialization issue between the CLI command `reset_memory_command` and the Python file `crew.py` for the `short_term_memory` and `entity_memory`. While the CLI command works well for `long_term_memory` and `knowledge_memory` since they don't require any arguments, it may fail if there's custom initialization for `short_term_memory`*
- [Commented](https://github.com/explodinggradients/ragas/pull/1880#issuecomment-2634875873) in [explodinggradients/ragas] on 2025-02-04.
  > *AI Summary: @Vidit-Ostwal has suggested coordinating with @sahusiddharth to discuss possible conflicts and resolve them.*
- [Commented](https://github.com/crewAIInc/crewAI/pull/1985#issuecomment-2634692022) in [crewAIInc/crewAI] on 2025-02-04.
  > *AI Summary: @Vidit-Ostwal has suggested that @bhancockio review the code and share their thoughts on its potential to enhance user experience. They are seeking feedback on the effectiveness of the new functionality in improving user satisfaction.*
- [Commented](https://github.com/explodinggradients/ragas/pull/1880#issuecomment-2634530854) in [explodinggradients/ragas] on 2025-02-04.
  > *AI Summary: @Vidit-Ostwal has suggested that the reported issue may be related to a previous unit test pull request made by @sahusiddharth. They have requested @sahusiddharth to verify if this is the case.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2025#issuecomment-2631615412) in [crewAIInc/crewAI] on 2025-02-03.
  > *AI Summary: @Vidit-Ostwal has suggested that the provided information is unclear and has requested further clarification. They believe that the suggested solution should be functional, but would like additional details to fully comprehend the implementation.*
- [Commented](https://github.com/explodinggradients/ragas/issues/1868#issuecomment-2629482947) in [explodinggradients/ragas] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has inquired if the present solution is satisfactory to @jjmachan and @dosu. The comment was made in the context of a broader discussion or problem-solving effort, but specific details or references were omitted.*
- [Commented](https://github.com/Lightning-AI/torchmetrics/issues/2920#issuecomment-2629456251) in [Lightning-AI/torchmetrics] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has suggested that the unexpected behavior observed is unique to your particular case of input tensors. They have examined the code and identified a condition that will be triggered in your case, leading to the warning mentioned. They have also tried using different input tensors, and the expected behavior*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2030) in [crewAIInc/crewAI]: Documentation Error in memory docs (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested that the sample code examples provided in the CrewAI documentation for embedding models should be updated to use `model_name` as the input parameter instead of `model`. This discrepancy is observed across multiple examples in the documentation.*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/1984) in [crewAIInc/crewAI]: output_log_file should also suppport JSON format. (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding a JSON format to the output_log_file to improve parsability. They believe this will partially address issue #1970. They are willing to submit a pull request for this change.*
- Raised an [issue](https://github.com/browser-use/browser-use/issues/407) in [browser-use/browser-use]: Use of use_vision while defining agent (2025-01-26).
  > *AI Summary: @Vidit-Ostwal has suggested looking into the purpose of the `use_vision` parameter when defining an agent. They have noticed that setting it to `True` results in a .gif being saved, but are uncertain if this indicates that multimodal processing of an image is occurring or if the agent is still relying*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2047) in [crewAIInc/crewAI]: Added reset memories function inside crew class (2025-02-06).
  > *AI Summary: @Vidit-Ostwal has suggested fixes for the memory reset issue raised in #2023. They propose removing the CLI command used for memory resetting and making corresponding documentation changes. However, they request confirmation that this solution aligns with the project's goals before implementing these changes.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2031) in [crewAIInc/crewAI]: Fixed the memory documentation (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the documentation issue raised in issue #2030. The specifics of the fix have not been provided in this comment.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/1985) in [crewAIInc/crewAI]: Added functionality to have json format as well for the logs (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding support to save logs as a JSON file. By setting the `output_log_file` parameter to `True` or providing a file name, and setting `save_as_json` to `True`, the crew will initialize with JSON logging enabled. This allows for easy parsing and working with the generated JSON file, which*
- Opened a [PR](https://github.com/explodinggradients/ragas/pull/1880) in [explodinggradients/ragas]: Changed the parse_run_traces to include last 4 letters of run_id (2025-01-25).
  > *AI Summary: @Vidit-Ostwal suggested a modification to the parse_run_traces function to enhance key uniqueness. The function now incorporates the last four characters of the trace's run_id, ensuring that each call has a distinct key. This change effectively resolves the issue of duplicate keys.*
- Opened a [PR](https://github.com/explodinggradients/ragas/pull/1879) in [explodinggradients/ragas]: Change the validate_samples functionality (2025-01-24).
  > *AI Summary: @Vidit-Ostwal has suggested changing the functionality of the `validate_samples` to explicitly indicate which indexed sample is causing an issue. This enhancement will provide more specific and actionable information to users encountering errors during sample validation.*

## ⭐ Starred Repositories
- Starred [sentient-engineering/sentient](https://github.com/sentient-engineering/sentient) on 2025-02-08.
- Starred [langflow-ai/langflow](https://github.com/langflow-ai/langflow) on 2025-02-07.
- Starred [langfuse/langfuse](https://github.com/langfuse/langfuse) on 2025-02-04.
- Starred [microsoft/autogen](https://github.com/microsoft/autogen) on 2025-01-31.
- Starred [browser-use/browser-use](https://github.com/browser-use/browser-use) on 2025-01-26.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI](https://github.com/Vidit-Ostwal/crewAI) on 2025-01-27.
- Forked [explodinggradients/ragas](https://github.com/Vidit-Ostwal/ragas) on 2025-01-24.
