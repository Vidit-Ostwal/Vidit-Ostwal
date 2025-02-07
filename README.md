# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2023#issuecomment-2640720257) in [crewAIInc/crewAI] on 2025-02-06.
  > *AI Summary: @Vidit-Ostwal has suggested that the problem may lie in the initialization of `short_term_memory` and `entity_memory`. Apparently, these initializations differ from how crew.py does it, causing issues with the `reset_memory_command`. The command should work fine for `long_term_memory` and `knowledge_memory`. Custom initialization of any memory may also cause problems with direct CLI*
- [Commented](https://github.com/explodinggradients/ragas/pull/1880#issuecomment-2634875873) in [explodinggradients/ragas] on 2025-02-04.
  > *AI Summary: @Vidit-Ostwal has suggested coordinating with @sahusiddharth to resolve any potential conflicts in the implementation of the feature.*
- [Commented](https://github.com/crewAIInc/crewAI/pull/1985#issuecomment-2634692022) in [crewAIInc/crewAI] on 2025-02-04.
  > *AI Summary: @Vidit-Ostwal has suggested reviewing the provided code for feedback and an assessment of whether this functionality enhances the user experience.*
- [Commented](https://github.com/explodinggradients/ragas/pull/1880#issuecomment-2634530854) in [explodinggradients/ragas] on 2025-02-04.
  > *AI Summary: @Vidit-Ostwal has suggested checking if the issue is related to the previous unit test PR made by @sahusiddharth.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2025#issuecomment-2631615412) in [crewAIInc/crewAI] on 2025-02-03.
  > *AI Summary: @Vidit-Ostwal has suggested sharing more details to clarify their understanding of a feature. They believe that a particular solution should function as intended, but require further clarification to fully comprehend how it works.*
- [Commented](https://github.com/explodinggradients/ragas/issues/1868#issuecomment-2629482947) in [explodinggradients/ragas] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has requested feedback on a proposed solution. They have tagged @jjmachan and @dosu in the comment to seek their input. However, the specific details of the solution being discussed are not provided in the comment.*
- [Commented](https://github.com/Lightning-AI/torchmetrics/issues/2920#issuecomment-2629456251) in [Lightning-AI/torchmetrics] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has suggested that the warning is raised because the variance of predis or target is close to zero. The condition `if (var_x < bound).any() or (var_y < bound).any():` is hit in this case. @Vidit-Ostwal also mentioned that this behavior is specific to the particular case of input tensors and*
- [Commented](https://github.com/crewAIInc/crewAI/issues/1977#issuecomment-2629395843) in [crewAIInc/crewAI] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has suggested a modification to the code. They have identified an error in `interpolate_inputs_and_add_conversation_history()` function due to the absence of the `detail` parameter. To resolve this, they recommend omitting the parameter from the description of `task 2`. Instead, they propose that `task 2` should reference the output of `task*
- [Commented](https://github.com/explodinggradients/ragas/pull/1880#issuecomment-2629385607) in [explodinggradients/ragas] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has updated the traces functionality to display traces in the format `{prompt_number} : {trace}`. The new traces provide detailed information about the input, output, and name of each prompt, including the ClaimDecompositionInput, NLIStatementInput, ClaimDecompositionOutput, and NLIStatementOutput objects. This updated format helps improve the clarity and organization of the traces.*
- [Commented](https://github.com/explodinggradients/ragas/issues/1871#issuecomment-2628965465) in [explodinggradients/ragas] on 2025-02-01.
  > *AI Summary: @Vidit-Ostwal has suggested considering user perspective, where making it easy to understand the flow would be beneficial. From an implementation standpoint, this change is thought to be straightforward. If @jjmachan agrees with this solution, @Vidit-Ostwal will update the PR to incorporate this modification.*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2030) in [crewAIInc/crewAI]: Documentation Error in memory docs (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested that the documentation for the embedding service should be updated to consistently use `model` instead of `model_name` as the input parameter for the embedder. Specifically, the following pages should be updated:

- https://docs.crewai.com/concepts/memory#using-azure-openai-embeddings
- https://docs.crewai.com/concepts/memory#using-google-ai-embeddings
- https://docs.crewai.com/concepts/memory#using-vertex-ai-embeddings
- https://docs.crewai.com/concepts/memory#using-cohere-embeddings*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/1984) in [crewAIInc/crewAI]: output_log_file should also suppport JSON format. (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding a JSON format to the output_log_file to make it parsable. This would address issue #1970, as JSON is more easily analyzable than .txt format. @Vidit-Ostwal is willing to contribute a pull request for this change.*
- Raised an [issue](https://github.com/browser-use/browser-use/issues/407) in [browser-use/browser-use]: Use of use_vision while defining agent (2025-01-26).
  > *AI Summary: @Vidit-Ostwal has suggested to clarify the usage of `use_vision set = True` when defining an agent. They wonder whether it triggers multimodal processing of images or simply leads to saving a .gif file without affecting the output. Additionally, they inquire about any cost matrix to verify if the multimodal processing*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2047) in [crewAIInc/crewAI]: Added reset memories function inside crew class (2025-02-06).
  > *AI Summary: @Vidit-Ostwal has suggested addressing the memory reset issue reported in issue #2023. They propose making the following additional adjustments:

1. Eliminate the CLI command for resetting memories
2. Update documentation

They are willing to implement these changes if they are in line with the current solution.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2031) in [crewAIInc/crewAI]: Fixed the memory documentation (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested to fix the documentation issue that was mentioned in issue #2030.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/1985) in [crewAIInc/crewAI]: Added functionality to have json format as well for the logs (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding support to save logs as a JSON file. Now, when initializing the Crew, you can specify the output_log_file parameter as a file name (e.g., "log.json") and set save_as_json to True. The resulting JSON file will contain an array of JSON events for easy parsing and manipulation.*
- Opened a [PR](https://github.com/explodinggradients/ragas/pull/1880) in [explodinggradients/ragas]: Changed the parse_run_traces to include last 4 letters of run_id (2025-01-25).
  > *AI Summary: @Vidit-Ostwal has suggested making a modification to the parse_run_traces function. This change will append the last 4 characters of the run_id to the trace, creating a unique key for every call. This enhancement is designed to improve the accuracy and efficiency of the key generation process.*
- Opened a [PR](https://github.com/explodinggradients/ragas/pull/1879) in [explodinggradients/ragas]: Change the validate_samples functionality (2025-01-24).
  > *AI Summary: @Vidit-Ostwal has suggested modifying the validate_samples functionality to pinpoint the problematic indexed sample. This enhancement provides more precise error reporting, enabling developers to quickly identify and resolve sample-related issues.*

## ⭐ Starred Repositories
- Starred [langfuse/langfuse](https://github.com/langfuse/langfuse) on 2025-02-04.
- Starred [microsoft/autogen](https://github.com/microsoft/autogen) on 2025-01-31.
- Starred [browser-use/browser-use](https://github.com/browser-use/browser-use) on 2025-01-26.
- Starred [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) on 2025-01-25.
- Starred [explodinggradients/ragas](https://github.com/explodinggradients/ragas) on 2025-01-24.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI](https://github.com/Vidit-Ostwal/crewAI) on 2025-01-27.
- Forked [explodinggradients/ragas](https://github.com/Vidit-Ostwal/ragas) on 2025-01-24.
