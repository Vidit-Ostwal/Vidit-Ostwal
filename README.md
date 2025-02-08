# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/pull/2047#issuecomment-2641883649) in [crewAIInc/crewAI] on 2025-02-07.
  > *AI Summary: @Vidit-Ostwal has suggested expanding the `get_crew` functionality to work with CLI commands. This would allow for direct linking between CLI commands and the current crew instance. @Vidit-Ostwal acknowledges that they initially missed this idea, but now they believe it would be a valuable addition to the project.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2023#issuecomment-2640720257) in [crewAIInc/crewAI] on 2025-02-06.
  > *AI Summary: @Vidit-Ostwal has suggested that the issue may lie within the initialization of `short_term_memory` and `entity_memory` when executing `reset_memory_command` from the CLI. This differs from the initialization process within `crew.py`. However, for `long_term_memory` and `knowledge_memory`, direct CLI commands should work effectively as they do not require arguments for initialization. Custom initialization*
- [Commented](https://github.com/explodinggradients/ragas/pull/1880#issuecomment-2634875873) in [explodinggradients/ragas] on 2025-02-04.
  > *AI Summary: @Vidit-Ostwal suggests coordinating with @sahusiddharth to resolve conflicts.*
- [Commented](https://github.com/crewAIInc/crewAI/pull/1985#issuecomment-2634692022) in [crewAIInc/crewAI] on 2025-02-04.
  > *AI Summary: @Vidit-Ostwal has suggested that @bhancockio review the provided code and provide feedback. They have also asked if the suggested code changes would enhance the user experience.*
- [Commented](https://github.com/explodinggradients/ragas/pull/1880#issuecomment-2634530854) in [explodinggradients/ragas] on 2025-02-04.
  > *AI Summary: @Vidit-Ostwal has suggested looking into whether the issue being experienced is a result of the previous unit test PR made by @sahusiddharth.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2025#issuecomment-2631615412) in [crewAIInc/crewAI] on 2025-02-03.
  > *AI Summary: @Vidit-Ostwal has suggested you provide more details as they are unable to understand the issue. They have also provided a potential solution, stating that it should resolve the problem.*
- [Commented](https://github.com/explodinggradients/ragas/issues/1868#issuecomment-2629482947) in [explodinggradients/ragas] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has requested feedback from @jjmachan and @dosu regarding the correctness of a provided solution. No specific details or context for the solution were provided in the comment, so the exact nature of the solution is unclear.*
- [Commented](https://github.com/Lightning-AI/torchmetrics/issues/2920#issuecomment-2629456251) in [Lightning-AI/torchmetrics] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal observed unexpected behavior while analyzing the codebase and believes that a particular conditional statement triggers a warning that flags possible instability in Pearictions or target correlation due to low variance in input tensors. They suggest investigating the specific input tensors to determine why this warning is being raised.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/1977#issuecomment-2629395843) in [crewAIInc/crewAI] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has suggested a change to Task 2's description to avoid the error caused by the absence of the 'detail' parameter. Instead of explicitly setting parameters, they propose using the output from Task 1 as input for Task 2. This will eliminate the need to manually specify parameters, ensuring that*
- [Commented](https://github.com/explodinggradients/ragas/pull/1880#issuecomment-2629385607) in [explodinggradients/ragas] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has suggested updating the traces functionality to include prompt numbers along with the traces. New traces will be formatted as `{prompt_number} : {trace}`. This allows for easier identification of specific traces, especially when multiple traces are present for a given input.*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2030) in [crewAIInc/crewAI]: Documentation Error in memory docs (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested that in the documentation examples for using embeddings, the `model_name` parameter should be replaced with `model`. They have provided links to specific examples in the documentation where this issue occurs. There are no steps to reproduce or expected behavior provided. The issue affects various operating systems, Python*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/1984) in [crewAIInc/crewAI]: output_log_file should also suppport JSON format. (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding a JSON format to the output log file for better parsability. This change would partially address issue #1970 and provide additional context for further analysis. @Vidit-Ostwal is willing to contribute a pull request for this feature.*
- Raised an [issue](https://github.com/browser-use/browser-use/issues/407) in [browser-use/browser-use]: Use of use_vision while defining agent (2025-01-26).
  > *AI Summary: @Vidit-Ostwal suggests clarifying the purpose of the `use_vision` parameter in agent definition. They observe that setting `use_vision` to `True` results in saving GIFs but leaves output unchanged. They inquire whether the `use_vision` parameter triggers multimodal image processing and if there is a metric to assess its activation. They provide no*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2047) in [crewAIInc/crewAI]: Added reset memories function inside crew class (2025-02-06).
  > *AI Summary: @Vidit-Ostwal has suggested fixes for the memory reset issue raised in #2023. Additionally, the CLI command for resetting memories will be removed. Documentation changes are also expected. @Vidit-Ostwal seeks confirmation that the proposed solution aligns with the project vision before implementing these changes.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2031) in [crewAIInc/crewAI]: Fixed the memory documentation (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the documentation issue raised in issue #2030. This update resolves the problem and ensures that the documentation accurately reflects the intended functionality of the code.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/1985) in [crewAIInc/crewAI]: Added functionality to have json format as well for the logs (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding support to save logs as a JSON file. This feature enables users to set `output_log_file` to True or specify a file name and set `save_as_json` to True while initializing the crew. The resulting JSON file provides an array of JSON events for convenient parsing and analysis.*
- Opened a [PR](https://github.com/explodinggradients/ragas/pull/1880) in [explodinggradients/ragas]: Changed the parse_run_traces to include last 4 letters of run_id (2025-01-25).
  > *AI Summary: @Vidit-Ostwal has suggested changing the parse_run_traces function to include the last four letters of the run ID of the trace. This is done to create a unique key for every call, ensuring that each call has a distinct identifier. The modification aims to enhance the traceability and organization of trace*
- Opened a [PR](https://github.com/explodinggradients/ragas/pull/1879) in [explodinggradients/ragas]: Change the validate_samples functionality (2025-01-24).
  > *AI Summary: @Vidit-Ostwal has suggested modifying the validate_samples functionality to include the indexed sample that is causing errors. This will provide more detailed information and aid in troubleshooting.*

## ⭐ Starred Repositories
- Starred [langflow-ai/langflow](https://github.com/langflow-ai/langflow) on 2025-02-07.
- Starred [langfuse/langfuse](https://github.com/langfuse/langfuse) on 2025-02-04.
- Starred [microsoft/autogen](https://github.com/microsoft/autogen) on 2025-01-31.
- Starred [browser-use/browser-use](https://github.com/browser-use/browser-use) on 2025-01-26.
- Starred [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) on 2025-01-25.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI](https://github.com/Vidit-Ostwal/crewAI) on 2025-01-27.
- Forked [explodinggradients/ragas](https://github.com/Vidit-Ostwal/ragas) on 2025-01-24.
