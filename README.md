# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2023#issuecomment-2640720257) in [crewAIInc/crewAI] on 2025-02-06.
  > *AI Summary: @Vidit-Ostwal has suggested that the issue may be caused by a discrepancy between how `reset_memory_command` initializes `short_term_memory` and `entity_memory` from the CLI and how they are initialized within `crew.py`. While the command works for `long_term_memory` and `knowledge_memory`, which do not require arguments, it may not function properly if custom initialization*
- [Commented](https://github.com/explodinggradients/ragas/pull/1880#issuecomment-2634875873) in [explodinggradients/ragas] on 2025-02-04.
  > *AI Summary: @Vidit-Ostwal has suggested coordinating with @sahusiddharth to resolve conflicts.*
- [Commented](https://github.com/crewAIInc/crewAI/pull/1985#issuecomment-2634692022) in [crewAIInc/crewAI] on 2025-02-04.
  > *AI Summary: @Vidit-Ostwal has suggested reviewing the provided code and sharing opinions on its quality. Additionally, they have asked whether the implemented functionality enhances user experience.*
- [Commented](https://github.com/explodinggradients/ragas/pull/1880#issuecomment-2634530854) in [explodinggradients/ragas] on 2025-02-04.
  > *AI Summary: @Vidit-Ostwal has suggested that you verify if the issue is related to the recent unit test PR you made.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2025#issuecomment-2631615412) in [crewAIInc/crewAI] on 2025-02-03.
  > *AI Summary: @Vidit-Ostwal has suggested that it would be helpful to provide more information about the issue, as they are currently unable to understand the problem. They believe that the suggested solution should work as intended.*
- [Commented](https://github.com/explodinggradients/ragas/issues/1868#issuecomment-2629482947) in [explodinggradients/ragas] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has requested feedback on a proposed solution. The commenter seeks confirmation from @jjmachan and @dosu regarding the accuracy of the solution but does not provide further context or details.*
- [Commented](https://github.com/Lightning-AI/torchmetrics/issues/2920#issuecomment-2629456251) in [Lightning-AI/torchmetrics] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has suggested that the unexpected behavior may be specific to the input tensors used. They have checked with different tensors and observed expected results, including `nan` when expected. The particular condition in the provided code snippet checks for variance close to zero, which could lead to instability in the*
- [Commented](https://github.com/crewAIInc/crewAI/issues/1977#issuecomment-2629395843) in [crewAIInc/crewAI] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has suggested modifying the code to address the error raised due to the absence of the `detail` parameter. They propose defining `task 2` without specifying the parameters and instead relying on the output of `task 1`, which should provide the necessary inputs. This approach eliminates the need to explicitly*
- [Commented](https://github.com/explodinggradients/ragas/pull/1880#issuecomment-2629385607) in [explodinggradients/ragas] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has suggested updating the traces functionality to include `{prompt_number} : {trace}` formatting. The new traces will resemble a more descriptive format, such as `{'prompt_1': {'name': 'claim_decomposition_prompt', 'input': ClaimDecompositionInput(response='Eiffel tower is in Paris'), 'output': ClaimDecompositionOutput(claims=['Eiffel tower is in Paris.'])}}`. This enhanced formatting provides a more organized and comprehensive representation of*
- [Commented](https://github.com/explodinggradients/ragas/issues/1871#issuecomment-2628965465) in [explodinggradients/ragas] on 2025-02-01.
  > *AI Summary: @Vidit-Ostwal suggests that from a user perspective, separating into separate sections will enhance comprehension of the flow. From an implementation standpoint, they believe it should be straightforward to implement. They request @jjmachan's input to confirm alignment and indicate their willingness to update the PR with the suggested modification upon approval.*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2030) in [crewAIInc/crewAI]: Documentation Error in memory docs (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested addressing an issue in the documentation for CrewAI's Memory concept. The documentation refers to an incorrect parameter name, "model," instead of the correct parameter name, "model_name." Specific examples of this error are provided in the comment for Azure OpenAI Embeddings, Google AI Embeddings, Vertex AI Embeddings, and*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/1984) in [crewAIInc/crewAI]: output_log_file should also suppport JSON format. (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested converting the output_log_file from .txt format to JSON format for easier parsing and analysis. This change would also partially address issue #1970. @Vidit-Ostwal is willing to contribute a pull request for this feature.*
- Raised an [issue](https://github.com/browser-use/browser-use/issues/407) in [browser-use/browser-use]: Use of use_vision while defining agent (2025-01-26).
  > *AI Summary: @Vidit-Ostwal has suggested an inquiry regarding the `use_vision` parameter in agent definition. They question its functionality when set to `True`. Specifically, they ask if screenshots are processed differently by the multimodal LLM or if the agent still relies primarily on scraping elements for decision-making. Additionally, they express concern about whether*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2047) in [crewAIInc/crewAI]: Added reset memories function inside crew class (2025-02-06).
  > *AI Summary: @Vidit-Ostwal has suggested fixing the reset memories issue reported in #2023. Additionally, they propose removing the CLI command used to reset memories and updating the documentation. However, they seek confirmation that their solution aligns with the project's requirements before implementing these changes.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2031) in [crewAIInc/crewAI]: Fixed the memory documentation (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the documentation issue reported in issue #2030. The documentation issue involved incorrect details in the instructions of the repository. This fix resolves the issue by updating the documentation with the correct instructions.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/1985) in [crewAIInc/crewAI]: Added functionality to have json format as well for the logs (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding support for saving logs in a JSON format. This feature can be enabled by setting `output_log_file` to `True` or a file name and `save_as_json` to `True` while initializing the crew. The generated JSON file will consist of an array of JSON events, facilitating easy parsing and*
- Opened a [PR](https://github.com/explodinggradients/ragas/pull/1880) in [explodinggradients/ragas]: Changed the parse_run_traces to include last 4 letters of run_id (2025-01-25).
  > *AI Summary: @Vidit-Ostwal has suggested altering the parse_run_traces function to generate a unique key for each call. This is accomplished by incorporating the final four characters of the trace's run_id into the key. This modification ensures a distinct identifier for every function invocation.*
- Opened a [PR](https://github.com/explodinggradients/ragas/pull/1879) in [explodinggradients/ragas]: Change the validate_samples functionality (2025-01-24).
  > *AI Summary: @Vidit-Ostwal has suggested modifying the validate_samples functionality to include identifying the specific indexed sample causing any issues. This modification enhances the functionality by providing more precise problem identification during validation.*

## ⭐ Starred Repositories
- Starred [langfuse/langfuse](https://github.com/langfuse/langfuse) on 2025-02-04.
- Starred [microsoft/autogen](https://github.com/microsoft/autogen) on 2025-01-31.
- Starred [browser-use/browser-use](https://github.com/browser-use/browser-use) on 2025-01-26.
- Starred [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) on 2025-01-25.
- Starred [explodinggradients/ragas](https://github.com/explodinggradients/ragas) on 2025-01-24.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI](https://github.com/Vidit-Ostwal/crewAI) on 2025-01-27.
- Forked [explodinggradients/ragas](https://github.com/Vidit-Ostwal/ragas) on 2025-01-24.
