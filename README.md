# Recent GitHub Activity for Vidit-Ostwal

## 💬 Recent Comments
- [Commented](https://github.com/crewAIInc/crewAI/issues/2023#issuecomment-2640720257) in [crewAIInc/crewAI] on 2025-02-06.
  > *AI Summary: @Vidit-Ostwal has suggested that `reset_memory_command` might be causing the issue since it initializes `short_term_memory` and `entity_memory` differently than in `crew.py`. While `reset_memory_command` may work for `long_term_memory` and `knowledge_memory`, it may not function properly if custom initialization is used for any memory.*
- [Commented](https://github.com/explodinggradients/ragas/pull/1880#issuecomment-2634875873) in [explodinggradients/ragas] on 2025-02-04.
  > *AI Summary: @Vidit-Ostwal has suggested coordinating with @sahusiddharth to resolve any potential conflicts.*
- [Commented](https://github.com/crewAIInc/crewAI/pull/1985#issuecomment-2634692022) in [crewAIInc/crewAI] on 2025-02-04.
  > *AI Summary: @Vidit-Ostwal has suggested that @bhancockio review the provided code and offer their thoughts. Additionally, @Vidit-Ostwal has requested feedback on whether this functionality enhances the user experience.*
- [Commented](https://github.com/explodinggradients/ragas/pull/1880#issuecomment-2634530854) in [explodinggradients/ragas] on 2025-02-04.
  > *AI Summary: @Vidit-Ostwal has suggested checking if the issue is caused by a previous unit test PR authored by @sahusiddharth.*
- [Commented](https://github.com/crewAIInc/crewAI/issues/2025#issuecomment-2631615412) in [crewAIInc/crewAI] on 2025-02-03.
  > *AI Summary: @Vidit-Ostwal has suggested sharing more details about a specific concern they have because they are not able to understand it. They believe that "This" should work in their opinion, but they request more clarity on the matter.*
- [Commented](https://github.com/explodinggradients/ragas/issues/1868#issuecomment-2629482947) in [explodinggradients/ragas] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has requested clarification from @jjmachan and @dosu on the correctness of the proposed solution. It is unclear what the suggested solution entails as the comment does not provide specific details or context.*
- [Commented](https://github.com/Lightning-AI/torchmetrics/issues/2920#issuecomment-2629456251) in [Lightning-AI/torchmetrics] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has suggested that the unexpected behavior is likely caused by a specific condition in the provided code snippet. This condition checks if the variance of two variables (`var_x` and `var_y`) is below a threshold (`bound`), which can lead to instability in calculations. They observed this issue in a specific*
- [Commented](https://github.com/crewAIInc/crewAI/issues/1977#issuecomment-2629395843) in [crewAIInc/crewAI] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has suggested modifying the code in `task 2` to address an error caused by attempting to access the `detail` parameter before it has been initialized. They propose removing the explicit parameter setting and instead using the output of `task 1` as input for `task 2`, ensuring that the necessary*
- [Commented](https://github.com/explodinggradients/ragas/pull/1880#issuecomment-2629385607) in [explodinggradients/ragas] on 2025-02-02.
  > *AI Summary: @Vidit-Ostwal has suggested updating the traces functionality to adopt the `{prompt_number} : {trace}` format. Under this format, each trace will be assigned a unique prompt number and will be represented as a key-value pair. The key will be the assigned number, while the value will be the trace itself.*
- [Commented](https://github.com/explodinggradients/ragas/issues/1871#issuecomment-2628965465) in [explodinggradients/ragas] on 2025-02-01.
  > *AI Summary: @Vidit-Ostwal has suggested a modification to the proposed solution, based on user perspective, for easier understanding of the flow. Implementation-wise, it is considered easy. @jjmachan is requested to provide their opinion on the suggested solution. If approved, the PR will be updated accordingly.*

## 🐛 Issues Raised
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/2030) in [crewAIInc/crewAI]: Documentation Error in memory docs (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested a change to the document at the following link: https://docs.crewai.com/concepts/memory The comment highlights that throughout the provided code examples in the document, the embedder parameter takes the input of 'model' instead of 'model_name', and this should be corrected to 'model_name'. This issue is present in the following*
- Raised an [issue](https://github.com/crewAIInc/crewAI/issues/1984) in [crewAIInc/crewAI]: output_log_file should also suppport JSON format. (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested a new feature to add JSON format to the `output_log_file` for better parsability and analysis. This addition partially addresses issue #1970. @Vidit-Ostwal expresses willingness to contribute a pull request for this enhancement.*
- Raised an [issue](https://github.com/browser-use/browser-use/issues/407) in [browser-use/browser-use]: Use of use_vision while defining agent (2025-01-26).
  > *AI Summary: @Vidit-Ostwal has suggested that the purpose of setting `use_vision` to `True` when defining an agent is unclear. They question whether screenshots are processed by the multimodal LLM or if scraping elements and making decisions based on those elements still occur. Additionally, they have not noticed any significant differences in output*

## 🚀 Pull Requests
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2047) in [crewAIInc/crewAI]: Added reset memories function inside crew class (2025-02-06).
  > *AI Summary: @Vidit-Ostwal has suggested resolving the reset memories issue reported in #2023. Additionally, they propose:

1. Eliminating the CLI command for memory reset
2. Implementing documentation updates

They are willing to make these changes if the suggested solution is aligned with the project's goals.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/2031) in [crewAIInc/crewAI]: Fixed the memory documentation (2025-02-04).
  > *AI Summary: @Vidit-Ostwal has suggested a commit that addresses the documentation issue outlined in issue #2030. This commit resolves the problem by making the necessary documentation updates and improvements.*
- Opened a [PR](https://github.com/crewAIInc/crewAI/pull/1985) in [crewAIInc/crewAI]: Added functionality to have json format as well for the logs (2025-01-27).
  > *AI Summary: @Vidit-Ostwal has suggested adding support to save logs as a JSON file. By setting output_log_file to True or providing a file name and enabling save_as_json, users can now save logs in a JSON format. The resulting JSON file will contain an array of JSON events, enabling easy parsing and manipulation.*
- Opened a [PR](https://github.com/explodinggradients/ragas/pull/1880) in [explodinggradients/ragas]: Changed the parse_run_traces to include last 4 letters of run_id (2025-01-25).
  > *AI Summary: @Vidit-Ostwal has suggested a change to the parse_run_traces function, to include the last 4 letters of the run_id of the trace. This modification results in a unique key for every call, resolving the issue of potential duplicate keys. The change has been implemented in pull request #1871.*
- Opened a [PR](https://github.com/explodinggradients/ragas/pull/1879) in [explodinggradients/ragas]: Change the validate_samples functionality (2025-01-24).
  > *AI Summary: @Vidit-Ostwal has suggested modifying the validate_samples functionality to include information about the specific indexed sample causing any issues encountered during validation. This enhancement provides more detailed feedback and facilitates quicker troubleshooting and resolution of validation errors.*

## ⭐ Starred Repositories
- Starred [langfuse/langfuse](https://github.com/langfuse/langfuse) on 2025-02-04.
- Starred [microsoft/autogen](https://github.com/microsoft/autogen) on 2025-01-31.
- Starred [browser-use/browser-use](https://github.com/browser-use/browser-use) on 2025-01-26.
- Starred [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) on 2025-01-25.
- Starred [explodinggradients/ragas](https://github.com/explodinggradients/ragas) on 2025-01-24.

## 🍴 Forked Repositories
- Forked [crewAIInc/crewAI](https://github.com/Vidit-Ostwal/crewAI) on 2025-01-27.
- Forked [explodinggradients/ragas](https://github.com/Vidit-Ostwal/ragas) on 2025-01-24.
