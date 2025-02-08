# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/pull/2047#issuecomment-2641883649) in [crewAIInc/crewAI] on 2025-02-07.
  > *AI Summary: @Vidit-Ostwal has suggested expanding the `get_crew` functionality to allow direct linking of CLI commands with the current crew instance. This would enhance the functionality and make it more user-friendly.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2023#issuecomment-2640720257) in [crewAIInc/crewAI] on 2025-02-06.
  > *AI Summary: @Vidit-Ostwal has suggested that the `reset_memory_command` executed from CLI may be causing issues due to differences in how it initializes `short_term_memory` and `entity_memory` compared to `crew.py`. While the command may work for `long_term_memory` and `knowledge_memory`, which do not require arguments for initialization, it may not function correctly if custom initialization*
- [Commented](https://github.com/explodinggradients/ragas/pull/1880#issuecomment-2634875873) in [explodinggradients/ragas] on 2025-02-04.
  > *AI Summary: @Vidit-Ostwal has suggested coordinating with @sahusiddharth to resolve potential conflicts.*
- [Commented](https://github.com/crewAIInc/crewAI/pull/1985#issuecomment-2634692022) in [crewAIInc/crewAI] on 2025-02-04.
  > *AI Summary: @Vidit-Ostwal has suggested that @bhancockio review provided code and share feedback. He also asks if the functionality enhances the user experience.*
- [Commented](https://github.com/explodinggradients/ragas/pull/1880#issuecomment-2634530854) in [explodinggradients/ragas] on 2025-02-04.
  > *AI Summary: @Vidit-Ostwal has suggested you check if the issue you are facing is due to a previous unit test PR made by @sahusiddharth. They have requested you to verify this possibility and provide an update.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2025#issuecomment-2631615412) in [crewAIInc/crewAI] on 2025-02-03.
  > *AI Summary: @Vidit-Ostwal has suggested sharing more details to clarify the issue as the current description is not clear enough to understand. Additionally, they believe that the proposed solution should work as intended.*
- [Commented](https://github.com/explodinggradients/ragas/issues/1868#issuecomment-2629482947) in [explodinggradients/ragas] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has suggested that @jjmachan and @dosu should review the current solution and provide feedback on its correctness.*
- [Commented](https://github.com/Lightning-AI/torchmetrics/issues/2920#issuecomment-2629456251) in [Lightning-AI/torchmetrics] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has suggested that the unexpected behavior encountered is specific to the provided input tensors. They analyzed the code and concluded that the warning is correctly raised when the variance of the input tensors is close to zero. @Vidit-Ostwal also suggests considering re-scaling the input or using a larger dtype*
- [Commented](https://github.com/crewAIInc/crewAI/issues/1977#issuecomment-2629395843) in [crewAIInc/crewAI] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has suggested that the error in `interpolate_inputs_and_add_conversation_history()` is due to the absence of the `detail` parameter. To resolve this, the description for `task 2` should be modified to include a reference to the output of `task 1` without specifying specific parameters. This will ensure that the necessary information is*
- [Commented](https://github.com/explodinggradients/ragas/pull/1880#issuecomment-2629385607) in [explodinggradients/ragas] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has suggested updating the traces functionality to display "{prompt_number} : {trace}".

The new trace format will be similar to the following, where 'prompt_1' indicates the first prompt:
```
{
  'prompt_1': {
    'name': 'claim_decomposition_prompt',
    'input': ClaimDecompositionInput(response='Eiffel tower is in Paris'),
    'output': ClaimDecompositionOutput(claims=['Eiffel tower is in Paris.'])
  }
}
```*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2030) in [crewAIInc/crewAI]: Documentation Error in memory docs (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested that the documentation examples for memory embeddings be updated. The examples currently use `model` instead of `model_name` as the parameter for the embedder, and should be updated to use `model_name` instead. The affected documentation pages include:

- https://docs.crewai.com/concepts/memory
- https://docs.crewai.com/concepts/memory#using-azure-openai-embeddings
- https://docs.crewai.com/concepts/memory#using-google-ai-embeddings
- https://docs.crewai.com/concepts/memory#using-vertex-ai-embeddings
- https://docs.crewai.com/concepts/memory#using-cohere-embeddings*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/1984) in [crewAIInc/crewAI]: output_log_file should also suppport JSON format. (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding JSON format to the output_log_file. Currently, the file has a .txt format, which is not parsable. JSON format would support further analysis and partially address issue #1970. @Vidit-Ostwal is willing to contribute a pull request with this change.*
- Raised an [issue](https://github.com/browser-use/browser-use/issues/407) in [browser-use/browser-use]: Use of use_vision while defining agent (2025-01-26).
  > *AI Summary: @Vidit-Ostwal has suggested clarifying the role of `use_vision` in defining an agent. They inquired about whether the screenshot is parsed by the multimodal LLM or through scraping elements when `use_vision` is set to `True`. Additionally, @Vidit-Ostwal requested a cost metric to determine if multimodal processing of an image is occurring.*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2047) in [crewAIInc/crewAI]: Added reset memories function inside crew class (2025-02-06).
  > *AI Summary: @Vidit-Ostwal has suggested addressing the memory reset issue reported in #2023 and introducing other changes. These include eliminating the CLI command for memory reset, updating the documentation, and aligning the proposed solution with the project's requirements. @Vidit-Ostwal is willing to implement these changes if the solution is deemed viable.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2031) in [crewAIInc/crewAI]: Fixed the memory documentation (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested a fix for the documentation issue mentioned in issue #2030. This resolves the problem that was previously reported.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/1985) in [crewAIInc/crewAI]: Added functionality to have json format as well for the logs (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding support for saving crew logs as a JSON file. You can enable this by setting `output_log_file` to True or providing a file name, and `save_as_json` to True. The JSON file will contain an array of JSON events, simplifying parsing and further processing. An example usage is*
- Opened a [PR](https://github.com/explodinggradients/ragas/pull/1880) in [explodinggradients/ragas]: Changed the parse_run_traces to include last 4 letters of run_id (2025-01-25).
  > *AI Summary: @Vidit-Ostwal has suggested modifying the `parse_run_traces` function by appending the last four characters of the `run_id` to the trace, thereby creating a unique key for each call. This modification aims to eliminate duplicate traces and enhance the uniqueness of keys assigned to each call.*
- Opened a [PR](https://github.com/explodinggradients/ragas/pull/1879) in [explodinggradients/ragas]: Change the validate_samples functionality (2025-01-24).
  > *AI Summary: @Vidit-Ostwal has suggested a modification to the validate_samples functionality. The change enables the functionality to specify which indexed sample is responsible for any identified issues. This enhancement provides more precise information for troubleshooting purposes.*

## ⭐ Starred Repositories
- Starred [langflow-ai/langflow](https://github.com/langflow-ai/langflow) on 2025-02-07.
- Starred [langfuse/langfuse](https://github.com/langfuse/langfuse) on 2025-02-04.
- Starred [microsoft/autogen](https://github.com/microsoft/autogen) on 2025-01-31.
- Starred [browser-use/browser-use](https://github.com/browser-use/browser-use) on 2025-01-26.
- Starred [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) on 2025-01-25.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI](https://github.com/Vidit-Ostwal/crewAI) on 2025-01-27.
- Forked [explodinggradients/ragas](https://github.com/Vidit-Ostwal/ragas) on 2025-01-24.
