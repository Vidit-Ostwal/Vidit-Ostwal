# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/pull/2047#issuecomment-2641883649) in [crewAIInc/crewAI] on 2025-02-07.
  > *AI Summary: @Vidit-Ostwal has suggested expanding the functionality to include a `get_crew` function. This function would allow for direct linking between cli commands and the current crew instance. @Vidit-Ostwal acknowledges that they initially overlooked this idea.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2023#issuecomment-2640720257) in [crewAIInc/crewAI] on 2025-02-06.
  > *AI Summary: @Vidit-Ostwal has suggested a potential issue in the initialization of `short_term_memory` and `entity_memory` between the `reset_memory_command` and `crew.py`. The `reset_memory_command` does not account for custom initialization of these memories, which may cause it to behave differently. To address this, the `reset_memory_command` should be expanded to support custom initialization scenarios.*
- [Commented](https://github.com/explodinggradients/ragas/pull/1880#issuecomment-2634875873) in [explodinggradients/ragas] on 2025-02-04.
  > *AI Summary: @Vidit-Ostwal has proposed coordinating with @sahusiddharth to address potential conflicts, ensuring a smooth resolution process.*
- [Commented](https://github.com/crewAIInc/crewAI/pull/1985#issuecomment-2634692022) in [crewAIInc/crewAI] on 2025-02-04.
  > *AI Summary: @Vidit-Ostwal has suggested that @bhancockio reviews the shared code and provides feedback. They also inquire if this functionality would enhance the user experience.*
- [Commented](https://github.com/explodinggradients/ragas/pull/1880#issuecomment-2634530854) in [explodinggradients/ragas] on 2025-02-04.
  > *AI Summary: @Vidit-Ostwal has suggested looking into a previous unit test PR made by @sahusiddharth to determine if it is the cause of the current issue.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2025#issuecomment-2631615412) in [crewAIInc/crewAI] on 2025-02-03.
  > *AI Summary: @Vidit-Ostwal has suggested that the provided solution might not be clear and has requested further clarification to better understand its implementation. They have expressed their belief that the proposed approach should work and would appreciate additional insights to enhance their comprehension.*
- [Commented](https://github.com/explodinggradients/ragas/issues/1868#issuecomment-2629482947) in [explodinggradients/ragas] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has suggested reviewing the provided solution with @jjmachan and @dosu to determine its correctness.*
- [Commented](https://github.com/Lightning-AI/torchmetrics/issues/2920#issuecomment-2629456251) in [Lightning-AI/torchmetrics] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has suggested that the issue may be specific to the input tensors used, and the warning is raised because the variance of the input tensors is close to zero. They suggest that re-scaling the input or using a larger dtype for computation may resolve the problem.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/1977#issuecomment-2629395843) in [crewAIInc/crewAI] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has suggested removing the `interpolate_inputs_and_add_conversation_history()` function from `task 2`. Instead, the description of `task 2` should clearly state that it takes the output of `task 1` as input. This modification will eliminate the need to explicitly set parameters for `task 2`.*
- [Commented](https://github.com/explodinggradients/ragas/pull/1880#issuecomment-2629385607) in [explodinggradients/ragas] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has suggested updating the traces functionality to present them as `{prompt_number}: {trace}`. The updated traces include prompt names, inputs, and outputs. This allows for easier identification and analysis of specific prompts and their corresponding traces.*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2030) in [crewAIInc/crewAI]: Documentation Error in memory docs (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested that there is an inconsistency in the code examples provided in the documentation. In the sample code examples, the `model` parameter is used instead of the `model_name` parameter. This inconsistency is present in code examples for various services, including Azure OpenAI Embeddings, Google AI Embeddings, Vertex AI*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/1984) in [crewAIInc/crewAI]: output_log_file should also suppport JSON format. (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding a JSON format option to the output_log_file for easier parsing and analysis. This enhancement partially addresses issue #1970. They are willing to contribute a pull request for this feature.*
- Raised an [issue](https://github.com/browser-use/browser-use/issues/407) in [browser-use/browser-use]: Use of use_vision while defining agent (2025-01-26).
  > *AI Summary: @Vidit-Ostwal has suggested clarifying the use of `use_vision`. They inquired about the role of `use_vision set = True` in agent definition and whether it triggers multimodal LLM processing of images. They observed that setting `use_vision = True` only saves a .gif file but does not seem to affect the output.*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2047) in [crewAIInc/crewAI]: Added reset memories function inside crew class (2025-02-06).
  > *AI Summary: @Vidit-Ostwal has suggested fixing the reset memories issue reported in issue #2023. They have also recommended removing the CLI command for resetting memories and making the necessary documentation changes. However, they are seeking confirmation that their proposed solution aligns with the team's plans.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2031) in [crewAIInc/crewAI]: Fixed the memory documentation (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the documentation issue mentioned in issue #2030. The proposed changes will resolve the inaccuracies and improve the clarity of the documentation, ensuring accurate and comprehensive technical references for users.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/1985) in [crewAIInc/crewAI]: Added functionality to have json format as well for the logs (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding support for saving logs as a JSON file. This feature allows users to set output_log_file to True or provide a file name during crew initialization. By enabling save_as_json, a JSON file containing an array of JSON events will be generated, making it easier to parse and*
- Opened a [PR](https://github.com/explodinggradients/ragas/pull/1880) in [explodinggradients/ragas]: Changed the parse_run_traces to include last 4 letters of run_id (2025-01-25).
  > *AI Summary: @Vidit-Ostwal has suggested changing the `parse_run_traces` function to include the last 4 letters of the run ID of the trace. This will create a unique key for every call, addressing the issue where multiple calls were getting the same key when the run IDs were the same.*
- Opened a [PR](https://github.com/explodinggradients/ragas/pull/1879) in [explodinggradients/ragas]: Change the validate_samples functionality (2025-01-24).
  > *AI Summary: @Vidit-Ostwal has suggested a change to the `validate_samples` functionality to indicate the specific indexed sample causing any observed issues. This enhancement provides more detailed information for debugging purposes, enabling developers to pinpoint the problematic sample more easily.*

## ⭐ Starred Repositories
- Starred [langfuse/langfuse](https://github.com/langfuse/langfuse) on 2025-02-04.
- Starred [microsoft/autogen](https://github.com/microsoft/autogen) on 2025-01-31.
- Starred [browser-use/browser-use](https://github.com/browser-use/browser-use) on 2025-01-26.
- Starred [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) on 2025-01-25.
- Starred [explodinggradients/ragas](https://github.com/explodinggradients/ragas) on 2025-01-24.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI](https://github.com/Vidit-Ostwal/crewAI) on 2025-01-27.
- Forked [explodinggradients/ragas](https://github.com/Vidit-Ostwal/ragas) on 2025-01-24.
